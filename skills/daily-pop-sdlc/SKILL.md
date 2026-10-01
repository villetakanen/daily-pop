---
name: daily-pop-sdlc
description: Run a project-aware Daily Pop when the user wants one worthwhile question connecting product, design, engineering, or operations evidence. Use available project lenses and an optional profile; propose one coherent improvement and wait for authorisation. Not a comprehensive SDLC audit or planning workflow.
---

# Daily Pop — SDLC

Find one small, resolvable mismatch or improvement across product, design, engineering, and operations context. This is the optional project-aware version of Daily Pop. It preserves the core ritual and works independently; installing the core skill is not required.

## Discover through available lenses

Spend roughly five minutes on read-only discovery. This is a discovery budget, not a mandatory delay or a delivery-size limit. Start with repository instructions and current task context. Use a profile identified by the user or project; otherwise optionally look for `DAILY_POP.md` at the project root. Use only sources and preferences the project actually has.

Possible lenses include:

| Available context | Questions to explore |
| --- | --- |
| Strategy, roadmap, tickets, acceptance criteria | Does implementation still match the intended product outcome? Is a ticket now redundant? |
| Research, design systems, flows, design decisions | Is a UI difference intentional, or has the underlying decision changed? |
| Specifications, API contracts, architecture, ADRs | Do the contract and implementation agree? Has a decision been superseded? |
| Tests, CI, releases, incidents, observability, runbooks | Does an operational lesson need a guardrail? Does a release promise match delivered behaviour? |

These are optional lenses, not a checklist. Prefer a useful connection between sources over a list of isolated defects. Compare ticket ↔ implementation, specification ↔ contract, ADR ↔ architecture, design system ↔ UI, release note ↔ product promise, or operational learning ↔ test when evidence supports it. Check dates, superseding decisions, and intentional exceptions; do not assume a document is authoritative merely because it is formal. Correcting a specification can be better than changing code.

If structured sources are missing or inaccessible, use code, comments, tests, history, naming, or incidental documentation. State material access limits without inventing evidence. Do not require integrations, tickets, CI, formal SDLC maturity, or new process to run a Pop.

Read an existing ledger identified by the project, or optionally `POP_LEDGER.md` at the root, to avoid repetition and learn what the user finds worthwhile. Explicit user intent and repository evidence outrank it. Revisit a resolved or declined question only when relevant evidence changes.

Choose one real, interesting, singular, actionable, proportionate, non-forced question. Cite concrete paths and lines or accessible source links, distinguish observations from inferences, and surface uncertainty that affects the decision. Optimise for “Was this worth interrupting my morning for?” rather than severity or finding counts. Keep other candidates internal. Do not recast emergencies, major incidents, or sprawling redesigns as Pops. If nothing meets the bar, return exactly: “No Pop worth interrupting you for today.”

## Ask

Use the same interaction contract as the core skill:

```md
## Daily Pop — [one clear question]

**What I found:** [brief, evidence-backed explanation]

**Why this is worth attention:** [why this improves project understanding or integrity]

**Possible delivery:** [one coherent change; what changes, what does not, and how to revert]

**Verification:** [how we will know the result is correct]

What should we do?
```

One delivery means one intention, one understandable outcome, one verification story, and one reversible change set. File count, changed lines, or elapsed time do not define suitability. A repository-wide mechanical migration can qualify; a decision or clarification can also be complete. Do not turn connected evidence into a bundle of independent tasks.

## Respond and deliver

Wait for the user's answer. “Do it” authorises the proposed delivery. “Tell me more” asks for explanation. Deferral or “that is intentional” does not authorise changes. Follow a reshaped request within its scope and resolve material ambiguity without repeatedly requesting permission already given.

Before acting, ensure the user has seen what changes, what stays unchanged, how verification works, and how to revert. If later evidence materially changes the intention or outcome, return to the user instead of silently expanding the work. Carry out the agreed action, preserve unrelated work, and verify the stated outcome. Report what changed, actual verification and any gaps, and rollback. Creating a follow-up does not authorise implementation; local changes do not automatically authorise publishing or deployment.

Create or update a ledger only with user authorisation or an established project workflow. Keep it concise: `date | question | resolution | reaction`. Record actual outcomes and only user-provided reactions: `🙂` (worth it), `😐` (fine), `🥱` (avoid this shape unless significance changes). The ledger is not a backlog, plan, or authority.
