# Foundations of Web Security — Personal Practice Lab

[![Platform](https://img.shields.io/badge/Platform-Docker%20%2B%20Django-0db7ed)](https://www.docker.com/)
[![Track](https://img.shields.io/badge/Track-Semester%20Simulation-blue)](docs/start-here.md)
[![Status](https://img.shields.io/badge/Status-Ready%20for%20Practice-success)](docs/start-here.md)

Personal practice repository inspired by Saarland University’s Foundations of Web Security exercise style.

Local-only practice lab inspired by Saarland's exercise format:
- Screecher-like track: offensive + defensive tasks on a vulnerable social app
- Jeopardy track: standalone attack-only challenges
- Checklist progression (no leaderboard)

## Quick Links
- Start here: `docs/start-here.md`
- Semester checklist: `checklists/semester-checklist.md`
- Weekly manifests: `apps/social_app/challenges/weeks/`
- Patch guides: `docs/patch-guides/`
- Safety policy: `docs/safety/AUP.md`

## Week Map (1–10)
| Week | Topic | Primary Route | Manifest |
|---|---|---|---|
| 01 | Baseline + Recon | `/` | `apps/social_app/challenges/weeks/week-01/manifest.md` |
| 02 | XSS | `/` | `apps/social_app/challenges/weeks/week-02/manifest.md` |
| 03 | CSP | `/csp-lab/` | `apps/social_app/challenges/weeks/week-03/manifest.md` |
| 04 | Cross-Origin Communication | `/origin/receiver/` | `apps/social_app/challenges/weeks/week-04/manifest.md` |
| 05 | Cross-Origin Attacks | `/attack-lab/` | `apps/social_app/challenges/weeks/week-05/manifest.md` |
| 06 | Database Insecurity | `/db-lab/` | `apps/social_app/challenges/weeks/week-06/manifest.md` |
| 07 | Server-Side Issues | `/server-lab/` | `apps/social_app/challenges/weeks/week-07/manifest.md` |
| 08 | Infrastructure Security | `/infra-lab/` | `apps/social_app/challenges/weeks/week-08/manifest.md` |
| 09 | Integrated Scenario | `/integrated-lab/` | `apps/social_app/challenges/weeks/week-09/manifest.md` |
| 10 | Exam Preparation | `docs/start-here.md` | `apps/social_app/challenges/weeks/week-10/manifest.md` |

## Project Info
- Last updated: 2026-03-25
- Mode: local-only training lab (`localhost`)
- Focus: offensive + defensive web security practice

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
4. Open app: <http://localhost:8000>
5. Admin: <http://localhost:8000/admin>
6. Follow the daily walkthrough: `docs/start-here.md`

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
