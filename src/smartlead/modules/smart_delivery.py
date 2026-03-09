"""Smart Delivery endpoints (~28 endpoints). Uses separate base URL."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.smart_delivery import (
    ManualPlacementRequest,
    AutomatedPlacementRequest,
    ListTestsRequest,
    CreateFolderRequest,
)


class SmartDeliveryModule:
    """Smart Delivery API -- uses smartdelivery.smartlead.ai."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def get_providers(self) -> Any:
        """GET /smart-delivery/region-provider-ids"""
        return await self._client.get("/smart-delivery/region-provider-ids", smart_delivery=True)

    async def create_manual_test(self, **kwargs: Any) -> Any:
        """POST /smart-delivery/manual-placement"""
        body = ManualPlacementRequest(**kwargs)
        return await self._client.post("/smart-delivery/manual-placement", json=body.model_dump(exclude_none=True), smart_delivery=True)

    async def create_automated_test(self, **kwargs: Any) -> Any:
        """POST /smart-delivery/automated-placement"""
        body = AutomatedPlacementRequest(**kwargs)
        return await self._client.post("/smart-delivery/automated-placement", json=body.model_dump(exclude_none=True), smart_delivery=True)

    async def get_test(self, test_id: int) -> Any:
        """GET /smart-delivery/spam-test/{id}"""
        return await self._client.get(f"/smart-delivery/spam-test/{test_id}", smart_delivery=True)

    async def delete_tests(self, test_ids: list[int]) -> Any:
        """POST /smart-delivery/delete-tests"""
        return await self._client.post("/smart-delivery/delete-tests", json={"test_ids": test_ids}, smart_delivery=True)

    async def stop_automated_test(self, test_id: int) -> Any:
        """PUT /smart-delivery/stop-automated-test"""
        return await self._client.put("/smart-delivery/stop-automated-test", json={"test_id": test_id}, smart_delivery=True)

    async def list_tests(self, offset: int = 0, limit: int = 20, **kwargs: Any) -> Any:
        """POST /smart-delivery/list-tests"""
        body = ListTestsRequest(offset=offset, limit=limit, **kwargs)
        return await self._client.post("/smart-delivery/list-tests", json=body.model_dump(exclude_none=True), smart_delivery=True)

    async def get_provider_report(self, test_id: int, **kwargs: Any) -> Any:
        """POST /smart-delivery/provider-wise-results"""
        return await self._client.post("/smart-delivery/provider-wise-results", json={"test_id": test_id, **kwargs}, smart_delivery=True)

    async def get_geo_report(self, test_id: int, **kwargs: Any) -> Any:
        """POST /smart-delivery/geo-wise-report"""
        return await self._client.post("/smart-delivery/geo-wise-report", json={"test_id": test_id, **kwargs}, smart_delivery=True)

    async def get_sender_report(self, test_id: int) -> Any:
        """GET /smart-delivery/sender-account-report"""
        return await self._client.get("/smart-delivery/sender-account-report", params={"test_id": test_id}, smart_delivery=True)

    async def get_spam_filter_report(self, test_id: int) -> Any:
        """GET /smart-delivery/spam-filter-report"""
        return await self._client.get("/smart-delivery/spam-filter-report", params={"test_id": test_id}, smart_delivery=True)

    async def get_dkim(self, test_id: int) -> Any:
        """GET /smart-delivery/dkim-details"""
        return await self._client.get("/smart-delivery/dkim-details", params={"test_id": test_id}, smart_delivery=True)

    async def get_spf(self, test_id: int) -> Any:
        """GET /smart-delivery/spf-details"""
        return await self._client.get("/smart-delivery/spf-details", params={"test_id": test_id}, smart_delivery=True)

    async def get_rdns(self, test_id: int) -> Any:
        """GET /smart-delivery/rdns-report"""
        return await self._client.get("/smart-delivery/rdns-report", params={"test_id": test_id}, smart_delivery=True)

    async def get_sender_accounts(self, test_id: int) -> Any:
        """GET /smart-delivery/sender-account-list"""
        return await self._client.get("/smart-delivery/sender-account-list", params={"test_id": test_id}, smart_delivery=True)

    async def get_ip_blacklists(self, test_id: int) -> Any:
        """GET /smart-delivery/blacklists"""
        return await self._client.get("/smart-delivery/blacklists", params={"test_id": test_id}, smart_delivery=True)

    async def get_domain_blacklist(self, test_id: int) -> Any:
        """GET /smart-delivery/domain-blacklist"""
        return await self._client.get("/smart-delivery/domain-blacklist", params={"test_id": test_id}, smart_delivery=True)

    async def get_test_email_content(self, test_id: int) -> Any:
        """GET /smart-delivery/test-email-content"""
        return await self._client.get("/smart-delivery/test-email-content", params={"test_id": test_id}, smart_delivery=True)

    async def get_ip_blacklist_count(self, test_id: int) -> Any:
        """GET /smart-delivery/ip-blacklist-count"""
        return await self._client.get("/smart-delivery/ip-blacklist-count", params={"test_id": test_id}, smart_delivery=True)

    async def get_email_headers(self, test_id: int) -> Any:
        """GET /smart-delivery/email-headers"""
        return await self._client.get("/smart-delivery/email-headers", params={"test_id": test_id}, smart_delivery=True)

    async def get_schedule_history(self, test_id: int) -> Any:
        """GET /smart-delivery/schedule-history"""
        return await self._client.get("/smart-delivery/schedule-history", params={"test_id": test_id}, smart_delivery=True)

    async def get_ip_details(self, test_id: int) -> Any:
        """GET /smart-delivery/ip-details"""
        return await self._client.get("/smart-delivery/ip-details", params={"test_id": test_id}, smart_delivery=True)

    async def get_mailbox_summary(self, test_id: int) -> Any:
        """GET /smart-delivery/mailbox-summary"""
        return await self._client.get("/smart-delivery/mailbox-summary", params={"test_id": test_id}, smart_delivery=True)

    async def get_mailbox_count(self, test_id: int) -> Any:
        """GET /smart-delivery/mailbox-count"""
        return await self._client.get("/smart-delivery/mailbox-count", params={"test_id": test_id}, smart_delivery=True)

    async def list_folders(self) -> Any:
        """GET /smart-delivery/folders"""
        return await self._client.get("/smart-delivery/folders", smart_delivery=True)

    async def create_folder(self, name: str) -> Any:
        """POST /smart-delivery/folders"""
        body = CreateFolderRequest(name=name)
        return await self._client.post("/smart-delivery/folders", json=body.model_dump(), smart_delivery=True)

    async def get_folder(self, folder_id: int) -> Any:
        """GET /smart-delivery/folders/{id}"""
        return await self._client.get(f"/smart-delivery/folders/{folder_id}", smart_delivery=True)

    async def delete_folder(self, folder_id: int) -> Any:
        """DELETE /smart-delivery/folders/{id}"""
        return await self._client.delete(f"/smart-delivery/folders/{folder_id}", smart_delivery=True)
