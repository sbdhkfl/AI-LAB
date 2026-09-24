"""Canonical AI requirement model."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AIRequirement:
    name: str
    purpose: str
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    preferred_language: str = "python"
    model_family: str | None = None
    execution_mode: str = "review-first"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AIRequirement":
        missing = [key for key in ("name", "purpose") if not data.get(key)]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
        return cls(
            name=str(data["name"]),
            purpose=str(data["purpose"]),
            inputs=[str(value) for value in data.get("inputs", [])],
            outputs=[str(value) for value in data.get("outputs", [])],
            capabilities=[str(value) for value in data.get("capabilities", [])],
            constraints=[str(value) for value in data.get("constraints", [])],
            preferred_language=str(data.get("preferred_language", "python")),
            model_family=data.get("model_family"),
            execution_mode=str(data.get("execution_mode", "review-first")),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "purpose": self.purpose,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "capabilities": self.capabilities,
            "constraints": self.constraints,
            "preferred_language": self.preferred_language,
            "model_family": self.model_family,
            "execution_mode": self.execution_mode,
        }
