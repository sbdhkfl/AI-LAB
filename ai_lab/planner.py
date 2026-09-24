"""Deterministic AI project planner."""
from dataclasses import dataclass,asdict
from .models import AIRequirement
@dataclass(frozen=True)
class ProjectPlan:
    project_name:str; language:str; components:list[str]; steps:list[str]; test_strategy:list[str]; debugging_strategy:list[str]
    def to_dict(self): return asdict(self)
def build_plan(req):
    components=["requirement-schema","validator","model-adapter","project-generator","test-suite"]+[f"capability:{c}" for c in req.capabilities]
    return ProjectPlan(req.name,req.preferred_language,components,["Validate specification.","Resolve model/component requirements.","Generate project scaffold.","Generate contract tests.","Run validation.","Review generated code before execution."],["Schema validation","I/O contract tests","Negative/error-path tests","Deterministic planner tests"],["Capture diagnostic codes.","Show failing stage and hint.","Preserve input for reproduction.","Re-run validation after fixes."])
