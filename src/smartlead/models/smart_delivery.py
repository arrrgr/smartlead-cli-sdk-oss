"""Smart Delivery models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class ManualPlacementRequest(BaseModel):
    name: Optional[str] = None
    email_account_ids: Optional[list[int]] = None
    provider_ids: Optional[list[int]] = None
    subject: Optional[str] = None
    email_body: Optional[str] = None
    folder_id: Optional[int] = None


class AutomatedPlacementRequest(BaseModel):
    name: Optional[str] = None
    email_account_ids: Optional[list[int]] = None
    provider_ids: Optional[list[int]] = None
    subject: Optional[str] = None
    email_body: Optional[str] = None
    frequency: Optional[str] = None
    folder_id: Optional[int] = None


class ListTestsRequest(BaseModel):
    offset: int = 0
    limit: int = 20
    folder_id: Optional[int] = None
    search: Optional[str] = None


class CreateFolderRequest(BaseModel):
    name: str


class SpamTestResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    test_type: Optional[str] = None
