# Week 09 — Integrated Scenario (Current Research Style)

## Objectives
- Build an end-to-end attack chain using multiple weaknesses.
- Prioritize mitigations by blast radius and exploitability.
- Practice writing concise incident-style exploit/defense reports.

## Offensive Chain (Suggested)
1. Entry via weak cross-origin trust (`/origin/receiver/`).
2. Session/state abuse (`/attack-lab/` endpoints).
3. Data extraction (`/db-lab/post-export/?author=...`).
4. Environment/infra leak (`/infra-lab/config-diag/?key=...`).

## Defensive Objectives
1. Break the chain at at least 3 points with layered controls.
2. Document which control blocks which stage.
3. Ensure no major feature regression after hardening.

## Deliverable
- One integrated writeup: attack path, impact, fixes, and validation evidence.
