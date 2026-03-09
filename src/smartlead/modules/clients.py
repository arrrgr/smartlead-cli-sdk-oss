"""Client management endpoints (~6 endpoints)."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.clients import (
    CreateClientRequest,
    CreateClientResponse,
    ClientResponse,
    CreateApiKeyRequest,
)


class ClientsModule:
    """Client management API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def create(self, **kwargs: Any) -> CreateClientResponse:
        """POST /client/save"""
        body = CreateClientRequest(**kwargs)
        data = await self._client.post("/client/save", json=body.model_dump(exclude_none=True))
        return CreateClientResponse(**data)

    async def list_all(self) -> list[ClientResponse]:
        """GET /client/"""
        data = await self._client.get("/client/")
        return [ClientResponse(**item) for item in data]

    async def create_api_key(self, key_name: str, client_id: str) -> dict[str, Any]:
        """POST /client/api-key"""
        body = CreateApiKeyRequest(keyName=key_name, clientId=client_id)
        return await self._client.post("/client/api-key", json=body.model_dump())

    async def list_api_keys(self) -> Any:
        """GET /client/api-key"""
        return await self._client.get("/client/api-key")

    async def delete_api_key(self, api_key_id: int) -> dict[str, Any]:
        """DELETE /client/api-key"""
        return await self._client.delete("/client/api-key", json={"id": api_key_id})

    async def reset_api_key(self, api_key_id: int) -> dict[str, Any]:
        """PUT /client/api-key"""
        return await self._client.put("/client/api-key", json={"id": api_key_id})
