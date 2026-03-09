# smartlead-cli

Unofficial CLI and AI agent for the [Smartlead](https://smartlead.ai) API.

Manage your cold email campaigns, leads, and mailboxes from the terminal — or talk to them in plain English via a Claude-powered agent.

---

## Install

```bash
pip install smartlead-cli
```

Requires Python 3.10+.

## Configure

```bash
export SMARTLEAD_API_KEY=your_api_key_here
```

Copy `.env.example` to `.env` and fill in your keys if you prefer a dotenv workflow.

---

## CLI Usage

### Campaigns

```bash
# List all campaigns
smartlead campaigns list

# Get campaign details
smartlead campaigns get 42

# Show sent/open/reply/bounce stats
smartlead campaigns stats 42

# Pause a campaign
smartlead campaigns pause 42

# Start or resume a campaign
smartlead campaigns start 42
```

### Leads

```bash
# List leads in a campaign
smartlead leads list 42 --limit 50

# Add a lead
smartlead leads add 42 john@acme.com --first-name John --last-name Doe --company Acme

# Look up a lead by email
smartlead leads get 42 john@acme.com
```

### Email Accounts

```bash
# List all email accounts
smartlead email-accounts list

# Show warmup stats for an account
smartlead email-accounts stats 7
```

### Analytics

```bash
# Account-wide day-wise overview
smartlead analytics overview

# Campaign-level analytics
smartlead analytics campaign 42
```

### JSON output

Every command accepts `--output json` for raw JSON:

```bash
smartlead campaigns stats 42 --output json
```

---

## AI Agent

The agent lets you manage Smartlead in plain English via a Claude-powered conversational interface.

```bash
export SMARTLEAD_API_KEY=your_key
export ANTHROPIC_API_KEY=your_key

cd agent
python agent.py
```

Example session:

```
You: How many replies did we get this week?
Assistant: You received 47 replies across all campaigns this week...

You: Pause campaign 42
  [calling pause_campaign...]
Assistant: Campaign 42 has been paused.

You: Add sarah@startupco.com to campaign 17
  [calling add_lead...]
Assistant: Sarah has been added to campaign 17.
```

See [agent/README.md](agent/README.md) for full setup and usage details.

---

## SDK

The underlying Python SDK is importable directly:

```python
from smartlead import SmartleadClient

async with SmartleadClient(api_key="YOUR_KEY") as client:
    campaigns = await client.global_analytics.campaign_list()
    stats = await client.analytics.get_statistics(campaign_id=42)
    await client.leads.add_to_campaign(42, leads=[{"email": "jane@co.com"}])
```

13 domain modules: `campaigns`, `leads`, `email_accounts`, `sequences`, `analytics`, `global_analytics`, `webhooks`, `block_list`, `clients`, `master_inbox`, `smart_delivery`, `smart_senders`, `smart_prospect`.

---

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-feature`)
3. Make your changes and add tests if applicable
4. Open a pull request

This is an unofficial project — PRs, bug reports, and feature requests are welcome.

---

## License

MIT. See [LICENSE](LICENSE).
