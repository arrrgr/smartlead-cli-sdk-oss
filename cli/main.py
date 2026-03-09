"""Smartlead CLI -- entry point and all subcommands."""

from __future__ import annotations

import asyncio
import json
import os
import sys
from typing import Optional

import typer
from rich.console import Console

from ._output import console, print_json, print_table, print_kv, error, success

app = typer.Typer(
    name="smartlead",
    help="Unofficial CLI for the Smartlead API.",
    no_args_is_help=True,
)
campaigns_app = typer.Typer(help="Manage campaigns.", no_args_is_help=True)
leads_app = typer.Typer(help="Manage leads.", no_args_is_help=True)
email_accounts_app = typer.Typer(help="Manage email accounts.", no_args_is_help=True)
analytics_app = typer.Typer(help="View analytics.", no_args_is_help=True)

app.add_typer(campaigns_app, name="campaigns")
app.add_typer(leads_app, name="leads")
app.add_typer(email_accounts_app, name="email-accounts")
app.add_typer(analytics_app, name="analytics")


def get_client():
    """Build a SmartleadClient from environment. Raises if key is missing."""
    # Import here to keep startup fast
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    from smartlead import SmartleadClient

    api_key = os.environ.get("SMARTLEAD_API_KEY")
    if not api_key:
        error("SMARTLEAD_API_KEY environment variable is not set.")
        error("Run: export SMARTLEAD_API_KEY=your_key_here")
        raise typer.Exit(code=1)
    return SmartleadClient(api_key=api_key)


def output_flag() -> str:
    """Placeholder -- actual output mode is passed per-command."""
    return "table"


# ---------------------------------------------------------------------------
# campaigns
# ---------------------------------------------------------------------------

@campaigns_app.command("list")
def campaigns_list(
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """List all campaigns."""
    client = get_client()

    async def _run():
        async with client:
            data = await client.global_analytics.campaign_list(limit=200)
        return data

    try:
        data = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    if output == "json":
        print_json(data)
        return

    # Normalise: the endpoint returns a list or a dict with a list inside
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict):
        rows = data.get("data") or data.get("campaigns") or [data]
    else:
        rows = []

    if not rows:
        console.print("No campaigns found.")
        return

    print_table(
        rows=[{
            "id": r.get("id", ""),
            "name": r.get("name", ""),
            "status": r.get("status", ""),
            "created_at": r.get("created_at", ""),
        } for r in rows],
        columns=["id", "name", "status", "created_at"],
    )


@campaigns_app.command("get")
def campaigns_get(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Get campaign details."""
    client = get_client()

    async def _run():
        async with client:
            return await client.campaigns.get(campaign_id)

    try:
        campaign = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    data = campaign.model_dump()
    if output == "json":
        print_json(data)
        return

    print_kv({k: v for k, v in data.items() if v is not None})


@campaigns_app.command("stats")
def campaigns_stats(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Show campaign overall stats."""
    client = get_client()

    async def _run():
        async with client:
            return await client.analytics.get_statistics(campaign_id)

    try:
        stats = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    data = stats.model_dump()
    if output == "json":
        print_json(data)
        return

    print_kv({
        "Campaign ID": data.get("id", campaign_id),
        "Name": data.get("name", ""),
        "Status": data.get("status", ""),
        "Sent": data.get("sent_count", 0),
        "Opens": data.get("open_count", 0),
        "Clicks": data.get("click_count", 0),
        "Replies": data.get("reply_count", 0),
        "Bounces": data.get("bounce_count", 0),
        "Unsubscribed": data.get("unsubscribed_count", 0),
    })


@campaigns_app.command("pause")
def campaigns_pause(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
):
    """Pause a campaign."""
    client = get_client()

    async def _run():
        async with client:
            return await client.campaigns.update_status(campaign_id, "PAUSED")

    try:
        asyncio.run(_run())
        success(f"Campaign {campaign_id} paused.")
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)


@campaigns_app.command("start")
def campaigns_start(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
):
    """Start or resume a campaign."""
    client = get_client()

    async def _run():
        async with client:
            return await client.campaigns.update_status(campaign_id, "START")

    try:
        asyncio.run(_run())
        success(f"Campaign {campaign_id} started.")
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)


# ---------------------------------------------------------------------------
# leads
# ---------------------------------------------------------------------------

