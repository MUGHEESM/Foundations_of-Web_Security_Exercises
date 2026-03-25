# Foundations of Web Security — Personal Practice Lab

Local-only practice lab inspired by Saarland's exercise format:
- Screecher-like track: offensive + defensive tasks on a vulnerable social app
- Jeopardy track: standalone attack-only challenges
- Checklist progression (no leaderboard)

## Scope
- Personal use only
- `localhost` only
- Dockerized for resettable weekly practice

## Quick Start
1. Copy `.env.example` to `.env`
2. Build and run:
   ```powershell
   docker compose up --build
   ```
3. Fresh reset + start (daily shortcut):
   ```powershell
   ./scripts/reset_week.ps1 -Week week-01
   ```
3. Open app: <http://localhost:8000>
4. Admin: <http://localhost:8000/admin>
5. Follow the daily walkthrough: `docs/start-here.md`

## Seeded Demo Accounts
- `alice / alice12345`
- `bob / bob12345`
- `charlie / charlie12345`

## Initial Structure
- `apps/social_app/` Django vulnerable social network
- `apps/social_app/challenges/weeks/` weekly exercise manifests
- `challenges/jeopardy/` standalone challenges
- `checklists/semester-checklist.md` progress tracker
- `docs/patch-guides/` defensive patch walkthroughs
- `scripts/` reset and verification scripts
- `docs/` safety rules and course mapping

## Week Cycle (Practice)
- Deploy week pack
- Solve offensive tasks
- Apply defensive fixes in your branch
- Run local verification
- Reset and move to next week

## Safety
See `docs/safety/AUP.md`.
