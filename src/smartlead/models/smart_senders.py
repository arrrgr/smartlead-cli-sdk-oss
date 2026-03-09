"""Smart senders models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class AutoGenerateMailboxesRequest(BaseModel):
    domain_id: Optional[int] = None
    count: Optional[int] = None
    prefix_pattern: Optional[str] = None


class PlaceOrderRequest(BaseModel):
    domain: Optional[str] = None
    vendor_id: Optional[int] = None
    mailbox_count: Optional[int] = None
    plan: Optional[str] = None
