"""Shared enums and common models used across the Smartlead SDK."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class CampaignStatus(str, Enum):
    DRAFTED = "DRAFTED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"
    PAUSED = "PAUSED"


class LeadStatus(str, Enum):
    STARTED = "STARTED"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"
    BLOCKED = "BLOCKED"


class EmailAccountType(str, Enum):
    SMTP = "SMTP"
    GMAIL = "GMAIL"
    ZOHO = "ZOHO"
    OUTLOOK = "OUTLOOK"


class TrackSetting(str, Enum):
    DONT_TRACK_EMAIL_OPEN = "DONT_TRACK_EMAIL_OPEN"
    DONT_TRACK_LINK_CLICK = "DONT_TRACK_LINK_CLICK"
    DONT_TRACK_REPLY_TO_AN_EMAIL = "DONT_TRACK_REPLY_TO_AN_EMAIL"


class StopLeadSetting(str, Enum):
    REPLY_TO_AN_EMAIL = "REPLY_TO_AN_EMAIL"
    CLICK_ON_A_LINK = "CLICK_ON_A_LINK"
    OPEN_AN_EMAIL = "OPEN_AN_EMAIL"


class CampaignStatusAction(str, Enum):
    """Values accepted by the PATCH campaign status endpoint."""
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"
    START = "START"


class VariantDistributionType(str, Enum):
    MANUAL_EQUAL = "MANUAL_EQUAL"
    MANUAL_PERCENTAGE = "MANUAL_PERCENTAGE"
    AI_EQUAL = "AI_EQUAL"


class WinningMetric(str, Enum):
    OPEN_RATE = "OPEN_RATE"
    CLICK_RATE = "CLICK_RATE"
    REPLY_RATE = "REPLY_RATE"
    POSITIVE_REPLY_RATE = "POSITIVE_REPLY_RATE"


class SequenceType(str, Enum):
    EMAIL = "EMAIL"
    MANUAL = "MANUAL"


class SortBy(str, Enum):
    REPLY_TIME_DESC = "REPLY_TIME_DESC"
    SENT_TIME_DESC = "SENT_TIME_DESC"


class SentimentType(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


class OkResponse(BaseModel):
    """Generic {"ok": true} response."""
    ok: bool = True


class PaginationParams(BaseModel):
    """Common pagination parameters."""
    offset: int = 0
    limit: int = 100
