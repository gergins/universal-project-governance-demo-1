# Universal Executable Capability Architecture (SDK-optional)

## Purpose and scope
This is a reusable specification for building applications that can actually perform authorized operations across browser/web, APIs, operating systems, files, data, cloud, and physical/integration providers. It is **not** a built-in capability grant, a deployed runtime, a promise that a model can operate any system, or a replacement for provider APIs and permissions.

## Four architectural separations
1. **Intent/planning**: product UI, deterministic workflow or optional LLM decides which capability is requested.
2. **Capability catalog**: typed registered operations describe contracts, permissions, risk, environment, preconditions, confirmation, reversibility, expected postconditions, limits, and evidence.
3. **Executor/gateway**: independently validates identity, arguments, permissions and approval; executes scoped adapter with timeouts, rate limits, idempotency, bounded retries, cancellation and audit.
4. **Evidence/report**: verified observations distinguish not started, awaiting approval, running, succeeded, failed, partially completed, unknown; report external IDs and reconciliation needed.

## Capability interface (proposed standard, not an OpenAI SDK API)
- id, version, description, category (read/write), supported targets (browser, API, OS, cloud, etc.)
- input JSON schema, output JSON schema, idempotency/side-effect semantics
- principal, resource scope, target environment, preconditions and prerequisites
- approval policy, allowed resource selectors, secret access by reference only
- timeout, retry policy, rate limits, cancellation support, compensation/rollback policy
- telemetry/audit fields, expected postconditions, verification procedure and evidence freshness
- owning service, adapter implementation, contract tests and threat model

Example: `website.publish` requires site ID, draft ID, scoped publishing token, explicit approval and target verification; successful API response alone does not prove public visibility. `db.migrate` requires environment, migration identifier, backup, human production approval and schema verification.

## Execution adapters (must be provisioned, never assumed)
- HTTP/REST, GraphQL, gRPC, webhooks; OAuth/API keys with least privilege and rotation.
- Browser/computer automation for visually operated sites when permitted; isolated browser session, explicit domain boundaries, selector/version drift detection, human confirmation for consequential actions.
- Local filesystem and shell/PowerShell; sandbox or constrained allowlisted commands, cwd identity, process exit status, stdout/stderr and filesystem diff.
- Database adapters; transactions, row-level security/role policy, migrations, read/write distinctions.
- Git/GitHub; branch and SHA preconditions, PR review, check conclusions and lease-based updates.
- Docker/container/runtime; image provenance, SBOM, scanning, lifecycle health, isolated execution.
- Cloud platforms such as Supabase/DigitalOcean; scoped project credentials, plan/apply distinctions, deployment IDs, service health and rollback.
- Optional MCP; exposed tools remain untrusted and need per-call independent gateway authorization.
- Future services: queues, messaging, calendars, payments, mobile platforms, accessibility services, device/IoT, voice/video — only through actual authorized adapters.

## Runtime selection (per operation or workflow)
1. Deterministic application code/state machine for predictable operations.
2. Workflow/job engine for durable scheduled or distributed operations.
3. Responses API with application-owned loop and tool dispatcher, when model selection is useful.
4. Agents SDK for managed application-side tool loop, handoffs, sessions and trace integration.
5. Managed Agents API for supported hosted orchestration.
Use a hybrid for mixed needs. Equivalent *functional* capabilities can be built without Agents SDK, but not for free: the application must implement orchestration, state, resumability, failure handling, authorization, tracing and tests itself. Never present SDK features as automatically available outside SDK.

## Reference execution state machine
REQUESTED -> VALIDATED -> AUTHORIZED -> (APPROVAL_REQUIRED -> APPROVED) -> QUEUED -> RUNNING -> VERIFYING -> SUCCEEDED
Failure/alternative transitions: REJECTED, DENIED, CANCELLED, TIMED_OUT, FAILED, PARTIAL, UNKNOWN_NEEDS_RECONCILIATION.
A failed network response after a write may have succeeded remotely; reconcile using idempotency key and provider operation ID before retry. Never auto-retry non-idempotent writes blindly.

## Mandatory security and correctness
- Treat model output and retrieved webpages/PR comments/tool responses as untrusted input; defend against prompt injection.
- Do not rely on LLM prompt guardrails as your authorization mechanism. Apply policy in executor/service; check after all handoffs and before every side effect.
- Obtain explicit human approval for significant production, monetary, credential, external communication, sensitive data or irreversible effects, as configured for the project.
- No unrestricted command/browser executor exposed directly to agent; use constrained adapters and sandbox.
- Keep secrets out of traces and model inputs by default; apply retention, privacy, tenant isolation and compliance policies.
- Maintain durable operation IDs, idempotency keys, audit events, deadlines, retries and compensating workflows as appropriate.
- Verify outcome from authoritative target state, not model summary.

## Reference workflow: deliver feature from idea
User -> requirements -> GitHub issue -> approved scoped implementation -> Codex/VS Code local branch -> checks/tests -> PR -> review/CI (if available) -> staging deploy -> stage verification -> human production approval -> production deploy -> external health check -> monitoring/incident recovery -> handoff.
A blocked CI is **BLOCKED**, never a pass. This is a reusable example, not evidence that a project has these tools available.

## Verification matrix
For each capability test: input rejection, identity mismatch, no-permission, approval absent, prompt injection, successful mocked execution, partial write, duplicate retry, timeout, environment confusion, provider unavailable, external verification mismatch, cancellation, rollback failure. Use isolated fakes for unit tests and credentialed provider sandboxes for integration tests.

## OpenAI references reviewed 2026-10-22
- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/sdk
- https://developers.openai.com/api/docs/guides/agents/running-agents
- https://developers.openai.com/api/docs/guides/tools
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/guardrails/