"""Smart senders endpoints (~7 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.smart_senders import AutoGenerateMailboxesRequest, PlaceOrderRequest


class SmartSendersModule:
    """Smart senders API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def get_mailbox_otp(self) -> Any:
        """GET /smart-senders/mailbox-otp"""
        return await self._client.get("/smart-senders/mailbox-otp")

    async def auto_generate_mailboxes(self, **kwargs: Any) -> Any:
        """POST /smart-senders/auto-generate-mailboxes"""
        body = AutoGenerateMailboxesRequest(**kwargs)
        return await self._client.post("/smart-senders/auto-generate-mailboxes", json=body.model_dump(exclude_none=True))

    async def search_domain(self, query: str) -> Any:
        """GET /smart-senders/search-domain"""
        return await self._client.get("/smart-senders/search-domain", params={"query": query})

    async def get_vendors(self) -> Any:
        """GET /smart-senders/vendors"""
        return await self._client.get("/smart-senders/vendors")

    async def place_order(self, **kwargs: Any) -> Any:
        """POST /smart-senders/place-order"""
        body = PlaceOrderRequest(**kwargs)
        return await self._client.post("/smart-senders/place-order", json=body.model_dump(exclude_none=True))

    async def list_domains(self) -> Any:
        """GET /smart-senders/domain-list"""
        return await self._client.get("/smart-senders/domain-list")

    async def get_order_details(self, order_id: Optional[int] = None) -> Any:
        """GET /smart-senders/order-details"""
        params = {"order_id": order_id} if order_id else None
        return await self._client.get("/smart-senders/order-details", params=params)
