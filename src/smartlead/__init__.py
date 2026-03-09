"""Smartlead Python SDK.

Usage::

    from smartlead import SmartleadClient

    async with SmartleadClient(api_key="YOUR_KEY") as client:
        campaign = await client.campaigns.create(name="My Campaign")
"""

from ._client import SmartleadClient
from ._config import SmartleadConfig
from ._errors import (
    SmartleadError,
    SmartleadAuthError,
    SmartleadNotFoundError,
    SmartleadRateLimitError,
    SmartleadValidationError,
    SmartleadServerError,
)

__all__ = [
    "SmartleadClient",
    "SmartleadConfig",
    "SmartleadError",
    "SmartleadAuthError",
    "SmartleadNotFoundError",
    "SmartleadRateLimitError",
    "SmartleadValidationError",
    "SmartleadServerError",
]
