"""Requirement validation."""

from .diagnostics import error, warning
from .models import AIRequirement

SUPPORTED_LANGUAGES = {
    "python",
    "c",
    "cpp",
    "java",
    "csharp",
    "javascript",
    "visual-basic",
    "sql",
    "r",
    "rust",
}


def validate(req: AIRequirement):
    out = []
    if len(req.name.strip()) < 2:
        out.append(
            error(
                "REQ001",
                "AI name is too short.",
                "Use a descriptive project name.",
            )
        )
    if len(req.purpose.strip()) < 15:
        out.append(
            error(
                "REQ002",
                "Purpose is too vague.",
                "Explain what the AI should do and for whom.",
            )
        )
    if not req.outputs:
        out.append(
            warning(
                "REQ003",
                "No outputs were specified.",
                "Add expected outputs for meaningful tests.",
            )
        )
    if req.preferred_language.lower() not in SUPPORTED_LANGUAGES:
        out.append(
            error(
                "LANG001",
                f"Unsupported target language: {req.preferred_language}",
                "Choose one of the ten ULC targets.",
            )
        )
    if req.execution_mode != "review-first":
        out.append(
            error(
                "SAFE001",
                "Only review-first execution is supported.",
                "Review generated code before execution.",
            )
        )
    if any(
        "password" in constraint.lower() or "api key" in constraint.lower()
        for constraint in req.constraints
    ):
        out.append(
            warning(
                "SEC001",
                "A constraint appears to mention a secret.",
                "Use environment variables or a secret store.",
            )
        )
    return out
