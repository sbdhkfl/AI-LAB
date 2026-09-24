"""Safe artifact generation; no generated code is executed."""

import json
from pathlib import Path

from .planner import build_plan


def generate_manifest(req, destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": "1",
        "requirement": req.to_dict(),
        "plan": build_plan(req).to_dict(),
        "execution_policy": "review-first",
    }
    output = destination / "ai-lab-manifest.json"
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return output
