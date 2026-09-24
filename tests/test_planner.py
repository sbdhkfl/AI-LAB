from ai_lab.models import AIRequirement
from ai_lab.planner import build_plan

def test_deterministic():
    r=AIRequirement("Assistant","A local assistant that answers questions.",outputs=["text"])
    assert build_plan(r).to_dict()==build_plan(r).to_dict()
    assert "project-generator" in build_plan(r).components
