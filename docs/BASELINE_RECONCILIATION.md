# Source baseline reconciliation gate

The private GitHub source and public demo `main` branches had identical 57 recursive Git tree entries at the time of the initial comparison. This does **not** establish parity with the original local v2.3 package.

## Compare against the original local package (PowerShell)

From this repository checkout:

```powershell
git pull --ff-only
powershell -NoProfile -File .\scripts\local_preflight.ps1
python .\scripts\compare_baseline.py --baseline "C:\PATH\TO\ORIGINAL\V2.3" --target .
```

Replace the baseline path with the **actual** root folder of the original v2.3 source package. Do not substitute the private GitHub repo for this local baseline.

The inventory checks relative file paths and SHA-256 for regular files. It skips common caches, `.git`, environments, platform-generated metadata and symbolic links; it is not a full byte-for-byte filesystem or git metadata comparison. The printed JSON includes matching, missing, extra and content-different files. Exit code 1 indicates that baseline files are missing or modified in the target; target-only additions are reported but do not make this historical import incomplete by themselves.

**Do not copy files automatically**: first classify intentional simplifications vs omissions, secrets and environment-specific artifacts. Each proposed addition must be reviewed independently before committing to the public demo.

Do not assert baseline completion if the original package cannot be located. CI remains on hold; this tool neither enables it nor claims a run.
