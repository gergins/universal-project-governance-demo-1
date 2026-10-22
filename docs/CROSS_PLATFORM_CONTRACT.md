# Platform responsibility matrix

| Surface | Verify first | Guardrail | Evidence of completion |
|---|---|---|---|
| ChatGPT conversations | exact repo and source revision | no assumed workspace access; historical chats are unverified | sourced report and handoff |
| ChatGPT Work | connected accounts, scope and target | least-privilege, human review for sensitive actions | confirmed action results |
| Codex | AGENTS, repo, sandbox, worktree | scoped branch, tests, approvals | tested diff and commit |
| VS Code/editor agents | opened folder, agent settings, terminal target | inspect changes before applying | diff and local test output |
| PowerShell | git root, branch, SHA, exit code | read-only preflight; no bypass tricks | timestamped command results |
| GitHub | repo, PR, workflow runs, branch protections | protected merges, peer review | exact PR/check/merge SHA |
| Docker | Dockerfile, build context, image digest | no embedded secrets, vulnerability scanning, least privilege | build digest + image tests |
| Supabase | actual project ID/environment, migrations, RLS | human approval for production data/auth/schema | migration and policy test results |
| DigitalOcean | app/project/region/release target | protected secrets, rollout and rollback | deployment ID and health checks |
| Other providers | exact account/resource/environment | least privilege, audit, scoped approval | provider receipt/health evidence |

Do not infer configured integrations from mention in docs. Require explicit approval for high-impact side effects. Do not claim enforcement exists based on this file alone.