from ai_lab.guide import GuideStep, ProjectGuide, beginner_rules


def test_guide_requires_consecutive_steps():
    guide = ProjectGuide("Demo", "A tiny demo.")
    guide.add(GuideStep(1, "Start", "Do it.", "It works.", "Try again."))
    try:
        guide.add(GuideStep(3, "Wrong", "Do it.", "It works.", "Try again."))
    except ValueError:
        pass
    else:
        raise AssertionError("non-consecutive steps should fail")


def test_guide_renders_expected_result_and_fix():
    guide = ProjectGuide("Demo", "A tiny demo.")
    guide.add(GuideStep(1, "Start", "Run X.", "Y appears.", "Run Z."))
    output = guide.render()
    assert "You should see" in output
    assert "If it does not work" in output
    assert "Step 1" in output


def test_beginner_rules_are_present():
    assert "Never assume the user already knows a technical term." in beginner_rules()
