# AI-LAB

AI-LAB is an open-source, modular laboratory for discovering, configuring, and building AI systems from detailed human-language requirements.

## Vision

AI-LAB connects human intent to reproducible AI projects. A user describes an AI in natural language, AI-LAB turns that specification into a structured project plan, selects compatible open-source components, validates the plan, generates project files, and provides diagnostics for failures.

AI-LAB works with the companion Universal-Language-Compiler (ULC). ULC handles human-language-to-code translation for supported programming languages; AI-LAB handles the higher-level AI project lifecycle.

## Core principles

- Open-source-first architecture.
- Model/provider adapters instead of hard-coded vendors.
- Human-readable project specifications.
- Deterministic validation wherever possible.
- Detailed diagnostics and actionable debugging.
- Tests before claiming a generated project is valid.
- Sandboxed execution boundaries; generated code is not automatically executed.
- Modular components that can be replaced or extended.
- No secrets committed to source control.

## MVP

The first implementation provides a structured AI specification schema, project planner, local model registry, validation and diagnostic reporting, project manifest generator, safe dry-run build workflow, CLI commands, unit tests, CI, and debugging documentation.

## Quick start

python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m ai_lab --help
python -m pytest

Try examples/assistant.yaml with:

python -m ai_lab plan examples/assistant.yaml
python -m ai_lab validate examples/assistant.yaml
python -m ai_lab models

## Safety boundary

AI-LAB can generate plans and source files, but the MVP does not automatically execute generated programs. Review generated code and dependencies before running them. Future sandboxing must use explicit isolation rather than treating generated code as trusted.

## Layout

ai_lab/ contains the core Python package. tests/ contains automated tests. examples/ contains requirements. docs/ contains architecture and debugging documentation. .github/workflows/ contains CI.

## License

MIT. See LICENSE.
