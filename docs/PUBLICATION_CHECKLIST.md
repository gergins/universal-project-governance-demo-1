# Publication and template-readiness gate

Status: PARTIAL IMPORT. Do not enable GitHub template use or claim production-ready controls yet.

## Stable invariants
- One accountable coordinator owns each request's outcome.
- Specialists have bounded authority; delegation never increases privileges.
- All external side effects cross an independently enforceable policy and execution boundary.
- Durable replay/checkpoint infrastructure is introduced only for workflows that need it.
- A successful outcome requires independent evidence. Use the simplest solution first.

## Confirmed GitHub content
Core README, AGENTS.md, read-only walking skeleton, eight tests, and major WHAT/HOW, capability, execution, security and assurance references have been published. Exact remote state must be re-fetched before claiming completeness.

## Required before declaring template-ready
1. Compare every path and content hash from the local validated v2.3 package against the repository.
2. Transfer missing manifest, remaining docs, reusable skills, evaluations and read-only validation scripts. Exclude bytecode and caches.
3. Consolidate README as a short map of authoritative entry points; label historical notes as references.
4. Keep CI workflow disabled until its actions are pinned and its behavior separately verified.
5. Initialize a fresh sample project from the template, replace placeholders, record source commit and validate the project-mode checks.
6. Run documented local tests and record results, environment and commit. Do not imply external API, deployment or security certification from unit tests.
7. Review branch protection, release criteria and risk approvals independently.
8. Record all unresolved gaps; permit publication of a clearly labeled draft but not a verified production framework.

## Separate concerns
VRS CI remains blocked and is not a dependency of this repository. The universal framework has no VRS-specific execution permissions.

## Change policy
Every new feature must state which verified deficiency it fixes. Prefer a small patch to an existing component; introduce new agents or services only when a distinct testable role justifies them.
