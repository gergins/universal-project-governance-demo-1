# Pre-publication design review — 2.3.0

Decision: architecture FROZEN at WHAT / HOW, single accountable coordinator, bounded specialists, independent deterministic control plane, optional durability. No new mandatory agents or services.

## Findings and disposition
- Master template setup: `template.status=master` deliberately permits placeholders. New initialized project must set its identity and source framework commit. KEEP.
- `AGENTS.md` remains compact and directs readers to focused references. KEEP. Avoid mandatory load of all reference documents.
- Tool authorization, approval and output verification are specified but not enforced by documents. KEEP the distinction: design vs operational system.
- Structural validator checks required files, manifest and skill headers. It does not audit security, source link freshness, real-world accessibility, or deployments. DO NOT claim otherwise.
- Framework v2.2.1 contains overlapping historical reference documents. KEEP for audit traceability, but make `README.md`, `AGENTS.md`, `WHAT_HOW_MODEL.md`, `COORDINATOR_EXECUTION_CONTRACT.md` and `EXECUTABLE_READINESS_GATE.md` authoritative entry points. Archive/merge duplicative material after a reference-link inventory, not by blind deletion.
- GitHub workflow currently uses `actions/checkout@v4` with a pending pinning note. Before requiring CI as a security gate, select and independently verify a specific reviewed SHA, then test the workflow on the universal repository. NOT DONE.
- Versioned source docs mention OpenAI specifics; treat these as documented reference patterns, not certification or endorsement.
- 2.3.0 adds a tiny stdlib-only executable **proof**, not a complete production orchestration runtime or Agents SDK parity.

## Proof boundaries
One coordinator, one specialist, one read-only allowlisted file tool, independent policy check, and independent postcondition predicate. Denied write/out-of-scope operations, wrong principals, missing files, unverifiable results and unknown adapter operations are covered by tests. No cloud integration, production data, network effects, approvals UI, durability, security isolation, real model inference, distributed concurrency, or external audit.

## Publication gate
Do not publish or merge until user authorizes publication, the target GitHub repository is verified and suitable, the framework source is checked for secrets and broken internal references, CI workflow security is independently reviewed, and new-project initialization instructions are verified. Runtime tests on the proof do not imply passing provider integration or certification.