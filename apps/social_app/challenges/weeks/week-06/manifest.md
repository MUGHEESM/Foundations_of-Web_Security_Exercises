# Week 06 — Database Insecurity

## Objectives
- Identify SQL query construction vulnerabilities.
- Identify authorization/data-leak flaws in data export APIs.
- Apply parameterization and object-level authorization controls.

## Offensive Tasks
1. SQL injection-style objective in `/db-lab/`
   - Inspect raw SQL rendering and search behavior.
   - Manipulate `term` to alter query behavior.
2. Access-control leak objective in `/db-lab/post-export/`
   - Request exports for users other than your own account.
   - Observe missing object-level authorization checks.

## Defensive Tasks
1. Replace string-formatted SQL with parameterized query or ORM query.
2. Remove sensitive password hash exposure from rendered output.
3. Enforce owner authorization in post export endpoint.
4. Re-test app behavior after patch.

## Evidence Checklist
- Request/response for SQL manipulation case.
- Unauthorized export proof before patch.
- Patch summary and regression check output.
