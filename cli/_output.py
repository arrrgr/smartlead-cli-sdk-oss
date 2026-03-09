"""Shared output helpers for the Smartlead CLI."""

from __future__ import annotations

import json
from typing import Any

from rich.console import Console
from rich.table import Table

console = Console()


def print_json(data: Any) -> None:
    """Print data as formatted JSON."""
    console.print_json(json.dumps(data, default=str))


def print_table(rows: list[dict[str, Any]], columns: list[str]) -> None:
    """Print a rich table from a list of dicts."""
    table = Table(show_header=True, header_style="bold cyan")
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*[str(row.get(col, "")) for col in columns])
    console.print(table)


def print_kv(data: dict[str, Any]) -> None:
    """Print key-value pairs as a simple table."""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Key", style="bold cyan")
    table.add_column("Value")
    for k, v in data.items():
        table.add_row(str(k), str(v))
    console.print(table)


def error(message: str) -> None:
    """Print an error message."""
    console.print(f"[bold red]Error:[/bold red] {message}")


def success(message: str) -> None:
    """Print a success message."""
    console.print(f"[bold green]OK:[/bold green] {message}")
