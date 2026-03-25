# Week 04 — Cross-Origin Communication

## Objectives
- Analyze insecure `postMessage` communication patterns.
- Identify CORS reflection misconfiguration on authenticated JSON endpoints.
- Apply origin validation and safe DOM handling.

## Offensive Tasks
1. `postMessage` receiver trust issue
   - Open `/origin/receiver/` and `/origin/sender/`.
   - Observe message acceptance without strict `event.origin` validation.
2. CORS reflection on profile export API
   - Endpoint: `/api/profile-export/`
   - Observe reflected `Access-Control-Allow-Origin` and permissive credentials header.

## Defensive Tasks
1. In receiver page, validate `event.origin` against allowlist and avoid `innerHTML` for untrusted data.
2. In sender page, use explicit target origin instead of `*`.
3. In API endpoint, remove origin reflection and enforce strict allowlist-based CORS behavior.

## Evidence Checklist
- Before/after header capture for `/api/profile-export/`.
- Before/after behavior for message receiver.
- Patch summary and verification output.
