# Agent Instructions

Read `README.md` before changing the project.

## Execution discipline

- Never guess; inspect the authoritative source first.
- Keep changes small and bounded.
- For work spanning multiple files or likely to run for a while, state the current batch, complete and verify it, report progress, then continue.
- If a patch, exact-text replacement, or expected match fails, reread the current source and diagnose the mismatch before retrying. Do not retry stale input.
- Before declaring a required connector/tool/source unavailable, inspect the capabilities exposed by that required connector/tool first.
- Preserve unrelated work and verify changes before reporting completion.
- Before any semantic/product/UX/business-rule/default/workflow/data-interpretation/classification/heuristic/fallback/persistent-data behaviour change: investigate, explain the current finding and exact proposed effect, then wait for Rob's explicit approval. Treat uncertain changes as semantic; mechanical no-behaviour changes may proceed.
- Never claim a preference, rule, memory, or instruction is persisted unless the authoritative persistent source was actually updated and verified.
- Record only reusable, verified failures in `.agents/LESSONS.md`.
