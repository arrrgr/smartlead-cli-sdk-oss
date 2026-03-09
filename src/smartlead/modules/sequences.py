"""Campaign sequence endpoints (~2 endpoints)."""

from __future__ import annotations

from typing import Union, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .._base_client import BaseSmartleadClient

from ..models.sequences import (
    SequenceStep,
    SaveSequenceStep,
    SaveSequencesRequest,
)


class SequencesModule:
    """Campaign sequence API."""

    def __init__(self, client: BaseSmartleadClient) -> None:
        self._client = client

    async def get(self, campaign_id: int) -> list[SequenceStep]:
        """GET /campaigns/{id}/sequences"""
        data = await self._client.get(f"/campaigns/{campaign_id}/sequences")
        if isinstance(data, list):
            return [SequenceStep(**item) for item in data]
        return [SequenceStep(**data)]

    async def save(self, campaign_id: int, sequences: Union[list[dict[str, Any]], list[SaveSequenceStep]]) -> dict[str, Any]:
        """POST /campaigns/{id}/sequences"""
        steps = [SaveSequenceStep(**s) if isinstance(s, dict) else s for s in sequences]
        body = SaveSequencesRequest(sequences=steps)
        return await self._client.post(
            f"/campaigns/{campaign_id}/sequences",
            json=body.model_dump(exclude_none=True),
        )
