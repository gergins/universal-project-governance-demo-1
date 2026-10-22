# Offline/read-only local preflight. Does not invoke GitHub Actions or cloud adapters.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    $python = Get-Command python -ErrorAction Stop
    & $python.Source scripts/validate_framework.py
    if ($LASTEXITCODE -ne 0) { throw "Framework validation failed (exit $LASTEXITCODE)" }
    & $python.Source -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw "Unit tests failed (exit $LASTEXITCODE)" }
    & $python.Source -m compileall -q proof scripts tests
    if ($LASTEXITCODE -ne 0) { throw "Python compilation failed (exit $LASTEXITCODE)" }
    Write-Host "PASS: offline preflight completed. This is not CI, deployment or security certification."
}
finally {
    Pop-Location
}
