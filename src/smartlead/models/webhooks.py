"""Webhook models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class WebhookConfig(BaseModel):
    webhook_url: str
    events: Optional[list[str]] = None
    active: bool = True


class WebhookPayload(BaseModel):
    """EMAIL_REPLY webhook payload structure."""
    sl_email_lead_id: Optional[str] = None
    sl_email_lead_map_id: Optional[str] = None
    sl_lead_email: Optional[str] = None
    campaign_id: Optional[int] = None
    campaign_name: Optional[str] = None
    campaign_status: Optional[str] = None
    sequence_number: Optional[int] = None
    to_email: Optional[str] = None
    to_name: Optional[str] = None
    from_email: Optional[str] = None
    cc_emails: Optional[str] = None
    subject: Optional[str] = None
    message_id: Optional[str] = None
    preview_text: Optional[str] = None
    time_replied: Optional[str] = None
    event_timestamp: Optional[str] = None
    stats_id: Optional[str] = None
    secret_key: Optional[str] = None
    app_url: Optional[str] = None
    ui_master_inbox_link: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_id: Optional[int] = None
    webhook_name: Optional[str] = None
    leadCorrespondence: Optional[dict[str, Any]] = None
