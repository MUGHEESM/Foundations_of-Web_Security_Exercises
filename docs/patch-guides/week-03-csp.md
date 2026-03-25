# Week 03 Patch Guide — CSP

## Baseline vs Weak Endpoint
- Global baseline CSP is set by middleware.
- `/csp-lab/` intentionally overrides CSP with weaker directives.

## Vulnerable Patterns
- Untrusted content rendered with `|safe` in `csp_lab.html`.
- Endpoint-specific CSP allows `'unsafe-inline'` and broad source allowances.

## Minimal Defensive Patch
1. In `csp_lab.html`, change `{{ note|safe }}` to `{{ note }}`.
2. In `views.py` (`csp_lab`), remove `'unsafe-inline'` and broad wildcards.
3. Prefer inheriting middleware baseline unless endpoint-specific relaxation is required.

## Suggested Safer CSP
- `default-src 'self'`
- `script-src 'self'`
- `style-src 'self'`
- `img-src 'self' data:`
- `object-src 'none'`
- `base-uri 'self'`
- `frame-ancestors 'none'`

## Regression Checklist
- `/`, `/csp-lab/`, login/register/feed routes render correctly.
- No functional breakage for posting/commenting/profile access.
