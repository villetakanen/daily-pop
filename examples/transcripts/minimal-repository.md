# A Pop in a tiny repository

This illustrative interaction shows a Pop in the [minimal repository](../minimal-repository/). It is not an agent-run result.

**User:** /pop

## Daily Pop — Should a whitespace-only name greet “friend”?

**What I found:** The README says an empty name after trimming should greet “friend”. In `greeting.py`, `greet` checks whether the original name is empty before trimming it, so three spaces produce `Hello, !`.

**Why this is worth attention:** The documented fallback and the behaviour disagree. Confirming the intended behaviour resolves a small but visible edge case.

**Possible delivery:** If the README describes the intended behaviour, trim before applying the fallback and add a regression check. If the current behaviour is intentional, correct the README and add a check that records it. Either choice leaves ordinary named greetings unchanged and can be reverted as one change set.

**Verification:** Check empty, whitespace-only, padded, and ordinary names against the agreed behaviour. Confirm the README describes those outcomes.

What should we do?

**User:** Do it. Blank names should greet friend.

**Agent:** [applies the agreed fix, checks those four cases, and reports the outcome and rollback]
