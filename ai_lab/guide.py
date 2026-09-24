"""Beginner-first project guidance."""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class GuideStep:
    number: int
    title: str
    do_this: str
    expect: str
    if_broken: str
    stop_point: bool = False

@dataclass
class ProjectGuide:
    title: str
    goal: str
    steps: list[GuideStep] = field(default_factory=list)

    def add(self, step: GuideStep) -> "ProjectGuide":
        if step.number != len(self.steps) + 1:
            raise ValueError("Guide steps must be numbered consecutively.")
        self.steps.append(step)
        return self

    def render(self) -> str:
        lines = [f"# {self.title}", "", "## What we're building", self.goal, ""]
        for step in self.steps:
            lines += [
                f"## Step {step.number} — {step.title}", "",
                step.do_this, "",
                f"**You should see:** {step.expect}", "",
                f"**If it does not work:** {step.if_broken}",
            ]
            if step.stop_point:
                lines += ["", "**STOP HERE.** Check this step before continuing."]
            lines += [""]
        return "\n".join(lines).rstrip()

def beginner_rules() -> tuple[str, ...]:
    return (
        "Explain the goal before giving commands.",
        "Use one action per numbered step whenever practical.",
        "Show exactly what success looks like.",
        "Put troubleshooting immediately after the step that can fail.",
        "Prefer complete copy-paste commands and complete files.",
        "Never assume the user already knows a technical term.",
        "Add safe STOP HERE checkpoints for hardware, credentials, and execution.",
        "Finish with a test checklist and a plain-English error path.",
    )
