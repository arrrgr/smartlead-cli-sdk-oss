"""Base HTTP client with auth, retry, and rate limiting."""

from __future__ import annotations

import asyncio
import time
from typing import Optional, Any

import httpx

from ._config import SmartleadConfig
from ._errors import SmartleadError, SmartleadRateLimitError, SmartleadServerError, raise_for_status


class BaseSmartleadClient:
    """Low-level HTTP client for the Smartlead API.

    Handles authentication (api_key query param), exponential backoff retry
    on 5xx / network errors, and simple rate-limit tracking.
    """

    def __init__(self, config: SmartleadConfig) -> None:
        self._config = config
        self._client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=httpx.Timeout(config.timeout),
        )
        self._sd_client = httpx.AsyncClient(
            base_url=config.smart_delivery_base_url,
            timeout=httpx.Timeout(config.timeout),
        )
        # Simple sliding-window rate limiter
        self._request_timestamps: list[float] = []

    # ------------------------------------------------------------------
    # Public request helpers
    # ------------------------------------------------------------------

    async def get(self, path: str, *, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        return await self._request("GET", path, params=params, smart_delivery=smart_delivery)

    async def post(self, path: str, *, json: Optional[dict[str, Any]] = None, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        return await self._request("POST", path, json=json, params=params, smart_delivery=smart_delivery)

    async def put(self, path: str, *, json: Optional[dict[str, Any]] = None, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        return await self._request("PUT", path, json=json, params=params, smart_delivery=smart_delivery)

    async def patch(self, path: str, *, json: Optional[dict[str, Any]] = None, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        return await self._request("PATCH", path, json=json, params=params, smart_delivery=smart_delivery)

    async def delete(self, path: str, *, json: Optional[dict[str, Any]] = None, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        return await self._request("DELETE", path, json=json, params=params, smart_delivery=smart_delivery)

    async def close(self) -> None:
        await self._client.aclose()
        await self._sd_client.aclose()

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    async def _request(self, method: str, path: str, *, json: Optional[dict[str, Any]] = None, params: Optional[dict[str, Any]] = None, smart_delivery: bool = False) -> Any:
        params = dict(params or {})
        params["api_key"] = self._config.api_key

        client = self._sd_client if smart_delivery else self._client

        last_exc: Optional[Exception] = None
        for attempt in range(self._config.max_retries + 1):
            await self._wait_for_rate_limit()
            try:
                response = await client.request(method, path, params=params, json=json)
                self._record_request()
                self._update_rate_limit_from_headers(response.headers)

                # Handle rate-limit response with retry
                if response.status_code == 429:
                    retry_after = float(response.headers.get("retry-after", "1"))
                    if attempt < self._config.max_retries:
                        await asyncio.sleep(retry_after)
                        continue
                    raise_for_status(429, self._safe_json(response))

                body = self._safe_json(response)
                raise_for_status(response.status_code, body)
                return body

            except (SmartleadRateLimitError, SmartleadServerError) as exc:
                last_exc = exc
                if attempt < self._config.max_retries:
                    delay = min(
                        self._config.retry_base_delay * (2 ** attempt),
                        self._config.retry_max_delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                raise

            except httpx.HTTPStatusError as exc:
                body = self._safe_json(exc.response)
                raise_for_status(exc.response.status_code, body)

            except (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout) as exc:
                last_exc = exc
                if attempt < self._config.max_retries:
                    delay = min(
                        self._config.retry_base_delay * (2 ** attempt),
                        self._config.retry_max_delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                raise SmartleadError(f"Network error after {self._config.max_retries} retries: {exc}") from exc

        raise last_exc or SmartleadError("Request failed after retries")  # pragma: no cover

    async def _wait_for_rate_limit(self) -> None:
        """Simple sliding-window rate limiter."""
        now = time.monotonic()
        window = 60.0
        self._request_timestamps = [t for t in self._request_timestamps if now - t < window]
        if len(self._request_timestamps) >= self._config.rate_limit_rpm:
            oldest = self._request_timestamps[0]
            sleep_time = window - (now - oldest) + 0.1
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)

    def _record_request(self) -> None:
        self._request_timestamps.append(time.monotonic())

    def _update_rate_limit_from_headers(self, headers: httpx.Headers) -> None:
        """Update rate limit tracking from response headers if present."""
        remaining = headers.get("x-ratelimit-remaining")
        if remaining is not None:
            try:
                remaining_int = int(remaining)
                if remaining_int <= 2:
                    # Near limit -- pad timestamps to slow down
                    now = time.monotonic()
                    while len([t for t in self._request_timestamps if now - t < 60.0]) < self._config.rate_limit_rpm - 1:
                        self._request_timestamps.append(now)
            except ValueError:
                pass

    @staticmethod
    def _safe_json(response: httpx.Response) -> dict:
        try:
            return response.json()
        except Exception:
            return {"error": response.text or f"HTTP {response.status_code}"}
