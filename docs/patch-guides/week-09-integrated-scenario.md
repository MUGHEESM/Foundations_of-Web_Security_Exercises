# Week 09 Patch Guide — Integrated Scenario

## Strategy
- Treat defenses as chain breakers, not isolated fixes.
- Fix highest-leverage trust boundaries first:
  1. Origin validation + safe DOM sinks
  2. CSRF + method enforcement
  3. Object-level authorization
  4. Diagnostics/config exposure controls

## Minimum Layered Controls
- Cross-origin messaging: strict origin allowlist.
- State-changing endpoints: POST + CSRF.
- Data exports: enforce ownership checks.
- Infra diagnostics: disable in production and remove secrets.

## Validation
- Verify each defensive control independently blocks its stage.
- Verify complete chain no longer succeeds end-to-end.
