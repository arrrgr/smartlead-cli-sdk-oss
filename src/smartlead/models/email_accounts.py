"""Email account request/response models."""

from __future__ import annotations

from typing import Union, Optional, Any

from pydantic import BaseModel


class CreateEmailAccountRequest(BaseModel):
    id: Optional[int] = None
    from_name: str
    from_email: str
    user_name: str
    password: str
    smtp_host: str
    smtp_port: int
    imap_host: str
    imap_port: int
    max_email_per_day: int = 100
    custom_tracking_url: Optional[str] = None
    bcc: Optional[str] = None
    signature: Optional[str] = None
    warmup_enabled: bool = False
    total_warmup_per_day: Optional[int] = None
    daily_rampup: Optional[int] = None
    reply_rate_percentage: Optional[int] = None
    client_id: Optional[int] = None


class CreateEmailAccountResponse(BaseModel):
    ok: bool
    message: Optional[str] = None
    emailAccountId: Optional[int] = None
    warmupKey: Optional[str] = None


class WarmupDetails(BaseModel):
    id: Optional[int] = None
    status: Optional[str] = None
    total_sent_count: Optional[int] = None
    total_spam_count: Optional[int] = None
    warmup_reputation: Optional[str] = None


class EmailAccountResponse(BaseModel):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    user_id: Optional[int] = None
    from_name: Optional[str] = None
    from_email: Optional[str] = None
    username: Optional[str] = None
    smtp_host: Optional[str] = None
    smtp_port: Optional[int] = None
    smtp_port_type: Optional[str] = None
    imap_host: Optional[str] = None
    imap_port: Optional[int] = None
    message_per_day: Optional[int] = None
    is_smtp_success: Optional[bool] = None
    is_imap_success: Optional[bool] = None
    type: Optional[str] = None
    daily_sent_count: Optional[int] = None
    client_id: Optional[int] = None
    warmup_details: Optional[WarmupDetails] = None
    password: Optional[str] = None
    imap_password: Optional[str] = None
    signature: Optional[str] = None
    custom_tracking_domain: Optional[str] = None
    bcc_email: Optional[str] = None
    smtp_failure_error: Optional[str] = None
    imap_failure_error: Optional[str] = None


class UpdateEmailAccountRequest(BaseModel):
    max_email_per_day: Optional[int] = None
    custom_tracking_url: Optional[str] = None
    bcc: Optional[str] = None
    signature: Optional[str] = None
    client_id: Optional[int] = None
    time_to_wait_in_mins: Optional[int] = None
    is_suspended: Optional[bool] = None


class AddToCampaignRequest(BaseModel):
    email_account_ids: list[int]


class RemoveFromCampaignRequest(BaseModel):
    email_accounts_ids: list[int]


class UpdateWarmupRequest(BaseModel):
    warmup_enabled: bool
    total_warmup_per_day: Optional[int] = None
    daily_rampup: Optional[int] = None
    reply_rate_percentage: Optional[Union[int, str]] = None
    warmup_key_id: Optional[str] = None
    auto_adjust_warmup: Optional[bool] = None
    is_rampup_enabled: Optional[bool] = None


class WarmupStatsByDate(BaseModel):
    id: Optional[int] = None
    date: Optional[str] = None
    sent_count: Optional[int] = None
    reply_count: Optional[int] = None
    save_from_spam_count: Optional[int] = None


class WarmupStatsResponse(BaseModel):
    id: Optional[int] = None
    sent_count: Optional[Union[int, str]] = None
    spam_count: Optional[Union[int, str]] = None
    inbox_count: Optional[Union[int, str]] = None
    warmup_email_received_count: Optional[Union[int, str]] = None
    stats_by_date: Optional[list[WarmupStatsByDate]] = None


class FetchMessagesRequest(BaseModel):
    limit: int = 100
    folder: Optional[str] = None
    includeBody: bool = False
    from_time: Optional[str] = None
    to_time: Optional[str] = None


class BulkDeleteRequest(BaseModel):
    ids: list[int]


class SaveOAuthEmailAccountRequest(BaseModel):
    from_name: Optional[str] = None
    from_email: Optional[str] = None
    oauth_token: Optional[str] = None
    refresh_token: Optional[str] = None
    provider: Optional[str] = None
    client_id: Optional[int] = None
    max_email_per_day: Optional[int] = None
    warmup_enabled: Optional[bool] = None
    total_warmup_per_day: Optional[int] = None
    daily_rampup: Optional[int] = None
    reply_rate_percentage: Optional[int] = None
