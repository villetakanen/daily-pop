# Manual skill checks

These cases check whether Daily Pop finds a useful question when evidence supports one and stays quiet when it does not. They are small regression checks, not a general measure of skill quality. One successful run does not guarantee later runs will match.

- [Minimal repository](minimal-repository.md): a mismatch between a promise and behaviour.
- [Nothing wrong](nothing-wrong.md): a consistent project with no intended Pop.

## Run a case

1. Copy only the case’s fixture contents into a new temporary directory outside this repository. Record a file inventory and content hashes so you can detect edits, additions, and deletions afterwards.
2. Start a fresh agent session with that directory as the project. Load the `daily-pop` skill separately, using the version you want to check. Do not provide this repository’s README, case descriptions, transcripts, expected outcomes, prior conversations, or results. Use neutral temporary directory names so the case name does not suggest an answer.
3. Invoke `/pop`. If the host has no such alias, use: “Use the supplied daily-pop skill to run a Daily Pop in this project.” This is the same request; do not add hints about the fixture.
4. Save the response and compare the file inventory and hashes. Stop before authorising a delivery. Read the case’s expected outcome only when assessing the run.
5. Record the date, skill revision, agent/model if known, prompt, response, file comparison, and assessment under the case’s Manual runs section. Link longer responses from `results/`. Say when a case was not run or did not meet expectations; do not fill in a model answer.

The agent may inspect the fixture and run its existing code or tests without changing files. Keep evaluation setup and output outside its project. Do not give an evaluator both fixtures in one session.

There is no automated agent runner. The greeting checks in the clean fixture establish its behaviour; they do not evaluate the skill.
