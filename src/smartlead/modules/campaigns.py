"""Campaign management endpoints (~9 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.campaigns import (
    CreateCampaignRequest,
    CreateCampaignResponse,
    CampaignResponse,
    UpdateScheduleRequest,
    UpdateSettingsRequest,
    UpdateStatusRequest,
    CreateSubsequenceRequest,
)


class CampaignsModule:
    """Campaign management API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def create(self, name: str, client_id: Optional[int] = None) -> CreateCampaignResponse:
        """POST /campaigns/create"""
        body = CreateCampaignRequest(name=name, client_id=client_id)
        data = await self._client.post("/campaigns/create", json=body.model_dump(exclude_none=True))
        return CreateCampaignResponse(**data)

    async def get(self, campaign_id: int) -> CampaignResponse:
        """GET /campaigns/{id}"""
        data = await self._client.get(f"/campaigns/{campaign_id}")
        return CampaignResponse(**data)

    async def delete(self, campaign_id: int) -> dict[str, Any]:
        """DELETE /campaigns/{id}"""
        return await self._client.delete(f"/campaigns/{campaign_id}")

    async def update_schedule(self, campaign_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /campaigns/{id} -- update schedule settings."""
        body = UpdateScheduleRequest(**kwargs)
        return await self._client.post(f"/campaigns/{campaign_id}", json=body.model_dump(exclude_none=True))

    async def update_settings(self, campaign_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /campaigns/{id}/settings"""
        body = UpdateSettingsRequest(**kwargs)
        return await self._client.post(f"/campaigns/{campaign_id}/settings", json=body.model_dump(exclude_none=True))

    async def update_status(self, campaign_id: int, status: str) -> dict[str, Any]:
        """POST /campaigns/{id}/status"""
        body = UpdateStatusRequest(status=status)
        return await self._client.post(f"/campaigns/{campaign_id}/status", json=body.model_dump())

    async def list_by_lead(self, lead_id: int) -> list[dict[str, Any]]:
        """GET /leads/{lead_id}/campaigns"""
        return await self._client.get(f"/leads/{lead_id}/campaigns")

    async def export_data(self, campaign_id: int) -> Any:
        """GET /campaigns/{id}/leads-export -- returns CSV data."""
        return await self._client.get(f"/campaigns/{campaign_id}/leads-export")

    async def create_subsequence(self, parent_campaign_id: int, name: Optional[str] = None) -> CreateCampaignResponse:
        """POST /campaigns/create-subsequence"""
        body = CreateSubsequenceRequest(parent_campaign_id=parent_campaign_id, name=name)
        data = await self._client.post("/campaigns/create-subsequence", json=body.model_dump(exclude_none=True))
        return CreateCampaignResponse(**data)
