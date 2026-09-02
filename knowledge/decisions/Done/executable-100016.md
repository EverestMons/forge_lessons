# forge_lessons — executable: PROVISIONING — forge_lessons gets its bootstrap (thread 79), and MACHINE_SETUP.md learns what tonight measured (v1.1: the daemon does not carry the variable, the shop has no bellows venv, the hooks are live COPIES)

**Date:** 2026-09-02 | **Project:** forge_lessons | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (the forge suite `src scripts` under the NEW venv in a scratch copy of the tree, and under the bellows interpreter — the fallback — unchanged; no bellows suite) | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always | **known_failures:** 0 | **Priority:** 2

**auto_close:** false

**Slug:** `forge-bootstrap-2026-09-02`

**Depends on:** the CEO's "All three" (2026-09-02 00:0x — the overnight list, this plan third); tuyere thread 79 (*forge_lessons has no venv on the mini — give it a bootstrap per the multi-machine sketch's third leg*, 2026-09-01); `MACHINE_SETUP.md` v1.0 (2026-09-01) and the facts measured since it was written — plan 100011's T-3 (the shop's interpreter; the daemon's environment), the `hooks-de-hardcode` plan (the harness loads copies); `Done/executable-100008.md` (the clone origin by kind for the TWO-REPOSITORIES-ONE-STEP shape: a forge_lessons worktree writing a governance file by absolute path with `git -C`, never `cd`). Walk register: `/Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-bootstrap-2026-09-02.md`.

**Tier computed, not judged (§1):** **T-1 fires** (two repositories: forge_lessons and eluvian-governance). **T-3 fires** — a bootstrap is BY DEFINITION run on machines other than the one that tested it; QA runs it here in a scratch copy, and the operator's act after close runs it on the canonical checkout. **T-8 fires** (a clone by kind). T-6 no — `MACHINE_SETUP.md` is the operator's checklist, created 2026-09-01 by direct edit (commit `3b347a7`), not doctrine, not the template, not a gate, not a contract; its own History row is the precedent. T-2/T-5 no (`.venv/` is gitignored in forge; nothing destructive; the governance edit is additive prose). → **T1: five-lens walk, no panel.**

## Why this exists

`MACHINE_SETUP.md` §2 says it plainly: *forge_lessons has no venv of its own yet (thread 79); its suite runs under the bellows interpreter.* Every forge plan since the mini came up (100005, 100007, 100008) pinned `/…/bellows/.venv/bin/python` by absolute path. Measured 2026-09-02: `forge_lessons/requirements.txt` declares one dependency (`pytest`); `.venv/` is already in its `.gitignore`; there is no bootstrap script; the suite under the bellows interpreter is `80 passed`; the system `python3` is 3.9.6 and Homebrew's `python3.12` is at `/opt/homebrew/bin/python3.12` (the interpreter bellows' own venv uses). And three facts the checklist should carry were measured after v1.0: the dashboard-launched daemon does NOT carry `$ELUVIAN_WRAP_ROOT` (pid 93535, 0 occurrences), so §1's "set the variable for a third layout" rescues sessions and hooks but not the daemon; the shop has NO bellows venv — its daemon and suite run on the system `python3` 3.9 (the Air's cold seat, 2026-09-01) — so §2's "every bellows tool and test runs under `bellows/.venv/bin/python`" is the mini's fact, not the shop's; and the harness loads the wrap hooks as COPIES from `~/.claude/eluvian/`, so a hooks change owes a per-machine copy the checklist never names.

## What this plan does

**In the forge_lessons worktree:**
- **F1 — NEW `scripts/bootstrap.sh`** (executable; the exact text below): creates `.venv` with `python3.12` where present else `python3`, prints the interpreter and its version, installs `requirements.txt`, runs `src scripts` once.
- **F2 — `CLAUDE.md`:** anchor `### RUN EXE\n` (count 1) → a new `### Interpreter` section inserted BEFORE it (text below), then `### RUN EXE\n` unchanged.

