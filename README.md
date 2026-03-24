# smartlead-sdk

Unofficial Python SDK and AI agent for the [Smartlead](https://smartlead.ai) cold email API.

170+ methods across 13 modules. Full async. Pydantic models. Built-in retries and rate limiting.

### What is an SDK?

An SDK (Software Development Kit) is a library your code imports directly. Instead of running terminal commands and reading text output, your Python scripts call methods like `client.leads.add_to_campaign()` and get structured data back. It's the difference between typing commands manually and having your code talk to an API natively.

### Why a Python SDK when Smartlead has an official CLI?

Smartlead's official CLI (`npm install -g @smartlead/cli`) is great. 130+ commands, clean output, works well for manual operations in the terminal. If you need to quickly check campaign stats or pause a send, use it.

But CLIs and SDKs solve different problems. A CLI is designed for a human typing commands. An SDK is designed for code calling code. When you're building AI agents or automation pipelines that manage campaigns programmatically, the difference matters:

- **No parsing** - SDK methods return Python objects. No subprocess calls, no capturing stdout, no regex on text output.
- **Chaining** - An agent can pull analytics, detect winning variants, and update 200 leads in a single async flow. With a CLI, that's three shell commands with string wrangling between each one.
- **Error recovery** - The SDK has built-in retries with exponential backoff on rate limits and server errors. Your agent handles failures gracefully instead of dying on a non-zero exit code.
- **Type safety** - Pydantic v2 models validate every request and response. Your agent knows exactly what fields exist before it sends anything.
- **Composability** - Import the SDK alongside pandas, the anthropic SDK, or any Python library. Build pipelines that go from data analysis to API calls without leaving Python.

We built this SDK before Smartlead released their CLI, and it covers modules their CLI doesn't expose yet (Smart Delivery: 28 methods, Smart Senders: 7 methods). The two tools complement each other - use the CLI for quick manual checks, use the SDK for anything programmatic or agentic.

---

## Install

```bash
pip install smartlead-sdk
```

Requires Python 3.9+.

## Configure

```bash
export SMARTLEAD_API_KEY=your_api_key_here
```

Or copy `.env.example` to `.env` for a dotenv workflow.

---

## SDK

Import and use directly in your scripts, agents, or automation pipelines.

```python
from smartlead import SmartleadClient

async with SmartleadClient(api_key="YOUR_KEY") as client:

    # Check how a campaign is performing
    stats = await client.analytics.get_statistics(campaign_id=3048174)
    print(f"Sent: {stats.sent_count}, Replies: {stats.reply_count}, Bounces: {stats.bounce_count}")

    # Pull all leads and filter by status
    leads = await client.leads.list_by_campaign(3048174, limit=500)
    unsent = [l for l in leads.data if l.lead_status == "STARTED"]
    print(f"{len(unsent)} leads still waiting to send")

    # Update a lead's custom fields (e.g. swap email copy variant)
    await client.leads.update(
        campaign_id=3048174,
        lead_id=lead.id,
        email=lead.email,
        custom_fields={"e1_variant": "A", "email_1": new_copy}
    )

    # Check which A/B variants are winning
    variants = await client.analytics.get_variant_statistics(campaign_id=3048174)

    # Monitor domain health across all sending domains
    health = await client.global_analytics.mailbox_health_by_domain(
        start_date="2026-03-01", end_date="2026-03-24"
    )

    # Add leads to a campaign with custom fields
    await client.leads.add_to_campaign(3048174, leads=[
        {
            "email": "ceo@example.com",
            "first_name": "Alex",
            "last_name": "Chen",
            "company_name": "Example Corp",
            "custom_fields": {
                "company_name_ai": "Example Corp",
                "first_name_russian": "Алекс",
                "country": "Georgia",
                "email_1": "Your personalized first email here...",
                "email_2": "Follow-up copy...",
                "email_3": "Final follow-up..."
            }
        }
    ])

    # Run a deliverability test
    test = await client.smart_delivery.create_manual_test(
        sender_email="alex@yourdomain.com",
        subject="Test email"
    )
```

### 13 Domain Modules

| Module | Methods | What it covers |
|---|---|---|
| `campaigns` | 9 | Create, update, delete, status, schedule, sequences, export, subsequences |
| `leads` | 17 | Add, update, pause, resume, delete, unsubscribe, categories, message history, push, deactivate |
| `email_accounts` | 16 | SMTP/IMAP create, OAuth (Google/Microsoft), warmup config, bulk delete, reconnect, tags, messages |
| `sequences` | 2 | Get and save email sequences per campaign |
| `analytics` | 9 | Campaign stats, date ranges, lead/mailbox/sequence/variant analytics, warmup stats |
| `global_analytics` | 22 | Cross-campaign stats: daily, by sent time, positive replies, domain health, provider performance, team board, lead categories |
| `webhooks` | 5 | List, create/update, delete, summary, retrigger failed |
| `block_list` | 3 | Add, list, remove blocked emails/domains |
| `clients` | 6 | Agency client management: create, list, API key CRUD |
| `master_inbox` | 20 | Unified inbox: replies, snoozed, important, scheduled, archived, reply/forward, tasks, notes, team assignment, domain blocking |
| `smart_delivery` | **28** | **Not in Smartlead CLI.** Deliverability testing: manual/automated tests, provider/geo/spam reports, SPF/DKIM/rDNS checks, IP/domain blacklists |
| `smart_prospect` | 26 | Contact discovery: search, fetch, find emails, saved searches, filters (industry, headcount, revenue, location, job title) |
| `smart_senders` | **7** | **Not in Smartlead CLI.** Domain ordering: search, purchase, OTP verification, vendor listing |

**Total: 170+ methods covering ~91% of Smartlead's API surface.**

### Key Features

- **Full async** - built on `httpx.AsyncClient`
- **Pydantic v2 models** - typed request/response objects for every endpoint
- **Auto-retry** - exponential backoff on 5xx and 429 (rate limit) errors
- **Sliding-window rate limiter** - stays within API limits automatically
- **Structured errors** - `SmartleadAuthError`, `SmartleadNotFoundError`, `SmartleadRateLimitError`, `SmartleadValidationError`, `SmartleadServerError`
- **Dual API support** - main API + Smart Delivery API (separate base URL) handled transparently

---

## AI Agent

A conversational Claude-powered agent that manages Smartlead via natural language.

```bash
export SMARTLEAD_API_KEY=your_key
export ANTHROPIC_API_KEY=your_key

cd agent
python agent.py
```

Ask it anything:

- "What's the reply rate on campaign 3048174?"
- "Which domains have bounce rates over 3%?"
- "Pause all campaigns currently active under client Acme"
- "Show me positive replies from the last 3 days for the Enron campaign. I want a csv with all lead data + entire message history "
- "Add these leads to the property management campaign we pushed live earlier today"

The agent has all 170+ SDK methods wired as tools out of the box. See [SKILLS.md](SKILLS.md) for the full reference, or [agent/README.md](agent/README.md) for how it works.

### Why SDK + Agent > CLI for automation

If you're building AI agents that manage cold email campaigns, the SDK gives you:

1. **Direct Python imports** - no subprocess calls or shell output parsing
2. **Structured data** - agents work with Python objects, not text blobs
3. **Chained operations** - analyze variants, detect winners, update leads in one flow
4. **Built-in error handling** - agents recover from failures instead of crashing on exit codes
5. **Composability** - combine with pandas, anthropic SDK, or any Python library
6. **Agent template included** - working example of a Claude-powered campaign manager

---

## Project Structure

```
smartlead-sdk/
  src/smartlead/          # Python SDK
    _base_client.py       # HTTP client, retries, rate limiting
    _client.py            # SmartleadClient (composes all modules)
    _config.py            # Configuration
    _errors.py            # Error hierarchy
    models/               # Pydantic request/response models (14 files)
    modules/              # API modules (13 domain modules)
  agent/                  # Claude AI agent
    agent.py              # Agentic loop
    tools.py              # Tool definitions for Claude
```

---

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Open a pull request

Bug reports and feature requests welcome.

---

## License

MIT. See [LICENSE](LICENSE).

---

Built by [Arthur Grishkevich](https://www.linkedin.com/in/arthurgrishkevich/) [Alchemail](https://alchemail.io).
