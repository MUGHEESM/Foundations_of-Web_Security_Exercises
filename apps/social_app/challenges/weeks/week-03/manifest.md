# Week 03 — Content Security Policy (CSP)

## Objectives
- Understand baseline response-header hardening.
- Identify and exploit a weak CSP configuration on a specific endpoint.
- Patch CSP and rendering flow without breaking app behavior.

## Offensive Tasks
1. Compare headers on `/` and `/csp-lab/`.
   - Identify why `/csp-lab/` is weaker than baseline.
2. Trigger script execution through the `note` query parameter on `/csp-lab/`.
   - Hint: inspect template rendering and allowed script sources.

## Defensive Tasks
1. Remove unsafe rendering of untrusted `note` content.
2. Tighten CSP override on `/csp-lab/` to align with global baseline.
3. Verify existing app features still work after the patch.

## Evidence Checklist
- Header comparison output (before/after).
- Payload and observable effect (before patch).
- Patch summary and verification output.
