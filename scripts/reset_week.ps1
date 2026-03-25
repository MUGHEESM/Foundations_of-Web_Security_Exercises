param(
    [string]$Week = "week-01"
)

Write-Host "[reset] stopping containers..."
docker compose down

Write-Host "[reset] removing SQLite database..."
$dbPath = "apps/social_app/db.sqlite3"
if (Test-Path $dbPath) {
    Remove-Item $dbPath -Force
}

Write-Host "[reset] starting clean environment for $Week..."
docker compose up --build -d

Write-Host "[reset] demo users and posts are seeded during app startup"
Write-Host "[reset] done"
