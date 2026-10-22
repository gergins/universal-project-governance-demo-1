# Coordination runtime: project-neutral design blueprint

Status: DESIGN ONLY. Applies only when selected by a product's capability requirements.

## Three layers
1. **Decision plane:** one accountable coordinator interprets goal, builds bounded task DAG, consults specialist roles, arbitrates disagreements and reports final evidence. Specialists are logical roles; no requirement for one model/process per role.
2. **Control plane:** non-model services enforce authenticated principal, delegated scopes, tenant/resource boundaries, input/output schemas, preconditions, human approval, budgets, legal state transitions, concurrency and idempotency. No delegation may expand authority.
3. **Execution plane:** real adapters invoke authorized APIs, code, databases, terminals and cloud providers; capture receipts and independently read postconditions. All tool output is untrusted for permissions and instructions.

## Capability roles, not required agent instances
Discovery, research, domain, product, human-experience/accessibility, architecture, engineering, integration, data, QA, security, reliability, operations, documentation. Each selected specialist contract contains responsibility, input, allowed tools, resource limits, expected output, acceptance evidence and escalation conditions. Use one agent or ordinary code unless specialization is justified.

## Task lifecycle
INTAKE -> DISCOVER -> PLAN -> VALIDATE_PLAN -> READY -> (AWAIT_APPROVAL) -> EXECUTE -> VERIFY -> SUCCEEDED or BLOCKED/FAILED/UNKNOWN_OUTCOME. Record every transition with owner, time, environment, policy decision and evidence reference. Approval is not execution; tool acknowledgement is not verified success.

## Execution necessities
- Record execution capability's concrete adapter, availability, environment, input schema, authentication/scopes and server-side authorization before work can run.
- Bound specialist recursion, model/tool turns, parallelism, runtime, cost, context and retries. Enforce per-resource write leases or equivalent version checks.
- On ambiguous timeouts, reconcile external state before retry. Use idempotency keys where provider guarantees them; otherwise document at-least-once behavior and recovery.
- Persist immutable execution receipts and authoritative task state distinct from prompt/session memory; use checkpoints for resume.
- No model call or external API side effect in deterministic replay logic. Store nondeterministic decisions as events or run calls as explicit activities with durable results.
- Cancel safely; cancellation cannot erase effects already executed. Escalate irreversible failures. Define compensation when actual rollback is possible.
- Require independent evidence before a completion claim; record unverified, partial and blocked outcomes honestly.
- Review prompt injection, data minimization, trace privacy and human-accessible feedback/approval UX.

## SDK-neutral integration strategy
Contracts and enforcement do not import vendor-specific agent classes. Adapters may use direct model calls, OpenAI Agents SDK, Temporal, LangGraph, Microsoft Agent Framework, MCP, ordinary functions or a native runtime. Choose one simple runtime initially; add durable workflow orchestration when interruptions, concurrency or long-running actions justify it. An adapter mentioned here is not installed or connected.

## Future first walking skeleton (deferred)
One coordinator, one bounded specialist role, one real read-only adapter, one persistent task record and one independent verifier. Prove the denied unauthorized call before enabling write operations. Then add state transitions, approvals, durability, parallelism, integrations, recovery and evaluations incrementally.

## Architecture decision gates
Require measurable justification before adding a separate specialist, runtime, workflow engine or SDK. Prefer simpler deterministic workflows. Treat documentation and structural checks as different from execution tests. No tests are claimed by this file.