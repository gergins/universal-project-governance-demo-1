# Agent capability execution — optional OpenAI Agents SDK profile

Status: reusable architecture guidance; no SDK integration or live execution is implied. Apply only to projects that benefit from agentic orchestration.

## Choose the simplest adequate architecture
1. Ordinary deterministic code or workflow for fixed repeatable operations.
2. Responses API when the application owns the model/tool loop and state.
3. OpenAI Agents SDK when agent loop, typed tools, approvals, sessions, tracing or specialist delegation are valuable.
4. Multiple agents only when boundaries and evaluations justify the complexity.

## Capability execution contract
Every capability must declare: `capability_id`, purpose, responsible owner, triggering event, input and output schema, required roles/scopes, target environment, data classification, tool adapter, allowable side effects, idempotency key strategy, cost/latency budget, timeout/retry policy, human approval conditions, fallback and rollback, evidence requirements, tests and observability.

Flow: request -> authenticate/authorize -> validate schema -> identify capability and target environment -> decide deterministic vs agent execution -> run tool-specific authorization and input checks -> request human approval if required -> tool execution -> validate output and external effects -> record evidence/trace with privacy controls -> return verified result or explicit failure.

A model output or SDK trace is not itself proof of a committed GitHub change, executed shell command, successful payment, migrated database or working deployment. Verify through the system of record.

## Agents SDK architecture
- **Agent and Runner:** instructions, model configuration, tools, loop boundaries and result handling.
- **Typed function tools:** executable application adapters with input schema and server-side authorization; tools operate using scoped credentials.
- **Hosted/execution tools:** understand execution location; shell, computer, patch, sandbox and hosted tools have distinct safeguards.
- **MCP:** register trusted servers and permitted tool inventory, validate every action and observe trust boundaries.
- **Manager/agent-as-tool:** one coordinator retains control over specialist subprocesses.
- **Handoffs:** specialists receive delegated control; restrict transferred context and separately validate permissions.
- **Sessions/state:** conversational continuity only, not authoritative operational state; avoid sensitive data over-retention.
- **Structured outputs:** validate against schema and business invariants, not only JSON shape.
- **Guardrails:** layer input/output and eligible function-tool guards; enforce security in adapters independent of LLM.
- **Human approval:** interrupt and resume using a bound capability, exact parameters, actor, context and expiry; re-authorize before side effects.
- **Tracing:** record execution/latency/token costs and error types; redact personal data, credentials and tool arguments as needed; respect deployment/ZDR restrictions.
- **Evals:** deterministic scripted tests for runner/tool routing, plus live integration and adversarial tests in controlled environments.

IMPORTANT: SDK function-tool guardrails do not cover all hosted, shell or built-in tools; handoff calls are separate. Do not mistake SDK guardrails for a general security perimeter.

## Example project policy (conceptual, not runnable infrastructure)
```
capability_id: issue.create
execution: agents_sdk_optional
inputs: {repository: string, title: string, body: string}
role: project_contributor
side_effect: github_issue_write
approval: required_if_external_or_high_risk
precondition: verify_repo_identity_and_write_scope
postcondition: fetch_created_issue_from_github
on_failure: return_error_with_evidence_no_success_claim
```

## Tests required before enabling an executable capability
1. Schema rejects malformed input and untrusted instruction injection.
2. Access denied on wrong repo, user, tenant and environment.
3. High-risk action cannot run without bound approval; approval cannot be replayed.
4. Tool timeout/failure is reported, not fabricated as success.
5. Handoff receives only necessary context and preserves authorizations.
6. Retry/idempotency prevents duplicate external effects.
7. Output is reconciled with provider state.
8. Sensitive data is redacted from logs and tracing.
9. Tool-run budgets and maximum turns prevent unbounded work.
10. Evaluate actual model behavior separately from mocked runtime behavior.

## Adoption and release status
`NOT_APPLICABLE` / `DESIGNED` / `IMPLEMENTED` / `TESTED` / `APPROVED` / `ENABLED` / `VERIFIED_IN_TARGET_ENVIRONMENT`. No automatic promotion.

## Official primary references (review for SDK version drift)
- Python SDK: https://openai.github.io/openai-agents-python/
- Python tools: https://openai.github.io/openai-agents-python/tools/
- Python guardrails: https://openai.github.io/openai-agents-python/guardrails/
- Python testing: https://openai.github.io/openai-agents-python/testing/
- TypeScript SDK: https://openai.github.io/openai-agents-js/
- TypeScript sessions: https://openai.github.io/openai-agents-js/guides/sessions/
- TypeScript tracing: https://openai.github.io/openai-agents-js/guides/tracing/