# Week 05 Patch Guide — Cross-Origin Attacks

## Vulnerable Patterns
- GET endpoint mutates session state (`/account/email-optin/`).
- Session preferences API disables CSRF checks.
- API reflects arbitrary `Origin` while allowing credentials.

## Minimal Defensive Patch
1. Convert `/account/email-optin/` to POST-only endpoint with CSRF token requirement.
2. Remove `@csrf_exempt` from `/api/session-preferences/`.
3. Restrict CORS with explicit trusted origin allowlist.
4. Avoid exposing unnecessary sensitive session metadata in API responses.

## Validation
- Cross-site GET should no longer mutate state.
- Cross-site POST without valid CSRF should fail.
- Untrusted origins should not receive CORS allow headers.
- Normal in-app updates should still function.
