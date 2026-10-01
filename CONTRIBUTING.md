# Contributing to Daily Pop

Bring a concrete example of a question the skill handled poorly, a useful interaction it missed, or distribution instructions that were unclear. Explain the observed behaviour and the improvement you expect. Avoid adding process for hypothetical edge cases.

The two skills are independently distributable. Keep their shared interaction contract aligned when changing discovery, quality criteria, authorisation, delivery, or ledger behaviour. Keep SDLC lenses optional and out of the core skill’s requirements.

Before proposing a change:

- Check each `SKILL.md` has valid YAML frontmatter with its matching folder name and a focused description.
- Check relative Markdown links from their containing files and follow installation instructions from a fresh download.
- Review both skills against a tiny repository, missing structured sources, an intentional exception, and a day with no worthwhile question.
- Confirm the agent presents one question, evidence, scope, verification, and rollback before acting; a deferral must not trigger changes.
- Confirm one broad but coherent delivery remains eligible, and no user reaction is invented for the ledger.

For meaningful workflow changes, include an example interaction showing the difference. Separate actual agent-run evidence from illustrative transcripts. No build step or application dependency is required for this Markdown distribution.
