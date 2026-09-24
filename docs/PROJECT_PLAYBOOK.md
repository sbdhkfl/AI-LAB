# AI-LAB Project Playbook

This template applies to **all AI-LAB projects**: software, AI, robotics, electronics, and Universal-Language-Compiler projects.

## Phase A — Understand
1. Say what the project does.
2. Explain unfamiliar words.
3. List exactly what is needed.
4. Separate required items from optional upgrades.
5. State what the finished project should do.

## Phase B — Prepare
1. Check operating system and versions.
2. Check hardware connections without powering risky circuits.
3. Create the project folder.
4. Install dependencies.
5. Verify each dependency with a small test.

## Phase C — Build
For each piece:
1. Give one clear action.
2. Give the expected result.
3. Give an immediate fix if the result is different.
4. Run a small test.
5. Only then continue.

## Phase D — Debug
A diagnostic should contain:
- error code
- severity
- plain-English explanation
- likely cause
- suggested fix
- verification step

When possible, preserve a reproducible debug record containing project version, step number, command/test name, expected result, observed result, and diagnostic code. Never put passwords, API keys, or private tokens into that record.

## Phase E — Test
Tests should cover normal input, missing input, invalid input, important edge cases, and failure recovery.

## Phase F — Review
Before execution or deployment:
- show generated files
- explain important files
- identify permissions and network access
- identify external services
- check for secrets
- let the user review the result

AI-LAB follows a **review-first execution boundary**. Generation succeeding does not mean code is automatically executed.

## Phase G — Finish
Provide the final checklist, how to start the project later, where configuration lives, how to update it, how to troubleshoot it, and how to safely remove it.

## Hardware-specific rule
Explicitly identify power source, voltage, ground, pin numbers, wire/component names, polarity where relevant, and a no-power wiring checkpoint. Never assume similar-looking connectors are interchangeable.

## AI-specific rule
Explain what the model does, where it runs, hardware requirements, model/license status, what data leaves the device, how to change models, and how to debug model failures.

## ULC-specific rule
Use:
**Human description → structured requirements → completeness check → target language → generated code → validation → tests → debugging → user review**
