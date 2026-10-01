---
name: daily-pop
description: Run the Daily Pop coffee-time ritual when the user asks for a Pop or one worthwhile project question. Explore available context, present one evidence-backed question, and carry out a coherent improvement only after authorisation. Not a general audit, planning session, or status report.
---

# Daily Pop

Find one real, useful question in the work at hand, then help deliver one coherent improvement. Optimise for “Was this worth interrupting my morning for?”

## Discover

Spend roughly five minutes surveying available project context. This is a discovery budget, not a mandatory delay or a limit on later delivery. Use read-only exploration until the user authorises action.

Start with repository instructions, current task context, relevant files, and Git history when available. Follow promising evidence rather than a mandatory checklist. Code, comments, tests, naming, dead files, dependencies, duplicated behaviour, unclear intent, and stale documentation can all offer questions. Do not require tickets, specs, ADRs, a design system, CI, or a vendor. Missing sources are limitations, not a reason to invent findings or set up infrastructure.

If a project profile or Pop Ledger is already identified in context, read it when useful. Otherwise, optionally look for `DAILY_POP.md` and `POP_LEDGER.md` at the project root. Neither is required. Respect local preferences without treating the ledger as authority; explicit user intent and repository evidence outrank it. Avoid repeating resolved or declined Pops unless relevant evidence changes.

Select one question that is real, interesting, singular, actionable, proportionate, and non-forced. Confirm its premise against concrete evidence and intentional exceptions. Separate observation from inference, cite paths and lines or accessible source links, and disclose uncertainty that affects the question. Do not imply inaccessible sources were checked.

Keep alternate candidates internal. Do not rank findings by severity or fill an output quota. Emergencies and major incidents belong in their existing response process, not a manufactured Pop delivery. A sprawling redesign is not a morning question. If no candidate meets the bar, return exactly: “No Pop worth interrupting you for today.”

## Ask

Use this interaction contract:

```md
## Daily Pop — [one clear question]

**What I found:** [brief, evidence-backed explanation]

**Why this is worth attention:** [why this improves project understanding or integrity]

**Possible delivery:** [one coherent change; what changes, what does not, and how to revert]

**Verification:** [how we will know the result is correct]

What should we do?
```

A valid delivery has one intention, one understandable outcome, one verification story, and one reversible change set. Do not reject it merely for touching many files or taking more than a few minutes. A mechanical repository-wide migration may qualify when its rationale, references, verification, and rollback are coherent. A clarification or decision may also be the whole outcome.

## Respond and deliver

Wait for the user's answer. “Do it” authorises the stated delivery; “tell me more” requests explanation; “leave it” or “that is intentional” is not permission to change it. Follow a reshaped request within its scope. Resolve ambiguity before consequential action, but do not repeatedly ask for permission already given.

Before implementation, ensure the user has seen what will change, what will not change, verification, and rollback. If new evidence materially changes the proposed intention or outcome, bring that change back to the user rather than silently broadening authorisation.

Carry out the agreed action, preserve unrelated work, and verify the stated outcome. Report the result, actual verification and any gaps, and how to revert the change. Do not treat an instruction to make a follow-up as permission to implement it, or local edits as permission to publish or deploy.

Use a ledger only when its maintenance is authorised by the user or an established project workflow. Keep entries concise: `date | question | resolution | reaction`. Record actual decisions and outcomes; never invent a user reaction. Optional reactions are `🙂` (worth it), `😐` (fine), and `🥱` (avoid this shape unless significance changes). The ledger is not a backlog, project plan, or source of authority.
