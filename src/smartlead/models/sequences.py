"""Campaign sequence models."""

from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class SequenceVariant(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: Optional[bool] = None
    subject: Optional[str] = None
    email_body: Optional[str] = None
    email_campaign_seq_id: Optional[int] = None
    variant_label: Optional[str] = None
    variant_distribution_percentage: Optional[int] = None


class SequenceStep(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    email_campaign_id: Optional[int] = None
    seq_number: Optional[int] = None
    subject: Optional[str] = None
    email_body: Optional[str] = None
    sequence_variants: Optional[list[SequenceVariant]] = None


class SeqDelayDetails(BaseModel):
    delay_in_days: int = 1


class SaveSequenceVariant(BaseModel):
    subject: str
    email_body: str
    variant_label: Optional[str] = None
    id: Optional[int] = None
    variant_distribution_percentage: Optional[int] = None


class SaveSequenceStep(BaseModel):
    id: Optional[int] = None
    seq_number: int
    seq_delay_details: Optional[SeqDelayDetails] = None
    variant_distribution_type: Optional[str] = None
    lead_distribution_percentage: Optional[int] = None
    winning_metric_property: Optional[str] = None
    seq_variants: Optional[list[SaveSequenceVariant]] = None
    seq_type: str = "EMAIL"
    subject: Optional[str] = None
    email_body: Optional[str] = None


class SaveSequencesRequest(BaseModel):
    sequences: list[SaveSequenceStep]
