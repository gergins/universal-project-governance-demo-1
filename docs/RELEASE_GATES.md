# Risk-adaptive authorization and release gates

A stage is a decision checkpoint, not proof of completion. Trivial low-risk work may skip unrelated paperwork; critical paths require proportionate independent testing and human review.

| Action | Required gate |
|---|---|
| Read-only inspection | correct identity and authorized read scope |
| Local isolated code change | scope reviewed, reversible diff, relevant tests |
| GitHub pull request | diff review, applicable policy/tests, no fabricated CI status |
| Staging deployment | target identity, rollback plan, secrets/data review, environment tests |
| Production deployment | named authorized approvals, verified release artifact, backups/rollback, deployment health checks |
| Irreversible data or telecom/emergency operation | specialist review, separate explicit human authorization, audited execution |

**CI states**: NOT_CONFIGURED, BLOCKED, NOT_RUN, RUNNING, FAILED, PASSED, UNKNOWN. A BLOCKED state is not PASSED, and a policy-only check is not product testing. If a project is on hold, don't run, bypass or modify CI without new owner direction.

**Automatable**: identity checks, format/schema validation, tests, scans, signed provenance where configured. **Not automatically satisfied**: product sign-off, legal judgment, security acceptance, user experience, emergency operation approval.

Use exact resource identifiers, environment names, timestamps and evidence links. No production deployment from template placeholders.