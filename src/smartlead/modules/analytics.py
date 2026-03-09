"""Campaign analytics & statistics endpoints (~8 endpoints)."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.analytics import CampaignStatistics, SequenceAnalyticsResponse


class AnalyticsModule:
    """Campaign-level analytics API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def get_statistics(self, campaign_id: int) -> CampaignStatistics:
        """GET /campaigns/{id}/statistics"""
        data = await self._client.get(f"/campaigns/{campaign_id}/statistics")
        return CampaignStatistics(**data)

    async def get_top_level(self, campaign_id: int) -> CampaignStatistics:
        """GET /campaigns/{id}/analytics"""
        data = await self._client.get(f"/campaigns/{campaign_id}/analytics")
        return CampaignStatistics(**data)

    async def get_by_date_range(
        self, campaign_id: int, start_date: str, end_date: str
    ) -> CampaignStatistics:
        """GET /campaigns/{id}/analytics-by-date"""
        params = {"start_date": start_date, "end_date": end_date}
        data = await self._client.get(f"/campaigns/{campaign_id}/analytics-by-date", params=params)
        return CampaignStatistics(**data)

    async def get_top_level_by_date(
        self, campaign_id: int, start_date: str, end_date: str
    ) -> CampaignStatistics:
        """GET /campaigns/{id}/top-level-analytics-by-date"""
        params = {"start_date": start_date, "end_date": end_date}
        data = await self._client.get(
            f"/campaigns/{campaign_id}/top-level-analytics-by-date", params=params
        )
        return CampaignStatistics(**data)

    async def get_lead_statistics(self, campaign_id: int) -> dict[str, Any]:
        """GET /campaigns/{id}/lead-statistics"""
        return await self._client.get(f"/campaigns/{campaign_id}/lead-statistics")

    async def get_mailbox_statistics(self, campaign_id: int) -> dict[str, Any]:
        """GET /campaigns/{id}/mailbox-statistics"""
        return await self._client.get(f"/campaigns/{campaign_id}/mailbox-statistics")

    async def get_sequence_analytics(
        self, campaign_id: int, start_date: str, end_date: str
    ) -> SequenceAnalyticsResponse:
        """GET /campaigns/{id}/sequence-analytics"""
        params = {"start_date": start_date, "end_date": end_date}
        data = await self._client.get(f"/campaigns/{campaign_id}/sequence-analytics", params=params)
        return SequenceAnalyticsResponse(**data)

    async def get_warmup_stats(self, account_id: int) -> dict[str, Any]:
        """GET /email-accounts/{id}/warmup-stats"""
        return await self._client.get(f"/email-accounts/{account_id}/warmup-stats")
