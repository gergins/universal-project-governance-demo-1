# Universal Idea-to-Product Playbook
Version 1.0 | Project-neutral | Integrates with AGENTS.md, EVIDENCE_PROTOCOL.md, DELIVERY_PLAN.md and project.manifest.json.

## Mission
Move any idea through evidence-based discovery, a minimally tested vertical slice, iterative delivery, and controlled operations. Use these stages adaptively; research can overlap, but release approval gates cannot be skipped. AI agents do not approve their own production releases. Historical chat is not live project state.

## Stage-by-stage execution plan
| # | Stage | Lead tool(s) | Deliverable | Exit evidence |
|---|---|---|---|---|
| 1 | Idea intake | Human + ChatGPT | IDEA_BRIEF.md | Defined user, problem and intended outcome |
| 2 | Discovery intelligence | ChatGPT + Work | DISCOVERY_REPORT.md | Credible sources, user input, assumptions and unknowns |
| 3 | Feasibility and alternatives | ChatGPT + Work | FEASIBILITY.md | Build/buy/reuse comparison and material risks |
| 4 | Product charter | Human + ChatGPT | PRODUCT_CHARTER.md | Explicit owner approval of scope and constraints |
| 5 | Capability catalog | ChatGPT | CAPABILITIES.md | Capabilities, dependencies, priorities, owners |
| 6 | User journeys and UX | Design specialists + ChatGPT | UX_SPEC.md | Tested flows; accessibility needs stated |
| 7 | Requirements and acceptance | ChatGPT + GitHub Issues | REQUIREMENTS.md / Issues | Testable acceptance criteria with IDs |
| 8 | System architecture | Architecture review + Codex | ARCHITECTURE.md + ADRs | Interfaces, security boundaries, failure modes reviewed |
| 9 | Technology and infrastructure | Engineering + Work | TECH_STACK.md | Decision, cost and provider assumptions documented |
| 10 | Repository foundation | GitHub + Codex | Repository, governance, branch strategy | Verified repo identity and permissions |
| 11 | Walking skeleton | Codex + local IDE | First runnable end-to-end path | Local tests and demonstration evidence |
| 12 | Iterative implementation | Codex + VS Code + PowerShell | Focused PRs with tests | Reviews and passing applicable checks |
| 13 | External integration/data | Engineering + providers | Migration, integration contracts | Contract, rollback, privacy/security tests |
| 14 | Quality validation | QA + specialists | TEST_EVIDENCE.md | Unit, integration, E2E, a11y, security, reliability checks |
| 15 | Staging and pilot | Cloud + operations + users | STAGING_REPORT.md | Healthy deployment, real pilot feedback, rollback plan |
| 16 | Release and production | Human approvers + GitHub + cloud | RELEASE_RECORD.md | Named approvals, deployment ID, smoke tests |
| 17 | Operations | Cloud + operations | OPERATIONS.md | Observability, SLOs, incidents, cost controls |
| 18 | Learning and evolution | Users + ChatGPT + GitHub | PRODUCT_IMPROVEMENTS.md | Measured feedback creates traceable new requirements |

## Interaction protocol / sequence
1. Human presents idea. ChatGPT turns it into questions, alternatives and versioned brief. Work may research public sources or connected approved data; cite what it actually examined.
2. Human approves a product charter, not implementation details inferred by AI. GitHub stores accepted artifacts, decisions and issue IDs. Use PR reviews for changes to baseline documents.
3. ChatGPT or Work drafts a bounded engineering task referencing issue ID, repo, branch, base commit, explicit requirements, acceptance criteria, dependencies, expected artifacts and allowed tools.
4. Codex reads AGENTS.md and the actual files at the target commit, creates or uses an approved feature branch, proposes minimal changes and runs permitted tests. VS Code is optional for human inspection and debugging; PowerShell preflight verifies local environment before terminal work.
5. Codex returns exact file diffs, command outcomes, limitations and follow-up risks. A PR binds implementation to requirements and evidence. GitHub CI is independent evidence only if a workflow actually runs and concludes successfully.
6. Reviewer approves merges according to repository policy. A merge does not imply deployment. Deployment requires provider/resource identity, environment approval, artifact digest, rollout and rollback plan.
7. Docker builds versioned artifacts, Supabase (if used) handles migration and RLS verification, DigitalOcean (if used) runs deployments and operational checks. Each provider must report its actual outcome, not one inferred from another.
8. Post-deployment metrics, user reports and incident findings flow back into issues, evaluations and prioritized roadmap items. New session must re-fetch operational state.

## Minimum developer task envelope
- Project and scope: repo owner/name, expected branch, base SHA, target environment.
- Requirement: ID, user story, rationale, explicit acceptance criteria and non-goals.
- Evidence: source files, approved ADR, API schema, known risks, fresh retrieved evidence.
- Permissions: allowed reads/writes, explicit prohibitions, approvals needed.
- Outputs: changed paths, diffs, checks, commands, logs, caveats, commit/PR links.
- Stop conditions: identity mismatch, unavailable credential, missing evidence, failing tests, blocked CI, approval required.

## Completion/status vocabulary
PROPOSED; DOCUMENTED; IMPLEMENTED_UNVERIFIED; LOCALLY_TESTED; CI_VERIFIED; STAGING_VERIFIED; HUMAN_APPROVED; PRODUCTION_DEPLOYED; POST_DEPLOY_VERIFIED; BLOCKED; UNKNOWN.
Never replace BLOCKED with PASS or UNKNOWN with COMPLETE. Test evidence expires for changing environments; revalidate as needed.

## Ownership and risk
Human product owner owns priorities and product acceptability. Domain specialists own specialized approvals. ChatGPT/Work own research and documentation assistance, not automatic legal or security certification. Codex owns proposed code changes, not the truth of production state. CI owns the outcomes of its actual checks. Platform operators own deployments, observability and rollback. A provider listed in a manifest is not proof it is provisioned.

## Reuse in a new repository
1. Copy the governance template to the new repository.
2. Set project.manifest.json, project charter and technology/target environments.
3. Initialize relevant issues, ADR templates, release gates and owner approvals.
4. Only then enable the CI and deployment automations that have been reviewed for this project's risks.
5. Read docs/CROSS_PLATFORM_START.md at the beginning of a new AI session; verify all runtime facts.

## CI hold safety
If a project marks CI as BLOCKED, do not rerun, rewrite, bypass, disable or claim passing status until explicitly authorized by the project owner. Work on independent design and documentation may continue without misreporting CI.

## OpenAI documentation (verified 2026-10-22)
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://developers.openai.com/tracks/building-agents
- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- https://developers.openai.com/api/docs/guides/agents/integrations-observability
- https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex