# AI-LAB Architecture

Pipeline: human specification -> parse -> normalize -> validate -> plan -> model/component adapters -> generation -> tests -> review -> optional isolated runner.

The canonical internal representation is AIRequirement. Validation catches missing requirements, unsupported ULC languages, unsafe execution modes, and obvious secret-handling mistakes. The planner is deterministic so failures can be reproduced. The registry stores metadata and must not assume downloadable weights imply an open-source license. The MVP generates a manifest rather than executing source. Future source generation integrates with Universal-Language-Compiler.

A future execution subsystem must use explicit sandboxing, resource limits, filesystem restrictions, dependency controls, and network policy.
