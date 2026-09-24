# Debugging Guide

Diagnostics use [SEVERITY] CODE: message plus an optional Hint.

## Workflow
1. Reproduce with the smallest requirement file.
2. Run ai-lab validate requirement.yaml.
3. Fix errors before warnings.
4. Validate again.
5. Run pytest.
6. Preserve the input and diagnostic output.
7. Report Python version, AI-LAB version, OS, command, and full error text.

## Common failures

File not found: verify the path and working directory.

YAML error: check indentation, quoting, colons, and list syntax.

Unsupported language: use Python, C, C++, Java, C#, JavaScript, Visual Basic, SQL, R, or Rust.

Secret warning: keep credentials out of requirements and source; use environment variables or a secret manager.

Generated code failure: inspect generated artifacts before execution and preserve the failure output for reproducible debugging.
