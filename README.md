# AI-LAB

AI-LAB is an open-source, modular laboratory for discovering, configuring, and building AI systems from detailed human-language requirements.

## The big idea

You explain what you want in normal human language. AI-LAB turns that idea into requirements, a plan, code/project files, tests, diagnostics, and a beginner-friendly build guide.

The companion Universal-Language-Compiler (ULC) layer handles translation from human intent to a selected programming language. AI-LAB handles the bigger project lifecycle around it.

## Beginner-first promise

**Every project we build in AI-LAB must be insanely easy to follow.**

A project is not considered beginner-ready just because its code works. Its instructions must tell the user exactly what to do next.

Every generated project should include:

1. What are we building? — simple explanation.
2. What do I need? — exact required hardware/software.
3. Before we start — a short checklist.
4. Step 1 → Step 2 → Step 3... — one action at a time.
5. Copy/paste commands whenever practical.
6. You should see — the expected result after each important step.
7. If it does not work — a nearby troubleshooting fix.
8. STOP HERE checkpoints before important or risky transitions.
9. Complete code/files instead of mystery snippets.
10. Tests after major stages so failures are caught early.
11. A final checklist proving the project is ready.

This applies to AI, software, robotics, electronics, ULC, model setup, debugging, and future project types.

See docs/BEGINNER_MODE.md and docs/PROJECT_PLAYBOOK.md.

## AI-LAB pipeline

**Human description → requirements → completeness check → model/component selection → architecture → ULC code generation → validation → tests → debugging → user review → optional controlled execution**

The system is designed so a beginner can use the simple path while developers can still access the underlying technical details.

## Debugging is part of the product

AI-LAB does not treat debugging as "figure it out yourself."

Diagnostics should explain:
- what happened
- why it probably happened
- the safest first fix
- how to verify the fix
- what information to collect if the fix fails

See docs/ERROR_MESSAGES.md for the error-writing standard.

## Open-source-first

AI-LAB prefers local and open components when practical, while still recording model/component licensing information. "Open weights" and "open source" are not automatically treated as the same thing.

## Safety boundary

The MVP does **not** automatically execute generated programs. Generated source and dependencies must be reviewed before execution. A future runner must use explicit isolation, resource limits, filesystem controls, dependency auditing, and network policy.

Never put passwords, API keys, or private tokens into project specifications or generated source.

## Quick start

Create a virtual environment, install the project, run tests, then open the CLI help:

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

## Layout

- ai_lab/ — core package and beginner-guide engine
- ai_lab/specification/ — project specification layer
- ai_lab/builder/ — project orchestration
- ai_lab/compiler/ — ULC integration boundary
- ai_lab/debugger/ — structured debugging
- ai_lab/testing/ — testing layer
- ai_lab/sandbox/ — future controlled execution boundary
- tests/ — automated tests
- examples/ — example project requirements
- docs/ — architecture, beginner mode, playbook, and debugging standards
- .github/workflows/ — CI

## License

MIT. See LICENSE.
