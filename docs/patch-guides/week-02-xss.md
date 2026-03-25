# Week 02 Patch Guide — XSS

## Vulnerable Sinks
- `feed.html`: `{{ query|safe }}`
- `feed.html`: `{{ comment.body|safe }}`

## Recommended Fix Pattern
1. Remove `|safe` for untrusted user-controlled content.
2. Keep default Django escaping for HTML contexts.
3. If rich text is ever needed, use an allowlist sanitizer and strict rendering context.

## Minimal Defensive Patch
- Change `{{ query|safe }}` to `{{ query }}`
- Change `{{ comment.body|safe }}` to `{{ comment.body }}`

## Regression Checklist
- Search still works and displays plain text query.
- Commenting still works and displays text safely.
- Existing routes function as before.

## Hardening Follow-up (Optional)
- Add baseline `Content-Security-Policy` header.
- Add tests for escaped rendering of search/comment payloads.
