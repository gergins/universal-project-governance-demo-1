# Failure Mode Register — design baseline v1.9.0

A cross-project risk inventory, not proof that a runtime handles these scenarios. Prioritize by selected capabilities and exposure; do not demand all simulations from every simple project. A blocked required control blocks the relevant operation, not unrelated safe analysis.

**Preserved invariants:** one accountable coordinator per outcome; specialists bounded by delegated authority; independently enforceable control plane; durable execution only where recovery and workflow duration justify it. A model is not an authorization or verification mechanism.

| # | Scenario | Class | Detection signal | Required handling | Future evidence |
|---|---|---|---|---|---|
| 01 | `identity-mismatch` | Authorization | Repository, tenant, or environment does not match | Block writes; verify immutable target identity | Verified target + scope |
| 02 | `tool-unavailable` | Connectivity | Adapter missing, disconnected or tool name unknown | Block affected task; re-discover available tools | Availability probe |
| 03 | `malformed-tool-call` | Validation | Bad schema, invalid output or incompatible version | Reject arguments before dispatch; return bounded error | Schema contract test |
| 04 | `prompt-injection` | Trust | Remote instructions attempt authority escalation | Treat retrieved content as data; deny privilege change | Injection rejection evidence |
| 05 | `permission-revoked` | Authorization | Token or permission revoked while task running | Reauthorize immediately before side effect; stop on denial | Policy decision and audit |
| 06 | `cross-tenant-leak` | Privacy | Wrong tenant or user context reaches adapter/specialist | Fail closed on scope mismatch; isolate and audit | Isolation verification |
| 07 | `approval-stale` | Approvals | Approval expired or applies to changed arguments | Recompute action digest; require new approval | Approval match and expiry check |
| 08 | `approval-rejected` | Approvals | Human rejects requested action | Do not dispatch; preserve denial and alternate plan | Denial receipt |
| 09 | `approval-resume-crash` | Durability | Pause/restart loses original approved context | Persist interruption and revalidate upon resume | Resume provenance |
| 10 | `max-turns` | Agent loop | Model never finishes inside bounded turns | Stop and classify incomplete; human escalation/replan | Bounded-run record |
| 11 | `model-timeout` | Agent loop | Model times out or provider is unavailable | Budgeted retry only if safe; preserve task status | Timeout classification |
| 12 | `model-invalid-output` | Agent loop | Unexpected model output, malformed JSON or missing tool | Validate and request bounded correction; never execute invalid plan | Output/schema checks |
| 13 | `model-refusal` | Agent loop | Agent refuses or cannot provide required output | Report blocked/unsupported; do not invent successful completion | Refusal record |
| 14 | `handoff-loop` | Delegation | Agents bounce work indefinitely | Set hop limit and ownership invariant | Delegation DAG and hop bound |
| 15 | `specialist-conflict` | Delegation | Specialists provide mutually incompatible answers | Evidence-based arbitration; escalate unresolved conflict | Conflict decision record |
| 16 | `specialist-scope` | Delegation | Specialist attempts unapproved tool or subdelegation | Deny at gateway; constrain tools/resources/budgets | Adapter denial test |
| 17 | `context-overflow` | Context | Context truncation omits important approvals or constraints | Rehydrate signed/authoritative state; no memory-as-approval | Context provenance |
| 18 | `context-poisoning` | Context | Old summary or tool output fabricates project facts | Re-fetch project evidence; quarantine untrusted text | Source comparison |
| 19 | `concurrent-write` | Concurrency | Parallel tasks race on shared file/resource | Lock or CAS/version checks; serialize conflicts | Conflict rejection test |
| 20 | `double-dispatch` | Side effects | Duplicate delivery/retry produces duplicate external action | Idempotency key or explicit reconciliation before retry | Deduplication evidence |
| 21 | `unknown-outcome` | Side effects | External request times out after possibly succeeding | Read target state before retry; UNKNOWN_OUTCOME status | Reconciliation receipt |
| 22 | `partial-operation` | Side effects | Only some multi-step external actions succeed | Track per-step effects; compensate safely or escalate | Partial-effect ledger |
| 23 | `rollback-failure` | Recovery | Compensation fails or cannot undo irreversible action | Keep incident open; human escalation; no false rollback claim | Recovery outcome |
| 24 | `worker-crash` | Durability | Worker dies during tool call | Restart from durable checkpoint, reconcile in-flight effects | Restart trace |
| 25 | `state-replay` | Durability | Replay accidentally reissues nondeterministic network action | Separate workflow decisions from recorded activity results | Replay equivalence test |
| 26 | `cancel-race` | Durability | Cancellation races with externally committed action | Best-effort cancel then inspect resulting target state | Cancellation reconciliation |
| 27 | `ci-blocked` | Delivery | CI cannot run or is expressly on hold | Never bypass or claim green; preserve blocker | Actual CI execution evidence |
| 28 | `environment-drift` | Delivery | Dev/staging success mistaken for production behavior | Require environment-specific verification | Deployment target identity |
| 29 | `deploy-health` | Delivery | Deployment accepted but service unhealthy | Smoke-check independently; rollback/escalate | Live health evidence |
| 30 | `secret-in-trace` | Observability | Trace, prompt or log includes sensitive credentials | Redact/minimize at capture boundary; limit retention | Redaction checks |
| 31 | `telemetry-down` | Observability | Evidence pipeline unavailable | Fail required gates closed; preserve local minimal audit or block | Observability availability |
| 32 | `budget-exceeded` | Resources | Token, time, API, cost or recursion ceilings exceeded | Stop new dispatch; report partial work | Budget ledger |
| 33 | `cost-surprise` | Resources | Unbounded expensive operation or cloud changes | Preflight estimated limits; approval for threshold crossing | Cost control record |
| 34 | `accessibility-failure` | Experience | Approval or error flow excludes users | Accessible alternative path, tested with affected users | Accessibility review |
| 35 | `unverified-feelings` | Experience | Claims user comfort/safety absent user evidence | Label hypothesis; plan respectful user evaluation | User research evidence |
| 36 | `compliance-assumption` | Governance | Documentation mistaken for legal/regulatory approval | Specialist signoff gate and jurisdiction-specific evidence | Named approval evidence |

## Failure handling contract
Every operational failure has `failure_id`, `task_id`, `environment`, `operation_id`, `cause_category`, `observed_at`, `state_before`, `state_after`, `external_effect_unknown`, `retry_safe`, `compensation_available`, `owner`, `severity`, `evidence_refs`, `next_action`.

Classify failure as VALIDATION, AUTHORIZATION, APPROVAL, TRANSIENT, PERMANENT, PARTIAL, UNKNOWN_OUTCOME, RESOURCE_LIMIT, SECURITY_INCIDENT, or EXTERNAL_BLOCKER. Map each category to an explicit state transition and escalation owner. Treat missing telemetry as lack of verification, not proof of no side effect.

## Verification strategy
Before implementation, derive selected failure scenarios into runnable test cases: injected faults, expected state transition, prohibited behavior, target readback, audit event, and acceptance criteria. Tests remain **NOT RUN** by default. Human testing verifies feeling and accessibility requirements; static validators alone cannot certify those.