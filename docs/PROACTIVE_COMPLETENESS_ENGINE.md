# Proactive Completeness Engine — don't wait for the user to know what to ask

## Role
At each idea, design or execution request, autonomously identify consequential missing capabilities and dependencies. Offer material omissions proactively with evidence and reason. Do not generate a maximal checklist or invent scope. The framework is a discovery and delivery system, not a promise that every integration is enabled.

## Operating loop
1. INTENT: Extract user goal, project identity, environment and authorization. Label missing information; start with safe discovery where possible.
2. WHAT: Select relevant discovery lenses from CAPABILITY_CATALOGUE.md (idea, research, domain, feeling, design, data, integration, security, engineering, testing, deployment, operations). Mark not-applicable categories with rationale.
3. DEPENDENCY EXPANSION: For each proposed feature or action, traverse preconditions backward until requirements are implementable: interfaces, authoritative source/data, identity, consent, auth, credential provenance, capability adapter, execution environment, permissions, error semantics, test fixtures, independent observable postcondition, lifecycle ownership.
4. HOW: Decide deterministic software or human process first. Add model/API, SDK or agent coordination only when judgement and tool selection justify it. Prefer existing trusted integrations and least complexity.
5. ACTION READINESS: Complete the executable-readiness checklist before calling something executable (see EXECUTABLE_READINESS_GATE.md).
6. DELIVERY: Map selected capabilities to staged outcomes, acceptance evidence, risks, costs, user-experience requirements and a responsible owner. Distinguish design vs implementation vs verified operation.
7. REVIEW LOOP: Re-run this gap analysis when new features, integrations, providers, risks, approvals or lifecycle transitions occur. Flag material omissions early; avoid repeated low-value concerns.
8. REPORT: Present ranked critical gaps, their consequence, how to close them, and the next safe task. Do not silently enlarge user-approved scope.

## Trigger questions agents must answer internally
- What must already exist for the requested behavior to work end to end?
- What real tool/application/provider performs the side effect?
- Who is authenticated, what resources may they access, and where is that enforced?
- How would we know the desired state changed, beyond a model saying so?
- What happens when a provider declines, partially succeeds, times out or is unavailable?
- How does the person feel in success, delay, failure and recovery?
- What security, privacy, accessibility, legal, cost or operational constraint could invalidate this design?
- Which test proves the assumption? If testing is deferred, what remains unverified?
- Can we reuse existing capabilities instead of making a new agent, tool or module?

## Anti-bloat policy
Core rules live in AGENTS.md. Topic knowledge belongs in focused references and reusable skills. Generate project files only after relevant lenses are selected; avoid identical policy copied into multiple files. Use the simplest verified implementation that meets the goal.

## Output schema for gap reports
`gap_id, dependency, evidence_state, risk, consequence, required_action, responsible_role, acceptance_evidence, disposition`
Dispositions: REQUIRED_NOW, REQUIRED_BEFORE_RELEASE, OPTIONAL, NOT_APPLICABLE, DEFERRED_APPROVED.