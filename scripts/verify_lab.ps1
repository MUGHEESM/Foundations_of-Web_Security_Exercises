$ErrorActionPreference = "Stop"

Write-Host "[verify] checking compose config"
docker compose config | Out-Null

Write-Host "[verify] checking required files"
$required = @(
    "apps/social_app/manage.py",
    "apps/social_app/challenges/weeks/week-01/manifest.md",
    "checklists/semester-checklist.md",
    "docs/safety/AUP.md"
)

foreach ($path in $required) {
    if (-not (Test-Path $path)) {
        throw "Missing required file: $path"
    }
}

Write-Host "[verify] baseline structure ok"
