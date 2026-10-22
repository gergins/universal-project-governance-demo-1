# Master Framework — pre-publication review and design optimization

Status: **DRAFT / NOT PUBLISHED**. A check of design against published patterns is not OpenAI certification. The current validator tests metadata/structure, not runtime behavior.

## Architecture that must remain stable
1. **WHAT:** project-specific discovery lenses and selected capabilities.
2. **HOW:** project-agnostic governance, operating skills, execution contracts, deployment controls.
3. **Accountable coordinator:** logical outcome owner, optionally implemented as ordinary code or a model-driven manager.
4. **Bounded specialists:** optional, narrowly-scoped delegates; delegation never increases authority.
5. **Independent control plane:** real server-side policy evaluation and validation at each side-effecting adapter, not just prompts or model guardrails.
6. **Durability by need:** enable durable engine when restart, long wait, approvals, retries, or partial effects warrant it.

## Decisions and design improvements
| Observation | Refinement | Rationale |
|---|---|---|
| Too many reference documents can obscure rules | Keep concise AGENTS.md; progressive disclosure by linked topic | Avoid instruction overload |
| 'SDK parity' could imply SDK installed | Define behavioral contracts independent of vendor | Distinguish specified vs connected vs verified |
| Existing eval scenarios are shallow | Add failure taxonomy and future evaluation seeds | Capture likely omissions before release |
| Retries without idempotency are unsafe | Require unknown-outcome reconciliation before repeated writes | Prevent double side effects |
| Approval can be confused with broad permission | Bind approvals to resource, exact args digest, actor, expiry | Least privilege and revalidation |
| Context summaries can stale or poison state | Separate memory, authoritative ledger and signed decisions | Evidence over narrative |
| Specialists may contradict or loop | Set ownership/hop/budget constraints and arbitration | Bounded coordination |
| Validation could be misread as readiness | Distinguish structural validator, simulation tests and live acceptance | Honest evidence labeling |
| Generic template can become bloated | Failure scenarios selected by risk; no required agent per domain | Project-independence |
| Cloud provider names can imply available access | Provider capability probes and separate credentials | No invented tool authority |

## OpenAI documented vs proposed
**Documented SDK surfaces:** agent loops, turn-limit exceptions, malformed model output, tool-name lookup behavior, tool execution configuration, session/history constraints, approval interruption/resumption, scoped guardrails and tracing (sources in OPENAI_SOURCE_NOTES.md).

**Our engineering proposals:** accountable coordinator as permanent logical owner, deterministic gateway, CAS state transitions, approval binding to argument digest, taxonomy, idempotency/compensation rules, optional durable workflow engine. They are consistent patterns but not assertions that OpenAI requires this exact architecture.

## Gate before GitHub publication
- Confirm master-template naming, licensing, no secrets, reference versions, and project-initialization flow.
- Review static validation plus a distinct **manual** test-plan acceptance; no false claim of test execution.
- Explicitly decide whether the master GitHub repository should initially be private.
- Create project-specific CI/release policies only after initialization.
- Record actual commit SHA once published; template versions do not automatically migrate.
- Do not enable production write adapters or publish this framework without an authorized repository action.

## Residual risk
Documentation alone cannot guarantee zero hallucinations, permissions enforcement, operational continuity, a secure application or production readiness. Runtime implementation, tests, code review, human validation and observed outcomes are necessary.