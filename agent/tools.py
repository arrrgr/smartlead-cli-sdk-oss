"""Smartlead tool definitions for the Claude agent.

Complete coverage of all 13 SDK modules and 170+ methods.
Tool naming convention: {module}__{method} (double underscore).
Module names match the attribute names on SmartleadClient.
"""

from __future__ import annotations

TOOLS = [
    # =========================================================================
    # CAMPAIGNS MODULE (9 methods)
    # =========================================================================
    {
        "name": "campaigns__create",
        "description": "Create a new campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Campaign name."},
                "client_id": {"type": "integer", "description": "Optional client ID to associate the campaign with."},
            },
            "required": ["name"],
        },
    },
    {
        "name": "campaigns__get",
        "description": "Get details of a specific campaign by ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "campaigns__delete",
        "description": "Delete a campaign by ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID to delete."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "campaigns__update_schedule",
        "description": "Update schedule settings for a campaign (timezone, days, hours, sending limits).",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "timezone": {"type": "string", "description": "Timezone string, e.g. 'America/New_York'."},
                "days_of_the_week": {"type": "array", "items": {"type": "integer"}, "description": "Days to send (0=Sun, 1=Mon, ..., 6=Sat)."},
                "start_hour": {"type": "string", "description": "Start hour, e.g. '09:00'."},
                "end_hour": {"type": "string", "description": "End hour, e.g. '17:00'."},
                "min_time_btw_emails": {"type": "integer", "description": "Minimum time between emails in minutes."},
                "max_new_leads_per_day": {"type": "integer", "description": "Maximum new leads to contact per day."},
                "schedule_start_time": {"type": "string", "description": "Campaign start time (ISO format)."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "campaigns__update_settings",
        "description": "Update campaign settings (name, tracking, unsubscribe text, plain text mode, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "name": {"type": "string", "description": "New campaign name."},
                "track_settings": {"type": "array", "items": {"type": "string"}, "description": "Tracking settings list."},
                "stop_lead_settings": {"type": "string", "description": "When to stop sending to a lead."},
                "unsubscribe_text": {"type": "string", "description": "Unsubscribe link text."},
                "send_as_plain_text": {"type": "boolean", "description": "Send as plain text."},
                "force_plain_text": {"type": "boolean", "description": "Force plain text mode."},
                "follow_up_percentage": {"type": "integer", "description": "Percentage of leads to follow up."},
                "client_id": {"type": "integer", "description": "Client ID."},
                "enable_ai_esp_matching": {"type": "boolean", "description": "Enable AI ESP matching."},
                "auto_pause_domain_leads_on_reply": {"type": "boolean", "description": "Auto-pause domain leads on reply."},
                "ignore_ss_mailbox_sending_limit": {"type": "boolean", "description": "Ignore Smart Senders mailbox sending limit."},
                "bounce_autopause_threshold": {"type": "string", "description": "Bounce auto-pause threshold."},
                "domain_level_rate_limit": {"type": "boolean", "description": "Enable domain-level rate limiting."},
                "out_of_office_detection_settings": {"type": "object", "description": "OOO detection settings object."},
                "ai_categorisation_options": {"type": "array", "items": {"type": "integer"}, "description": "AI categorization option IDs."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "campaigns__update_status",
        "description": "Update campaign status (START, PAUSED, or STOPPED).",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "status": {"type": "string", "enum": ["START", "PAUSED", "STOPPED"], "description": "New status."},
            },
            "required": ["campaign_id", "status"],
        },
    },
    {
        "name": "campaigns__list_by_lead",
        "description": "List all campaigns a lead belongs to.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["lead_id"],
        },
    },
    {
        "name": "campaigns__export_data",
        "description": "Export campaign leads data as CSV.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "campaigns__create_subsequence",
        "description": "Create a subsequence (child campaign) under a parent campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "parent_campaign_id": {"type": "integer", "description": "The parent campaign ID."},
                "name": {"type": "string", "description": "Optional name for the subsequence."},
            },
            "required": ["parent_campaign_id"],
        },
    },

    # =========================================================================
    # LEADS MODULE (17 methods)
    # =========================================================================
    {
        "name": "leads__add_to_campaign",
        "description": "Add leads to a campaign. Each lead needs at minimum an email address.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "leads": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "email": {"type": "string"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "company_name": {"type": "string"},
                            "phone_number": {"type": "string"},
                            "website": {"type": "string"},
                            "location": {"type": "string"},
                            "linkedin_profile": {"type": "string"},
                            "company_url": {"type": "string"},
                            "custom_fields": {"type": "object"},
                        },
                        "required": ["email"],
                    },
                    "description": "List of lead objects.",
                },
                "settings": {
                    "type": "object",
                    "properties": {
                        "ignore_global_block_list": {"type": "boolean"},
                        "ignore_unsubscribe_list": {"type": "boolean"},
                        "ignore_community_bounce_list": {"type": "boolean"},
                        "ignore_duplicate_leads_in_other_campaign": {"type": "boolean"},
                        "return_lead_ids": {"type": "boolean"},
                    },
                    "description": "Optional import settings.",
                },
            },
            "required": ["campaign_id", "leads"],
        },
    },
    {
        "name": "leads__list_by_campaign",
        "description": "List leads in a campaign with optional filters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max leads to return (default 100)."},
                "status": {"type": "string", "description": "Filter by lead status."},
                "lead_category_id": {"type": "integer", "description": "Filter by lead category ID."},
                "created_at_gt": {"type": "string", "description": "Filter leads created after this datetime."},
                "last_sent_time_gt": {"type": "string", "description": "Filter by last sent time greater than."},
                "event_time_gt": {"type": "string", "description": "Filter by event time greater than."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "leads__get_by_email",
        "description": "Look up a lead by email address across all campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "The email address to look up."},
            },
            "required": ["email"],
        },
    },
    {
        "name": "leads__list_global",
        "description": "List leads globally across all campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max leads to return (default 100)."},
                "created_at_gt": {"type": "string", "description": "Filter leads created after this datetime."},
                "email": {"type": "string", "description": "Filter by email address."},
            },
            "required": [],
        },
    },
    {
        "name": "leads__list_categories",
        "description": "List all available lead categories (e.g. Interested, Not Interested, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "leads__update",
        "description": "Update a lead's data in a specific campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
                "first_name": {"type": "string", "description": "Updated first name."},
                "last_name": {"type": "string", "description": "Updated last name."},
                "email": {"type": "string", "description": "Updated email."},
                "phone_number": {"type": "string", "description": "Updated phone number."},
                "company_name": {"type": "string", "description": "Updated company name."},
                "website": {"type": "string", "description": "Updated website."},
                "location": {"type": "string", "description": "Updated location."},
                "custom_fields": {"type": "object", "description": "Updated custom fields."},
                "linkedin_profile": {"type": "string", "description": "Updated LinkedIn profile URL."},
                "company_url": {"type": "string", "description": "Updated company URL."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__update_category",
        "description": "Update the category of a lead in a campaign (e.g. Interested, Meeting Booked).",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
                "category_id": {"type": "integer", "description": "The category ID to set."},
                "pause_lead": {"type": "boolean", "description": "Whether to pause the lead after categorizing (default false)."},
            },
            "required": ["campaign_id", "lead_id", "category_id"],
        },
    },
    {
        "name": "leads__resume",
        "description": "Resume a paused lead in a campaign, optionally with a delay.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
                "delay_days": {"type": "integer", "description": "Days to wait before resuming (default 0)."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__pause",
        "description": "Pause a lead in a campaign to stop sending emails to them.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__delete",
        "description": "Delete a lead from a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__unsubscribe",
        "description": "Unsubscribe a lead from a specific campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__unsubscribe_all",
        "description": "Unsubscribe a lead from all campaigns globally.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["lead_id"],
        },
    },
    {
        "name": "leads__get_campaign_overview",
        "description": "Get an overview of a lead's status across all campaigns they belong to.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_id": {"type": "integer", "description": "The lead ID."},
            },
            "required": ["lead_id"],
        },
    },
    {
        "name": "leads__get_sequence_details",
        "description": "Get sequence details for a specific lead-campaign mapping.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_map_id": {"type": "integer", "description": "The lead map ID (campaign-lead mapping)."},
            },
            "required": ["lead_map_id"],
        },
    },
    {
        "name": "leads__get_message_history",
        "description": "Get the full email message history for a lead in a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "lead_id": {"type": "integer", "description": "The lead ID."},
                "event_time_gt": {"type": "string", "description": "Filter messages after this datetime."},
            },
            "required": ["campaign_id", "lead_id"],
        },
    },
    {
        "name": "leads__move_to_inactive",
        "description": "Move leads to an inactive list. Can move specific leads or all leads matching filters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "list_id": {"type": "integer", "description": "Target inactive list ID."},
                "lead_ids": {"type": "array", "items": {"type": "integer"}, "description": "Specific lead IDs to move."},
                "all_leads": {"type": "boolean", "description": "Move all leads matching filters (default false)."},
                "filters": {
                    "type": "object",
                    "properties": {
                        "campaignId": {"type": "string"},
                        "status": {"type": "string"},
                        "leadCategoryIds": {"type": "string"},
                        "emailStatus": {"type": "string"},
                    },
                    "description": "Filters for selecting leads to move.",
                },
                "action": {"type": "string", "description": "Action type (default 'move')."},
            },
            "required": ["list_id"],
        },
    },
    {
        "name": "leads__push_to_campaign",
        "description": "Push leads from one source into a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "Target campaign ID."},
                "lead_ids": {"type": "array", "items": {"type": "integer"}, "description": "Lead IDs to push."},
            },
            "required": ["campaign_id"],
        },
    },

    # =========================================================================
    # EMAIL ACCOUNTS MODULE (16 methods)
    # =========================================================================
    {
        "name": "email_accounts__create",
        "description": "Create a new email account with SMTP/IMAP credentials.",
        "input_schema": {
            "type": "object",
            "properties": {
                "from_name": {"type": "string", "description": "Sender display name."},
                "from_email": {"type": "string", "description": "Sender email address."},
                "user_name": {"type": "string", "description": "SMTP/IMAP username."},
                "password": {"type": "string", "description": "SMTP/IMAP password."},
                "smtp_host": {"type": "string", "description": "SMTP server hostname."},
                "smtp_port": {"type": "integer", "description": "SMTP server port."},
                "imap_host": {"type": "string", "description": "IMAP server hostname."},
                "imap_port": {"type": "integer", "description": "IMAP server port."},
                "max_email_per_day": {"type": "integer", "description": "Max emails per day (default 100)."},
                "custom_tracking_url": {"type": "string", "description": "Custom tracking domain URL."},
                "bcc": {"type": "string", "description": "BCC email address."},
                "signature": {"type": "string", "description": "Email signature HTML."},
                "warmup_enabled": {"type": "boolean", "description": "Enable warmup (default false)."},
                "total_warmup_per_day": {"type": "integer", "description": "Total warmup emails per day."},
                "daily_rampup": {"type": "integer", "description": "Daily rampup increment."},
                "reply_rate_percentage": {"type": "integer", "description": "Target warmup reply rate percentage."},
                "client_id": {"type": "integer", "description": "Client ID to associate with."},
            },
            "required": ["from_name", "from_email", "user_name", "password", "smtp_host", "smtp_port", "imap_host", "imap_port"],
        },
    },
    {
        "name": "email_accounts__list_all",
        "description": "List all email accounts with optional filters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max accounts to return (default 100)."},
                "username": {"type": "string", "description": "Filter by username."},
                "client_id": {"type": "string", "description": "Filter by client ID."},
            },
            "required": [],
        },
    },
    {
        "name": "email_accounts__get",
        "description": "Get details of a specific email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
                "fetch_campaigns": {"type": "boolean", "description": "Include associated campaigns (default false)."},
                "fetch_tags": {"type": "boolean", "description": "Include tags (default false)."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__update",
        "description": "Update an email account's settings.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
                "max_email_per_day": {"type": "integer", "description": "Max emails per day."},
                "custom_tracking_url": {"type": "string", "description": "Custom tracking domain."},
                "bcc": {"type": "string", "description": "BCC email address."},
                "signature": {"type": "string", "description": "Email signature HTML."},
                "client_id": {"type": "integer", "description": "Client ID."},
                "time_to_wait_in_mins": {"type": "integer", "description": "Time to wait between emails in minutes."},
                "is_suspended": {"type": "boolean", "description": "Suspend the account."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__add_to_campaign",
        "description": "Add email accounts to a campaign for sending.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "email_account_ids": {"type": "array", "items": {"type": "integer"}, "description": "Email account IDs to add."},
            },
            "required": ["campaign_id", "email_account_ids"],
        },
    },
    {
        "name": "email_accounts__remove_from_campaign",
        "description": "Remove email accounts from a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "email_account_ids": {"type": "array", "items": {"type": "integer"}, "description": "Email account IDs to remove."},
            },
            "required": ["campaign_id", "email_account_ids"],
        },
    },
    {
        "name": "email_accounts__list_by_campaign",
        "description": "List all email accounts assigned to a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "email_accounts__update_warmup",
        "description": "Update warmup settings for an email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
                "warmup_enabled": {"type": "boolean", "description": "Enable or disable warmup."},
                "total_warmup_per_day": {"type": "integer", "description": "Total warmup emails per day."},
                "daily_rampup": {"type": "integer", "description": "Daily rampup increment."},
                "reply_rate_percentage": {"type": "integer", "description": "Target warmup reply rate percentage."},
                "warmup_key_id": {"type": "string", "description": "Warmup key ID."},
                "auto_adjust_warmup": {"type": "boolean", "description": "Auto-adjust warmup settings."},
                "is_rampup_enabled": {"type": "boolean", "description": "Enable rampup."},
            },
            "required": ["account_id", "warmup_enabled"],
        },
    },
    {
        "name": "email_accounts__get_warmup_stats",
        "description": "Get warmup statistics for an email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__reconnect_failed",
        "description": "Attempt to reconnect all failed email accounts.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "email_accounts__fetch_messages",
        "description": "Fetch email messages from an email account's mailbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
                "limit": {"type": "integer", "description": "Max messages to return (default 100)."},
                "folder": {"type": "string", "description": "Mailbox folder (e.g. INBOX, SENT)."},
                "includeBody": {"type": "boolean", "description": "Include email body content (default false)."},
                "from_time": {"type": "string", "description": "Fetch messages after this time."},
                "to_time": {"type": "string", "description": "Fetch messages before this time."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__delete",
        "description": "Delete an email account by ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID to delete."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__bulk_delete",
        "description": "Delete multiple email accounts at once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_ids": {"type": "array", "items": {"type": "integer"}, "description": "List of email account IDs to delete."},
            },
            "required": ["account_ids"],
        },
    },
    {
        "name": "email_accounts__save_oauth_email_account",
        "description": "Save an email account using OAuth credentials (Google or Microsoft).",
        "input_schema": {
            "type": "object",
            "properties": {
                "from_name": {"type": "string", "description": "Sender display name."},
                "from_email": {"type": "string", "description": "Sender email address."},
                "oauth_token": {"type": "string", "description": "OAuth access token."},
                "refresh_token": {"type": "string", "description": "OAuth refresh token."},
                "provider": {"type": "string", "description": "OAuth provider (google or microsoft)."},
                "client_id": {"type": "integer", "description": "Client ID."},
                "max_email_per_day": {"type": "integer", "description": "Max emails per day."},
                "warmup_enabled": {"type": "boolean", "description": "Enable warmup."},
                "total_warmup_per_day": {"type": "integer", "description": "Total warmup emails per day."},
                "daily_rampup": {"type": "integer", "description": "Daily rampup increment."},
                "reply_rate_percentage": {"type": "integer", "description": "Target warmup reply rate."},
            },
            "required": [],
        },
    },
    {
        "name": "email_accounts__disconnect_google",
        "description": "Disconnect a Google OAuth email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
            },
            "required": ["account_id"],
        },
    },
    {
        "name": "email_accounts__disconnect_microsoft",
        "description": "Disconnect a Microsoft OAuth email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
            },
            "required": ["account_id"],
        },
    },

    # =========================================================================
    # SEQUENCES MODULE (2 methods)
    # =========================================================================
    {
        "name": "sequences__get",
        "description": "Get the email sequences (steps and variants) for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "sequences__save",
        "description": "Save (create or update) email sequences for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "sequences": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "seq_number": {"type": "integer", "description": "Sequence step number (1, 2, 3...)."},
                            "seq_type": {"type": "string", "description": "Sequence type (default 'EMAIL')."},
                            "subject": {"type": "string", "description": "Email subject line."},
                            "email_body": {"type": "string", "description": "Email body HTML."},
                            "id": {"type": "integer", "description": "Existing sequence step ID (for updates)."},
                            "seq_delay_details": {"type": "object", "description": "Delay details, e.g. {\"delay_in_days\": 1}."},
                            "variant_distribution_type": {"type": "string", "description": "Variant distribution type."},
                            "lead_distribution_percentage": {"type": "integer", "description": "Lead distribution percentage."},
                            "winning_metric_property": {"type": "string", "description": "Winning metric for A/B testing."},
                            "seq_variants": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "subject": {"type": "string"},
                                        "email_body": {"type": "string"},
                                        "variant_label": {"type": "string"},
                                        "id": {"type": "integer"},
                                        "variant_distribution_percentage": {"type": "integer"},
                                    },
                                    "required": ["subject", "email_body"],
                                },
                                "description": "A/B test variants for this step.",
                            },
                        },
                        "required": ["seq_number"],
                    },
                    "description": "List of sequence steps.",
                },
            },
            "required": ["campaign_id", "sequences"],
        },
    },

    # =========================================================================
    # ANALYTICS MODULE (9 methods)
    # =========================================================================
    {
        "name": "analytics__get_statistics",
        "description": "Get detailed statistics for a campaign (sent, opens, clicks, replies, bounces).",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "analytics__get_top_level",
        "description": "Get top-level analytics summary for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "analytics__get_by_date_range",
        "description": "Get campaign analytics filtered by date range.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": ["campaign_id", "start_date", "end_date"],
        },
    },
    {
        "name": "analytics__get_top_level_by_date",
        "description": "Get top-level campaign analytics filtered by date range.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": ["campaign_id", "start_date", "end_date"],
        },
    },
    {
        "name": "analytics__get_lead_statistics",
        "description": "Get lead-level statistics for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "analytics__get_mailbox_statistics",
        "description": "Get per-mailbox sending statistics for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "analytics__get_sequence_analytics",
        "description": "Get per-sequence-step analytics for a campaign over a date range.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": ["campaign_id", "start_date", "end_date"],
        },
    },
    {
        "name": "analytics__get_variant_statistics",
        "description": "Get A/B variant statistics for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "analytics__get_warmup_stats",
        "description": "Get warmup statistics for an email account.",
        "input_schema": {
            "type": "object",
            "properties": {
                "account_id": {"type": "integer", "description": "The email account ID."},
            },
            "required": ["account_id"],
        },
    },

    # =========================================================================
    # GLOBAL ANALYTICS MODULE (22 methods)
    # =========================================================================
    {
        "name": "global_analytics__campaign_list",
        "description": "List campaigns with analytics data (paginated).",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max campaigns to return (default 100)."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__client_list",
        "description": "List clients with analytics data.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__client_monthly_count",
        "description": "Get month-wise client statistics.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__overall_stats",
        "description": "Get account-wide overall statistics (v2).",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__daily_stats",
        "description": "Get day-wise overall statistics across all campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__daily_stats_by_sent_time",
        "description": "Get day-wise statistics grouped by sent time.",
        "input_schema": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__daily_positive_replies",
        "description": "Get day-wise positive reply statistics.",
        "input_schema": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__daily_positive_replies_by_sent_time",
        "description": "Get day-wise positive reply statistics grouped by sent time.",
        "input_schema": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)."},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__campaign_overall_stats",
        "description": "Get overall stats for a specific campaign via global analytics.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "Optional campaign ID to filter."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__client_overall_stats",
        "description": "Get overall stats for a specific client.",
        "input_schema": {
            "type": "object",
            "properties": {
                "client_id": {"type": "integer", "description": "Optional client ID to filter."},
            },
            "required": [],
        },
    },
    {
        "name": "global_analytics__mailbox_health_by_name",
        "description": "Get mailbox health metrics grouped by mailbox name.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__mailbox_health_by_domain",
        "description": "Get mailbox health metrics grouped by domain.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__mailbox_performance_by_provider",
        "description": "Get mailbox performance metrics grouped by provider (Google, Microsoft, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__team_stats",
        "description": "Get team board overall statistics.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__lead_stats",
        "description": "Get overall lead statistics across all campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__lead_category_responses",
        "description": "Get lead response statistics grouped by category.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__first_reply_stats",
        "description": "Get statistics on how long campaigns take to get first replies.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__follow_up_reply_rate",
        "description": "Get follow-up reply rate statistics.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__lead_reply_time",
        "description": "Get statistics on lead-to-reply time.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__campaign_response_stats",
        "description": "Get campaign response statistics.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__campaign_status_stats",
        "description": "Get campaign statistics grouped by status.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "global_analytics__mailbox_overall_stats",
        "description": "Get overall mailbox statistics across all accounts.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },

    # =========================================================================
    # WEBHOOKS MODULE (5 methods)
    # =========================================================================
    {
        "name": "webhooks__list",
        "description": "List all webhooks for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "webhooks__create_or_update",
        "description": "Create or update a webhook for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "webhook_url": {"type": "string", "description": "The webhook URL to receive events."},
                "events": {"type": "array", "items": {"type": "string"}, "description": "List of event types to subscribe to."},
                "active": {"type": "boolean", "description": "Whether the webhook is active (default true)."},
            },
            "required": ["campaign_id", "webhook_url"],
        },
    },
    {
        "name": "webhooks__delete",
        "description": "Delete all webhooks for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "webhooks__get_summary",
        "description": "Get a summary of webhook events and deliveries for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "webhooks__retrigger_failed",
        "description": "Retrigger all failed webhook events for a campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
            },
            "required": ["campaign_id"],
        },
    },

    # =========================================================================
    # BLOCK LIST MODULE (3 methods)
    # =========================================================================
    {
        "name": "block_list__add",
        "description": "Add domains or email addresses to the global block list.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domains": {"type": "array", "items": {"type": "string"}, "description": "Domains or emails to block."},
                "client_id": {"type": "integer", "description": "Optional client ID to scope the block list."},
            },
            "required": ["domains"],
        },
    },
    {
        "name": "block_list__list",
        "description": "List entries in the global block list.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max entries to return (default 100)."},
                "filter_client_id": {"type": "string", "description": "Filter by client ID."},
                "filter_email_or_domain": {"type": "string", "description": "Filter by email or domain."},
                "filter_email_with_domain": {"type": "string", "description": "Filter emails with a specific domain."},
            },
            "required": [],
        },
    },
    {
        "name": "block_list__delete",
        "description": "Delete a block list entry by ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "entry_id": {"type": "integer", "description": "The block list entry ID to delete."},
            },
            "required": ["entry_id"],
        },
    },

    # =========================================================================
    # CLIENTS MODULE (6 methods)
    # =========================================================================
    {
        "name": "clients__create",
        "description": "Create a new client (for agency accounts).",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Client name."},
                "email": {"type": "string", "description": "Client email address."},
                "permission": {"type": "array", "items": {"type": "string"}, "description": "Permission list."},
                "logo": {"type": "string", "description": "Logo data."},
                "logo_url": {"type": "string", "description": "Logo URL."},
                "password": {"type": "string", "description": "Client password."},
            },
            "required": ["name", "email"],
        },
    },
    {
        "name": "clients__list_all",
        "description": "List all clients in the account.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "clients__create_api_key",
        "description": "Create a new API key for a client.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key_name": {"type": "string", "description": "Name for the API key."},
                "client_id": {"type": "string", "description": "Client ID."},
            },
            "required": ["key_name", "client_id"],
        },
    },
    {
        "name": "clients__list_api_keys",
        "description": "List all client API keys.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "clients__delete_api_key",
        "description": "Delete a client API key by ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "api_key_id": {"type": "integer", "description": "The API key ID to delete."},
            },
            "required": ["api_key_id"],
        },
    },
    {
        "name": "clients__reset_api_key",
        "description": "Reset (regenerate) a client API key.",
        "input_schema": {
            "type": "object",
            "properties": {
                "api_key_id": {"type": "integer", "description": "The API key ID to reset."},
            },
            "required": ["api_key_id"],
        },
    },

    # =========================================================================
    # MASTER INBOX MODULE (20 methods)
    # =========================================================================
    {
        "name": "master_inbox__get_replies",
        "description": "Get replies from the master inbox with optional filters and sorting.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max replies to return (default 10)."},
                "filters": {
                    "type": "object",
                    "properties": {
                        "search": {"type": "string"},
                        "leadCategories": {"type": "object"},
                        "emailStatus": {"type": "array", "items": {"type": "string"}},
                        "campaignId": {"type": "array", "items": {"type": "integer"}},
                        "emailAccountId": {"type": "array", "items": {"type": "integer"}},
                        "campaignTeamMemberId": {"type": "array", "items": {"type": "integer"}},
                        "campaignTagId": {"type": "array", "items": {"type": "integer"}},
                        "campaignClientId": {"type": "array", "items": {"type": "integer"}},
                        "replyTimeBetween": {"type": "array", "items": {"type": "string"}},
                    },
                    "description": "Filter criteria.",
                },
                "sort_by": {"type": "string", "description": "Sort field."},
                "fetch_message_history": {"type": "boolean", "description": "Include message history (default false)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_lead",
        "description": "Get a specific lead from the master inbox by lead map ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_map_id": {"type": "integer", "description": "The lead map ID."},
            },
            "required": ["lead_map_id"],
        },
    },
    {
        "name": "master_inbox__reply_to_lead",
        "description": "Send a reply to a lead from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "email_stats_id": {"type": "string", "description": "The email stats ID to reply to."},
                "email_body": {"type": "string", "description": "The reply email body."},
                "reply_message_id": {"type": "string", "description": "Message ID to reply to."},
                "reply_email_time": {"type": "string", "description": "Time of the email being replied to."},
            },
            "required": ["campaign_id", "email_stats_id", "email_body"],
        },
    },
    {
        "name": "master_inbox__forward_reply",
        "description": "Forward an email from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {"type": "integer", "description": "The campaign ID."},
                "email_stats_id": {"type": "string", "description": "The email stats ID to forward."},
                "email_body": {"type": "string", "description": "The forwarded email body."},
                "reply_message_id": {"type": "string", "description": "Original message ID."},
                "reply_email_time": {"type": "string", "description": "Original email time."},
            },
            "required": ["campaign_id", "email_stats_id", "email_body"],
        },
    },
    {
        "name": "master_inbox__update_revenue",
        "description": "Update the revenue value for a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "revenue": {"type": "number", "description": "Revenue value."},
            },
            "required": ["email_lead_map_id", "revenue"],
        },
    },
    {
        "name": "master_inbox__update_category",
        "description": "Update the category for a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "category_id": {"type": "integer", "description": "The category ID."},
            },
            "required": ["email_lead_map_id", "category_id"],
        },
    },
    {
        "name": "master_inbox__get_snoozed",
        "description": "Get snoozed messages from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max messages to return (default 10)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_important",
        "description": "Get important messages from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max messages to return (default 10)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_scheduled",
        "description": "Get scheduled messages from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max messages to return (default 10)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_reminders",
        "description": "Get reminder messages from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max messages to return (default 10)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_archived",
        "description": "Get archived messages from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max messages to return (default 10)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__get_untracked",
        "description": "Get untracked replies from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "master_inbox__update_read_status",
        "description": "Mark a lead as read or unread in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "is_read": {"type": "boolean", "description": "True to mark as read, false for unread."},
            },
            "required": ["email_lead_map_id", "is_read"],
        },
    },
    {
        "name": "master_inbox__set_reminder",
        "description": "Set a reminder for a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "reminder_time": {"type": "string", "description": "Reminder time (ISO format)."},
                "note": {"type": "string", "description": "Reminder note."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__create_task",
        "description": "Create a task for a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "task": {"type": "string", "description": "Task description."},
                "due_date": {"type": "string", "description": "Due date (ISO format)."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__create_note",
        "description": "Create a note for a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "note": {"type": "string", "description": "Note content."},
            },
            "required": [],
        },
    },
    {
        "name": "master_inbox__push_to_subsequence",
        "description": "Push a lead into a subsequence campaign.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "subsequence_id": {"type": "integer", "description": "The subsequence campaign ID."},
            },
            "required": ["email_lead_map_id", "subsequence_id"],
        },
    },
    {
        "name": "master_inbox__assign_team_member",
        "description": "Assign a team member to a lead in the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
                "team_member_id": {"type": "integer", "description": "The team member ID."},
            },
            "required": ["email_lead_map_id", "team_member_id"],
        },
    },
    {
        "name": "master_inbox__block_domains",
        "description": "Block domains from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domains": {"type": "array", "items": {"type": "string"}, "description": "Domains to block."},
            },
            "required": ["domains"],
        },
    },
    {
        "name": "master_inbox__resume_lead",
        "description": "Resume a paused lead from the master inbox.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email_lead_map_id": {"type": "integer", "description": "The email lead map ID."},
            },
            "required": ["email_lead_map_id"],
        },
    },

    # =========================================================================
    # SMART DELIVERY MODULE (28 methods)
    # =========================================================================
    {
        "name": "smart_delivery__get_providers",
        "description": "Get available email providers and region IDs for deliverability testing.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_delivery__create_manual_test",
        "description": "Create a manual inbox placement test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Test name."},
                "email_account_ids": {"type": "array", "items": {"type": "integer"}, "description": "Email account IDs to test."},
                "provider_ids": {"type": "array", "items": {"type": "integer"}, "description": "Provider IDs to test against."},
                "subject": {"type": "string", "description": "Test email subject."},
                "email_body": {"type": "string", "description": "Test email body."},
                "folder_id": {"type": "integer", "description": "Folder ID to organize the test."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_delivery__create_automated_test",
        "description": "Create an automated recurring inbox placement test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Test name."},
                "email_account_ids": {"type": "array", "items": {"type": "integer"}, "description": "Email account IDs to test."},
                "provider_ids": {"type": "array", "items": {"type": "integer"}, "description": "Provider IDs to test against."},
                "subject": {"type": "string", "description": "Test email subject."},
                "email_body": {"type": "string", "description": "Test email body."},
                "frequency": {"type": "string", "description": "Test frequency (e.g. 'daily', 'weekly')."},
                "folder_id": {"type": "integer", "description": "Folder ID to organize the test."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_delivery__get_test",
        "description": "Get details and results of a specific deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__delete_tests",
        "description": "Delete multiple deliverability tests.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_ids": {"type": "array", "items": {"type": "integer"}, "description": "Test IDs to delete."},
            },
            "required": ["test_ids"],
        },
    },
    {
        "name": "smart_delivery__stop_automated_test",
        "description": "Stop a running automated deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID to stop."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__list_tests",
        "description": "List all deliverability tests with pagination and filters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max tests to return (default 20)."},
                "folder_id": {"type": "integer", "description": "Filter by folder ID."},
                "search": {"type": "string", "description": "Search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_delivery__get_provider_report",
        "description": "Get provider-wise results for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_geo_report",
        "description": "Get geo-wise report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_sender_report",
        "description": "Get sender account report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_spam_filter_report",
        "description": "Get spam filter report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_dkim",
        "description": "Get DKIM details for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_spf",
        "description": "Get SPF details for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_rdns",
        "description": "Get rDNS report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_sender_accounts",
        "description": "Get sender account list for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_ip_blacklists",
        "description": "Get IP blacklist report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_domain_blacklist",
        "description": "Get domain blacklist report for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_test_email_content",
        "description": "Get the email content used in a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_ip_blacklist_count",
        "description": "Get IP blacklist count for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_email_headers",
        "description": "Get email headers from a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_schedule_history",
        "description": "Get schedule history for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_ip_details",
        "description": "Get IP details for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_mailbox_summary",
        "description": "Get mailbox summary for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__get_mailbox_count",
        "description": "Get mailbox count for a deliverability test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_id": {"type": "integer", "description": "The test ID."},
            },
            "required": ["test_id"],
        },
    },
    {
        "name": "smart_delivery__list_folders",
        "description": "List all Smart Delivery test folders.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_delivery__create_folder",
        "description": "Create a new Smart Delivery test folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Folder name."},
            },
            "required": ["name"],
        },
    },
    {
        "name": "smart_delivery__get_folder",
        "description": "Get details of a Smart Delivery test folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "folder_id": {"type": "integer", "description": "The folder ID."},
            },
            "required": ["folder_id"],
        },
    },
    {
        "name": "smart_delivery__delete_folder",
        "description": "Delete a Smart Delivery test folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "folder_id": {"type": "integer", "description": "The folder ID to delete."},
            },
            "required": ["folder_id"],
        },
    },

    # =========================================================================
    # SMART SENDERS MODULE (7 methods)
    # =========================================================================
    {
        "name": "smart_senders__get_mailbox_otp",
        "description": "Get the OTP for mailbox verification.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_senders__auto_generate_mailboxes",
        "description": "Auto-generate mailboxes for a domain.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain_id": {"type": "integer", "description": "Domain ID."},
                "count": {"type": "integer", "description": "Number of mailboxes to generate."},
                "prefix_pattern": {"type": "string", "description": "Prefix pattern for mailbox names."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_senders__search_domain",
        "description": "Search for available domains.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Domain search query."},
            },
            "required": ["query"],
        },
    },
    {
        "name": "smart_senders__get_vendors",
        "description": "List available domain vendors.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_senders__place_order",
        "description": "Place an order for a domain and mailboxes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Domain to order."},
                "vendor_id": {"type": "integer", "description": "Vendor ID."},
                "mailbox_count": {"type": "integer", "description": "Number of mailboxes."},
                "plan": {"type": "string", "description": "Plan name."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_senders__list_domains",
        "description": "List all Smart Senders domains.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_senders__get_order_details",
        "description": "Get details of a domain order.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer", "description": "The order ID."},
            },
            "required": [],
        },
    },

    # =========================================================================
    # SMART PROSPECT MODULE (26 methods)
    # =========================================================================
    {
        "name": "smart_prospect__get_departments",
        "description": "Get available departments for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_cities",
        "description": "Search for cities for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "City search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_countries",
        "description": "Get available countries for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_states",
        "description": "Get states for a country for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {
                "country": {"type": "string", "description": "Country name or code."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_industries",
        "description": "Get available industries for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_sub_industries",
        "description": "Get sub-industries for a specific industry.",
        "input_schema": {
            "type": "object",
            "properties": {
                "industry_id": {"type": "integer", "description": "Parent industry ID."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_head_counts",
        "description": "Get available company headcount ranges for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_levels",
        "description": "Get available job levels for prospect filtering (C-level, VP, Director, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_revenue_options",
        "description": "Get available company revenue ranges for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_companies",
        "description": "Search for companies by name.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Company name search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_domains",
        "description": "Search for company domains.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Domain search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_job_titles",
        "description": "Search for job titles.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Job title search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_keywords",
        "description": "Search for keywords for prospect filtering.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Keyword search query."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__search_contacts",
        "description": "Search for prospect contacts using filters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filters": {"type": "object", "description": "Search filter criteria."},
                "offset": {"type": "integer", "description": "Pagination offset (default 0)."},
                "limit": {"type": "integer", "description": "Max contacts to return (default 25)."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__fetch_contacts",
        "description": "Fetch (enrich) specific contacts or contacts from a search.",
        "input_schema": {
            "type": "object",
            "properties": {
                "contact_ids": {"type": "array", "items": {"type": "integer"}, "description": "Contact IDs to fetch."},
                "search_id": {"type": "integer", "description": "Search ID to fetch contacts from."},
            },
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_contacts",
        "description": "Get details of specific contacts by IDs.",
        "input_schema": {
            "type": "object",
            "properties": {
                "contact_ids": {"type": "array", "items": {"type": "integer"}, "description": "Contact IDs."},
            },
            "required": ["contact_ids"],
        },
    },
    {
        "name": "smart_prospect__review_contacts",
        "description": "Review (approve/reject) fetched contacts.",
        "input_schema": {
            "type": "object",
            "properties": {
                "contact_ids": {"type": "array", "items": {"type": "integer"}, "description": "Contact IDs to review."},
                "status": {"type": "string", "description": "Review status to set."},
            },
            "required": ["contact_ids", "status"],
        },
    },
    {
        "name": "smart_prospect__get_saved_searches",
        "description": "List saved prospect searches.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_recent_searches",
        "description": "List recent prospect searches.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_fetched_searches",
        "description": "List searches that have fetched (enriched) contacts.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__save_search",
        "description": "Save a prospect search with filters for later reuse.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name for the saved search."},
                "filters": {"type": "object", "description": "Search filter criteria."},
            },
            "required": ["name"],
        },
    },
    {
        "name": "smart_prospect__update_saved_search",
        "description": "Update a saved prospect search.",
        "input_schema": {
            "type": "object",
            "properties": {
                "search_id": {"type": "integer", "description": "The saved search ID."},
                "name": {"type": "string", "description": "Updated search name."},
                "filters": {"type": "object", "description": "Updated filter criteria."},
            },
            "required": ["search_id"],
        },
    },
    {
        "name": "smart_prospect__update_fetched_lead",
        "description": "Update data for a fetched prospect lead.",
        "input_schema": {
            "type": "object",
            "properties": {
                "lead_id": {"type": "integer", "description": "The lead ID."},
                "data": {"type": "object", "description": "Updated lead data."},
            },
            "required": ["lead_id"],
        },
    },
    {
        "name": "smart_prospect__get_search_analytics",
        "description": "Get analytics for prospect searches.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__get_reply_analytics",
        "description": "Get reply analytics for prospected contacts.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "smart_prospect__find_emails",
        "description": "Find email addresses for a person.",
        "input_schema": {
            "type": "object",
            "properties": {
                "first_name": {"type": "string", "description": "Person's first name."},
                "last_name": {"type": "string", "description": "Person's last name."},
                "domain": {"type": "string", "description": "Company domain."},
                "company_name": {"type": "string", "description": "Company name."},
                "linkedin_url": {"type": "string", "description": "LinkedIn profile URL."},
            },
            "required": [],
        },
    },
]
