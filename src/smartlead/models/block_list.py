"""Global block list models."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class AddBlockListRequest(BaseModel):
    domain_block_list: list[str]
    client_id: Optional[int] = None


class AddBlockListResponse(BaseModel):
    uploadCount: Optional[int] = None
    totalDomainAdded: Optional[int] = None


class BlockListEntry(BaseModel):
    id: int
    email_or_domain: Optional[str] = None
    created_at: Optional[str] = None
    source: Optional[str] = None
    client_id: Optional[int] = None
