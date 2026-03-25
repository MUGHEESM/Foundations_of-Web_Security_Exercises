# Week 06 Patch Guide — Database Insecurity

## Vulnerable Patterns
- SQL query string is built with unsanitized user input.
- Sensitive fields are returned/displayed unnecessarily.
- Export endpoint lacks object-level authorization checks.

## Minimal Defensive Patch
1. Use ORM filters (`username__icontains`) or parameterized cursor execution.
2. Never expose password hashes in templates/API responses.
3. In `/db-lab/post-export/`, restrict exports to `request.user` (or explicit ACL rules).
4. Return least-privilege response payloads.

## Validation
- Injection payloads no longer alter query semantics.
- Unauthorized export attempts are denied.
- Legitimate own-data export remains functional.
- Existing social app features still work.
