"""Global block list endpoints (~3 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.block_list import AddBlockListRequest, AddBlockListResponse, BlockListEntry


class BlockListModule:
    """Global block list API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def add(self, domains: list[str], client_id: Optional[int] = None) -> AddBlockListResponse:
        """POST /leads/add-domain-block-list"""
        body = AddBlockListRequest(domain_block_list=domains, client_id=client_id)
        data = await self._client.post("/leads/add-domain-block-list", json=body.model_dump(exclude_none=True))
        return AddBlockListResponse(**data)

    async def list(
        self,
        offset: int = 0,
        limit: int = 100,
        filter_client_id: Optional[str] = None,
        filter_email_or_domain: Optional[str] = None,
        filter_email_with_domain: Optional[str] = None,
    ) -> list[BlockListEntry]:
        """GET /leads/get-domain-block-list"""
        params: dict[str, Any] = {"offset": offset, "limit": limit}
        if filter_client_id:
            params["filter_client_id"] = filter_client_id
        if filter_email_or_domain:
            params["filter_email_or_domain"] = filter_email_or_domain
        if filter_email_with_domain:
            params["filter_email_with_domain"] = filter_email_with_domain
        data = await self._client.get("/leads/get-domain-block-list", params=params)
        return [BlockListEntry(**item) for item in data]

    async def delete(self, entry_id: int) -> dict[str, Any]:
        """DELETE /leads/delete-domain-block-list"""
        return await self._client.delete("/leads/delete-domain-block-list", params={"id": entry_id})
