# Week 10 Guide — Exam Preparation

## Recommended Workflow
1. Timed offense block (60-90 min): solve 4 mixed tasks.
2. Timed defense block (60-90 min): patch 4 mixed flaws.
3. Validation block (30 min): run checks and confirm no regressions.

## Fast Recall Templates
- XSS: identify source/sink/context → encode/sanitize → retest.
- CORS/CSRF: trust boundary + credentials + token/method controls.
- DB/authorization: parameterize + least-data + owner checks.
- Server-side: no shell interpolation + canonical path checks.

## Final Checklist
- Can you explain impact and fix in 2-3 sentences per flaw?
- Can you produce minimal safe patch quickly?
- Can you verify behavior with one reproducible test per fix?
