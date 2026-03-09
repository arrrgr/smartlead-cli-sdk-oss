"""Global analytics endpoints (~22 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient


class GlobalAnalyticsModule:
    """Account-wide analytics API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    def _params(self, **kwargs: Any) -> dict[str, Any]:
        return {k: v for k, v in kwargs.items() if v is not None}

    async def campaign_list(self, offset: int = 0, limit: int = 100, **kwargs: Any) -> Any:
        """GET /analytics/campaign-list"""
        return await self._client.get("/analytics/campaign-list", params=self._params(offset=offset, limit=limit, **kwargs))

    async def client_list(self, **kwargs: Any) -> Any:
        """GET /analytics/client-list"""
        return await self._client.get("/analytics/client-list", params=self._params(**kwargs))

    async def client_monthly_count(self, **kwargs: Any) -> Any:
        """GET /analytics/client-month-wise-count"""
        return await self._client.get("/analytics/client-month-wise-count", params=self._params(**kwargs))

    async def overall_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/overall-stats-v2"""
        return await self._client.get("/analytics/overall-stats-v2", params=self._params(**kwargs))

    async def daily_stats(self, start_date: Optional[str] = None, end_date: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /analytics/day-wise-overall-stats"""
        return await self._client.get("/analytics/day-wise-overall-stats", params=self._params(start_date=start_date, end_date=end_date, **kwargs))

    async def daily_stats_by_sent_time(self, start_date: Optional[str] = None, end_date: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /analytics/day-wise-overall-stats-by-sent-time"""
        return await self._client.get("/analytics/day-wise-overall-stats-by-sent-time", params=self._params(start_date=start_date, end_date=end_date, **kwargs))

    async def daily_positive_replies(self, start_date: Optional[str] = None, end_date: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /analytics/day-wise-positive-reply-stats"""
        return await self._client.get("/analytics/day-wise-positive-reply-stats", params=self._params(start_date=start_date, end_date=end_date, **kwargs))

    async def daily_positive_replies_by_sent_time(self, start_date: Optional[str] = None, end_date: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /analytics/day-wise-positive-reply-stats-by-sent-time"""
        return await self._client.get("/analytics/day-wise-positive-reply-stats-by-sent-time", params=self._params(start_date=start_date, end_date=end_date, **kwargs))

    async def campaign_overall_stats(self, campaign_id: Optional[int] = None, **kwargs: Any) -> Any:
        """GET /analytics/campaign-overall-stats"""
        return await self._client.get("/analytics/campaign-overall-stats", params=self._params(campaign_id=campaign_id, **kwargs))

    async def client_overall_stats(self, client_id: Optional[int] = None, **kwargs: Any) -> Any:
        """GET /analytics/client-overall-stats"""
        return await self._client.get("/analytics/client-overall-stats", params=self._params(client_id=client_id, **kwargs))

    async def mailbox_health_by_name(self, **kwargs: Any) -> Any:
        """GET /analytics/mailbox-name-wise-health-metrics"""
        return await self._client.get("/analytics/mailbox-name-wise-health-metrics", params=self._params(**kwargs))

    async def mailbox_health_by_domain(self, **kwargs: Any) -> Any:
        """GET /analytics/mailbox-domain-wise-health-metrics"""
        return await self._client.get("/analytics/mailbox-domain-wise-health-metrics", params=self._params(**kwargs))

    async def mailbox_performance_by_provider(self, **kwargs: Any) -> Any:
        """GET /analytics/mailbox-provider-wise-overall-performance"""
        return await self._client.get("/analytics/mailbox-provider-wise-overall-performance", params=self._params(**kwargs))

    async def team_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/team-board-overall-stats"""
        return await self._client.get("/analytics/team-board-overall-stats", params=self._params(**kwargs))

    async def lead_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/lead-overall-stats"""
        return await self._client.get("/analytics/lead-overall-stats", params=self._params(**kwargs))

    async def lead_category_responses(self, **kwargs: Any) -> Any:
        """GET /analytics/lead-category-wise-response"""
        return await self._client.get("/analytics/lead-category-wise-response", params=self._params(**kwargs))

    async def first_reply_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/campaign-leads-take-for-first-reply"""
        return await self._client.get("/analytics/campaign-leads-take-for-first-reply", params=self._params(**kwargs))

    async def follow_up_reply_rate(self, **kwargs: Any) -> Any:
        """GET /analytics/campaign-follow-up-reply-rate"""
        return await self._client.get("/analytics/campaign-follow-up-reply-rate", params=self._params(**kwargs))

    async def lead_reply_time(self, **kwargs: Any) -> Any:
        """GET /analytics/campaign-lead-to-reply-time"""
        return await self._client.get("/analytics/campaign-lead-to-reply-time", params=self._params(**kwargs))

    async def campaign_response_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/campaign-response-stats"""
        return await self._client.get("/analytics/campaign-response-stats", params=self._params(**kwargs))

    async def campaign_status_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/campaign-status-stats"""
        return await self._client.get("/analytics/campaign-status-stats", params=self._params(**kwargs))

    async def mailbox_overall_stats(self, **kwargs: Any) -> Any:
        """GET /analytics/mailbox-overall-stats"""
        return await self._client.get("/analytics/mailbox-overall-stats", params=self._params(**kwargs))
