# Daily Pop

**One question worth thinking about. One coherent improvement.**

Daily Pop is a coffee-time ritual in which an agent finds one question worth thinking about—and helps turn the answer into one coherent improvement.

Start a Pop, get coffee, and let your agent spend roughly five minutes exploring the project. It returns with one evidence-backed question, why it matters, and a possible delivery. You decide, reshape, defer, or authorise. Only then does it carry out the agreed action and verify it.

```text
You:   /pop
Agent: Is this acceptance criterion still describing the behaviour we want?
       Here's the evidence, and one possible change.
You:   The implementation is right. Correct the specification.
Agent: [makes the authorised correction and verifies it]
```

A good Pop wakes up your project intuition and leaves the project better than yesterday. If nothing meets the bar, the right answer is: **“No Pop worth interrupting you for today.”**

## Why this works

One question gives you something specific to think about at the start of the day. The agent has already gathered the evidence, so you can spend your attention on what it means for the project. A familiar place in your morning—while getting coffee, for example—makes room for that reflection before other work takes over.

You bring context the agent may be missing. Its question gives you a chance to explain an intentional exception, reconsider a decision, or agree to a change. You choose what happens next, including leaving things as they are. The agent can also return without a question when it finds nothing worth your attention; there is no daily quota to fill.

If you keep a Pop Ledger, your responses give future discovery passes something to learn from. A record of what you found useful or tedious helps the agent choose questions that suit you and the project, and avoid repeating settled discussions. That feedback is how the ritual can improve with use: the agent can consult it the next time it explores.

## Start with the core skill

Start with [daily-pop](skills/daily-pop/SKILL.md) in any repository. It finds one real, useful question in the work at hand and helps deliver one coherent improvement.

When your project has product, design, architecture, or operations sources worth connecting, move to [daily-pop-sdlc](skills/daily-pop-sdlc/SKILL.md). It extends the same ritual with questions across those sources: whether a ticket matches the implementation, for example, or an architecture decision still describes the system.

The SDLC version is an example of a complete [ASDLC.io](https://asdlc.io/)-style project skill. Its project lenses come first, followed by the inherited core contract. It uses the sources you have and does not require a particular vendor or a mature process. Each skill is independently installable; the SDLC package includes the core contract, so you only need one.

## Use it

This repository distributes plain Markdown agent skills. There is no application, service, or runtime to install.

1. Download a skill ZIP from the [v0.3.0 release](https://github.com/villetakanen/daily-pop/releases/tag/v0.3.0), or clone the repository with `git clone https://github.com/villetakanen/daily-pop.git`.
2. Choose `skills/daily-pop/` or `skills/daily-pop-sdlc/`. Install that entire folder in the skill location supported by your agent host, following that host’s instructions. Keep the folder name and `SKILL.md` intact.
3. Open the project you want to explore and invoke the chosen skill by name.

Each release ZIP contains one skill folder and its MIT license. When using a ZIP, install the extracted `daily-pop/` or `daily-pop-sdlc/` folder. To pin a cloned checkout to this release, run `git checkout v0.3.0` inside it.

You can also try it without installation: give your agent the chosen `SKILL.md` and ask it to use those instructions for a Daily Pop in your project.

> Use the daily-pop skill to run a Daily Pop in this repository. Spend roughly five minutes exploring, then bring me one evidence-backed question and a possible coherent delivery. Wait for my answer before changing anything.

`/pop` is the ritual’s intended shorthand. These files do not register a slash command automatically. If your host supports custom commands or aliases, map `/pop` to your chosen skill. Otherwise invoke the skill by name or use the prompt above. Choose one variant per invocation; running both does not mean two questions.

## What comes back

```md
## Daily Pop — [one clear question]

**What I found:** [brief, evidence-backed explanation]

**Why this is worth attention:** [why this improves project understanding or integrity]

**Possible delivery:** [one coherent change; what changes, what does not, and how to revert]

**Verification:** [how we will know the result is correct]

What should we do?
```

Answer naturally: “do it,” “leave it,” “that is intentional,” “make a follow-up,” or “tell me more.” An explanation or deferral is not permission to implement. A clarified decision can be the complete outcome.

The question must be real, interesting, singular, actionable, proportionate, and non-forced. Daily Pop optimises for **“Was this worth interrupting my morning for?”**, not severity scores or finding counts.

## What counts as one improvement?

One intention, one understandable outcome, one verification story, and one reversible change set. Scope is not measured in minutes, lines, or files. A repository-wide filename migration can qualify if it has one policy rationale, updates every reference, verifies cleanly, and can be reverted together.

Before delivery, the agent explains what will change, what will not change, how it will verify the result, and how to revert it. The five-minute guideline applies to discovery, not to authorised delivery.

## Add context only when it helps

The core skill needs no tickets, specifications, ADRs, design system, CI access, or vendor integration. Code, comments, tests, history, and incidental documentation are enough.

Either skill can read an optional project profile. Copy [the example profile](examples/project-profile.md) to `docs/DAILY_POP.md`, or tell the agent where your existing profile lives. Keep only sources and preferences you actually use. Sources mostly help the SDLC skill; preferences help both. The profile is a local convention, not required configuration.

An optional `docs/POP_LEDGER.md` can help avoid repetition and calibrate taste:

```text
2026-10-01 | Is retrying 401 correct? | Removed retry; added regression test | 🙂
```

Use `🙂` for worth it, `😐` for fine, and `🥱` for less of this unless its significance changes. Reactions come from you; the agent should not invent them. The ledger stays concise and is never a backlog or source of authority. Explicit intent and repository evidence outrank it. Creating or updating it is part of an agreed workflow, not an automatic side effect of discovery. If your profile or ledger already lives elsewhere, tell the agent its location; no move is required.

See [the illustrative interaction](examples/transcripts/minimal-repository.md) for a complete Pop in a tiny repository. Some evaluation fixtures are intentionally imperfect; that context stays outside the projects the agent explores. The [manual checks](evals/README.md) cover both a useful Pop and a day with no question.

## What Daily Pop is not

Daily planning, a status report, an AI-generated backlog, a lint report, or manufactured trivia. It does not replace planning, triage, incident management, or code review; rank the project’s most important work; act without authorisation; or turn a morning question into a sprawling redesign.

## Contributing

Changes should improve the quality of the question or the clarity of delivery while keeping both skills useful in small repositories. The SDLC skill must remain a superset of the core contract. Its inherited sections must match the core skill’s Discover, Ask, and Respond and deliver sections, including ledger rules; only heading levels differ. Update both copies when the core contract changes.

## License

[MIT](LICENSE). Include the license when redistributing either skill.
