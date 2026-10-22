# Implementation Assurance and Certification Readiness

Version 2.1 | Design-only assurance pathway. No OpenAI endorsement, certified implementation, audit, or runtime performance claim.

## Three claims that must not be conflated
1. **OpenAI guidance aligned**: traceable mapping to dated official documentation. This is an engineering claim, not official validation.
2. **Independently verified implementation**: identifiable running version and environment with reproducible tests, evaluations and independent reviewers. Scoped to evidence, not universal correctness.
3. **External certification or endorsement**: only valid if a competent issuer has a documented assessment program, defined scope, and issued verifiable written attestation. No general OpenAI Agents SDK application certification has been confirmed as of 2026-10-22. Never use OpenAI Certified or OpenAI endorsed branding without authorization. OpenAI educational learner credentials and OpenAI's own SOC/ISO audits do not certify this template or applications created from it.

## Assurance lifecycle
DESIGN_ONLY -> IMPLEMENTED -> DETERMINISTIC_TESTED -> INTEGRATION_VERIFIED -> ADVERSARIAL_REVIEWED -> STAGING_EVALUATED -> HUMAN_RELEASE_APPROVED -> OPERATED_AND_MONITORED -> INDEPENDENTLY_ASSESSED -> CERTIFICATION_RECORDED (only where applicable).
Transitions are claims requiring dated evidence, reviewer, environment and immutable commit/build ID. A blocked gate cannot be silently skipped.

## Evidence checklist, only where relevant to a project
- **Scope and provenance**: precise product, code/version/commit, services, regions and environments; decision records; ownership and data flows.
- **Requirements to evidence**: capability ID -> acceptance criteria -> test/eval -> observed outcome -> reviewer; include feeling-oriented and accessibility acceptance.
- **Coordinator correctness**: one accountable owner; bounded specialists; delegation/non-escalation; deterministic policy and approval; denial and unknown-outcome paths.
- **Tool boundary**: real adapters, scoped identity and secrets, schema validation, audit, timeout/cancel, safe retry, idempotency and reconciliation; independently verified external effects.
- **Model and agent quality**: dataset design, representative user journeys, scripted deterministic tests, live model evals, prompt-injection/red-team tests, hallucinated-success detection, regression baselines, thresholds and drift monitoring.
- **Privacy/security**: threat model, secret/dependency/code scanning, human review, retention, incident handling, pentest appropriate to risk, remediation evidence and tenant isolation.
- **Resilience**: crash/replay, concurrent access, revoked approval, degraded provider, rate limits, rollback, backup/restore when applicable.
- **Human experience**: usable and accessible approvals/errors, safe fallback, targeted research and independent user feedback.
- **Supply chain**: reproducible builds, dependency pinning, artifact hashes, provenance/SBOM as appropriate, protected releases and change controls.
- **Operations**: actual staging/prod verification, observability, alert/incident ownership, change management, monitoring over time and residual risk register.
- **External auditor**: select the applicable standard and assessor for the product, jurisdiction, risk and data scope. Record issued attestation identifier, date, scope, exceptions and expiration. Do not invent one.

## OpenAI SDK boundary-specific testing
Use `ScriptedModel` and `assert_complete()` for deterministic SDK run loops, tools, handoffs and errors; scripted sandbox/realtime components for their normalized boundaries. These are not substitutes for model-quality evaluations, provider HTTP tests, real sandbox security, live credentials/permissions, or actual external state changes.

Input guardrails may run in parallel by default, so side effects can begin before a failure is detected; choose blocking input checks for risky workflows. Tool guardrails do not uniformly cover hosted tools, built-in shell/computer tools, or handoffs. Apply independent application authorization at every real action boundary, before side effects.

## Minimum assurance packet (versioned per project)
`scope.md`, `requirements-traceability.csv`, `architecture-and-threat-model.md`, `test-and-eval-results.md`, `security-review.md`, `human-experience-results.md`, `release-evidence.md`, `residual-risks.md`, `reviewer-signoffs.md`, `certifications.md` (empty/unverified until issued). Generate only for applicable selected work; do not litter master template with blank evidence claims.

## Source references (checked 2026-10-22)
- https://openai.github.io/openai-agents-python/testing/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://developers.openai.com/api/docs/guides/agents/sdk
- https://openai.com/security-and-privacy/
- https://help.openai.com/en/articles/20001151-openai-certified-app

No general third-party OpenAI certification or endorsement for a custom Agents SDK implementation was verified. Verify applicable program availability directly before seeking certification.

## SDK-independent assurance detail
See `SDK_PARITY_ASSURANCE.md` for test boundaries, evidence matrix, recovery edge cases and required negative test scenarios. This is not an OpenAI certification.