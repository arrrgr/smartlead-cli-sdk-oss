"""Smart prospect models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class SearchContactsRequest(BaseModel):
    filters: Optional[dict[str, Any]] = None
    offset: int = 0
    limit: int = 25


class FetchContactsRequest(BaseModel):
    contact_ids: Optional[list[int]] = None
    search_id: Optional[int] = None


class GetContactsRequest(BaseModel):
    contact_ids: Optional[list[int]] = None


class ReviewContactsRequest(BaseModel):
    contact_ids: Optional[list[int]] = None
    status: Optional[str] = None


class SaveSearchRequest(BaseModel):
    name: str
    filters: Optional[dict[str, Any]] = None


class UpdateSavedSearchRequest(BaseModel):
    search_id: int
    name: Optional[str] = None
    filters: Optional[dict[str, Any]] = None


class UpdateFetchedLeadRequest(BaseModel):
    lead_id: int
    data: Optional[dict[str, Any]] = None


class FindEmailsRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    domain: Optional[str] = None
    company_name: Optional[str] = None
    linkedin_url: Optional[str] = None
