# Week 05 — Cross-Origin Attacks

## Objectives
- Practice exploiting CORS misconfiguration with credentials.
- Practice CSRF on state-changing endpoints.
- Understand session integrity impact when requests are forged.

## Offensive Tasks
1. CORS misconfiguration objective
   - Inspect headers on `/api/session-preferences/` and `/api/profile-export/`.
   - Identify risky origin reflection + credential exposure pattern.
2. CSRF/session objective
   - Trigger state change through `/account/email-optin/?value=...` without an anti-CSRF mechanism.
   - Trigger POST preference updates against `/api/session-preferences/` where CSRF checks are disabled.

## Defensive Tasks
1. Require POST + CSRF for account state changes.
2. Remove `@csrf_exempt` from session preference API and enforce token checks.
3. Replace CORS origin reflection with strict allowlist policy.
4. Re-test app behavior after patch.

## Evidence Checklist
- Header capture before/after hardening.
- CSRF proof-of-concept behavior before patch.
- Post-patch blocked behavior and functional regression check.
