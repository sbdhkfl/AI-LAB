"""Structured diagnostics."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: str
    message: str
    hint: str = ""

    def format(self) -> str:
        suffix = f" Hint: {self.hint}" if self.hint else ""
        return f"[{self.severity}] {self.code}: {self.message}{suffix}"


def error(code, message, hint=""):
    return Diagnostic(code, "ERROR", message, hint)


def warning(code, message, hint=""):
    return Diagnostic(code, "WARNING", message, hint)
