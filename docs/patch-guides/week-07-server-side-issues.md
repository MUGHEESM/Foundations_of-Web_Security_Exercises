# Week 07 Patch Guide — Server-Side Issues

## Vulnerable Patterns
- Shell command created with unsanitized user input.
- Path built by direct concatenation with user-supplied filename.

## Minimal Defensive Patch
1. Command execution:
   - Validate `host` with strict regex/allowlist.
   - Use `subprocess.run([...], shell=False, check=False, capture_output=True, text=True)`.
2. File handling:
   - Resolve canonical path and enforce it stays within allowed base directory.
   - Reject path segments like `..` and absolute paths.
3. Response hygiene:
   - Avoid exposing full internal filesystem details in responses.

## Validation
- Injection payloads should not trigger arbitrary command execution.
- Traversal payloads should be rejected.
- Normal ping and allowed file reads still function.
