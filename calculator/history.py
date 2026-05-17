"""Calculation history persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


HISTORY_PATH = Path(__file__).resolve().parent.parent / "data" / "history.json"


def load_history() -> list[dict[str, Any]]:
    if not HISTORY_PATH.exists():
        return []

    try:
        return json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_history(entries: list[dict[str, Any]]) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    HISTORY_PATH.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def add_history(expression: str, result: str) -> None:
    entries = load_history()
    entries.append({"expression": expression, "result": result})
    save_history(entries[-100:])


def clear_history() -> None:
    save_history([])