**In the governance checkout, by absolute path (`GOV=/Users/marklehn/Developer/eluvian-governance`), every anchor count 1 at v1.0 (`f1f0987fd6f1d4c0`):**
- **G1 — §2 forge bullet:** anchor `- `forge_lessons`: **has no venv of its own yet (thread 79).**` (the line's start; the script matches the WHOLE line that begins with it — count 1 — and replaces that whole line, not the prefix) → the line replaced by: `- `forge_lessons`: `scripts/bootstrap.sh` (thread 79; plan forge-bootstrap, 2026-09-02) creates `.venv` with `python3.12` where present else `python3`, installs `requirements.txt` (one entry, `pytest`, measured) and runs the suite once (`80 passed` on the mini, 2026-09-02). Until a machine has run it, the suite runs under the bellows interpreter (`/…/bellows/.venv/bin/python -m pytest src scripts -q` from the forge checkout); plans name the interpreter they run under.`
- **G2 — §2 bellows bullet gains the shop's fact:** anchor `hid 11 suite failures for an unknown period.` (count 1) → the same text followed by ` ⚠️ The shop has NO bellows venv (measured 2026-09-01 by the Air's cold seat for plan 100011): its daemon and suite run on the system `python3` 3.9 with `pytest` installed there — so "every bellows tool and test runs under `bellows/.venv/bin/python`" is the mini's fact, and a plan whose A0 demands that venv HALTs on the shop (100011's T-3).`
- **G3 — §1 the daemon caveat:** anchor `Set `ELUVIAN_WRAP_ROOT` to the governance root if the layout differs from both.` (count 1) → the same text followed by ` ⚠️ That variable rescues SESSIONS and HOOKS (the harness sets it from `~/.claude/settings.json`) but NOT the daemon — the dashboard-launched daemon's environment does not carry it (measured 2026-09-01, pid 93535: 0 occurrences). A third layout therefore needs either one of the two named shapes (`bellows_root.resolve_governance_root`, plan 100011, admits the ancestors of the bellows checkout and exactly two siblings, `<parent>/eluvian-governance` and `<parent>`) or the variable placed in the daemon's own environment.`
- **G4 — §6 the hooks act:** anchor `- Every act lands in the shared git namespaces` (the line's start, count 1) → a new line INSERTED BEFORE it: `- Hooks: the harness loads COPIES from `~/.claude/eluvian/` (`bellows/hooks/README.md`; measured 2026-09-02 — regular files, not links). After any change under `bellows/hooks/eluvian/`, copy the changed files there, then run one changed hook by hand with `ELUVIAN_WRAP_ROOT` removed as the canary (plan hooks-de-hardcode).`
- **G5 — the version line:** anchor `**Version:** 1.0 (2026-09-01).` (count 1) → `**Version:** 1.1 (2026-09-02).`
- **G6 — the History row:** anchor `## History\n` (count 1) → the same heading followed by `- **1.1 (2026-09-02):** forge_lessons gains its bootstrap (thread 79; §2 rewritten); §1 gains the daemon-does-not-carry-the-variable caveat; §2's bellows bullet gains the shop's interpreter fact; §6 gains the hooks-install act. Sources: plans 100011 (T-3, the Air's shop run), 100012, 100013 (2026-09-01) and hooks-de-hardcode (2026-09-02); `walk-register-de-hardcode-2026-09-01.md`.`

**`scripts/bootstrap.sh`, exact text:**
```
#!/usr/bin/env bash
# forge_lessons bootstrap — thread 79 / MACHINE_SETUP.md §2 (plan forge-bootstrap, 2026-09-02).
# Creates .venv with the newest python3.12 on PATH (else python3), installs requirements.txt,
# and runs the suite once. Idempotent: an existing .venv is reused. Run from anywhere.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="$(command -v python3.12 || command -v python3)"
echo "interpreter: $PY ($("$PY" --version 2>&1))"
[ -x .venv/bin/python ] || "$PY" -m venv .venv
.venv/bin/python -m pip install -q -r requirements.txt
echo "venv: $(pwd)/.venv ($(.venv/bin/python --version 2>&1))"
exec .venv/bin/python -m pytest src scripts -q -p no:cacheprovider
```

**The `### Interpreter` section (F2), exact text:**
```
### Interpreter

This project's suite runs under its own venv: `scripts/bootstrap.sh` creates `.venv` (`python3.12` where present, else `python3`), installs `requirements.txt` and runs `src scripts` once — MACHINE_SETUP.md §2 (thread 79). Until a machine has run it, the bellows interpreter is the pinned fallback: `/…/bellows/.venv/bin/python -m pytest src scripts -q` from the forge checkout. Plans name the interpreter they run under.

```

