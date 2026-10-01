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

## Choose your skill

| Skill | Use it when | Promise |
| --- | --- | --- |
| [daily-pop](skills/daily-pop/SKILL.md) | You have a repository or work context, however small or messy. | Find one real, useful question, then help deliver one coherent improvement. |
| [daily-pop-sdlc](skills/daily-pop-sdlc/SKILL.md) | You also have product, design, engineering, or operations sources worth connecting. | Find one small, resolvable mismatch or improvement across those sources. |

These are sibling skills with the same interaction contract. The SDLC version adds project lenses; it does not require a mature process, specific vendor, or access to every source. Either folder can be distributed independently.

## Use it

This repository distributes plain Markdown agent skills. There is no application, service, or runtime to install.

1. Download a skill ZIP from the [v0.2.0 release](https://github.com/villetakanen/daily-pop/releases/tag/v0.2.0), or clone the repository with `git clone https://github.com/villetakanen/daily-pop.git`.
2. Choose `skills/daily-pop/` or `skills/daily-pop-sdlc/`. Install that entire folder in the skill location supported by your agent host, following that host’s instructions. Keep the folder name and `SKILL.md` intact.
3. Open the project you want to explore and invoke the chosen skill by name.

Each release ZIP contains one skill folder and its MIT license. When using a ZIP, install the extracted `daily-pop/` or `daily-pop-sdlc/` folder. To pin a cloned checkout to this release, run `git checkout v0.2.0` inside it.

You can also try it without installation: give your agent the chosen `SKILL.md` and ask it to use those instructions for a Daily Pop in your project.

> Use the daily-pop skill to run a Daily Pop in this repository. Spend roughly five minutes exploring, then bring me one evidence-backed question and a possible coherent delivery. Wait for my answer before changing anything.

`/pop` is the ritual’s intended shorthand. These files do not register a slash command automatically. If your host supports custom commands or aliases, map `/pop` to your chosen skill. Otherwise invoke the skill by name or use the prompt above. Choose one variant per invocation; running both does not mean two questions.

## What comes back

```md
## Daily Pop — [one clear question]

**What I found:** [brief explanation with evidence references]

**Why this is worth attention:** [why it improves understanding or integrity]

**Possible delivery:** [what changes, what stays unchanged, and how to revert]

**Verification:** [how we will know the result is correct]

What should we do?
```

Answer naturally: “do it,” “close it,” “leave it,” “that is intentional,” “make a follow-up,” or “tell me more.” An explanation or deferral is not permission to implement. A clarified decision can be the complete outcome.

The question must be real, interesting, singular, actionable, proportionate, and non-forced. Daily Pop optimises for **“Was this worth interrupting my morning for?”**, not severity scores or finding counts.

## What counts as one improvement?

One intention, one understandable outcome, one verification story, and one reversible change set. Scope is not measured in minutes, lines, or files. A repository-wide filename migration can qualify if it has one policy rationale, updates every reference, verifies cleanly, and can be reverted together.

Before delivery, the agent explains what will change, what will not change, how it will verify the result, and how to revert it. The five-minute guideline applies to discovery, not to authorised delivery.

## Add context only when it helps

The core skill needs no tickets, specifications, ADRs, design system, CI access, or vendor integration. Code, comments, tests, history, and incidental documentation are enough.

For the SDLC skill, optionally copy [the example profile](examples/project-profile.md) to `DAILY_POP.md` in your project root, or tell the agent where your existing profile lives. Retain only sources and preferences you actually have. The profile is a local convention, not required configuration.

An optional `POP_LEDGER.md` can help avoid repetition and calibrate taste:

```text
2026-10-01 | Is retrying 401 correct? | Removed retry; added regression test | 🙂
```

Use `🙂` for worth it, `😐` for fine, and `🥱` for less of this unless its significance changes. Reactions come from you; the agent should not invent them. The ledger stays concise and is never a backlog or source of authority. Explicit intent and repository evidence outrank it. Creating or updating it is part of an agreed workflow, not an automatic side effect of discovery.

See [the minimal repository example](examples/minimal-repository/README.md) for a complete illustrative Pop without formal engineering machinery.

## What Daily Pop is not

Daily planning, a status report, an AI-generated backlog, a lint report, or manufactured trivia. It does not replace planning, triage, incident management, or code review; rank the project’s most important work; act without authorisation; or turn a morning question into a sprawling redesign.

## Contributing

Changes should improve the quality of the question or the clarity of delivery while keeping both skills compatible and useful in small repositories.

## License

[MIT](LICENSE). Include the license when redistributing either skill.
