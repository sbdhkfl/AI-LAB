"""Structured diagnostics."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: str
    message: str
    hint: str = ""
    def format(self) -> str:
        return f"[{self.severity}] {self.code}: {self.message}" + (f" Hint: {self.hint}" if self.hint else "")

def error(code, message, hint=""): return Diagnostic(code,"ERROR",message,hint)
def warning(code, message, hint=""): return Diagnostic(code,"WARNING",message,hint)
