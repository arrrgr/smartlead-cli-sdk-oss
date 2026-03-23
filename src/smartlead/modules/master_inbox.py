"""Master inbox endpoints (~20 endpoints)."""

from __future__ import annotations

from typing import Union, Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.master_inbox import (
    InboxRepliesRequest,
    InboxFilters,
    ReplyToLeadRequest,
    UpdateRevenueRequest,
    UpdateCategoryRequest,
    SetReminderRequest,
    CreateTaskRequest,
    CreateNoteRequest,
    PushToSubsequenceRequest,
    AssignTeamMemberRequest,
    BlockDomainsRequest,
    ResumeLeadRequest,
)


class MasterInboxModule:
    """Master inbox API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def get_replies(
        self,
        offset: int = 0,
        limit: int = 10,
        filters: Optional[Union[dict[str, Any], InboxFilters]] = None,
        sort_by: Optional[str] = None,
        fetch_message_history: bool = False,
    ) -> Any:
        """POST /master-inbox/inbox-replies"""
        if isinstance(filters, dict):
            filters = InboxFilters(**filters)
        body = InboxRepliesRequest(offset=offset, limit=limit, filters=filters, sortBy=sort_by)
        params = {"fetch_message_history": True} if fetch_message_history else None
        return await self._client.post(
            "/master-inbox/inbox-replies",
            json=body.model_dump(exclude_none=True),
            params=params,
        )

    async def get_lead(self, lead_map_id: int) -> Any:
        """GET /master-inbox/{id}"""
        return await self._client.get(f"/master-inbox/{lead_map_id}")

    async def reply_to_lead(self, campaign_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /campaigns/{id}/reply-email-thread"""
        body = ReplyToLeadRequest(**kwargs)
        return await self._client.post(
            f"/campaigns/{campaign_id}/reply-email-thread",
            json=body.model_dump(exclude_none=True),
        )

    async def forward_reply(self, campaign_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /campaigns/{id}/forward-email"""
        body = ReplyToLeadRequest(**kwargs)
        return await self._client.post(
            f"/campaigns/{campaign_id}/forward-email",
            json=body.model_dump(exclude_none=True),
        )

    async def update_revenue(self, email_lead_map_id: int, revenue: float) -> dict[str, Any]:
        """PATCH /master-inbox/update-revenue"""
        body = UpdateRevenueRequest(email_lead_map_id=email_lead_map_id, revenue=revenue)
        return await self._client.patch("/master-inbox/update-revenue", json=body.model_dump())

    async def update_category(self, email_lead_map_id: int, category_id: int) -> dict[str, Any]:
        """PATCH /master-inbox/update-category"""
        body = UpdateCategoryRequest(email_lead_map_id=email_lead_map_id, category_id=category_id)
        return await self._client.patch("/master-inbox/update-category", json=body.model_dump(exclude_none=True))

    async def get_snoozed(self, offset: int = 0, limit: int = 10, **kwargs: Any) -> Any:
        """POST /master-inbox/snoozed-messages"""
        return await self._client.post("/master-inbox/snoozed-messages", json={"offset": offset, "limit": limit, **kwargs})

    async def get_important(self, offset: int = 0, limit: int = 10, **kwargs: Any) -> Any:
        """POST /master-inbox/important-messages"""
        return await self._client.post("/master-inbox/important-messages", json={"offset": offset, "limit": limit, **kwargs})

    async def get_scheduled(self, offset: int = 0, limit: int = 10, **kwargs: Any) -> Any:
        """POST /master-inbox/scheduled-messages"""
        return await self._client.post("/master-inbox/scheduled-messages", json={"offset": offset, "limit": limit, **kwargs})

    async def get_reminders(self, offset: int = 0, limit: int = 10, **kwargs: Any) -> Any:
        """POST /master-inbox/reminder-messages"""
        return await self._client.post("/master-inbox/reminder-messages", json={"offset": offset, "limit": limit, **kwargs})

    async def get_archived(self, offset: int = 0, limit: int = 10, **kwargs: Any) -> Any:
        """POST /master-inbox/archived-messages"""
        return await self._client.post("/master-inbox/archived-messages", json={"offset": offset, "limit": limit, **kwargs})

    async def get_untracked(self) -> Any:
        """GET /master-inbox/untracked-replies"""
        return await self._client.get("/master-inbox/untracked-replies")

    async def update_read_status(self, email_lead_map_id: int, is_read: bool) -> dict[str, Any]:
        """PATCH /master-inbox/read-status"""
        return await self._client.patch(
            "/master-inbox/read-status",
            json={"email_lead_map_id": email_lead_map_id, "is_read": is_read},
        )

    async def set_reminder(self, **kwargs: Any) -> dict[str, Any]:
        """POST /master-inbox/set-reminder"""
        body = SetReminderRequest(**kwargs)
        return await self._client.post("/master-inbox/set-reminder", json=body.model_dump(exclude_none=True))

    async def create_task(self, **kwargs: Any) -> dict[str, Any]:
        """POST /master-inbox/create-lead-task"""
        body = CreateTaskRequest(**kwargs)
        return await self._client.post("/master-inbox/create-lead-task", json=body.model_dump(exclude_none=True))

    async def create_note(self, **kwargs: Any) -> dict[str, Any]:
        """POST /master-inbox/create-lead-note"""
        body = CreateNoteRequest(**kwargs)
        return await self._client.post("/master-inbox/create-lead-note", json=body.model_dump(exclude_none=True))

    async def push_to_subsequence(self, email_lead_map_id: int, subsequence_id: int) -> dict[str, Any]:
        """POST /master-inbox/push-to-subsequence"""
        body = PushToSubsequenceRequest(email_lead_map_id=email_lead_map_id, sub_sequence_id=subsequence_id)
        return await self._client.post("/master-inbox/push-to-subsequence", json=body.model_dump(exclude_none=True))

    async def assign_team_member(self, email_lead_map_id: int, team_member_id: int) -> dict[str, Any]:
        """POST /master-inbox/update-team-member"""
        body = AssignTeamMemberRequest(email_lead_map_id=email_lead_map_id, team_member_id=team_member_id)
        return await self._client.post("/master-inbox/update-team-member", json=body.model_dump())

    async def block_domains(self, domains: list[str]) -> dict[str, Any]:
        """POST /master-inbox/block-domains"""
        body = BlockDomainsRequest(domains=domains)
        return await self._client.post("/master-inbox/block-domains", json=body.model_dump())

    async def resume_lead(self, email_lead_map_id: int) -> dict[str, Any]:
        """PATCH /master-inbox/resume-lead"""
        body = ResumeLeadRequest(email_lead_map_id=email_lead_map_id)
        return await self._client.patch("/master-inbox/resume-lead", json=body.model_dump())
