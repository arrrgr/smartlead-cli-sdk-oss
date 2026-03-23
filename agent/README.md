# Smartlead Agent

A conversational AI agent that manages your Smartlead account in plain English, powered by Claude.

## What it does

Ask questions and give instructions naturally:

- "What's the reply rate on campaign 3048174?"
- "Pause all campaigns with bounce rates over 5%"
- "Add these 50 leads to the property management campaign"
- "Which domains have the worst deliverability this week?"
- "Show me all positive replies from the last 3 days"

The agent calls the Smartlead API through the SDK and reports back in plain English. It maintains conversation history so you can ask follow-ups naturally.

## Setup

### 1. Install

From the repo root:

```bash
pip install -e .
```

Or install dependencies directly:

```bash
pip install anthropic httpx pydantic python-dotenv
```

### 2. Set environment variables

```bash
export SMARTLEAD_API_KEY=your_smartlead_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 3. Run

```bash
cd agent
python agent.py
```

## How it works

The agent runs a standard Claude tool-use loop:

1. You type a message
2. Claude reads it and decides which Smartlead tool(s) to call
3. The agent executes the tool(s) against the live Smartlead API via the SDK
4. Claude summarizes the results in plain English
5. If Claude needs more data, it calls additional tools automatically (agentic loop)
6. Repeat

The key insight: Claude doesn't talk to the API directly. It calls tools defined in `tools.py`, which map to SDK methods in `execute_tool()` inside `agent.py`. This means:

- **The SDK handles auth, retries, and rate limiting** - the agent doesn't worry about HTTP
- **Structured data flows both ways** - Claude gets clean JSON, not raw API responses
- **Error handling is centralized** - `SmartleadError` exceptions are caught and returned to Claude as context

## Starter tools (7 included)

The agent ships with 7 tools as a working starting point:

| Tool | SDK Method | What it does |
|---|---|---|
| `list_campaigns` | `global_analytics.campaign_list()` | List all campaigns with ID, name, status |
| `get_campaign_stats` | `analytics.get_statistics()` | Sent, opens, clicks, replies, bounces for a campaign |
| `list_leads` | `leads.list_by_campaign()` | Leads in a campaign with email, name, status |
| `add_lead` | `leads.add_to_campaign()` | Add a single lead to a campaign |
| `pause_campaign` | `campaigns.update_status("PAUSED")` | Pause an active campaign |
| `start_campaign` | `campaigns.update_status("START")` | Start or resume a campaign |
| `get_analytics_overview` | `global_analytics.daily_stats()` | Account-wide daily analytics |

## Adding more tools

The SDK has **170+ methods across 13 modules**. The 7 starter tools are just the beginning. To add a new tool:

### 1. Define the tool schema in `tools.py`

```python
{
    "name": "get_domain_health",
    "description": "Check deliverability health metrics for all sending domains in a date range.",
    "input_schema": {
        "type": "object",
        "properties": {
            "start_date": {
                "type": "string",
                "description": "Start date (YYYY-MM-DD)"
            },
            "end_date": {
                "type": "string",
                "description": "End date (YYYY-MM-DD)"
            }
        },
        "required": ["start_date", "end_date"]
    }
}
```

### 2. Add the handler in `agent.py`

```python
elif tool_name == "get_domain_health":
    data = await client.global_analytics.mailbox_health_by_domain(
        start_date=tool_input["start_date"],
        end_date=tool_input["end_date"]
    )
    return data
```

That's it. Claude will automatically discover and use the new tool.

### High-value tools to add

These SDK methods are especially useful as agent tools:

**Campaign management**
- `analytics.get_variant_statistics()` - A/B variant performance
- `leads.update()` - update lead custom fields (e.g. swap copy variants)
- `leads.pause()` / `leads.resume()` - per-lead control
- `campaigns.update_settings()` - change campaign config

**Deliverability monitoring**
- `global_analytics.mailbox_health_by_domain()` - domain-level health
- `global_analytics.mailbox_health_by_name()` - per-mailbox health
- `global_analytics.mailbox_performance_by_provider()` - Gmail vs Outlook vs etc.
- `smart_delivery.create_automated_test()` - run deliverability tests
- `email_accounts.get_warmup_stats()` - warmup progress

**Inbox and replies**
- `master_inbox.get_replies()` - fetch all replies
- `master_inbox.reply_to_lead()` - send a reply
- `master_inbox.update_category()` - categorize leads (Interested, Not Interested, etc.)
- `master_inbox.create_task()` / `create_note()` - CRM-style follow-ups

**Prospecting**
- `smart_prospect.search_contacts()` - find contacts by title, industry, location
- `smart_prospect.find_emails()` - get emails for contacts
- `smart_prospect.fetch_contacts()` - pull full contact details

**Lead operations**
- `leads.get_by_email()` - look up a lead across campaigns
- `leads.list_global()` - search all leads
- `leads.update_category()` - mark leads as interested/not interested
- `block_list.add()` - block domains or emails

See the full SDK module reference in the main [README](../README.md).

## Model

Uses `claude-opus-4-6` by default. Change the `MODEL` variable in `agent.py` to use a different model. `claude-sonnet-4-6` works well for most tasks and is faster/cheaper.

## Exiting

Press `Ctrl+C` to exit cleanly.
