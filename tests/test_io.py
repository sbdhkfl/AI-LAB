from ai_lab.io import load_requirement


def test_yaml(tmp_path):
    path = tmp_path / "req.yaml"
    path.write_text(
        "name: Demo\npurpose: A demo assistant for testing.\noutputs: [text]\n",
        encoding="utf-8",
    )
    requirement = load_requirement(path)
    assert requirement.name == "Demo"
    assert requirement.outputs == ["text"]
