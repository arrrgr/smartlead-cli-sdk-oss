"""Master inbox models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class InboxFilters(BaseModel):
    search: Optional[str] = None
    leadCategories: Optional[dict[str, Any]] = None
    emailStatus: Optional[list[str]] = None
    campaignId: Optional[list[int]] = None
    emailAccountId: Optional[list[int]] = None
    campaignTeamMemberId: Optional[list[int]] = None
    campaignTagId: Optional[list[int]] = None
    campaignClientId: Optional[list[int]] = None
    replyTimeBetween: Optional[list[str]] = None


class InboxRepliesRequest(BaseModel):
    offset: int = 0
    limit: int = 10
    filters: Optional[InboxFilters] = None
    sortBy: Optional[str] = None


class ReplyToLeadRequest(BaseModel):
    email_stats_id: str
    email_body: str
    reply_message_id: Optional[str] = None
    reply_email_time: Optional[str] = None


class UpdateRevenueRequest(BaseModel):
    email_lead_map_id: int
    revenue: float


class UpdateCategoryRequest(BaseModel):
    email_lead_map_id: Optional[int] = None
    category_id: Optional[int] = None


class SetReminderRequest(BaseModel):
    email_lead_map_id: Optional[int] = None
    reminder_time: Optional[str] = None
    note: Optional[str] = None


class CreateTaskRequest(BaseModel):
    email_lead_map_id: Optional[int] = None
    task: Optional[str] = None
    due_date: Optional[str] = None


class CreateNoteRequest(BaseModel):
    email_lead_map_id: Optional[int] = None
    note: Optional[str] = None


class PushToSubsequenceRequest(BaseModel):
    email_lead_map_id: Optional[int] = None
    sub_sequence_id: Optional[int] = None


class AssignTeamMemberRequest(BaseModel):
    email_lead_map_id: int
    team_member_id: int


class BlockDomainsRequest(BaseModel):
    domains: list[str]


class ResumeLeadRequest(BaseModel):
    email_lead_map_id: int
