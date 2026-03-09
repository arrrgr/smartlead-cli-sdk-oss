"""Smart prospect endpoints (~26 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.smart_prospect import (
    SearchContactsRequest,
    FetchContactsRequest,
    GetContactsRequest,
    ReviewContactsRequest,
    SaveSearchRequest,
    UpdateSavedSearchRequest,
    UpdateFetchedLeadRequest,
    FindEmailsRequest,
)


class SmartProspectModule:
    """Smart prospect API -- contact discovery and enrichment."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    # -- Lookup endpoints (GET) --

    async def get_departments(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/departments"""
        return await self._client.get("/smart-prospect/departments", params=kwargs or None)

    async def get_cities(self, query: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/cities"""
        params = {k: v for k, v in {**kwargs, "query": query}.items() if v is not None}
        return await self._client.get("/smart-prospect/cities", params=params or None)

    async def get_countries(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/countries"""
        return await self._client.get("/smart-prospect/countries", params=kwargs or None)

    async def get_states(self, country: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/states"""
        params = {k: v for k, v in {**kwargs, "country": country}.items() if v is not None}
        return await self._client.get("/smart-prospect/states", params=params or None)

    async def get_industries(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/industries"""
        return await self._client.get("/smart-prospect/industries", params=kwargs or None)

    async def get_sub_industries(self, industry_id: Optional[int] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/sub-industries"""
        params = {k: v for k, v in {**kwargs, "industry_id": industry_id}.items() if v is not None}
        return await self._client.get("/smart-prospect/sub-industries", params=params or None)

    async def get_head_counts(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/head-counts"""
        return await self._client.get("/smart-prospect/head-counts", params=kwargs or None)

    async def get_levels(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/levels"""
        return await self._client.get("/smart-prospect/levels", params=kwargs or None)

    async def get_revenue_options(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/revenue"""
        return await self._client.get("/smart-prospect/revenue", params=kwargs or None)

    async def get_companies(self, query: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/companies"""
        params = {k: v for k, v in {**kwargs, "query": query}.items() if v is not None}
        return await self._client.get("/smart-prospect/companies", params=params or None)

    async def get_domains(self, query: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/domains"""
        params = {k: v for k, v in {**kwargs, "query": query}.items() if v is not None}
        return await self._client.get("/smart-prospect/domains", params=params or None)

    async def get_job_titles(self, query: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/job-titles"""
        params = {k: v for k, v in {**kwargs, "query": query}.items() if v is not None}
        return await self._client.get("/smart-prospect/job-titles", params=params or None)

    async def get_keywords(self, query: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /smart-prospect/keywords"""
        params = {k: v for k, v in {**kwargs, "query": query}.items() if v is not None}
        return await self._client.get("/smart-prospect/keywords", params=params or None)

    # -- Contact operations (POST/PATCH) --

    async def search_contacts(self, filters: Optional[dict[str, Any]] = None, offset: int = 0, limit: int = 25) -> Any:
        """POST /smart-prospect/search-contacts"""
        body = SearchContactsRequest(filters=filters, offset=offset, limit=limit)
        return await self._client.post("/smart-prospect/search-contacts", json=body.model_dump(exclude_none=True))

    async def fetch_contacts(self, contact_ids: Optional[list[int]] = None, search_id: Optional[int] = None) -> Any:
        """POST /smart-prospect/fetch-contacts"""
        body = FetchContactsRequest(contact_ids=contact_ids, search_id=search_id)
        return await self._client.post("/smart-prospect/fetch-contacts", json=body.model_dump(exclude_none=True))

    async def get_contacts(self, contact_ids: list[int]) -> Any:
        """POST /smart-prospect/get-contacts"""
        body = GetContactsRequest(contact_ids=contact_ids)
        return await self._client.post("/smart-prospect/get-contacts", json=body.model_dump(exclude_none=True))

    async def review_contacts(self, contact_ids: list[int], status: str) -> Any:
        """PATCH /smart-prospect/review-contacts"""
        body = ReviewContactsRequest(contact_ids=contact_ids, status=status)
        return await self._client.patch("/smart-prospect/review-contacts", json=body.model_dump(exclude_none=True))

    # -- Search management --

    async def get_saved_searches(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/saved-searches"""
        return await self._client.get("/smart-prospect/saved-searches", params=kwargs or None)

    async def get_recent_searches(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/recent-searches"""
        return await self._client.get("/smart-prospect/recent-searches", params=kwargs or None)

    async def get_fetched_searches(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/fetched-searches"""
        return await self._client.get("/smart-prospect/fetched-searches", params=kwargs or None)

    async def save_search(self, name: str, filters: Optional[dict[str, Any]] = None) -> Any:
        """POST /smart-prospect/save-search"""
        body = SaveSearchRequest(name=name, filters=filters)
        return await self._client.post("/smart-prospect/save-search", json=body.model_dump(exclude_none=True))

    async def update_saved_search(self, search_id: int, **kwargs: Any) -> Any:
        """PUT /smart-prospect/update-saved-search"""
        body = UpdateSavedSearchRequest(search_id=search_id, **kwargs)
        return await self._client.put("/smart-prospect/update-saved-search", json=body.model_dump(exclude_none=True))

    async def update_fetched_lead(self, lead_id: int, data: Optional[dict[str, Any]] = None) -> Any:
        """PUT /smart-prospect/update-fetched-lead"""
        body = UpdateFetchedLeadRequest(lead_id=lead_id, data=data)
        return await self._client.put("/smart-prospect/update-fetched-lead", json=body.model_dump(exclude_none=True))

    # -- Analytics --

    async def get_search_analytics(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/search-analytics"""
        return await self._client.get("/smart-prospect/search-analytics", params=kwargs or None)

    async def get_reply_analytics(self, **kwargs: Any) -> Any:
        """GET /smart-prospect/reply-analytics"""
        return await self._client.get("/smart-prospect/reply-analytics", params=kwargs or None)

    async def find_emails(self, **kwargs: Any) -> Any:
        """POST /smart-prospect/find-emails"""
        body = FindEmailsRequest(**kwargs)
        return await self._client.post("/smart-prospect/find-emails", json=body.model_dump(exclude_none=True))
