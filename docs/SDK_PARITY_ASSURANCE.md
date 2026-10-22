# SDK-Inspired, SDK-Independent Assurance Contract

Version 2.2 — design specification. No live tests, endorsement, certification or production assurance has been obtained.

## Purpose and scope
Adopt the OpenAI Agents SDK’s useful testing and observability boundaries as a **reference contract**, not an SDK dependency. Implement equivalent behavior in other runtimes only where the selected product actually requires it. Preserve one accountable coordinator, bounded specialists, independently enforceable control plane, and optional durability.

## Evidence matrix
| Boundary | What must be assured | Proof required | Cannot conclude from it |
|---|---|---|---|
| Model / agent loop | bounded turns, valid tool choices, fallback, malformed-output and exception handling | scripted agent-run tests and call assertions | live model reliability |
| Delegation / handoff | scoped authority, control ownership, specialist budgets and handback | scripted delegation and denied handoff tests | server-side authorization |
| Tool contracts | input/output schemas, rejected invalid arguments, execution errors | function-tool contract tests | cloud-provider behavior |
| Control plane | authenticated principal, resource-specific deny/allow, approval expiry and parameter binding | real policy-engine tests with negative cases | that vendor credentials work |
| Interrupt / resume | serialized pending approval, exact action, no double execution | pause/restart/reject/revoke test | universal crash safety |
| Session/history | concurrency ownership, exact checkpoint recovery, corruption and stale state | session and persistence fault injection | a live provider result |
| External adapters | identity, TLS/network failures, throttling, side effects, idempotency, reconciliation | integration tests against named provider/environment | production approval |
| Sandbox / computer | isolation, resource limits, filesystem and network policies | real provider sandbox and adversarial tests | protection from scripted mock |
| Tracing and logs | task/trace/tool correlation, redaction, retention and audit provenance | inspected traces and privacy tests | certified security posture |
| Evaluation | task success, task failure, hallucinated completion, prompt injection, human experience | frozen datasets, graders, baseline and repeatable run IDs | performance on all future cases |
| Release and operations | build identity, environment, health, rollback, incident ownership | signed review and live staging/production checks | endorsement by OpenAI |

## SDK details extracted and translated
- SDK `ScriptedModel` exercises the normalized runner loop, handoffs, tools, guardrails, retries, streaming and sessions without real model or provider requests; require comparable deterministic fixtures for whichever runtime is selected. Tests must assert inputs/calls and exhaust planned steps (`assert_complete` in SDK tests).
- SDK scripted sandbox, Realtime and Voice components validate their **normalized** interactions; they do not emulate provider wire protocols, real sandbox isolation, media transport or live model quality. Only select those test surfaces when the product uses those capabilities.
- SDK `RunResult` and `RunState` expose outputs, items, agents and resumable state; our framework requires operation receipts, coordinator state and independently observed postconditions, distinct from conversational context.
- SDK documents specific session-write recovery behavior and an **unrecoverable terminal-persistence boundary**. A custom runtime must design explicit ambiguity outcomes and avoid blindly replaying a completed action or terminal lifecycle hooks.
- SDK runner exposes max-turn limits, structured errors, hooks and streaming cancellation. Set limits, budgets, cancellation semantics and exceptions in the chosen runtime; never presume that a cancelled request undoes external effects.
- SDK tracing records model, tool, handoff and guardrail spans. Correlate to external operation IDs and redact sensitive content; tracing alone is neither an authorization control nor verification of the provider effect.
- SDK human approval/pause/resume is a workflow primitive; our application must enforce identity, scope, exact-argument approval, expiry, revocation and renewed authorization at the actual tool boundary.
- SDK integrates with durable engines (including Temporal, Dapr and Restate); make an engine optional and select it for actual long-running/restart requirements, not by default.

## Assurance ladder — independently testable claims
SPECIFIED → IMPLEMENTED → SCRIPTED_VERIFIED → POLICY_VERIFIED → PROVIDER_INTEGRATION_VERIFIED → ADVERSARIAL_VERIFIED → STAGING_VERIFIED → HUMAN_APPROVED → OPERATIONAL → INDEPENDENTLY_ASSESSED.
Every transition requires `target`, `version/commit`, `environment`, `test_or_eval_id`, `result`, `timestamp`, `reviewer`, and immutable evidence reference. No automatic promotion from docs or a model self-report. Certification requires an actual external scheme and issuer evidence; it is not a default stage.

## Assurance fixture manifest (per selected project, not master template)
- Runtime type and version; selected capability contracts and risk classification.
- Cases: success, invalid input, denied permission, missing tool, max-turns, malformed output, tool timeout, prompt injection, revoked approval, provider outage, ambiguous success, duplicate request, concurrent write, checkpoint corruption, restart, cancellation, independent verification failure and accessible recovery.
- For each case: preconditions, test boundary (scripted vs live), expected decision and state, observable evidence, redaction requirements and failure owner.
- Cover *all critical capability-specific side effects* before an external production release; document deferrals and reviewer acceptance explicitly.

## OpenAI source references, checked October 22 2026
- https://openai.github.io/openai-agents-python/testing/
- https://openai.github.io/openai-agents-python/results/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/tracing/
- https://developers.openai.com/api/docs/guides/agents/sdk

This document is a reusable design standard and is **not proof** of conformity with OpenAI or of a deployed runtime.