"""Small reusable GUI widget helpers."""

from __future__ import annotations

import customtkinter as ctk


def make_button(parent: ctk.CTkBaseClass, text: str, command) -> ctk.CTkButton:
    return ctk.CTkButton(parent, text=text, command=command, height=42)
