"""Unit conversion helpers."""

from __future__ import annotations


_CONVERSIONS = {
    ("cm", "m"): 0.01,
    ("m", "cm"): 100,
    ("m", "km"): 0.001,
    ("km", "m"): 1000,
    ("g", "kg"): 0.001,
    ("kg", "g"): 1000,
    ("c", "f"): lambda value: (value * 9 / 5) + 32,
    ("f", "c"): lambda value: (value - 32) * 5 / 9,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    source = from_unit.lower()
    target = to_unit.lower()

    if source == target:
        return value

    rule = _CONVERSIONS.get((source, target))
    if rule is None:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")

    if callable(rule):
        return rule(value)
    return value * rule
