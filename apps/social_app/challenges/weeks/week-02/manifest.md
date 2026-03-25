# Week 02 — Cross-Site Scripting (XSS)

## Objectives
- Practice reflected and stored XSS discovery/exploitation.
- Implement context-appropriate output encoding fixes.

## Offensive Tasks
1. Reflected XSS in search results rendering.
   - Route: `/`
   - Input vector: query parameter `q`
2. Stored XSS via comment body rendering.
   - Route: `/post/<id>/comment/` then view `/`
   - Input vector: comment form body

## Defensive Tasks
1. Remove unsafe rendering in search results while preserving search UX.
2. Remove unsafe rendering of user comments while preserving formatting expectations.
3. Re-test: register/login/post/comment/search/profile/notes.

## Suggested Evidence
- Request payload used for reflected XSS.
- Stored payload and trigger context.
- Diff summary of defensive changes.
- Screenshot or terminal output of verification script.
