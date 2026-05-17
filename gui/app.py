"""CustomTkinter application for the advanced calculator."""

from __future__ import annotations

import customtkinter as ctk

from calculator.history import add_history, clear_history, load_history
from calculator.scientific import evaluate_expression
from .themes import APP_TITLE, WINDOW_SIZE
from .widgets import make_button


class CalculatorApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title(APP_TITLE)
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)

        self.expression = ctk.StringVar()
        self._build_ui()

    def _build_ui(self) -> None:
        display = ctk.CTkEntry(
            self,
            textvariable=self.expression,
            font=("Segoe UI", 28),
            justify="right",
            height=70,
        )
        display.pack(fill="x", padx=16, pady=(16, 8))

        buttons = [
            ["7", "8", "9", "/", "sqrt("],
            ["4", "5", "6", "*", "sin("],
            ["1", "2", "3", "-", "cos("],
            ["0", ".", "(", ")", "+"],
            ["pi", "log(", "exp(", "^", "C"],
        ]

        grid = ctk.CTkFrame(self)
        grid.pack(fill="both", expand=True, padx=16, pady=8)

        for row_index, row in enumerate(buttons):
            grid.grid_rowconfigure(row_index, weight=1)
            for column_index, label in enumerate(row):
                grid.grid_columnconfigure(column_index, weight=1)
                command = self._clear if label == "C" else lambda value=label: self._append(value)
                button = make_button(grid, label, command)
                button.grid(row=row_index, column=column_index, padx=4, pady=4, sticky="nsew")

        actions = ctk.CTkFrame(self)
        actions.pack(fill="x", padx=16, pady=(0, 12))

        make_button(actions, "=", self._calculate).pack(side="left", expand=True, fill="x", padx=(0, 4))
        make_button(actions, "History", self._show_history).pack(side="left", expand=True, fill="x", padx=4)
        make_button(actions, "Clear History", self._clear_history).pack(side="left", expand=True, fill="x", padx=(4, 0))

    def _append(self, value: str) -> None:
        if value == "^":
            value = "**"
        self.expression.set(self.expression.get() + value)

    def _clear(self) -> None:
        self.expression.set("")

    def _calculate(self) -> None:
        expression = self.expression.get()
        try:
            result = evaluate_expression(expression)
        except Exception as exc:
            result = f"Error: {exc}"

        self.expression.set(result)
        if expression and not result.startswith("Error:"):
            add_history(expression, result)

    def _show_history(self) -> None:
        history = load_history()
        window = ctk.CTkToplevel(self)
        window.title("History")
        window.geometry("360x420")

        text = ctk.CTkTextbox(window)
        text.pack(fill="both", expand=True, padx=12, pady=12)

        if not history:
            text.insert("end", "No history yet.")
        else:
            for item in history:
                text.insert("end", f"{item['expression']} = {item['result']}\n")
        text.configure(state="disabled")

    def _clear_history(self) -> None:
        clear_history()
