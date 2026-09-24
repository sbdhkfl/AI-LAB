from ai_lab.models import AIRequirement
from ai_lab.planner import build_plan


def test_deterministic():
    requirement = AIRequirement(
        "Assistant",
        "A local assistant that answers questions.",
        outputs=["text"],
    )
    first = build_plan(requirement).to_dict()
    second = build_plan(requirement).to_dict()
    assert first == second
    assert "project-generator" in build_plan(requirement).components
