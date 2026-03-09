"""SmartleadClient -- facade composing all API modules."""

from __future__ import annotations

from ._base_client import BaseSmartleadClient
from ._config import SmartleadConfig
from .modules.campaigns import CampaignsModule
from .modules.leads import LeadsModule
from .modules.email_accounts import EmailAccountsModule
from .modules.sequences import SequencesModule
from .modules.analytics import AnalyticsModule
from .modules.global_analytics import GlobalAnalyticsModule
from .modules.webhooks import WebhooksModule
from .modules.block_list import BlockListModule
from .modules.clients import ClientsModule
from .modules.master_inbox import MasterInboxModule
from .modules.smart_delivery import SmartDeliveryModule
from .modules.smart_senders import SmartSendersModule
from .modules.smart_prospect import SmartProspectModule


class SmartleadClient:
    """High-level Smartlead API client.

    Composes all 13 domain modules into a single entry point::

        client = SmartleadClient(api_key="YOUR_KEY")
        campaigns = await client.campaigns.create(name="My Campaign")
        leads = await client.leads.add_to_campaign(campaign_id=123, leads=[...])
        stats = await client.analytics.get_statistics(campaign_id=123)
        await client.close()

    Can also be used as an async context manager::

        async with SmartleadClient(api_key="YOUR_KEY") as client:
            campaigns = await client.campaigns.create(name="My Campaign")
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://server.smartlead.ai/api/v1",
        smart_delivery_base_url: str = "https://smartdelivery.smartlead.ai/api/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self._config = SmartleadConfig(
            api_key=api_key,
            base_url=base_url,
            smart_delivery_base_url=smart_delivery_base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._base_client = BaseSmartleadClient(self._config)

        # Domain modules
        self.campaigns = CampaignsModule(self._base_client)
        self.leads = LeadsModule(self._base_client)
        self.email_accounts = EmailAccountsModule(self._base_client)
        self.sequences = SequencesModule(self._base_client)
        self.analytics = AnalyticsModule(self._base_client)
        self.global_analytics = GlobalAnalyticsModule(self._base_client)
        self.webhooks = WebhooksModule(self._base_client)
        self.block_list = BlockListModule(self._base_client)
        self.clients = ClientsModule(self._base_client)
        self.master_inbox = MasterInboxModule(self._base_client)
        self.smart_delivery = SmartDeliveryModule(self._base_client)
        self.smart_senders = SmartSendersModule(self._base_client)
        self.smart_prospect = SmartProspectModule(self._base_client)

    async def close(self) -> None:
        """Close the underlying HTTP clients."""
        await self._base_client.close()

    async def __aenter__(self) -> SmartleadClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()
