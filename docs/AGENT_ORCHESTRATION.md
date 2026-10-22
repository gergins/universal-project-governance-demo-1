# Universal Agent Orchestration Architecture

Version 1.4.0. Provider-neutral, SDK-optional design specification; NOT an installed/executable orchestration service.

## Objective and trust boundaries
Coordinate bounded tasks across real tools and specialist agents while retaining explicit human ownership. A model may propose plans or tool calls; authenticated application code enforces permissions, budgets, approvals, execution and result verification. A registry entry does not prove an adapter is configured.

## Runtime choices (choose per task)
- Deterministic pipeline/state machine for predictable tasks; default for irreversible or regulated execution.
- Responses API + application-owned loop, when custom dispatch and persistence are necessary.
- OpenAI Agents SDK for managed in-process loops, handoffs, sessions, guardrails, tracing and tools.
- OpenAI Agents API for service-managed workflows when appropriate and available.
- Hybrid: LLM proposes bounded plans; deterministic orchestrator validates dependencies, authorization, and transitions.

The framework requires capability parity at the CONTRACT level, not identical SDK internals. Equivalent resilience, observability and safety need independent implementation and testing.

## Components and accountabilities
1. **Intake/identity/context:** authenticate requester, determine environment, source revision, user intent and applicable project policies.
2. **Planner:** produce typed task graph with node IDs, dependencies, outcomes, constraints, non-goals, risk and bounded depth. Planning is untrusted until checked.
3. **Capability discovery:** lookup name, schema, provider adapter, permissions, actual availability, preconditions, side effects, idempotency and independent verification procedure.
4. **Policy/approval engine:** verify identity, role, resource scope and environment. Require explicit, logged approval for high-risk actions; deny-by-default; independently enforce at the connector/gateway.
5. **Coordinator/scheduler:** deterministic task-state machine, dependency resolution, bounded concurrency, deadlines and rate limits, task leases and deduplication.
6. **Specialists:** optional research, design, engineering, QA, security, release agents. Pass bounded task contracts; specialist assertions are not verification.
7. **Tool gateway/adapters:** schema validation, scoped credentials, execution isolation, deterministic error types, result receipts; never shell/browser/cloud access by implication.
8. **Durable state:** append-only event ledger, job/task state, checkpoints, external operation IDs, causal parent ID, and resume token. Store secrets outside logs.
9. **Verifier:** compare postconditions against authoritative target state via independent read paths where possible; distinguish action accepted, executed, verified and approved.
10. **Observability/evals:** trace IDs, model/tool versions, latency/cost budgets, redacted audit events, offline scenarios, integration and red-team checks.
11. **Recovery:** detect uncertain outcomes; reconcile before retries; compensate where possible; escalate when state cannot be proven. Rollback is not guaranteed.
12. **Human interaction:** show plan, risks, approvals, progress, interruptions, failures and evidence-based final result; include accessible and feeling-oriented experience.

## Task state machine
`DRAFT -> VALIDATED -> READY -> RUNNING -> VERIFYING -> SUCCEEDED`
Alternative states: `WAITING_APPROVAL`, `BLOCKED`, `FAILED`, `CANCELLED`, `UNKNOWN_OUTCOME`, `COMPENSATING`.
Forbidden: reporting SUCCEEDED without required verified postconditions; continuing after denied approval; auto-retrying an unknown side-effect outcome without reconciliation.

## Runtime execution loop
1. Intake: verify project+environment and caller identity.
2. Fetch current facts, available capabilities and authorization; create bounded plan.
3. Reject cycles, missing adapters, unchecked scope, excessive cost/concurrency, unsafe task graph.
4. For each ready node: check policy; pause for approval if required; execute once with idempotency token when supported.
5. Record tool receipt; verify external outcome independently; advance state only after verified postconditions.
6. On failure: classify (unavailable, denied, invalid input, transient, permanent, uncertain, partial); reconcile before retry or compensate.
7. Stop at budget/turn/time limits; hand off durable resume state if incomplete.
8. Produce evidence-linked summary, executed and skipped operations, blockers and next safe action.

## Multi-agent delegation
Prefer **manager-as-owner with specialists as tools** for bounded tasks and a single accountable report. Use **handoffs** only when ownership of a conversation/work stream genuinely transfers. Apply the same permissions to each delegated agent; do not inherit elevated access implicitly. Restrict recursion, concurrency and tool grants.

## Capability contract schema (illustrative)
`id`, `version`, `provider`, `adapter`, `input_schema`, `output_schema`, `preconditions`, `required_scopes`, `risk_level`, `side_effects`, `approval_policy`, `timeout_seconds`, `retry_policy`, `idempotency_scope`, `verify`, `compensation`, `audit_redaction`, `owner`.

## Safe progression and proof
`PLAN_CREATED` does not mean `TASK_STARTED`; `TOOL_ACCEPTED` does not mean `EFFECT_CONFIRMED`; `CHECKS_PASSED` does not mean `RELEASE_APPROVED`; `DEPLOY_TRIGGERED` does not mean `SERVICE_HEALTHY`.

## Starting implementation slice
One read-only capability -> verified tool receipt -> durable trace -> denied unauthorized request -> interrupted/resumed run -> idempotent mock write -> uncertain-outcome reconciliation -> independent provider verification -> approval-gated real write.

## OpenAI primary references (accessed 2026-10-22)
- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/sdk
- https://developers.openai.com/api/docs/guides/agents/running-agents
- https://developers.openai.com/api/docs/guides/agents/orchestration
- https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- https://developers.openai.com/api/docs/guides/agents/integrations-observability