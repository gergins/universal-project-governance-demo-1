# Executable Readiness Gate — mandatory before claiming a workflow can act

A feature exists as documentation until a real capability adapter and runtime are implemented, connected, authorized and verified. A model, SDK, plugin, or tool name is NOT evidence of access or permission.

## Stage A — capability definition
- Unique action name/version, desired effect, input/output schema and constraints
- Concrete execution target/resource/environment (no vague 'anywhere')
- Real implementation route: API, SDK integration, MCP, CLI, browser automation, desktop integration or human step
- Required read-only discovery/inspection of provider capabilities and limits

## Stage B — authorization & protection
- Authenticated user/service principal and delegated actor chain
- Fine-grained scopes, tenant/resource boundaries and server-side allow/deny policy
- Credential issuance, storage, rotation/revocation and secret redaction
- Human approval class and immutable binding to action, target, parameters digest and expiry
- Prompt-injection handling: all remote text and tool output untrusted, no policy elevation
- Provider/API terms, privacy and consent, user access and any jurisdiction-specific restrictions

## Stage C — deterministic execution
- Tool implementation, input validation, timeouts, cancellation, concurrency limits, rate/cost budgets
- Idempotency keys or explicit 'cannot safely retry' classification
- Typed error categories: denied, invalid, unavailable, transient, permanent, partial and unknown-outcome
- Durable operation ID, task state, correlation ID and structured receipt
- Verify postconditions through independent read where feasible; no self-reported success
- Unknown-outcome reconciliation and compensation/rollback design
- Explicit offline/mock vs connected live execution modes

## Stage D — product integration
- UI entry point and transparent feedback/progress/approval interactions
- Accessibility and feeling-oriented failure/recovery journeys
- Test plan (unit, contract, integration, security, failure injection, human acceptance)
- Observability, audit and privacy-preserving retention
- Safe deployment, environment-specific configuration, versioning and operations owner

## Readiness labels
SPECIFIED: design contracts exist, execution may not.
IMPLEMENTED: real adapter/code exists; live access not proven.
CONNECTED: target/auth available but end-to-end effect unverified.
VERIFIED: authorized operation and independent expected outcome verified in named environment.
OPERATIONAL: deployed with monitoring, incident ownership and ongoing access reviews.
BLOCKED/UNVERIFIED: missing access, CI, approval or evidence; never infer an outcome.

## Boundary warning
OpenAI SDK function-tool guardrails do not apply uniformly to hosted tools, computer/shell tools or handoffs. Enforcement must happen at each actual adapter and authorization boundary. Agents SDK is optional; the gate is mandatory for any execution runtime.