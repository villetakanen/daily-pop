# A Pop in a tiny repository

This is an illustrative repository fixture, not a finding about Daily Pop itself. It needs no ticket tracker, ADRs, CI, or project profile.

## Project promise

The [greeting function](greeting.py) trims surrounding whitespace from a name and says hello. If the name is empty after trimming, it greets “friend”.

Run it from this directory with `python3 greeting.py`. It currently prints `Hello, !` for a whitespace-only name.

## Example interaction

**User:** /pop

### Daily Pop — Should a whitespace-only name greet “friend”?

**What I found:** The project promise above says an empty name after trimming should greet “friend”. In `greeting.py`, `greet` checks whether the original name is empty before trimming it, so three spaces produce `Hello, !`.

**Why this is worth attention:** The documented fallback and the behaviour disagree. Confirming the intended behaviour resolves a small but visible edge case.

**Possible delivery:** Trim before applying the fallback, and add a regression check. Ordinary named greetings stay unchanged. Keep the fix and check in one change set that can be reverted together.

**Verification:** Check empty, whitespace-only, padded, and ordinary names against the project promise.

What should we do?

**User:** Do it. Blank names should greet friend.

**Agent:** [applies the agreed fix, checks those four cases, and reports the outcome and rollback]

The fixture deliberately retains the discrepancy so you can try the skill against it. The transcript is illustrative; it is not a claim that a delivery has been executed.
