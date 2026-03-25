# Semester Checklist (No Scoring)

## Status Legend
- [ ] Not started
- [~] In progress
- [x] Completed

## Week 1 — Baseline App + Recon
- [ ] Deploy week 1 pack
- [ ] Identify app routes and trust boundaries
- [ ] Complete offensive task(s)
- [ ] Apply defensive fix(es)
- [ ] Verify functionality still works

## Week 2 — XSS
- [ ] Stored XSS objective (comment rendering)
- [ ] Reflected XSS objective (search query rendering)
- [ ] Defensive sanitization + output encoding
- [ ] Regression check

## Week 3 — CSP
- [ ] Compare baseline CSP and `/csp-lab/` policy
- [ ] Bypass weak CSP objective on `/csp-lab/`
- [ ] Tighten CSP policy and remove unsafe rendering
- [ ] Verify no breakage for essential features

## Week 4 — Cross-Origin Communication
- [ ] Analyze `/origin/receiver/` message origin checks
- [ ] Exploit weak validation path in receiver flow
- [ ] Analyze and patch CORS reflection in `/api/profile-export/`
- [ ] Patch origin checks and safe DOM sink usage

## Week 5 — Cross-Origin Attacks
- [ ] Analyze CORS reflection in `/api/profile-export/` and `/api/session-preferences/`
- [ ] Complete CSRF/session objective via `/account/email-optin/` and session preferences API
- [ ] Apply defensive CORS headers and CSRF token enforcement

## Week 6 — Database Insecurity
- [ ] Injection/query misuse objective in `/db-lab/`
- [ ] Access-control data leak objective in `/db-lab/post-export/`
- [ ] Patch query construction and authorization path

## Week 7 — Server-Side Issues
- [ ] Insecure file handling objective in `/server-lab/file-view/`
- [ ] Command/code injection objective in `/server-lab/ping/`
- [ ] Defense with strict validation and least-privilege execution

## Week 8 — Infrastructure Security
- [ ] Security headers audit via `/infra-lab/header-audit/`
- [ ] Secret/config handling audit via `/infra-lab/config-diag/`
- [ ] Infrastructure hardening pass (headers + diagnostics exposure)

## Week 9 — Integrated Scenario
- [ ] Complete integrated chain from `/integrated-lab/` flow
- [ ] Document exploit path and impact end-to-end
- [ ] Apply layered mitigations that break chain stages

## Week 10 — Exam Prep
- [ ] Re-solve mixed tasks from Weeks 2/4/6/7 under timebox
- [ ] Reproduce key fixes from memory and validate
- [ ] Final personal weak-area notes and patch templates
