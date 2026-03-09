"""Lead management endpoints (~17 endpoints)."""

from __future__ import annotations

from typing import Union, Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.leads import (
    AddLeadsRequest,
    AddLeadsResponse,
    AddLeadsSettings,
    LeadData,
    ListLeadsResponse,
    LeadByEmailResponse,
    GlobalLeadsResponse,
    LeadCategory,
    UpdateLeadRequest,
    UpdateCategoryRequest,
    ResumeLeadRequest,
    MessageHistoryResponse,
    MoveToInactiveRequest,
    MoveToInactiveFilters,
    PushToCampaignRequest,
)


class LeadsModule:
    """Lead management API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def add_to_campaign(
        self,
        campaign_id: int,
        leads: Union[list[dict[str, Any]], list[LeadData]],
        settings: Optional[Union[dict[str, Any], AddLeadsSettings]] = None,
    ) -> AddLeadsResponse:
        """POST /campaigns/{id}/leads"""
        lead_list = [LeadData(**ld) if isinstance(ld, dict) else ld for ld in leads]
        if isinstance(settings, dict):
            settings = AddLeadsSettings(**settings)
        body = AddLeadsRequest(lead_list=lead_list, settings=settings)
        data = await self._client.post(
            f"/campaigns/{campaign_id}/leads",
            json=body.model_dump(exclude_none=True),
        )
        return AddLeadsResponse(**data)

    async def list_by_campaign(
        self,
        campaign_id: int,
        offset: int = 0,
        limit: int = 100,
        status: Optional[str] = None,
        lead_category_id: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        last_sent_time_gt: Optional[str] = None,
        event_time_gt: Optional[str] = None,
    ) -> ListLeadsResponse:
        """GET /campaigns/{id}/leads"""
        params: dict[str, Any] = {"offset": offset, "limit": limit}
        if status:
            params["status"] = status
        if lead_category_id is not None:
            params["lead_category_id"] = lead_category_id
        if created_at_gt:
            params["created_at_gt"] = created_at_gt
        if last_sent_time_gt:
            params["last_sent_time_gt"] = last_sent_time_gt
        if event_time_gt:
            params["event_time_gt"] = event_time_gt
        data = await self._client.get(f"/campaigns/{campaign_id}/leads", params=params)
        return ListLeadsResponse(**data)

    async def get_by_email(self, email: str) -> LeadByEmailResponse:
        """GET /leads/?email=EMAIL"""
        data = await self._client.get("/leads/", params={"email": email})
        return LeadByEmailResponse(**data)

    async def list_global(
        self,
        offset: int = 0,
        limit: int = 100,
        created_at_gt: Optional[str] = None,
        email: Optional[str] = None,
    ) -> GlobalLeadsResponse:
        """GET /leads/global-leads"""
        params: dict[str, Any] = {"offset": offset, "limit": limit}
        if created_at_gt:
            params["created_at_gt"] = created_at_gt
        if email:
            params["email"] = email
        data = await self._client.get("/leads/global-leads", params=params)
        return GlobalLeadsResponse(**data)

    async def list_categories(self) -> list[LeadCategory]:
        """GET /leads/fetch-categories"""
        data = await self._client.get("/leads/fetch-categories")
        return [LeadCategory(**item) for item in data]

    async def update(self, campaign_id: int, lead_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /campaigns/{id}/leads/{lid}"""
        body = UpdateLeadRequest(**kwargs)
        return await self._client.post(
            f"/campaigns/{campaign_id}/leads/{lead_id}",
            json=body.model_dump(exclude_none=True),
        )

    async def update_category(
        self, campaign_id: int, lead_id: int, category_id: int, pause_lead: bool = False
    ) -> dict[str, Any]:
        """POST /campaigns/{id}/leads/{lid}/category"""
        body = UpdateCategoryRequest(category_id=category_id, pause_lead=pause_lead)
        return await self._client.post(
            f"/campaigns/{campaign_id}/leads/{lead_id}/category",
            json=body.model_dump(),
        )

    async def resume(
        self, campaign_id: int, lead_id: int, delay_days: Optional[int] = 0
    ) -> dict[str, Any]:
        """POST /campaigns/{id}/leads/{lid}/resume"""
        body = ResumeLeadRequest(resume_lead_with_delay_days=delay_days)
        return await self._client.post(
            f"/campaigns/{campaign_id}/leads/{lead_id}/resume",
            json=body.model_dump(exclude_none=True),
        )

    async def pause(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """POST /campaigns/{id}/leads/{lid}/pause"""
        return await self._client.post(f"/campaigns/{campaign_id}/leads/{lead_id}/pause")

    async def delete(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """DELETE /campaigns/{id}/leads/{lid}"""
        return await self._client.delete(f"/campaigns/{campaign_id}/leads/{lead_id}")

    async def unsubscribe(self, campaign_id: int, lead_id: int) -> dict[str, Any]:
        """POST /campaigns/{id}/leads/{lid}/unsubscribe"""
        return await self._client.post(f"/campaigns/{campaign_id}/leads/{lead_id}/unsubscribe")

    async def unsubscribe_all(self, lead_id: int) -> dict[str, Any]:
        """POST /leads/{lid}/unsubscribe"""
        return await self._client.post(f"/leads/{lead_id}/unsubscribe")

    async def get_campaign_overview(self, lead_id: int) -> dict[str, Any]:
        """GET /leads/{lid}/campaign-overview"""
        return await self._client.get(f"/leads/{lead_id}/campaign-overview")

    async def get_sequence_details(self, lead_map_id: int) -> dict[str, Any]:
        """GET /leads/{leadMapId}/sequence-details"""
        return await self._client.get(f"/leads/{lead_map_id}/sequence-details")

    async def get_message_history(
        self, campaign_id: int, lead_id: int, event_time_gt: Optional[str] = None
    ) -> MessageHistoryResponse:
        """GET /campaigns/{id}/leads/{lid}/message-history"""
        params: dict[str, Any] = {}
        if event_time_gt:
            params["event_time_gt"] = event_time_gt
        data = await self._client.get(
            f"/campaigns/{campaign_id}/leads/{lead_id}/message-history",
            params=params if params else None,
        )
        return MessageHistoryResponse(**data)

    async def move_to_inactive(
        self,
        list_id: int,
        lead_ids: Optional[list[int]] = None,
        all_leads: bool = False,
        filters: Optional[dict[str, Any]] = None,
        action: str = "move",
    ) -> dict[str, Any]:
        """POST /leads/push-to-list"""
        f = MoveToInactiveFilters(**filters) if filters else None
        body = MoveToInactiveRequest(
            listId=list_id, leadIds=lead_ids, allLeads=all_leads, filters=f, action=action
        )
        return await self._client.post("/leads/push-to-list", json=body.model_dump(exclude_none=True))

    async def push_to_campaign(
        self, campaign_id: int, lead_ids: Optional[list[int]] = None
    ) -> dict[str, Any]:
        """POST /leads/push-to-campaign"""
        body = PushToCampaignRequest(campaign_id=campaign_id, lead_ids=lead_ids)
        return await self._client.post("/leads/push-to-campaign", json=body.model_dump(exclude_none=True))
