# Week 01 — Baseline + Intro Vulnerabilities

## Objectives
- Understand app flow and trust boundaries.
- Practice finding one client-side issue and one access-control issue.

## Offensive Tasks
1. Reflected XSS in search display on feed page.
   - Target route: `/`
   - Hint: inspect how search term is rendered.
2. Insecure owner filter in private notes endpoint.
   - Target route: `/notes/?owner=<username>`
   - Hint: verify authorization before data filtering.

## Defensive Tasks
1. Remove unsafe rendering for search query and preserve functionality.
2. Enforce owner-based authorization in notes endpoint.
3. Re-run basic functionality checks (register, login, post, comment).

## Evidence Checklist
- Screenshot or request/response for each exploit.
- Short patch explanation for each fix.
- Confirmation of functionality after fixes.
