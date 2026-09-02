# Dev Log — forge-bootstrap-2026-09-02 (plan 100016) — Step 1 (DEV)

**Date:** 2026-09-02 | **Agent:** forge_lessons Developer

## A0 — Roots

- **FORGE root:** `/Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100016` → `TREE_OK` (requirements.txt and src/ present)
- **GOV root:** `/Users/marklehn/Developer/eluvian-governance` → `GOV_OK` (MACHINE_SETUP.md and COMPANY.md present)
- **BPY (bellows interpreter):** `/Users/marklehn/Developer/bellows/.venv/bin/python`

## A1 — Pins (all match plan)

| pin | what | measured | expected | match |
|---|---|---|---|---|
| P1 | GOV_SHA (MACHINE_SETUP.md v1.0) | `f1f0987fd6f1d4c0` | `f1f0987fd6f1d4c0` | ✅ |
| P2 | CLAUDE_SHA (forge CLAUDE.md) | `6d8cb99dec6192be` | `6d8cb99dec6192be` | ✅ |
| P3 | ANCHORS — 7 anchors, each count 1 | all 1 | all 1 | ✅ |
| P4 | FORGE_SUITE under bellows interpreter | `80 passed` | `80 passed` | ✅ |
| P5 | python3 → Python 3.9.6; python3.12 → /opt/homebrew/bin/python3.12 (Python 3.12.14); requirements.txt → `pytest`; .venv/ at .gitignore line 4 | measured | as stated | ✅ |

Governance porcelain check: `git -C "$GOV" status --porcelain -- MACHINE_SETUP.md` → empty (clean) ✅

## A2 — F1 + F2

- **F1:** `scripts/bootstrap.sh` written exactly as specified; `chmod +x` applied; `bash -n` exit=0 (syntax clean)
- **F2:** `### Interpreter` section inserted before `### RUN EXE`; `/usr/bin/grep -cF -- '### Interpreter' CLAUDE.md` → 1 ✅

## A3 — G1–G6 (MACHINE_SETUP.md at $GOV)

All six anchor counts asserted (each 1) before any edit. All six edits applied:

| edit | anchor asserted (count 1) | result |
|---|---|---|
| G1 | `- \`forge_lessons\`: **has no venv of its own yet (thread 79).**` | whole line replaced with bootstrap bullet |
| G2 | `hid 11 suite failures for an unknown period.` | shop NO-bellows-venv fact appended |
| G3 | `Set \`ELUVIAN_WRAP_ROOT\` to the governance root if the layout differs from both.` | daemon-does-not-carry-the-variable caveat appended |
| G4 | `- Every act lands in the shared git namespaces` | new Hooks line inserted before |
| G5 | `**Version:** 1.0 (2026-09-01).` | replaced with 1.1 (2026-09-02) |
| G6 | `## History\n` | 1.1 row inserted after heading |

**P6 tokens post-edit (all verified):**
- `**Version:** 1.1 (2026-09-02).` → 1
- `- **1.1 (2026-09-02):**` → 1
- `scripts/bootstrap.sh` → 1
- `NO bellows venv` → 1
- `does not carry it` → 1
- `- Hooks: the harness loads COPIES` → 1
- `has no venv of its own yet` → 0

**diff --stat:** `MACHINE_SETUP.md | 10 ++++++---- (1 file changed, 6 insertions, 4 deletions)`

**Governance commit:** `18d3559 [100016] MACHINE_SETUP v1.1: forge bootstrap (thread 79), the daemon's missing variable, the shop's interpreter, the hooks-install act`

## A4 — Bootstrap proven on scratch copy

**Scratch path:** `/tmp/fb-scratch-100016` (built with `git archive HEAD | tar -x -C "$S"; cp scripts/bootstrap.sh "$S/scripts/bootstrap.sh"`)

**First run:**
```
interpreter: /opt/homebrew/bin/python3.12 (Python 3.12.14)
venv: /tmp/fb-scratch-100016/.venv (Python 3.12.14)
80 passed in 0.40s
exit=0
VENV_CREATED
```

**Second run (idempotence):**
```
interpreter: /opt/homebrew/bin/python3.12 (Python 3.12.14)
venv: /tmp/fb-scratch-100016/.venv (Python 3.12.14)
80 passed in 0.97s
exit=0
```
(venv reused — no re-creation; interpreter unchanged)

**P4 fallback re-check (bellows interpreter from worktree):**
```
80 passed in 0.15s
exit=0
```

## Status: Complete
