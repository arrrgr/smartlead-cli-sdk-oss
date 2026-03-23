# smartlead-sdk
**Status**: active
**Last updated**: 2026-03-24

## Purpose
Open-source unofficial Python SDK and AI agent for the Smartlead cold email API.

## Instructions for Claude
- The SDK is fully async (httpx) - all module methods are `async def`
- Follow existing patterns in `_base_client.py` when adding new API methods
- Models use Pydantic v2 - check `models/` for existing patterns
- Agent uses Claude tool_use - check `agent/tools.py` for tool definition format
- When adding a new SDK method, also add a matching tool definition in `agent/tools.py`

## Contents

| Item | Type | Description |
|---|---|---|
| `src/smartlead/` | folder | Python SDK - core library |
| `src/smartlead/_base_client.py` | file | HTTP client with retries, rate limiting, dual API support |
| `src/smartlead/_client.py` | file | `SmartleadClient` - main facade composing all 13 modules |
| `src/smartlead/_config.py` | file | `SmartleadConfig` dataclass |
| `src/smartlead/_errors.py` | file | Error hierarchy (Auth, NotFound, RateLimit, Validation, Server) |
| `src/smartlead/models/` | folder | Pydantic v2 request/response models (14 files, one per module) |
| `src/smartlead/modules/` | folder | API modules (13 domain modules, 170+ methods total) |
| `agent/` | folder | Claude-powered conversational AI agent |
| `agent/agent.py` | file | Agentic loop with dynamic tool dispatch |
| `agent/tools.py` | file | 170 tool definitions for Claude covering all 13 SDK modules |
| `SKILLS.md` | file | Human-friendly reference of all 170 agent tools with example prompts |
| `pyproject.toml` | file | Build config (hatchling), dependencies |
| `.env.example` | file | Example environment variables |
| `.github/workflows/publish.yml` | file | PyPI publish workflow (on tag push) |
| `LICENSE` | file | MIT License |
| `README.md` | file | Full documentation with SDK and agent usage |

## SDK Modules (13 total, 170+ methods)

| Module | Methods | Coverage |
|---|---|---|
| `campaigns` | 9 | Create, update, delete, status, schedule, sequences, export, subsequences |
| `leads` | 17 | Full lead lifecycle: add, update, pause, resume, delete, categories, history |
| `email_accounts` | 16 | SMTP/IMAP, OAuth, warmup, bulk delete, reconnect, tags, messages |
| `sequences` | 2 | Get and save email sequences |
| `analytics` | 9 | Campaign stats, date ranges, lead/mailbox/sequence/variant analytics |
| `global_analytics` | 22 | Cross-campaign: daily, replies, domain health, provider perf, team board |
| `webhooks` | 5 | CRUD + summary + retrigger |
| `block_list` | 3 | Email/domain blocking |
| `clients` | 6 | Agency client + API key management |
| `master_inbox` | 20 | Unified inbox: replies, actions, tasks, notes, team assignment |
| `smart_delivery` | 28 | Deliverability testing, SPF/DKIM/rDNS, blacklists |
| `smart_prospect` | 26 | Contact discovery, search, enrichment, saved searches |
| `smart_senders` | 7 | Domain ordering and management |

## Change Log
- **2026-03-24** - Cleaned up for open-source release. Removed CLI (Smartlead has an official one). Added SKILLS.md.
- **2026-03-23** - Rebuilt agent with 170 tools covering all 13 SDK modules. Dynamic dispatch replaces if/elif chain.
- **2026-03-23** - Added 9 missing SDK methods, updated README with full module table
- **2026-03-09** - Initial build: 13 modules, AI agent, MIT license
