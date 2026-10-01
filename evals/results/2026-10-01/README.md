# Manual runs — 2026-10-01

These are observed agent responses from the 0.3.0 work, not illustrative transcripts. Each run used a fresh Codex agent with no conversation history, one isolated fixture, and the core skill supplied separately. The runner did not expose a model version. No agent received the expected outcomes or this repository’s documentation.

The [prompts](prompts.txt) record the request and paths. Filesystem links in the saved responses refer to the temporary projects used during these runs.

## Results

| Run | Fixture | Skill candidate | Result | Saved final response |
| --- | --- | --- | --- | --- |
| a | Minimal repository | First | Failed: found the mismatch but offered only a code correction. | [Response](minimal-repository-first.txt) |
| b | Nothing wrong | First | Passed: exact No-Pop sentence. | [Response](nothing-wrong-first.txt) |
| c | Minimal repository | Revised | Passed: one question, evidence, code and documentation alternatives, verification, and rollback. | [Response](minimal-repository-final.txt) |
| d | Nothing wrong | Revised | Passed: exact No-Pop sentence. | [Response](nothing-wrong-final.txt) |

All four projects kept the same files and contents, with no generated directories. The [file checks](file-checks.json) record their before-and-after SHA-256 hashes and the skill hash used for each run.

## Change between candidates

The first candidate said to describe a delivery for each reading when the question is a decision between two readings. Run a did not apply that instruction to the documentation mismatch.

The revised candidate adds: “For a mismatch between documentation and behaviour, ask which should change and describe both alternatives, unless an explicit decision in the available context rules one out.” Both skills contain this clarification. The fixtures and evaluation prompts stayed the same; runs c and d used new agents and new copies of the projects.

- First core skill SHA-256: `07a809ec3515e06b7d11f5056c5f7427f6e53ac87063731a6a527dc924eb037f`
- Revised core skill SHA-256: `10644513f9b1e6f593422739d848d95a0ecc79647f3c39f78a8c942a4d53cfd9`

The revised candidate is the core skill packaged in 0.3.0. These two passing cases provide limited regression evidence; they do not establish how often the skill will succeed on other projects.
