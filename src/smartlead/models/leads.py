"""Lead request/response models."""

from __future__ import annotations

from typing import Union, Optional, Any

from pydantic import BaseModel


class LeadData(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    phone_number: Optional[Union[int, str]] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    custom_fields: Optional[dict[str, Any]] = None
    linkedin_profile: Optional[str] = None
    company_url: Optional[str] = None


class AddLeadsSettings(BaseModel):
    ignore_global_block_list: bool = False
    ignore_unsubscribe_list: bool = False
    ignore_community_bounce_list: bool = False
    ignore_duplicate_leads_in_other_campaign: bool = False
    return_lead_ids: bool = True


class AddLeadsRequest(BaseModel):
    lead_list: list[LeadData]
    settings: Optional[AddLeadsSettings] = None


class EmailToLeadIdMap(BaseModel):
    newlyAddedLeads: Optional[dict[str, str]] = None
    existingLeads: Optional[dict[str, str]] = None
    existingLeadsInOtherCampaigns: Optional[dict[str, str]] = None


class AddLeadsResponse(BaseModel):
    ok: bool
    upload_count: Optional[int] = None
    total_leads: Optional[int] = None
    already_added_to_campaign: Optional[int] = None
    duplicate_count: Optional[int] = None
    invalid_email_count: Optional[int] = None
    unsubscribed_leads: Optional[int] = None
    is_lead_limit_exhausted: Optional[bool] = None
    lead_import_stopped_count: Optional[int] = None
    error: Optional[str] = None
    emailToLeadIdMap: Optional[EmailToLeadIdMap] = None


class LeadInCampaign(BaseModel):
    id: Optional[Union[int, str]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[Union[int, str]] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    custom_fields: Optional[dict[str, Any]] = None
    linkedin_profile: Optional[str] = None
    company_url: Optional[str] = None
    is_unsubscribed: Optional[bool] = None


class CampaignLeadEntry(BaseModel):
    campaign_lead_map_id: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    lead: Optional[LeadInCampaign] = None


class ListLeadsResponse(BaseModel):
    total_leads: Optional[int] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    data: Optional[list[CampaignLeadEntry]] = None


class GlobalLeadCampaign(BaseModel):
    campaign_id: Optional[int] = None
    lead_status: Optional[str] = None
    campaign_name: Optional[str] = None
    lead_added_at: Optional[str] = None
    campaign_status: Optional[str] = None
    email_lead_map_id: Optional[int] = None
    lead_last_seq_number: Optional[int] = None


class GlobalLead(BaseModel):
    id: Optional[Union[int, str]] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    company_url: Optional[str] = None
    phone_number: Optional[Union[int, str]] = None
    location: Optional[str] = None
    custom_fields: Optional[dict[str, Any]] = None
    linkedin_profile: Optional[str] = None
    created_at: Optional[str] = None
    user_id: Optional[int] = None
    campaigns: Optional[list[GlobalLeadCampaign]] = None


class GlobalLeadsResponse(BaseModel):
    data: Optional[list[GlobalLead]] = None
    skip: Optional[int] = None
    limit: Optional[int] = None
    hasMore: Optional[bool] = None


class LeadCategory(BaseModel):
    id: int
    created_at: Optional[str] = None
    name: Optional[str] = None
    sentiment_type: Optional[str] = None


class UpdateLeadRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[Union[int, str]] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    custom_fields: Optional[dict[str, Any]] = None
    linkedin_profile: Optional[str] = None
    company_url: Optional[str] = None


class UpdateCategoryRequest(BaseModel):
    category_id: int
    pause_lead: bool = False


class ResumeLeadRequest(BaseModel):
    resume_lead_with_delay_days: Optional[int] = 0


class MoveToInactiveFilters(BaseModel):
    campaignId: Optional[str] = None
    status: Optional[str] = None
    leadCategoryIds: Optional[str] = None
    emailStatus: Optional[str] = None


class MoveToInactiveRequest(BaseModel):
    listId: int
    leadIds: Optional[list[int]] = None
    allLeads: bool = False
    filters: Optional[MoveToInactiveFilters] = None
    action: str = "move"


class PushToCampaignRequest(BaseModel):
    campaign_id: Optional[int] = None
    lead_ids: Optional[list[int]] = None


class LeadByEmailResponse(BaseModel):
    id: Optional[Union[int, str]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    phone_number: Optional[str] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    custom_fields: Optional[dict[str, Any]] = None
    linkedin_profile: Optional[str] = None
    is_unsubscribed: Optional[bool] = None
    unsubscribed_client_id_map: Optional[dict[str, Any]] = None
    lead_campaign_data: Optional[list[dict[str, Any]]] = None


class MessageHistoryEntry(BaseModel):
    type: Optional[str] = None
    message_id: Optional[str] = None
    stats_id: Optional[str] = None
    time: Optional[str] = None
    email_body: Optional[str] = None
    subject: Optional[str] = None
    email_seq_number: Optional[str] = None
    open_count: Optional[int] = None
    click_count: Optional[int] = None
    click_details: Optional[dict[str, Any]] = None


class MessageHistoryResponse(BaseModel):
    history: Optional[list[MessageHistoryEntry]] = None
    from_email: Optional[str] = None
    to: Optional[str] = None
