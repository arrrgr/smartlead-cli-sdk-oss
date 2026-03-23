"""Email account management endpoints (~16 endpoints)."""

from __future__ import annotations

from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.email_accounts import (
    CreateEmailAccountRequest,
    CreateEmailAccountResponse,
    EmailAccountResponse,
    UpdateEmailAccountRequest,
    AddToCampaignRequest,
    RemoveFromCampaignRequest,
    UpdateWarmupRequest,
    WarmupStatsResponse,
    FetchMessagesRequest,
    BulkDeleteRequest,
    SaveOAuthEmailAccountRequest,
)


class EmailAccountsModule:
    """Email account management API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def create(self, **kwargs: Any) -> CreateEmailAccountResponse:
        """POST /email-accounts/save"""
        body = CreateEmailAccountRequest(**kwargs)
        data = await self._client.post("/email-accounts/save", json=body.model_dump(exclude_none=True))
        return CreateEmailAccountResponse(**data)

    async def list_all(
        self,
        offset: int = 0,
        limit: int = 100,
        username: Optional[str] = None,
        client_id: Optional[str] = None,
    ) -> list[EmailAccountResponse]:
        """GET /email-accounts/"""
        params: dict[str, Any] = {"offset": offset, "limit": limit}
        if username:
            params["username"] = username
        if client_id:
            params["client_id"] = client_id
        data = await self._client.get("/email-accounts/", params=params)
        return [EmailAccountResponse(**item) for item in data]

    async def get(
        self,
        account_id: int,
        fetch_campaigns: bool = False,
        fetch_tags: bool = False,
    ) -> EmailAccountResponse:
        """GET /email-accounts/{id}/"""
        params: dict[str, Any] = {}
        if fetch_campaigns:
            params["fetch_campaigns"] = True
        if fetch_tags:
            params["fetch_tags"] = True
        data = await self._client.get(f"/email-accounts/{account_id}/", params=params if params else None)
        return EmailAccountResponse(**data)

    async def update(self, account_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /email-accounts/{id}"""
        body = UpdateEmailAccountRequest(**kwargs)
        return await self._client.post(
            f"/email-accounts/{account_id}",
            json=body.model_dump(exclude_none=True),
        )

    async def add_to_campaign(self, campaign_id: int, email_account_ids: list[int]) -> dict[str, Any]:
        """POST /campaigns/{id}/email-accounts"""
        body = AddToCampaignRequest(email_account_ids=email_account_ids)
        return await self._client.post(
            f"/campaigns/{campaign_id}/email-accounts",
            json=body.model_dump(),
        )

    async def remove_from_campaign(self, campaign_id: int, email_account_ids: list[int]) -> dict[str, Any]:
        """DELETE /campaigns/{id}/email-accounts"""
        body = RemoveFromCampaignRequest(email_accounts_ids=email_account_ids)
        return await self._client.delete(
            f"/campaigns/{campaign_id}/email-accounts",
            json=body.model_dump(),
        )

    async def list_by_campaign(self, campaign_id: int) -> list[EmailAccountResponse]:
        """GET /campaigns/{id}/email-accounts"""
        data = await self._client.get(f"/campaigns/{campaign_id}/email-accounts")
        return [EmailAccountResponse(**item) for item in data]

    async def update_warmup(self, account_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /email-accounts/{id}/warmup"""
        body = UpdateWarmupRequest(**kwargs)
        return await self._client.post(
            f"/email-accounts/{account_id}/warmup",
            json=body.model_dump(exclude_none=True),
        )

    async def get_warmup_stats(self, account_id: int) -> WarmupStatsResponse:
        """GET /email-accounts/{id}/warmup-stats"""
        data = await self._client.get(f"/email-accounts/{account_id}/warmup-stats")
        return WarmupStatsResponse(**data)

    async def reconnect_failed(self) -> dict[str, Any]:
        """POST /email-accounts/reconnect-failed-email-accounts"""
        return await self._client.post("/email-accounts/reconnect-failed-email-accounts", json={})

    async def fetch_messages(self, account_id: int, **kwargs: Any) -> dict[str, Any]:
        """POST /email-accounts/{id}/fetch-messages"""
        body = FetchMessagesRequest(**kwargs)
        payload = body.model_dump(exclude_none=True)
        # Rename fields to match API expectations
        if "from_time" in payload:
            payload["from"] = payload.pop("from_time")
        if "to_time" in payload:
            payload["to"] = payload.pop("to_time")
        return await self._client.post(f"/email-accounts/{account_id}/fetch-messages", json=payload)

    async def delete(self, account_id: int) -> dict[str, Any]:
        """DELETE /email-accounts/{id}"""
        return await self._client.delete(f"/email-accounts/{account_id}")

    async def bulk_delete(self, account_ids: list[int]) -> dict[str, Any]:
        """POST /email-accounts/bulk-delete"""
        body = BulkDeleteRequest(ids=account_ids)
        return await self._client.post("/email-accounts/bulk-delete", json=body.model_dump())

    async def save_oauth_email_account(self, **kwargs: Any) -> dict[str, Any]:
        """POST /email-accounts/save-oauth"""
        body = SaveOAuthEmailAccountRequest(**kwargs)
        return await self._client.post("/email-accounts/save-oauth", json=body.model_dump(exclude_none=True))

    async def disconnect_google(self, account_id: int) -> dict[str, Any]:
        """POST /email-accounts/{id}/disconnect-google"""
        return await self._client.post(f"/email-accounts/{account_id}/disconnect-google", json={})

    async def disconnect_microsoft(self, account_id: int) -> dict[str, Any]:
        """POST /email-accounts/{id}/disconnect-microsoft"""
        return await self._client.post(f"/email-accounts/{account_id}/disconnect-microsoft", json={})
