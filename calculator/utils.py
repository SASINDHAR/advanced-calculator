"""Shared utility helpers."""

from __future__ import annotations


def format_result(value: object) -> str:
    text = str(value)
    if text.endswith(".0"):
        return text[:-2]
    return text


def is_number(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True
