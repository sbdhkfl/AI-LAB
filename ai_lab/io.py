"""Requirement file loading."""

import json
from pathlib import Path

import yaml

from .models import AIRequirement


def load_requirement(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Requirement file not found: {path}")
    if path.suffix.lower() in {".yaml", ".yml"}:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    elif path.suffix.lower() == ".json":
        raw = json.loads(path.read_text(encoding="utf-8"))
    else:
        raise ValueError("Requirement files must use .yaml, .yml, or .json")
    if not isinstance(raw, dict):
        raise TypeError("Requirement document must be an object.")
    return AIRequirement.from_dict(raw)
