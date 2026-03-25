# Week 08 Patch Guide — Infrastructure Security

## Vulnerable Patterns
- Insecure/verbose operational headers in responses.
- Diagnostic endpoint exposing env-config values based on user-controlled key.
- Debug/runtime metadata exposed too broadly.

## Minimal Defensive Patch
1. Header hardening
   - Remove `X-Powered-By` and unnecessary custom `Server` details.
   - Use strict `X-Frame-Options: DENY` or equivalent CSP `frame-ancestors`.
2. Diagnostics hardening
   - Disable diagnostics in production mode.
   - Replace arbitrary key lookup with fixed allowlisted diagnostics fields.
   - Never return secret-like values (keys, tokens, passwords, connection strings).
3. Operational hardening
   - Keep `DEBUG=False` outside local dev.
   - Review and tighten `ALLOWED_HOSTS` for deployment environments.

## Validation
- Header audit endpoint no longer discloses insecure values.
- Config endpoint no longer leaks environment values.
- Core app features continue to function.
