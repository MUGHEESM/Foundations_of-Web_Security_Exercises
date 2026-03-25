# web-016: Config Diagnostics Leak

## Goal
Spot and fix secret exposure in diagnostics endpoint logic.

## Files
- `snippet.py`

## Tasks
- Explain why user-controlled env-key reads are dangerous.
- Replace with safe allowlisted diagnostics output.
