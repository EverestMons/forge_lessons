# dev-log-classify-w30c-2026-09-12

## Header

Step: 4 — Lessons Agent: classify batch C
Range: batch C — MAXE+83 to MAXE+122 (541–580), read from Step 1's dev log
MAXE (from Step 1 dev log) = 458
Batch C range: entry ids 541 to 580 (40 entries)
MAXP_C (pre-insert) = 548

## Dispatch-State Determination

DETERMINATION: FRESH

Probe 1 (working tree): knowledge/development/dev-log-classify-w30c-2026-09-12.md — absent (exit=1)
Probe 2 (committed HEAD): not present (exit=1)
Probe 3 (git log --all): 0 commits
Positive control (knowledge/FORWARD.md): present (exit=0)
All three absent → FRESH (no prior dispatch)

## Pre-Flight

**Work list (get_unclassified_entries):**
40 ids: exactly 541–580
All batch C ids present: True
Non-batch-C ids: []

**Proposals on batch C range (entry_id 541–580):** 0 (expected 0)

**M3 before:**
Total proposals: 548 (expected 548 = 466+82)
  accepted: 23
  implemented: 334
  proposed: 82
  reference: 35
  rejected: 42
  stale: 3
  superseded: 29
Accepted: 23 ✓

**MAXP_C = 548** (expected 548 — bound, never hard-coded)

**M5 — triple-set (ids <= 466):** 466 triples captured, SET-IDENTICAL to Step 1's capture

**M6:** 580 entries, MAX(id)=580 ✓

## Classification — Batch C (entries 541–580)

All 40 entries have entry_date 2026-09-09, 2026-09-10, 2026-09-11, or 2026-09-12 — all >= 2026-09-04 → all carry [AUTHOR-CONFLICT] prefix in reasoning.