## What this plan does NOT do

- **Does not create the venv on the canonical checkout.** `.venv/` is per-machine (gitignored); creating it is the operator's act after this plan closes — the Planner's session on the mini runs `scripts/bootstrap.sh` once and records the output; the shop's session on its next wrap. QA proves the script on a SCRATCH copy of the tree.
- Does not touch bellows, the daemon, doctrine, or `MACHINE_SETUP.md` beyond the six anchored edits. Does not push the governance commit (the Planner pushes after the pause, as for 100008).
- Does not resolve thread 79 or thread 80 in tuyere (thread closure is a keyboard act).

## MUST-PRESERVE

- ⚠️ **TWO REPOSITORIES, ONE STEP.** The forge edits happen in your worktree; the governance edits happen in the LIVE governance checkout at `$GOV` by absolute path — `git -C "$GOV"` for every git act there, never `cd`. Before touching it: `git -C "$GOV" status --porcelain -- MACHINE_SETUP.md` must be EMPTY and `shasum` of the file must equal P1's — a dirty or moved file is a HALT. Commit there by explicit pathspec; do not push.
- **Every anchor count-asserted BEFORE editing**, with a script (a heredoc'd Python is fine), never a blind replace; the six governance edits are ADDITIVE except G1 (a whole-line replacement) and G5 (the version line).
- **The bootstrap is idempotent and exits nonzero on any failure** (`set -euo pipefail`; the suite's exit is the script's exit via `exec`).
- **`known_failures: 0`**: the forge suite is `80 passed` under both interpreters; anything else is a HALT/Critical.

## Numbers discipline — the pins DEV re-derives (measured 2026-09-02 by the Planner)

| pin | what | value | how |
|---|---|---|---|
| P1 | **`GOV_SHA`** — `MACHINE_SETUP.md` at v1.0 | `f1f0987fd6f1d4c0` | `shasum -a 256 "$GOV/MACHINE_SETUP.md" \| cut -c1-16` |
| P2 | **`CLAUDE_SHA`** — forge `CLAUDE.md` | `6d8cb99dec6192be` | same, in the worktree |
| P3 | **`ANCHORS`** — F2 + G1–G6 | **7**, each count 1 | `/usr/bin/grep -cF -- '<anchor>' <file>` |
| P4 | **`FORGE_SUITE`** — under the bellows interpreter, from the forge tree | `80 passed` | `/Users/marklehn/Developer/bellows/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider` |
| P5 | **`INTERPRETERS`** | `python3` → `Python 3.9.6`; `python3.12` → `/opt/homebrew/bin/python3.12`; `requirements.txt` → one line, `pytest`; `.venv/` in `.gitignore` (line 4) | `python3 --version; command -v python3.12; cat requirements.txt; grep -n venv .gitignore` |
| P6 | **`TOKENS`** post-edit in `MACHINE_SETUP.md` | `**Version:** 1.1 (2026-09-02).` 1 · `- **1.1 (2026-09-02):**` 1 · `scripts/bootstrap.sh` 1 · `NO bellows venv` 1 · `does not carry it` 1 · `- Hooks: the harness loads COPIES` 1 · `has no venv of its own yet` 0 | same |

## STEP 1 — DEV

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename this file. You are the forge_lessons Developer.
>
> ⛔ **A0 — resolve BOTH roots in one compound and state both in the dev log:** `cd "$(git rev-parse --show-toplevel)" && [ -f requirements.txt ] && [ -d src ] && echo TREE_OK` — HALT unless TREE_OK; `GOV=/Users/marklehn/Developer/eluvian-governance; [ -f "$GOV/MACHINE_SETUP.md" ] && [ -f "$GOV/COMPANY.md" ] && echo GOV_OK` — HALT unless GOV_OK. Re-derive `GOV` in every compound. `BPY=/Users/marklehn/Developer/bellows/.venv/bin/python` (the fallback interpreter; re-derive per compound).
>
> ⛔ **A1 — re-derive P1–P5; state each; a mismatch is a HALT quoting both.** Then `git -C "$GOV" status --porcelain -- MACHINE_SETUP.md` → EMPTY (else HALT: someone is editing it).
>
> **A2 — F1:** write `scripts/bootstrap.sh` EXACTLY as given (heredoc with a quoted delimiter so nothing expands), `chmod +x scripts/bootstrap.sh`, `bash -n scripts/bootstrap.sh` → exit 0. **F2:** the `### Interpreter` section inserted before `### RUN EXE` (anchor count 1 asserted first). `/usr/bin/grep -cF -- '### Interpreter' CLAUDE.md` → 1.
>
> **A3 — G1–G6 at `$GOV/MACHINE_SETUP.md`** with one script that asserts each of the six anchor counts (1) before applying, applies all six, then asserts P6. Then `git -C "$GOV" diff --stat -- MACHINE_SETUP.md` (state the line counts) and `git -C "$GOV" add MACHINE_SETUP.md && git -C "$GOV" commit -m "[<id from your plan filename>] MACHINE_SETUP v1.1: forge bootstrap (thread 79), the daemon's missing variable, the shop's interpreter, the hooks-install act" -- MACHINE_SETUP.md`; `git -C "$GOV" log --oneline -1 -- MACHINE_SETUP.md` → that commit. Do NOT push.
>
> **A4 — prove the bootstrap on a SCRATCH copy** (never on the worktree, never on the canonical checkout): `S=/tmp/fb-scratch-$(basename "$(pwd)"); rm -rf "$S"; mkdir -p "$S"; git archive HEAD | tar -x -C "$S"; cp scripts/bootstrap.sh "$S/scripts/bootstrap.sh"; bash "$S/scripts/bootstrap.sh"; echo "exit=$?"` → the `interpreter:` line naming `/opt/homebrew/bin/python3.12`, a `venv:` line, `80 passed`, `exit=0`; `test -x "$S/.venv/bin/python" && echo VENV_CREATED`. Then run it a SECOND time (idempotence) → `80 passed`, `exit=0`, and no re-creation (the `venv:` line's interpreter unchanged). Then P4 again from your worktree under `$BPY` → `80 passed` (the fallback still works).
>
> **A5 — dev-log + commit by explicit pathspec.** `knowledge/development/dev-log-forge-bootstrap-2026-09-02.md`: both roots, A1's pins, the seven anchor counts, P6, the governance commit hash, A4's raw lines. `git add scripts/bootstrap.sh CLAUDE.md knowledge/development/dev-log-forge-bootstrap-2026-09-02.md && git commit -m "[<id>] forge bootstrap (thread 79): scripts/bootstrap.sh + CLAUDE.md Interpreter section; MACHINE_SETUP v1.1 committed in governance" -- scripts/bootstrap.sh CLAUDE.md knowledge/development/dev-log-forge-bootstrap-2026-09-02.md`. `git status --short` → empty. STOP.
>
> **Deposits:**
> - `knowledge/development/dev-log-forge-bootstrap-2026-09-02.md`
> - `scripts/bootstrap.sh`
> - `CLAUDE.md`
> - `/Users/marklehn/Developer/eluvian-governance/MACHINE_SETUP.md`
>
> **Scope:**
> - `knowledge/development/dev-log-forge-bootstrap-2026-09-02.md`
> - `scripts/bootstrap.sh`
> - `CLAUDE.md`
> - `/Users/marklehn/Developer/eluvian-governance/MACHINE_SETUP.md`

## STEP 2 — QA

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message.** You are the forge_lessons QA agent. `cd "$(git rev-parse --show-toplevel)"`; `GOV=/Users/marklehn/Developer/eluvian-governance`; `BPY=/Users/marklehn/Developer/bellows/.venv/bin/python` — re-derive both per compound.
>
> **(A) Rule 20 self-check** — the canonical block at the path the dispatcher's mandate names (this machine's `RULE_20_SELF_CHECK_BLOCK.md`; quote the path you were handed). Run with:
> - `plan_slug`: `forge-bootstrap-2026-09-02`
> - `qa_report_path`: `"$(pwd)/knowledge/qa/evidence/forge-bootstrap-2026-09-02/qa-receipt.md"`
> - `evidence_dir`: `"$(pwd)/knowledge/qa/evidence/forge-bootstrap-2026-09-02"`
> - `required_evidence_files`: `["probes-raw.txt", "full-suite-forge-bootstrap.txt"]`
>
> **(B) Items — raw output appended to `probes-raw.txt` (`mkdir -p` the evidence dir first):**
> - **Item 1 — the forge commit is what the plan says:** `git show --stat HEAD --format=` lists exactly the three forge paths; `test -x scripts/bootstrap.sh && echo EXEC_BIT`; `bash -n scripts/bootstrap.sh; echo "syntax=$?"` → 0; `/usr/bin/grep -cF -- '### Interpreter' CLAUDE.md` → 1.
> - **Item 2 — the governance commit and tokens (P6):** `git -C "$GOV" log --oneline -1 -- MACHINE_SETUP.md` (the `[<id>]` commit); the seven P6 greps against `$GOV/MACHINE_SETUP.md`, each with its count; `git -C "$GOV" status --porcelain -- MACHINE_SETUP.md` → EMPTY.
> - **Item 3 — the bootstrap, by a second pair of hands (T-3):** A4 repeated in your OWN scratch copy (`/tmp/fb-qa-$(basename "$(pwd)")`), twice: first run → `interpreter:` naming `python3.12`, `80 passed`, `exit=0`, `VENV_CREATED`; second run → `80 passed`, `exit=0`. Then the adversarial variant: `PATH=/usr/bin:/bin bash "<scratch>/scripts/bootstrap.sh"` in a THIRD scratch copy (no Homebrew on PATH) → the `interpreter:` line names `/usr/bin/python3` (3.9.6), pip prints its "You are using pip version 21.2.4 … consider upgrading" WARNING on stderr (expected under 3.9 — measured at walk 0, not a failure), and the suite still runs (`80 passed`, measured at walk 0 under a fresh 3.9 venv's pytest 8.4.2) — quote the lines.
> - **Item 4 — the full-suite file:** `"$BPY" -m pytest src scripts -q -p no:cacheprovider > knowledge/qa/evidence/forge-bootstrap-2026-09-02/full-suite-forge-bootstrap.txt 2>&1; echo "exit=$?" >> knowledge/qa/evidence/forge-bootstrap-2026-09-02/full-suite-forge-bootstrap.txt` → `80 passed`, `exit=0` (the fallback interpreter, unchanged by this plan).
>
> **(C) The report** `qa-receipt.md`: the verification table, the operator-act note (the venv on the canonical checkouts is still owed per machine; the Planner pushes governance), the Rule 20 stdout APPENDED. Commit: `git add knowledge/qa/evidence/forge-bootstrap-2026-09-02/ && git commit -m "[<id>] QA: forge bootstrap proven twice on scratch + no-Homebrew variant; MACHINE_SETUP v1.1 tokens" -- knowledge/qa/evidence/forge-bootstrap-2026-09-02/`. STOP.
>
> **Deposits:**
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/qa-receipt.md`
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/probes-raw.txt`
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/full-suite-forge-bootstrap.txt`
>
> **Scope:**
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/qa-receipt.md`
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/probes-raw.txt`
> - `knowledge/qa/evidence/forge-bootstrap-2026-09-02/full-suite-forge-bootstrap.txt`

Rule 20 banner (byte-exact, produced by RUNNING the canonical block — never hand-authored):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```

---

## Drafting Cycle

**Tier:** T1 — T-1 (two repos), T-3 (a bootstrap runs elsewhere by definition), T-8 fire; no T2 trigger. Five-lens walk, no panel.

**Walk register:** /Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-bootstrap-2026-09-02.md

**Walk 0 (context pin, measured):** the two file shas; seven anchors counted (1 each); the forge suite under the bellows interpreter `80 passed`; the interpreters on this machine; `requirements.txt` and `.gitignore` read; 100008's two-repositories-one-step pattern read at source; the consumer dry-run (§2.0) on the register's walk-0 line.

**Direction verdict (after walk 1): PROCEED.** Tested: the premise (thread 79's gap and the three post-v1.0 facts, each with its measured source), the mechanism (one script, one section, six anchored prose edits by absolute path in the 100008 shape; the bootstrap proven at walk 0 under both interpreters on a scratch copy), the scope (the venv on canonical checkouts stays the operator's act; governance push stays the Planner's).

**Walks:**
- Weak spots:          w1 2 folded — instruction 2 / record 0 (G1's anchor was a line PREFIX with a whole-line replacement implied — now stated: match the whole line beginning with it; Item 3's no-Homebrew variant left "works or fails loudly" open — walk 0 measured it: a 3.9 venv installs pytest 8.4.2 with pip's upgrade WARNING on stderr and the suite passes, so the expected lines are stated)
- Destruction:         w1 dry — nothing destructive: `.venv/` gitignored and created only in scratch by the plan; the governance edits additive except one line and the version; `set -euo pipefail` + `exec` make the bootstrap fail loudly; the governance file's porcelain and sha checked before it is touched
- Vulnerabilities:     w1 dry — `git -C` never `cd` (100008's HIGH); `GOV`/`BPY`/`S` re-derived per compound; a quoted heredoc delimiter for the script text so `$(…)` does not expand at write time; `bash -n` before any run; the archive-then-copy order in A4 stated (the script is not yet committed when A4 runs)
- Integration-record:  w1 1 folded — instruction 0 / record 1 (the manifest's `class: pending` → `shop-infra`, the depositor's measured assignment against the forge project root — a hold, released under the standing sentence)
- ACID:                w1 dry — two commits in two repositories from one step, each by explicit pathspec, the governance one first so the forge dev-log can carry its hash; a HALT before A3 leaves governance untouched, a HALT after it leaves a committed-but-unpushed governance change the Planner sees at the pause
- **Walk 1 total: 3 findings, 3 folded — instruction 2 / record 1; 0 of 3 fold-introduced.**
- Weak spots:          w2 dry — instruction 0 / record 0 — F1's script and F2's section re-read once each against their anchors; G1–G6 re-read against the v1.0 lines
- Destruction:         w2 dry — instruction 0 / record 0 — unchanged
- Vulnerabilities:     w2 dry — instruction 0 / record 0 — unchanged
- Integration-record:  w2 dry — instruction 0 / record 0 — `propagation_check` clean; the manifest below is the emitter's, spliced at the freeze
- ACID:                w2 dry — instruction 0 / record 0 — unchanged
- **Walk 2 total: 0 findings — instruction 0 / record 0, ALL FIVE LENSES DRY.** Instruction series 2 → 0.

**Conformance (§5):** first run at walk 0 (shape-stability) and re-run after walk 1 and at the freeze: `plan_lint` exit 0 / 0 FAIL at the faithful mirror — expected WARN set (o2)×4 (forge-relative deposits) and the two advisory "mentions tests but declares no test scope" lines (the Test Scope header names the forge suite; the heuristic keys on a phrase it does not find — advisory, left as is); `cycle_check` BAR_MET; `fold_check` baseline saved; `propagation_check` exit 0.

**Closing:** ✅ **BAR MET — walk 2 dry (all five lenses) after walk 1's three folds; T1, no panel owed, none convened.** Substrate present (the register committed at each phase; `fold_check` baseline). The closing-record re-read (§2.7) ran against this block, the register and the emitted manifest at the freeze.

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: scripts/bootstrap.sh, CLAUDE.md, /Users/marklehn/Developer/eluvian-governance/MACHINE_SETUP.md
class: shop-infra
reads: /Users/marklehn/Developer/forge_lessons/requirements.txt, /Users/marklehn/Developer/forge_lessons/.gitignore, /Users/marklehn/Developer/forge_lessons/CLAUDE.md, /Users/marklehn/Developer/eluvian-governance/MACHINE_SETUP.md, /Users/marklehn/Developer/forge_lessons/knowledge/decisions/Done/executable-100008.md
writes: scripts/bootstrap.sh, CLAUDE.md, /Users/marklehn/Developer/eluvian-governance/MACHINE_SETUP.md, knowledge/development/dev-log-forge-bootstrap-2026-09-02.md, knowledge/qa/evidence/forge-bootstrap-2026-09-02/qa-receipt.md, knowledge/qa/evidence/forge-bootstrap-2026-09-02/probes-raw.txt, knowledge/qa/evidence/forge-bootstrap-2026-09-02/full-suite-forge-bootstrap.txt
open_forks: whether the shop's bellows checkout should also get a bootstrap (its interpreter is the system python3 — a MACHINE_SETUP question for the CEO, not this plan's)
walks: 2
yields: 2, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=PASS
coherence: 2/2 walks have register rows
