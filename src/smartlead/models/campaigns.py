"""Campaign request/response models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel, Field


class CreateCampaignRequest(BaseModel):
    name: str
    client_id: Optional[int] = None


class CreateCampaignResponse(BaseModel):
    ok: bool
    id: int
    name: str
    created_at: str


class CampaignResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None
    track_settings: Any = None
    scheduler_cron_value: Optional[str] = None
    min_time_btwn_emails: Optional[int] = None
    max_leads_per_day: Optional[int] = None
    stop_lead_settings: Optional[str] = None
    unsubscribe_text: Optional[str] = None
    client_id: Optional[int] = None
    enable_ai_esp_matching: Optional[bool] = None
    send_as_plain_text: Optional[bool] = None
    follow_up_percentage: Optional[int] = None


class UpdateScheduleRequest(BaseModel):
    timezone: Optional[str] = None
    days_of_the_week: Optional[list[int]] = None
    start_hour: Optional[str] = None
    end_hour: Optional[str] = None
    min_time_btw_emails: Optional[int] = None
    max_new_leads_per_day: Optional[int] = None
    schedule_start_time: Optional[str] = None


class OutOfOfficeSettings(BaseModel):
    ignoreOOOasReply: Optional[bool] = None
    autoReactivateOOO: Optional[bool] = None
    reactivateOOOwithDelay: Optional[int] = None
    autoCategorizeOOO: Optional[bool] = None


class UpdateSettingsRequest(BaseModel):
    name: Optional[str] = None
    track_settings: Optional[list[str]] = None
    stop_lead_settings: Optional[str] = None
    unsubscribe_text: Optional[str] = None
    send_as_plain_text: Optional[bool] = None
    force_plain_text: Optional[bool] = None
    follow_up_percentage: Optional[int] = None
    client_id: Optional[int] = None
    enable_ai_esp_matching: Optional[bool] = None
    auto_pause_domain_leads_on_reply: Optional[bool] = None
    ignore_ss_mailbox_sending_limit: Optional[bool] = None
    bounce_autopause_threshold: Optional[str] = None
    domain_level_rate_limit: Optional[bool] = None
    out_of_office_detection_settings: Optional[OutOfOfficeSettings] = None
    ai_categorisation_options: Optional[list[int]] = None


class UpdateStatusRequest(BaseModel):
    status: str  # PAUSED, STOPPED, START


class CampaignSummary(BaseModel):
    id: int
    status: Optional[str] = None
    name: Optional[str] = None


class CreateSubsequenceRequest(BaseModel):
    parent_campaign_id: int
    name: Optional[str] = None