DISPOSITION | entry=541 | proposal=549 | category=governance_rule | remedy: Add rule: a gate or lint that reads a deposit must be invoked by the deposit's author before the deposit; the DEV's commit line chains the gate function (e.g., tools/check_deposit.py) before git-add; the Planner runs the register lint at each walk close, not only at the fold | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=542 | proposal=550 | category=structural | remedy: Fix commit-subject assert to check both lens number AND lens name (array-supplied): pattern *'lens $i — ${NAME[$i]}'*; declare shell arrays as associative (declare -A) to prevent leading-element shift | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=543 | proposal=551 | category=governance_rule | remedy: Formalize close sequence as fixed: closing lines written → baseline saved → emitter run → lines spliced by key (regex on ^key: ) → baseline saved again → STORED==LIVE diff gate before commit; commit subject naming an act is written after the act's own check passes | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=544 | proposal=552 | category=governance_rule | remedy: Add Planner rule: every post-condition naming a command is RUN at the close over whatever artifact exists at that moment, with output pasted beside it; a post-condition with no runnable command is rewritten until it has one | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=545 | proposal=553 | category=governance_rule | remedy: Add planning rule: before wiring an analysis tool into a gate, benchmark it against the trivial baseline (grep, git log, one-line AST walk) on a known instance; measure precision on the highest-count output; read the tool's schema for what is NOT a node before trusting a recall claim | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=546 | proposal=554 | category=governance_rule | remedy: Add rule: any plan instruction pointing another tree for reads must state in the same sentence that every write goes to the current worktree ($(git rev-parse --show-toplevel)); Deposits listed as worktree-relative paths; post-condition includes git status of canonical tree showing nothing new under the deposit's directory | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=547 | proposal=555 | category=governance_rule | remedy: Add rule: an autopilot session under a CEO delegation executes only the named acts; when a step needs an act outside the list, choose the reversible option (withdrawal over commit, pause over override) and record what was withheld in the baton; the delegation text is quoted in every verdict file the session writes | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=548 | proposal=556 | category=structural | remedy: Promote WARNs that name a gate silence (e.g., 'will NOT be gated', 'missing cold-panel line') to FAIL in plan_lint; update commit-loop gates to print WARN lines alongside the FAIL count | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=549 | proposal=557 | category=governance_rule | remedy: Add QA rule: before a continue verdict on a plan that ships a tool, run the tool once on the ordinary case named in the plan's prose; refuse the verdict when the tool refuses on that case; the (b) check reads the QA's choice of cases, not the tool itself | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=550 | proposal=558 | category=governance_rule | remedy: Add Planner rule: before ruling on or refactoring a pinned behavior, read three things in order — the ratified test, the ratifying plan's premise sentence, and the doctrine/register history for any later correction of that premise; a design whose premise the record has since falsified is 'un-reconciled', not a defect | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=551 | proposal=559 | category=governance_rule | remedy: Add rule: before promoting or adding a lint row letter, enumerate every consumer of the exit and row text, read each consumer's filter, and pick a letter outside all filters; check the letter's git history (git log -S) because a retired letter carries its failure record | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=552 | proposal=560 | category=instrumentation | remedy: Add drafting checklist item: for any tool or lint change, run git archive of HEAD in scratch, apply the change, and run pytest once; include blast-radius result (any breaking tests found and their disposition) in the plan before deposit | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=553 | proposal=561 | category=structural | remedy: Implement --dry flag in lens_commit.py that writes the DRY line to the walk register; enforce that descriptions name no other lens/walk; run the observer after every lens commit and on a scratch project-shaped copy before the receipt | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=554 | proposal=562 | category=governance_rule | remedy: Add drafting cycle rule: a cold panel is licensed only by a dry walk, the lens-4 signal, or the CEO's call; copy a precedent's condition (the measured yield that licensed it), not its shape | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=555 | proposal=563 | category=governance_rule | remedy: Add Planner rule: run every tool bare and read its exit code before the next act; a verdict is its own call authored only after reading the check's printed output; a close is confirmed by its 'commit OK' line before the receipt exists; a deposit on bytes no commit holds is withdrawn | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=556 | proposal=564 | category=governance_rule | remedy: Extend probe-environment rule: pass multi-assignment env vars explicitly or via ${=VAR} under zsh (not bare $VAR); run probes from a directory that holds none of the artifacts, or read the tool's BASIS before believing a zero result | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=557 | proposal=565 | category=structural | remedy: Fix register fold-row appender: before appending a row, check if the last non-blank line is a table row; if not, emit the two-line table header first | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=558 | proposal=566 | category=governance_rule | remedy: Add rule: before filing a thread from a seat's or census's attribution, grep the code that produces the effect (grep the call, not the name); when a filed thread is found misfiled, supersede it with a thread naming the measured producer rather than editing the plan around it | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=559 | proposal=567 | category=governance_rule | remedy: Add rule: before reading a table's rows as per-key records, read the write site and its context; document the actual granularity in the tool's limits section; calibrate on instances from both arms before trusting a classifier | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=560 | proposal=568 | category=governance_rule | remedy: Add Planner rule: when a tool emits the number the record will carry, the prose quotes the tool's number (via --dry-run or equivalent), never a hand tally of the same thing; two counts of one quantity in one document is an ACID finding | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=561 | proposal=569 | category=governance_rule | remedy: Add rule: in a scripted per-lens chain, every path is absolute and every lens commit's --stat is read before the next lens runs; a chain's first silent failure (wrong path, wrong interpreter) reshapes every later step | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=562 | proposal=570 | category=structural | remedy: Use git log -L <lineno>,<end_lineno>:file (AST-derived line range) instead of -L ':name:file' for Python function history traces; add planning rule: benchmark on both top-level and nested function forms before assuming the query domain is uniform | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=563 | proposal=571 | category=governance_rule | remedy: Add rule: a 'verbatim', 'whole', or 'all N' claim in a deposit is verified by the last line or byte count at the (b) read, not by the section heading; an instrument the doc must carry is written into the doc before the teardown item runs, with a post-condition naming the line count | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=564 | proposal=572 | category=governance_rule | remedy: Add rule for background watches: name interpreter, script, and every file absolutely (not CWD-relative); logic distinguishes three states — condition seen, condition not seen, and nothing read (empty read is not 'gone'); a confirmation step using the same broken read confirms nothing | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=565 | proposal=573 | category=governance_rule | remedy: Add planning rule: before designing a remote mechanism for a 'manual act', measure the process tree (who spawned it, what session it lives in, what restarts it); the verb usually exists and the missing piece is only parentage | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=566 | proposal=574 | category=governance_rule | remedy: Add Planner rule: before drafting from a thread, grep each item against the live tool and template changelog; items contradicted by newer rules are retired (not built); dispositions recorded in the plan as rulings on evidence | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=567 | proposal=575 | category=structural | remedy: Fix status.py: replace mode=ro URI with a plain connection using PRAGMA query_only (so WAL can create the -shm file); add explicit handler for SQLITE_CANTOPEN returning the STOPPED state; add test exercising the stopped state with no writer process present | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=568 | proposal=576 | category=governance_rule | remedy: Add rule: a premise about library behavior is a version fact; the pin names interpreter path and library version beside the value; measurement is always under the interpreter the plan mandates; when a premise holds on one version only, the plan states so and version-gates the mechanism | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=569 | proposal=577 | category=governance_rule | remedy: Add rule: before a test or read-only step invokes a callee, enumerate what the callee names absolutely (launchd labels, ports, canonical paths, live DBs); check those resources before and after the step, not only the sandbox; isolation from tmp_path or worktree applies only to code that takes its paths from them | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=570 | proposal=578 | category=governance_rule | remedy: Add rule: at the (b) read, every figure in a re-derivation is matched to the command in the step's transcript that printed it; a figure with no command is struck and corrected before any continue or override; pin rows for surfaces the step cannot reach are marked 'Planner-measured, not re-derived by the step' | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=571 | proposal=579 | category=structural | remedy: Fix path guard: check explicitly for None return from the lookup function before calling realpath; use a sentinel value the comparison side can never hold; add test where the lookup fails and verify the guard refuses | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=572 | proposal=580 | category=structural | remedy: Fix threads done --commit: add -m, -c, or --first-parent to git diff-tree call so merge commits report their file list; add test with a two-parent commit; at authoring, require commit file-list tools to declare their merge behavior | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=573 | proposal=581 | category=governance_rule | remedy: Add test rule: version-compatibility tests name the interpreter they run under, run the oldest shop interpreter (currently Python 3.9.6), and check import as well as parse; each interpreter gap fix is verified by running the suite under the old interpreter, not by the new test alone | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=574 | proposal=582 | category=governance_rule | remedy: Add rule: before trusting a liveness discriminator, name the death it must detect and verify the property it reads changes at that death; use pid, run-authored heartbeat, or a process-held lock — not files the run created or the host's heartbeat; give the discriminator a test in which the run dies and its artifacts stay | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=575 | proposal=583 | category=governance_rule | remedy: Add rule: in a log with time-only stamps, anchor every reading to a known event of the day by line number before calling anything today's; a time-of-day match never stands for a timestamp in a log that crosses midnight | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=576 | proposal=584 | category=governance_rule | remedy: Add test rule: a confirm-then-act control requires tests on both branches — cancel proves nothing happens without consent, confirm proves the act happens; the mutant set must include one that deletes the act itself, which only the positive test can kill | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=577 | proposal=585 | category=governance_rule | remedy: Add drafting rule: for cross-repo plans, run every gate command the plan will invoke (pre-check, mutation tool, observer) against a scratch archive of the target repo with the plan's own paths before deposit; a host tool's path pattern is an interface the target repo never agreed to | markers: [AUTHOR-CONFLICT] RIDER
DISPOSITION | entry=578 | proposal=586 | category=governance_rule | remedy: Add walk rule: a command added or changed by a fold is treated as new v0 for standing-rules diff purposes; the fold's register row names which rules the new instruction was checked against (CLAUDE.md, plan preamble, cited lessons) | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=579 | proposal=587 | category=governance_rule | remedy: Add rule: when a step exercises a guarded tool on a copy of live state, list what the copy holds at snapshot time (the step's own in-flight row first); write the edit the copy needs beforehand, or give the tool a way to exclude the caller; never leave the executor to improvise the fix | markers: [AUTHOR-CONFLICT]
DISPOSITION | entry=580 | proposal=588 | category=structural | remedy: Fix lens_commit.py: detect a dry lens by the presence/absence of its own DRY line artifact rather than by whether the register was otherwise unchanged; add explicit flag for the dry case to avoid inference from diff; or check the DRY line directly as the artifact | markers: [AUTHOR-CONFLICT]

