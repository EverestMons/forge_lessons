# QA Receipt — forge-bootstrap-2026-09-02 (plan 100016)

**Date:** 2026-09-02 | **Agent:** forge_lessons QA | **Step:** 2 (QA)

## Verification

| item | probe | expected | actual | status |
|---|---|---|---|---|
| 1a | `git show --stat HEAD` paths | CLAUDE.md, dev-log-forge-bootstrap-2026-09-02.md, scripts/bootstrap.sh (3 files) | exactly those 3 files, 98 insertions | ✅ |
| 1b | `test -x scripts/bootstrap.sh` | EXEC_BIT | EXEC_BIT | ✅ |
| 1c | `bash -n scripts/bootstrap.sh` | syntax=0 | syntax=0 | ✅ |
| 1d | `### Interpreter` count in CLAUDE.md | 1 | 1 | ✅ |
| 2a | governance log -1 MACHINE_SETUP.md | `[100016]` commit | `18d3559 [100016] MACHINE_SETUP v1.1: forge bootstrap (thread 79), the daemon's missing variable, the shop's interpreter, the hooks-install act` | ✅ |
| 2b | P6 token `**Version:** 1.1 (2026-09-02).` | 1 | 1 | ✅ |
| 2c | P6 token `- **1.1 (2026-09-02):**` | 1 | 1 | ✅ |
| 2d | P6 token `scripts/bootstrap.sh` in MACHINE_SETUP.md | 1 | 1 | ✅ |
| 2e | P6 token `NO bellows venv` | 1 | 1 | ✅ |
| 2f | P6 token `does not carry it` | 1 | 1 | ✅ |
| 2g | P6 token `- Hooks: the harness loads COPIES` | 1 | 1 | ✅ |
| 2h | P6 token `has no venv of its own yet` | 0 | 0 | ✅ |
| 2i | governance porcelain MACHINE_SETUP.md | empty | empty | ✅ |
| 3a | QA scratch run 1 — interpreter line | `python3.12` | `interpreter: /opt/homebrew/bin/python3.12 (Python 3.12.14)` | ✅ |
| 3b | QA scratch run 1 — suite | 80 passed, exit=0, VENV_CREATED | 80 passed in 0.22s, exit=0, VENV_CREATED | ✅ |
| 3c | QA scratch run 2 — idempotence | 80 passed, exit=0, venv reused | 80 passed in 0.15s, exit=0, venv reused | ✅ |
| 3d | Adversarial (no Homebrew, PATH=/usr/bin:/bin) — interpreter | `/usr/bin/python3` (3.9.6) | `interpreter: /usr/bin/python3 (Python 3.9.6)` | ✅ |
| 3e | Adversarial — pip WARNING (expected under 3.9) | pip 21.2.4 upgrade warning on stderr | `WARNING: You are using pip version 21.2.4; however, version 26.0.1 is available.` | ✅ |
| 3f | Adversarial — suite | 80 passed, exit=0 | 80 passed in 0.24s, exit=0 | ✅ |
| 4a | Full suite under bellows interpreter (`$BPY -m pytest src scripts -q`) | 80 passed, exit=0 | 80 passed in 0.22s, exit=0 | ✅ |

## Operator Act (post-close, owed per machine)

The `.venv/` is per-machine (gitignored). Creating it on the canonical checkouts is the operator's act:
- **Mini (canonical checkout):** Planner's session runs `scripts/bootstrap.sh` once after close and records output.
- **Shop:** next wrap session runs `scripts/bootstrap.sh` on the shop checkout.

The Planner pushes the governance commit (`18d3559`) after the pause — not this step's responsibility.

## Rule 20 Self-Check

*The canonical block output is appended below.*

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100016/knowledge/qa/evidence/forge-bootstrap-2026-09-02/
Files verified: 2
