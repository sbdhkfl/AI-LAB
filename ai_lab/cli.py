"""AI-LAB command line interface."""

import argparse
import json
import sys

from .generator import generate_manifest
from .io import load_requirement
from .planner import build_plan
from .registry import ModelRegistry
from .validator import validate


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ai-lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in ("plan", "validate"):
        command = subparsers.add_parser(name)
        command.add_argument("requirement")

    command = subparsers.add_parser("generate")
    command.add_argument("requirement")
    command.add_argument("destination")
    subparsers.add_parser("models")

    args = parser.parse_args(argv)

    try:
        if args.command == "models":
            for model in ModelRegistry().list():
                print(f"{model.name} | {model.family} | {model.license}")
            return 0

        requirement = load_requirement(args.requirement)
        diagnostics = validate(requirement)

        if args.command == "validate":
            for diagnostic in diagnostics:
                print(diagnostic.format())
            if not diagnostics:
                print("VALID: requirement passed AI-LAB validation.")
            return 1 if any(d.severity == "ERROR" for d in diagnostics) else 0

        if any(d.severity == "ERROR" for d in diagnostics):
            for diagnostic in diagnostics:
                print(diagnostic.format(), file=sys.stderr)
            return 1

        if args.command == "plan":
            print(json.dumps(build_plan(requirement).to_dict(), indent=2))
        else:
            print(generate_manifest(requirement, args.destination))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[ERROR] AI001: {exc}", file=sys.stderr)
        return 2
