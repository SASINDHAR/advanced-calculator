"""Scientific expression evaluation."""

from __future__ import annotations

import sympy as sp


_ALLOWED_NAMES = {
    "E": sp.E,
    "pi": sp.pi,
    "sqrt": sp.sqrt,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "log": sp.log,
    "ln": sp.log,
    "exp": sp.exp,
    "factorial": sp.factorial,
}


def evaluate_expression(expression: str) -> str:
    """Evaluate a mathematical expression and return a readable result."""
    if not expression.strip():
        return ""

    parsed = sp.sympify(expression, locals=_ALLOWED_NAMES)
    result = sp.N(parsed)

    if result == int(result):
        return str(int(result))
    return str(result)
