"""Smartlead error hierarchy."""

from __future__ import annotations


class SmartleadError(Exception):
    """Base error for all Smartlead API errors."""

    def __init__(self, message: str, status_code: int | None = None, response_body: dict | None = None) -> None:
        self.status_code = status_code
        self.response_body = response_body or {}
        super().__init__(message)

    @property
    def is_retryable(self) -> bool:
        return False


class SmartleadAuthError(SmartleadError):
    """401 Unauthorized -- invalid or missing API key."""


class SmartleadValidationError(SmartleadError):
    """400 Bad Request -- invalid request parameters."""


class SmartleadNotFoundError(SmartleadError):
    """404 Not Found -- resource does not exist."""


class SmartleadRateLimitError(SmartleadError):
    """429 Too Many Requests -- rate limit exceeded."""

    @property
    def is_retryable(self) -> bool:
        return True


class SmartleadServerError(SmartleadError):
    """5xx Server Error -- transient server-side failure."""

    @property
    def is_retryable(self) -> bool:
        return True


def raise_for_status(status_code: int, body: dict) -> None:
    """Raise the appropriate SmartleadError based on HTTP status code."""
    if 200 <= status_code < 300:
        return
    message = body.get("error") or body.get("message") or f"HTTP {status_code}"
    if status_code == 401:
        raise SmartleadAuthError(message, status_code, body)
    if status_code == 400:
        raise SmartleadValidationError(message, status_code, body)
    if status_code == 404:
        raise SmartleadNotFoundError(message, status_code, body)
    if status_code == 429:
        raise SmartleadRateLimitError(message, status_code, body)
    if status_code >= 500:
        raise SmartleadServerError(message, status_code, body)
    raise SmartleadError(message, status_code, body)
