# Week 07 — Code Execution & Assorted Server-Side Issues

## Objectives
- Identify unsafe command construction on the server.
- Identify insecure file path handling and traversal exposure.
- Apply strict input validation and safer APIs.

## Offensive Tasks
1. Command execution objective
   - Endpoint: `/server-lab/ping/?host=...`
   - Analyze how user input is interpolated into shell command execution.
2. File handling objective
   - Endpoint: `/server-lab/file-view/?name=...`
   - Explore path traversal behavior due to weak path handling.

## Defensive Tasks
1. Replace shell command construction with safe subprocess usage and strict host validation.
2. Restrict file access to an allowlisted base directory using canonical path checks.
3. Keep existing functionality while blocking traversal and command abuse.

## Evidence Checklist
- Before/after command behavior.
- Before/after file path traversal behavior.
- Patch summary + regression verification output.
