"""Client management models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class CreateClientRequest(BaseModel):
    name: str
    email: str
    permission: Optional[list[str]] = None
    logo: Optional[str] = None
    logo_url: Optional[str] = None
    password: Optional[str] = None


class CreateClientResponse(BaseModel):
    ok: bool = True
    clientId: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class ClientPermission(BaseModel):
    permission: Optional[list[str]] = None
    retricted_category: Optional[list[Any]] = None


class ClientResponse(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    user_id: Optional[int] = None
    logo: Optional[str] = None
    logo_url: Optional[str] = None
    client_permision: Optional[ClientPermission] = None


class CreateApiKeyRequest(BaseModel):
    keyName: str
    clientId: str


class ApiKeyResponse(BaseModel):
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    client_id: Optional[int] = None
    api_key: Optional[str] = None
    deleted_at: Optional[str] = None
