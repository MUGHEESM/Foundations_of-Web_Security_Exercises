# Start Here — Daily Practice Plan

## 1) First Launch (One-Time)
1. Start the lab:
   - `docker compose up --build`
2. Sign in with seeded users:
   - `alice / alice12345`
   - `bob / bob12345`
   - `charlie / charlie12345`
3. Confirm core pages load:
   - `/`
   - `/notes/`
   - `/csp-lab/`
   - `/origin/receiver/`
   - `/attack-lab/`
   - `/db-lab/`
   - `/server-lab/`
   - `/infra-lab/`
   - `/integrated-lab/`

## Quick Daily One-Liner
- `./scripts/reset_week.ps1 -Week week-01`
- This performs a clean reset, rebuild, startup, and demo-data seeding.

## 2) Weekly Practice Rhythm (Recommended)
- Day 1: Read current week manifest in `apps/social_app/challenges/weeks/week-XX/manifest.md`
- Day 2: Solve offensive objectives and record evidence.
- Day 3: Apply defensive fixes in your own branch.
- Day 4: Re-test feature behavior and run `./scripts/verify_lab.ps1`.
- Day 5: Write short lessons learned (what failed, what fixed it).

## 3) 14-Day Pre-Lecture Sprint
### Days 1-2
- Week 01 + Week 02 (baseline + XSS)
### Days 3-4
- Week 03 + Week 04 (CSP + cross-origin communication)
### Days 5-6
- Week 05 + Week 06 (cross-origin attacks + database insecurity)
### Days 7-8
- Week 07 + Week 08 (server-side issues + infrastructure security)
### Days 9-10
- Week 09 integrated scenario (full chain + mitigation mapping)
### Days 11-12
- Week 10 exam prep speed drills
### Days 13-14
- Re-do weakest two areas from checklist with strict timebox

## 4) Daily Evidence Template
- Objective attempted:
- Payload/test used:
- Observed behavior:
- Fix applied:
- Verification result:
- One-sentence takeaway:

## 5) Reset Between Sessions
- `./scripts/reset_week.ps1 -Week week-0X`
- This recreates data and re-seeds demo accounts/posts.
