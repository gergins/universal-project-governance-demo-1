# Local verification evidence — first controlled increment

Scope: read-only proof and master-template validation only. No cloud credentials, network adapter, write permissions, deployment, CI or certification.

## Execute in a clean local checkout (Windows PowerShell)

```powershell
git status --short
git rev-parse HEAD
powershell -NoProfile -File scripts/local_preflight.ps1
git status --short
```

Capture the actual commit SHA, Python version, exit status, observed tests and any working-tree changes. The preflight runs structural checks, all unittest discovery tests, and Python syntax compilation; it makes no cloud claims. Compilation may create ignored or untracked `__pycache__` directories; do not interpret a dirty checkout as a passing cleanliness gate.

## Reconciliation gate before template readiness

Compare the local v2.3 baseline against this repository with a path/hash inventory. Missing historical skills, evaluations and guides remain *unverified and not imported* until individually reconciled. Do not invent parity or mark the template ready from structural success alone.

## CI hold

Do not add or activate a GitHub Actions workflow until intended workflow contents, third-party action SHA pinning and GitHub permission boundaries are reviewed; CI availability must be verified separately. Do not report successful GitHub CI without a real run URL and conclusion.

## Evidence states

- **Documented**: source and tests exist in GitHub.
- **Observed locally**: actual command output and commit recorded.
- **Observed CI**: actual GitHub Actions run and conclusion recorded.
- **Not verified**: any other untested claim.

The executable control plane in this repository is intentionally read-only; a successful test cannot certify general-purpose agent authorization.
