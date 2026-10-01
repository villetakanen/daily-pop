# Minimal repository

**Fixture:** [examples/minimal-repository/](../examples/minimal-repository/)

**Skill:** `daily-pop`

**Prompt:** `/pop`

Use the [manual run procedure](README.md) to keep expectations out of the agent’s context.

## Expected outcome

One Pop asks whether a whitespace-only name should greet “friend”. It cites the README promise and the fallback being chosen before whitespace is stripped in `greeting.py`. It describes two possible deliveries for that one decision: fix the code to match the promise, or correct the promise if the current behaviour is intended. It includes verification and rollback, changes no files, and raises no second question.

Equivalent wording is fine. Returning no Pop, repeating an example answer supplied in context, silently picking the intended behaviour, or editing the fixture does not meet this case’s expectations.

## Manual runs

2026-10-01: the first 0.3.0 candidate found the mismatch but omitted the documentation alternative. After clarifying the decision rule, a fresh run passed. Neither run changed files. See the [run record and responses](results/2026-10-01/README.md).
