from ai_lab.models import AIRequirement
from ai_lab.validator import validate


def test_valid():
    requirement = AIRequirement(
        "Test Assistant",
        "A useful assistant for answering questions.",
        outputs=["text"],
    )
    assert not any(
        diagnostic.severity == "ERROR" for diagnostic in validate(requirement)
    )


def test_vague():
    requirement = AIRequirement("Test", "")
    assert any(diagnostic.code == "REQ002" for diagnostic in validate(requirement))


def test_language():
    requirement = AIRequirement(
        "Test Assistant",
        "A useful assistant for answering questions.",
        preferred_language="brain",
    )
    assert any(diagnostic.code == "LANG001" for diagnostic in validate(requirement))


def test_execution():
    requirement = AIRequirement(
        "Test Assistant",
        "A useful assistant for answering questions.",
        execution_mode="auto",
    )
    assert any(diagnostic.code == "SAFE001" for diagnostic in validate(requirement))
