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
SYSTEM_PROMPT = (
    "You are a Smartlead assistant. Use the available tools to help manage "
    "campaigns, leads, and email accounts. When the user asks for information "
    "or to take an action, call the appropriate tool and summarise the result "
    "in plain English. Be concise and direct."
)


def get_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Error: {name} environment variable is not set.")
        sys.exit(1)
    return value


def execute_tool(client: SmartleadClient, tool_name: str, tool_input: dict) -> str:
    """Execute a tool call and return the result as a JSON string."""

    async def _run():
        if tool_name == "list_campaigns":
            data = await client.global_analytics.campaign_list(limit=200)
            return data

        elif tool_name == "get_campaign_stats":
            stats = await client.analytics.get_statistics(tool_input["campaign_id"])
            return stats.model_dump()

        elif tool_name == "list_leads":
            limit = tool_input.get("limit", 100)
            result = await client.leads.list_by_campaign(
                tool_input["campaign_id"], limit=limit
            )
            return result.model_dump()

        elif tool_name == "add_lead":
            lead_data = {"email": tool_input["email"]}
            if "first_name" in tool_input:
                lead_data["first_name"] = tool_input["first_name"]
            if "last_name" in tool_input:
                lead_data["last_name"] = tool_input["last_name"]
            if "company" in tool_input:
                lead_data["company_name"] = tool_input["company"]
            result = await client.leads.add_to_campaign(
                tool_input["campaign_id"], leads=[lead_data]
            )
            return result.model_dump()

        elif tool_name == "pause_campaign":
            result = await client.campaigns.update_status(tool_input["campaign_id"], "PAUSED")
            return result

        elif tool_name == "start_campaign":
            result = await client.campaigns.update_status(tool_input["campaign_id"], "START")
            return result

        elif tool_name == "get_analytics_overview":
            data = await client.global_analytics.daily_stats()
            return data

        else:
            return {"error": f"Unknown tool: {tool_name}"}

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
