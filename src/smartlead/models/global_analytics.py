"""Global analytics models."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class GlobalAnalyticsParams(BaseModel):
    """Common query parameters for global analytics endpoints."""
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    campaign_id: Optional[int] = None
    client_id: Optional[int] = None
