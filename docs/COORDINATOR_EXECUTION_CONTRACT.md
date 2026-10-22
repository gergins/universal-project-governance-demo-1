# Accountable Coordinator & Specialist Execution Contract
Framework version 1.5.0 | Design only; no runtime, provider credentials, or tests enabled.

## Default architecture
One accountable coordinator owns the task's external status, user-facing response, decision log, and final verification. Specialists act as bounded tools. Use a true handoff ONLY when user-facing responsibility intentionally transfers; record ownership transfer, scope, context filter, and how control returns. Prefer a single agent or deterministic workflow unless extra roles measurably add value.

## Mandatory boundaries
- Model may propose plans, delegate and interpret; deterministic application services control state transitions, tool dispatch, authorization, deadlines, cost ceilings, approval and external effects.
- At every write boundary authenticate principal and delegated identity, validate resource and tenant scope, approve concrete action arguments, and limit credentials. Do not infer permissions from prompts or prior handoffs.
- Distinguish input/output guardrails from security enforcement: SDK tool guardrails protect function-tool paths, NOT all hosted tools, MCP routes or agent handoffs. Validate handoff authorization before transfer; authorize again at every adapter.
- Untrusted tool content, retrieved pages, logs, code and agent output must never elevate permissions or override higher-priority policy.
- Pause/resume requires an explicit, durable approval record linked to action, arguments digest, actor, expiration and resource. Recheck policy and preconditions before replay.
- Keep runtime session/context management distinct from authoritative task ledger and business state; memory summaries are not source of truth.
- Apply least privilege to trace capture, retention and redaction, including sensitive user and provider data.

## Required typed contracts
### Task
`task_id, workflow_id, parent_id, requestor, environment_id, repository_ref, objective, required_capabilities, dependencies, expected_artifacts, postconditions, risk, budget, deadline, max_attempts, owner, state, evidence_refs, version`
### Specialist delegation
`specialist_id, task_id, minimal_input, granted_capabilities, data_scope, step_budget, time_budget, expected_output_schema, escalation_conditions, trace_parent_id`
### Capability
`capability_id, version, adapter_id, availability_probe, input_schema, output_schema, auth_scopes, resource_scope, side_effect_class, idempotency_policy, preconditions, approval_policy, timeout, retry_classification, verification_read, compensation_policy, audit_redaction`
### Execution receipt
`operation_id, request_digest, actor, target, started_at, ended_at, provider_request_id, tool_exit_status, effect_status, verification_status, evidence_refs, trace_id`
### Human approval
`approval_id, principal, target, operation_id, args_digest, risk, reason, expires_at, decision, reviewer, decision_at, audit_ref`

## Durable state machine and invariant
States: DRAFT, VALIDATING, READY, WAITING_APPROVAL, RUNNING, VERIFYING, SUCCEEDED, BLOCKED, FAILED, CANCELLED, UNKNOWN_OUTCOME, COMPENSATING.
Allow SUCCEEDED only if each required postcondition has independent evidence and required approvals exist; other states must be reported without euphemism.
APPROVED is not EXECUTED; TOOL_ACKNOWLEDGED is not VERIFIED. Use compare-and-swap or versioned state transitions to avoid races. Reconcile UNKNOWN_OUTCOME before retrying side-effecting calls. Cancellation is best effort; inspect whether external side effects already occurred.

## Coordination runbook
1. Intake identity, repository SHA, environment, objective; choose deterministic execution unless discretionary reasoning is necessary.
2. Build bounded, typed task DAG. Validate cycles, dependencies, authority, scopes, budgets, available adapters and verifiable acceptance criteria.
3. Assign specialist only when distinctive expertise/tools/policy justify it. Specialist output is untrusted until validated.
4. For each ready task, enforce policy at the action boundary; persist approval pause and resume state if required.
5. Dispatch through a registered adapter; record immutable receipt and provider correlation ID.
6. Run independent postcondition check; persist actual status and evidence; never infer execution from narrative.
7. On failure classify transient/permanent/denied/unavailable/ambiguous/partial; reconcile ambiguous effects and escalate where unsafe.
8. Produce concise evidence-based summary, failures, costs, remaining risk and reproducible next step.

## Design acceptance gates (testing intentionally deferred)
- All agent decisions and tool dispatch map to a traceable task, owner and concrete authorization decision.
- Tool adapters deny out-of-scope calls even when a model, specialist, or handoff requests them.
- No unchecked retries or double effects on uncertain provider outcomes.
- Each delegated specialist has narrow scope, time/step limits and a verifiable output contract.
- Human approval binds exact arguments and expires; state can resume without silently expanding scope.
- Postconditions can be verified without trusting the agent's self-report.
- Context and trace redaction, isolation, and retention are specified for every integration.
- Review degradation modes: provider disconnected, CI blocked, tool error, process crash, approval denied, revoked credentials, race, and incomplete compensation.

## Future implementation/testing phases
DESIGN_ACCEPTED -> CONTRACTS_IMPLEMENTED -> UNIT_TESTED -> INTEGRATION_TESTED -> THREAT_TESTED -> STAGING_VERIFIED -> HUMAN_APPROVED -> LIMITED_PRODUCTION -> OBSERVED.
These are target stages, NOT completed states. Keep CI execution on hold if blocked by project instruction.

## OpenAI references, reviewed 2026-10-22
- https://developers.openai.com/api/docs/guides/agents/orchestration
- https://developers.openai.com/api/docs/guides/agents/running-agents
- https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- https://developers.openai.com/api/docs/guides/agents/integrations-observability
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/testing/