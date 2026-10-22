# WHAT / HOW — universal idea-to-product model

## WHAT: New product repository
WHAT defines the particular idea and product, not the template's implementation mechanism.
- Idea and opportunity: problem, outcomes, alternatives, feasibility, evidence and unknowns.
- Research: users, market, science/technology, competitors and source confidence.
- Domain: domain terminology, rules, workflows, stakeholders, country-specific obligations and experts.
- Human experience: target feelings, accessibility, trust, user agency, usability, error and recovery experience.
- Product: value, jobs-to-be-done, journeys, requirements, capability catalogue and success measures.
- Design: information architecture, interface and interaction contracts, brand consistency and inclusive research.
- Engineering: system components, data, integration, realtime/performance, reliability and maintainability.
- Security & compliance: threat model, privacy, accessibility and jurisdictional review (never implied certification).
- Quality: acceptance, unit/integration/end-to-end, security, performance, pilot and evidence.
- Delivery: cost, deployment, telemetry, support, rollback, incidents and improvement.
- AI when justified: agent autonomy, tools, coordination, guardrails, model evaluation and human oversight.

Each capability belongs to a project only after selection. Set status: NOT_APPLICABLE, CANDIDATE, SELECTED, SPECIFIED, IMPLEMENTED, VERIFIED, OPERATED. Mark rationale, owner, acceptance criteria and dependencies. Avoid generating a tool/agent for every capability.

## HOW: Reusable template
HOW owns lifecycle guidance, concise `AGENTS.md`, targeted skills, preflight, risk policy, execution contracts, approvals, deterministic validation, documentation/handoff, and framework versioning.
HOW is not a hidden runtime: its executable operations require configured adapters/tools and credentials. It never infers completion from intentions.

## Workflow
1. Describe an idea, select/create a fresh project repository from the master template (or copy the documented template with source version).
2. Populate project manifest and `docs/PROJECT_BRIEF.md`. Verify owner/repo, commit, context and access.
3. Run WHAT discovery, classify candidate domains, ask for approval only at consequential decision points.
4. Generate selected capability catalogue with acceptance criteria and intended human experience.
5. Choose HOW execution path for each task: ordinary deterministic code, human workflow, Codex, direct model API, SDK or multi-agent orchestration, only if justified.
6. Have one coordinator retain accountable task state; delegation is bounded and independent authorization is enforced by real tools.
7. Build a small verified vertical slice, iterate from evidence; label unavailable CI and deployment explicitly.
8. Review, approve, ship under separate release controls; record observations and revise the product backlog.
9. When master framework changes, propose reviewed project-specific upgrades (templates do not auto-update).

## Ownership separation
Master repository contains universal instructions, catalogs, schemas, validators, and illustrative templates. Each new project owns its goals, domain facts, source, decisions, tests, environment IDs, credentials and operational state. Never copy another project's secrets or approvals.

## Design economy
Use progressive disclosure: `AGENTS.md` points to this document; capabilities are a menu, not required documents. New files/agents are added when there is an actionable need. Avoid duplicate policy and make all versioned references stable.