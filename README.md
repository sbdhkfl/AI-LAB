# AI-LAB

AI-LAB is an open-source, modular laboratory for discovering, configuring, and building AI systems from detailed human-language requirements.

## Vision

A user describes an AI in natural language. AI-LAB turns that specification into a structured plan, validates it, resolves compatible open-source components, generates project artifacts, and provides detailed diagnostics. It works with the companion Universal-Language-Compiler (ULC): ULC translates human intent into supported programming languages; AI-LAB manages the higher-level AI project lifecycle.

## Features

- Human-readable AI specifications
- Model/component registry with license metadata
- Deterministic planning and validation
- Detailed diagnostic codes and debugging workflow
- Project manifest generation
- Automated tests and CI
- Modular adapter architecture
- Review-first execution boundary
- Security guidance and secret-handling rules

## Quick start

python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
python -m ai_lab --help

Example commands:

python -m ai_lab validate examples/assistant.yaml
python -m ai_lab plan examples/assistant.yaml
python -m ai_lab models
python -m ai_lab generate examples/assistant.yaml generated/

## Safety boundary

The MVP does not automatically execute generated programs. Generated source and dependencies must be reviewed before execution. A future runner must use explicit isolation, resource limits, filesystem controls, and network policy.

## Layout

ai_lab/ = core package; tests/ = automated tests; examples/ = requirements; docs/ = architecture and debugging; .github/workflows/ = CI.

## License

MIT. See LICENSE.
