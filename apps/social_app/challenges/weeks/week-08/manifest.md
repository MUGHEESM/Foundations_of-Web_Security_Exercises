# Week 08 — Infrastructure Security

## Objectives
- Audit response headers for infrastructure hardening issues.
- Identify unsafe diagnostics/config exposure behavior.
- Apply least-disclosure and secure-defaults mindset.

## Offensive Tasks
1. Header audit objective
   - Endpoint: `/infra-lab/header-audit/`
   - Identify weak/misleading headers and missing protections.
2. Config diagnostics exposure objective
   - Endpoint: `/infra-lab/config-diag/?key=...`
   - Demonstrate how arbitrary env-key reads leak operational secrets.

## Defensive Tasks
1. Remove or sanitize identifying headers and enforce secure frame policy.
2. Restrict diagnostics endpoint to safe metadata only (or remove it in production mode).
3. Block arbitrary environment variable access from request input.
4. Verify app still runs with baseline hardening.

## Evidence Checklist
- Header snapshot before/after patch.
- Config leak proof before patch.
- Post-patch behavior + regression checks.
