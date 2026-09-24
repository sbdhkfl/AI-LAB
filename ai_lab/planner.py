"""Deterministic AI project planner."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ProjectPlan:
    project_name: str
    language: str
    components: list[str]
    steps: list[str]
    test_strategy: list[str]
    debugging_strategy: list[str]

    def to_dict(self):
        return asdict(self)


def build_plan(req):
    components = [
        "requirement-schema",
        "validator",
        "model-adapter",
        "project-generator",
        "test-suite",
    ] + [f"capability:{capability}" for capability in req.capabilities]

    steps = [
        "Validate specification.",
        "Resolve model/component requirements.",
        "Generate project scaffold.",
        "Generate contract tests.",
        "Run validation.",
        "Review generated code before execution.",
    ]
    tests = [
        "Schema validation",
        "I/O contract tests",
        "Negative/error-path tests",
        "Deterministic planner tests",
    ]
    debugging = [
        "Capture diagnostic codes.",
        "Show failing stage and hint.",
        "Preserve input for reproduction.",
        "Re-run validation after fixes.",
    ]
    return ProjectPlan(
        req.name,
        req.preferred_language,
        components,
        steps,
        tests,
        debugging,
    )