@leads_app.command("list")
def leads_list(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    limit: int = typer.Option(100, "--limit", "-l", help="Maximum leads to return"),
    offset: int = typer.Option(0, "--offset", help="Offset for pagination"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """List leads in a campaign."""
    client = get_client()

    async def _run():
        async with client:
            return await client.leads.list_by_campaign(campaign_id, offset=offset, limit=limit)

    try:
        result = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    if output == "json":
        print_json(result.model_dump())
        return

    rows = result.data or []
    if not rows:
        console.print("No leads found.")
        return

    print_table(
        rows=[{
            "id": r.lead.id if r.lead else "",
            "email": r.lead.email if r.lead else "",
            "first_name": r.lead.first_name if r.lead else "",
            "last_name": r.lead.last_name if r.lead else "",
            "company": r.lead.company_name if r.lead else "",
            "status": r.status or "",
        } for r in rows],
        columns=["id", "email", "first_name", "last_name", "company", "status"],
    )
    console.print(f"\nTotal: {result.total_leads} leads")


@leads_app.command("add")
def leads_add(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    email: str = typer.Argument(..., help="Lead email address"),
    first_name: Optional[str] = typer.Option(None, "--first-name", help="First name"),
    last_name: Optional[str] = typer.Option(None, "--last-name", help="Last name"),
    company: Optional[str] = typer.Option(None, "--company", help="Company name"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Add a single lead to a campaign."""
    client = get_client()

    lead_data = {"email": email}
    if first_name:
        lead_data["first_name"] = first_name
    if last_name:
        lead_data["last_name"] = last_name
    if company:
        lead_data["company_name"] = company

    async def _run():
        async with client:
            return await client.leads.add_to_campaign(campaign_id, leads=[lead_data])

    try:
        result = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    if output == "json":
        print_json(result.model_dump())
        return

    print_kv({
        "OK": result.ok,
        "Uploaded": result.upload_count,
        "Total in campaign": result.total_leads,
        "Duplicates": result.duplicate_count,
        "Invalid emails": result.invalid_email_count,
    })


@leads_app.command("get")
def leads_get(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    email: str = typer.Argument(..., help="Lead email address"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Get lead details by email."""
    client = get_client()

    async def _run():
        async with client:
            return await client.leads.get_by_email(email)

    try:
        lead = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    data = lead.model_dump()
    if output == "json":
        print_json(data)
        return

    print_kv({k: v for k, v in data.items() if v is not None and k != "lead_campaign_data"})


# ---------------------------------------------------------------------------
# email-accounts
# ---------------------------------------------------------------------------

@email_accounts_app.command("list")
def email_accounts_list(
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """List all email accounts."""
    client = get_client()

    async def _run():
        async with client:
            return await client.email_accounts.list_all(limit=200)

    try:
        accounts = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    if output == "json":
        print_json([a.model_dump() for a in accounts])
        return

    if not accounts:
        console.print("No email accounts found.")
        return

    print_table(
        rows=[{
            "id": a.id,
            "from_email": a.from_email or "",
            "from_name": a.from_name or "",
            "smtp_host": a.smtp_host or "",
            "smtp_ok": "yes" if a.is_smtp_success else "no",
            "imap_ok": "yes" if a.is_imap_success else "no",
            "sent_today": a.daily_sent_count or 0,
        } for a in accounts],
        columns=["id", "from_email", "from_name", "smtp_host", "smtp_ok", "imap_ok", "sent_today"],
    )


@email_accounts_app.command("stats")
def email_accounts_stats(
    account_id: int = typer.Argument(..., help="Email account ID"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Show warmup stats for an email account."""
    client = get_client()

    async def _run():
        async with client:
            return await client.email_accounts.get_warmup_stats(account_id)

    try:
        stats = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    data = stats.model_dump()
    if output == "json":
        print_json(data)
        return

    print_kv({
        "Account ID": data.get("id", account_id),
        "Sent (total)": data.get("sent_count", 0),
        "Spam count": data.get("spam_count", 0),
        "Inbox count": data.get("inbox_count", 0),
        "Warmup emails received": data.get("warmup_email_received_count", 0),
    })


# ---------------------------------------------------------------------------
# analytics
# ---------------------------------------------------------------------------

@analytics_app.command("overview")
def analytics_overview(
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Show global day-wise stats (last 7 days)."""
    client = get_client()

    async def _run():
        async with client:
            return await client.global_analytics.daily_stats()

    try:
        data = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    if output == "json":
        print_json(data)
        return

    rows = data if isinstance(data, list) else (data.get("data") or [data])
    if not rows:
        console.print("No data available.")
        return

    print_table(
        rows=[{
            "date": r.get("date", ""),
            "sent": r.get("sent_count", 0),
            "opens": r.get("open_count", 0),
            "replies": r.get("reply_count", 0),
            "bounces": r.get("bounce_count", 0),
        } for r in rows],
        columns=["date", "sent", "opens", "replies", "bounces"],
    )


@analytics_app.command("campaign")
def analytics_campaign(
    campaign_id: int = typer.Argument(..., help="Campaign ID"),
    output: str = typer.Option("table", "--output", "-o", help="Output format: table or json"),
):
    """Show analytics for a specific campaign."""
    client = get_client()

    async def _run():
        async with client:
            return await client.analytics.get_top_level(campaign_id)

    try:
        stats = asyncio.run(_run())
    except Exception as exc:
        error(str(exc))
        raise typer.Exit(code=1)

    data = stats.model_dump()
    if output == "json":
        print_json(data)
        return

    print_kv({
        "Campaign": data.get("name", campaign_id),
        "Status": data.get("status", ""),
        "Sent": data.get("sent_count", 0),
        "Unique opens": data.get("unique_open_count", 0),
        "Clicks": data.get("click_count", 0),
        "Replies": data.get("reply_count", 0),
        "Bounces": data.get("bounce_count", 0),
        "Unsubscribed": data.get("unsubscribed_count", 0),
    })


def main():
    app()


if __name__ == "__main__":
    main()