## Commit

Single conn.commit() issued after all 40 inserts.

## Post-Conditions (fresh read-only connection)

**M2 — unclassified:** [] (expected []) ✓
**M3 — total proposals:** 588 (expected 466+122=588)
  accepted: 23, implemented: 334, proposed: 122, reference: 35, rejected: 42, stale: 3, superseded: 29
  Accepted still 23 ✓
**M4 — new proposals with wrong route/status:** 0 (expected 0) ✓
**M17a — entries with multiple new proposals:** [] ✓
**M17b — new proposals outside entry band:** 0 ✓
**M5 — triple-set SET-IDENTICAL (466 triples, ids<=466):** True ✓
**M6 — entries:** 580, MAX(id)=580 ✓
**M7 — proposals with [AUTHOR-CONFLICT] in reasoning:** 108
  M7 direction 1 — marked entry ids == dated entry ids (ids with date>=2026-09-04): True (108==108) ✓
  M7 direction 2 — early-dated entries with marker: 0 ✓
**M12 — stale proposals:** 3 (expected 3) ✓
**M16 — new duplicate proposals:** 0 ✓
**M8 — sha prefix:** 0c99d2073e5072f83058 ✓

**M15 — DISPOSITION line count:**
Count of DISPOSITION lines: 40 (expected: 40)
M15: OK
