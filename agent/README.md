# Smartlead Agent

A conversational AI agent that lets you manage your Smartlead account in plain English, powered by Claude.

## What it does

Ask questions and give instructions like:
- "How many emails did we send yesterday?"
- "Pause campaign 42"
- "Add john@acme.com to campaign 17 as a lead from Acme Corp"
- "Show me the stats for my top 3 campaigns"

The agent uses Claude to understand your intent, calls the Smartlead API, and reports back in plain English.

## Setup

### 1. Install dependencies

From the repo root:

```bash
pip install anthropic httpx pydantic python-dotenv
```

Or with the full package:

```bash
pip install smartlead-cli
```

### 2. Set environment variables

```bash
export SMARTLEAD_API_KEY=your_smartlead_api_key_here
export ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

Or create a `.env` file in the repo root and load it:

```bash
cp ../.env.example ../.env
# Edit ../.env with your keys
source ../.env
```

### 3. Run the agent

```bash
cd agent
python agent.py
```

## How it works

The agent runs an interactive loop:

1. You type a message
2. Claude reads it and decides which Smartlead tool(s) to call
3. The agent executes the tool(s) against the live Smartlead API
4. Claude summarises the results in plain English
5. Repeat

The agent maintains conversation history within the session, so you can ask follow-up questions naturally.

## Available tools

| Tool | Description |
|---|---|
| `list_campaigns` | List all campaigns (ID, name, status) |
| `get_campaign_stats` | Sent, opens, clicks, replies, bounces for a campaign |
| `list_leads` | Leads in a campaign with their status |
| `add_lead` | Add a lead to a campaign |
| `pause_campaign` | Pause a campaign |
| `start_campaign` | Start or resume a campaign |
| `get_analytics_overview` | Account-wide day-wise analytics |

## Model

The agent uses `claude-opus-4-6` by default. To change the model, edit the `MODEL` variable in `agent.py`.

## Exiting

Press `Ctrl+C` to exit cleanly.
