# Week 04 Patch Guide — Cross-Origin Communication

## Vulnerable Patterns in Lab
- Receiver accepts any `postMessage` origin.
- Receiver writes incoming message via `innerHTML`.
- Sender uses `postMessage(..., "*")`.
- API reflects `Origin` directly in `Access-Control-Allow-Origin`.

## Minimal Defensive Patch
1. Receiver:
   - Check `event.origin` against strict allowlist.
   - Use `textContent` instead of `innerHTML` for message display.
2. Sender:
   - Use explicit target origin (e.g., exact trusted origin).
3. API:
   - Do not reflect arbitrary origin.
   - Return CORS headers only for trusted origins.
   - Keep credential sharing disabled unless strictly required.

## Validation Checklist
- Untrusted origins cannot change receiver state.
- Trusted communication still works.
- CORS headers are strict and predictable.
- Existing app features continue to work.
