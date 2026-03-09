"""Analytics & statistics models."""

from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, field_validator


class CampaignStatistics(BaseModel):
    """Campaign statistics -- note that the analytics endpoints return counts as strings."""
    id: Optional[int] = None
    user_id: Optional[Union[int, str]] = None
    created_at: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None
    sent_count: int = 0
    unique_sent_count: int = 0
    open_count: int = 0
    unique_open_count: int = 0
    click_count: int = 0
    unique_click_count: int = 0
    reply_count: int = 0
    block_count: int = 0
    bounce_count: int = 0
    unsubscribed_count: int = 0
    total_count: int = 0
    drafted_count: int = 0
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    @field_validator(
        "sent_count", "unique_sent_count", "open_count", "unique_open_count",
        "click_count", "unique_click_count", "reply_count", "block_count",
        "bounce_count", "unsubscribed_count", "total_count", "drafted_count",
        mode="before",
    )
    @classmethod
    def coerce_str_to_int(cls, v: Optional[Union[str, int]]) -> int:
        if v is None:
            return 0
        if isinstance(v, str):
            try:
                return int(v)
            except ValueError:
                return 0
        return v


class SequenceAnalyticsEntry(BaseModel):
    email_campaign_seq_id: Optional[int] = None
    sent_count: int = 0
    skipped_count: int = 0
    open_count: int = 0
    click_count: int = 0
    reply_count: int = 0
    bounce_count: int = 0
    unsubscribed_count: int = 0
    failed_count: int = 0
    stopped_count: int = 0
    ln_connection_req_pending_count: int = 0
    ln_connection_req_accepted_count: int = 0
    ln_connection_req_skipped_sent_msg_count: int = 0
    positive_reply_count: int = 0


class SequenceAnalyticsResponse(BaseModel):
    ok: bool = True
    data: Optional[list[SequenceAnalyticsEntry]] = None
