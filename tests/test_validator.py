from ai_lab.models import AIRequirement
from ai_lab.validator import validate

def test_valid():
    r=AIRequirement("Test Assistant","A useful assistant for answering questions.",outputs=["text"])
    assert not any(d.severity=="ERROR" for d in validate(r))
def test_vague():
    assert any(d.code=="REQ002" for d in validate(AIRequirement("Test","")))
def test_language():
    r=AIRequirement("Test Assistant","A useful assistant for answering questions.",preferred_language="brain")
    assert any(d.code=="LANG001" for d in validate(r))
def test_execution():
    r=AIRequirement("Test Assistant","A useful assistant for answering questions.",execution_mode="auto")
    assert any(d.code=="SAFE001" for d in validate(r))
