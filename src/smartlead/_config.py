"""Smartlead client configuration."""

from __future__ import annotations

from pydantic import BaseModel, Field


class SmartleadConfig(BaseModel):
    """Configuration for the Smartlead API client."""

    api_key: str = Field(..., description="Smartlead API key")
    base_url: str = Field(
        default="https://server.smartlead.ai/api/v1",
        description="Base URL for the Smartlead API",
    )
    smart_delivery_base_url: str = Field(
        default="https://smartdelivery.smartlead.ai/api/v1",
        description="Base URL for Smart Delivery endpoints",
    )
    timeout: float = Field(default=30.0, description="Request timeout in seconds")
    max_retries: int = Field(default=3, description="Maximum retry attempts on 5xx/network errors")
    retry_base_delay: float = Field(default=1.0, description="Base delay for exponential backoff (seconds)")
    retry_max_delay: float = Field(default=10.0, description="Maximum retry delay (seconds)")
    rate_limit_rpm: int = Field(default=60, description="Rate limit: requests per minute")
