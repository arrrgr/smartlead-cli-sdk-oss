"""Claude-powered Smartlead agent.

Runs an interactive loop where you can ask questions and give instructions
about your Smartlead campaigns, leads, and analytics in plain English.
The agent uses Claude to understand your requests and calls the Smartlead
API on your behalf.

Usage:
    python agent.py

Required environment variables:
    SMARTLEAD_API_KEY   -- Your Smartlead API key
    ANTHROPIC_API_KEY   -- Your Anthropic API key
"""

from __future__ import annotations

import asyncio
import json
import os
import sys

# Allow running from the repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import anthropic
from smartlead import SmartleadClient, SmartleadError

from tools import TOOLS

MODEL = "claude-opus-4-6"
SYSTEM_PROMPT = """\
You are a Smartlead assistant with full access to the Smartlead API. You can manage:

- Campaigns: create, update, delete, change status (start/pause/stop), update schedules and settings, create subsequences, export data
- Leads: add to campaigns, list, update, categorize, pause/resume, delete, unsubscribe, view message history, move between lists
- Email accounts: create (SMTP/IMAP and OAuth), list, update, delete, manage warmup, add/remove from campaigns, fetch messages, reconnect failed accounts
- Sequences: get and save email sequences with A/B variants
- Analytics: campaign statistics, date-range analytics, lead/mailbox/sequence/variant stats, warmup stats
- Global analytics: account-wide daily stats, positive replies, mailbox health by domain/name/provider, team board, lead stats, campaign response/status stats
- Webhooks: create, list, delete, get summaries, retrigger failed events
- Block list: add, list, delete blocked domains/emails
- Clients: create, list, manage API keys (for agency accounts)
- Master inbox: get replies, reply to leads, forward emails, update categories/revenue, manage tasks/notes/reminders, assign team members, block domains, resume leads
- Smart Delivery: inbox placement testing (manual and automated), SPF/DKIM/rDNS reports, blacklist checks, folder management
- Smart Senders: domain search and ordering, mailbox generation, vendor listing
- Smart Prospect: contact discovery, search with filters (industry, location, headcount, job title, etc.), email finding, saved searches

When the user asks for information or to take an action, call the appropriate tool and summarize the result in plain English. Be concise and direct. Never use em dashes.\
"""


def get_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Error: {name} environment variable is not set.")
        sys.exit(1)
    return value


def execute_tool(client: SmartleadClient, tool_name: str, tool_input: dict) -> str:
    """Execute any tool by routing to the correct SDK module and method.

    Tool names use the convention: module__method (double underscore).
    The module name matches the attribute name on SmartleadClient.
    """

    async def _run():
        parts = tool_name.split("__", 1)
        if len(parts) != 2:
            return {"error": f"Invalid tool name format: {tool_name}. Expected module__method."}

        module_name, method_name = parts

        module = getattr(client, module_name, None)
        if module is None:
            return {"error": f"Unknown module: {module_name}"}

        method = getattr(module, method_name, None)
        if method is None:
            return {"error": f"Unknown method: {method_name} on {module_name}"}

        result = await method(**tool_input)

        # Handle different return types
        if hasattr(result, "model_dump"):
            return result.model_dump()
        if isinstance(result, list):
            return [
                item.model_dump() if hasattr(item, "model_dump") else item
                for item in result
            ]
        return result

    try:
        result = asyncio.run(_run())
        return json.dumps(result, default=str)
    except SmartleadError as exc:
        return json.dumps({"error": str(exc), "status_code": exc.status_code})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def run_agent():
    """Main interactive agent loop."""
    smartlead_key = get_env("SMARTLEAD_API_KEY")
    anthropic_key = get_env("ANTHROPIC_API_KEY")

    sl_client = SmartleadClient(api_key=smartlead_key)
    anthropic_client = anthropic.Anthropic(api_key=anthropic_key)

    messages: list[dict] = []

    print("Smartlead Agent (powered by Claude)")
    print(f"Loaded {len(TOOLS)} tools across 13 modules.")
    print("Type your question or instruction. Press Ctrl+C to exit.\n")

    try:
        while True:
            try:
                user_input = input("You: ").strip()
            except EOFError:
                break

            if not user_input:
                continue

            messages.append({"role": "user", "content": user_input})

            # Agentic loop: keep calling Claude until no more tool calls
            while True:
                response = anthropic_client.messages.create(
                    model=MODEL,
                    max_tokens=4096,
                    system=SYSTEM_PROMPT,
                    tools=TOOLS,
                    messages=messages,
                )

                # Collect text and tool use blocks
                text_parts = []
                tool_calls = []
                for block in response.content:
                    if block.type == "text":
                        text_parts.append(block.text)
                    elif block.type == "tool_use":
                        tool_calls.append(block)

                # Print any text the model produced
                if text_parts:
                    print(f"\nAssistant: {''.join(text_parts)}\n")

                # If no tool calls, we're done with this turn
                if not tool_calls or response.stop_reason == "end_turn":
                    # Append the full assistant response to history
                    messages.append({"role": "assistant", "content": response.content})
                    break

                # Append the assistant message (with tool_use blocks)
                messages.append({"role": "assistant", "content": response.content})

                # Execute each tool call and collect results
                tool_results = []
                for tool_call in tool_calls:
                    print(f"  [calling {tool_call.name}...]")
                    result = execute_tool(sl_client, tool_call.name, tool_call.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tool_call.id,
                        "content": result,
                    })

                # Feed tool results back
                messages.append({"role": "user", "content": tool_results})

    except KeyboardInterrupt:
        print("\n\nGoodbye.")
    finally:
        asyncio.run(sl_client.close())


if __name__ == "__main__":
    run_agent()
