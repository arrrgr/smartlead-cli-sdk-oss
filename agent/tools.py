"""Smartlead tool definitions for the Claude agent."""

from __future__ import annotations

TOOLS = [
    {
        "name": "list_campaigns",
        "description": "List all campaigns in the Smartlead account with their IDs, names, and statuses.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "get_campaign_stats",
        "description": "Get detailed statistics for a specific campaign: sent count, opens, clicks, replies, bounces, unsubscribes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {
                    "type": "integer",
                    "description": "The numeric ID of the campaign.",
                }
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "list_leads",
        "description": "List leads in a campaign with their email, name, company, and status.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {
                    "type": "integer",
                    "description": "The numeric ID of the campaign.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of leads to return (default 100).",
                },
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "add_lead",
        "description": "Add a single lead to a campaign by email address.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {
                    "type": "integer",
                    "description": "The numeric ID of the campaign.",
                },
                "email": {
                    "type": "string",
                    "description": "The lead's email address.",
                },
                "first_name": {
                    "type": "string",
                    "description": "The lead's first name (optional).",
                },
                "last_name": {
                    "type": "string",
                    "description": "The lead's last name (optional).",
                },
                "company": {
                    "type": "string",
                    "description": "The lead's company name (optional).",
                },
            },
            "required": ["campaign_id", "email"],
        },
    },
    {
        "name": "pause_campaign",
        "description": "Pause an active campaign to stop sending emails.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {
                    "type": "integer",
                    "description": "The numeric ID of the campaign to pause.",
                }
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "start_campaign",
        "description": "Start or resume a campaign to begin/continue sending emails.",
        "input_schema": {
            "type": "object",
            "properties": {
                "campaign_id": {
                    "type": "integer",
                    "description": "The numeric ID of the campaign to start.",
                }
            },
            "required": ["campaign_id"],
        },
    },
    {
        "name": "get_analytics_overview",
        "description": "Get account-wide day-wise analytics showing sent, opens, replies, and bounces across all campaigns.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]
