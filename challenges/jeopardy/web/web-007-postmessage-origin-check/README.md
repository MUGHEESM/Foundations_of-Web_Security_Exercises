# web-007: postMessage Origin Check

## Goal
Find and fix trust issues in cross-window messaging.

## Files
- `receiver_snippet.js`

## Tasks
- Explain why missing `event.origin` validation is dangerous.
- Propose an allowlist-based validation patch.
- Replace unsafe sink usage with a safer DOM API.
