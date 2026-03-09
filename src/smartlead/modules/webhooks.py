"""Webhook endpoints (~5 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.webhooks import WebhookConfig


class WebhooksModule:
    """Webhook management API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def list(self, campaign_id: int) -> Any:
        """GET /campaigns/{id}/webhooks"""
        return await self._client.get(f"/campaigns/{campaign_id}/webhooks")

    async def create_or_update(self, campaign_id: int, webhook_url: str, events: Optional[list[str]] = None, active: bool = True) -> dict[str, Any]:
        """POST /campaigns/{id}/webhooks"""
        body = WebhookConfig(webhook_url=webhook_url, events=events, active=active)
        return await self._client.post(
            f"/campaigns/{campaign_id}/webhooks",
            json=body.model_dump(exclude_none=True),
        )

    async def delete(self, campaign_id: int) -> dict[str, Any]:
        """DELETE /campaigns/{id}/webhooks"""
        return await self._client.delete(f"/campaigns/{campaign_id}/webhooks")

    async def get_summary(self, campaign_id: int) -> Any:
        """GET /campaigns/{id}/webhooks/summary"""
        return await self._client.get(f"/campaigns/{campaign_id}/webhooks/summary")

    async def retrigger_failed(self, campaign_id: int) -> dict[str, Any]:
        """POST /campaigns/{id}/webhooks/retrigger-failed-events"""
        return await self._client.post(f"/campaigns/{campaign_id}/webhooks/retrigger-failed-events")
