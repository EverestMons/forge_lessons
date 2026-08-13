# Lessons Report — 2026-08-13


## Summary


| Category | Count |
|---|---|
| governance_rule | 3 |
| instrumentation | 1 |

**Total proposals:** 4


## Governance Rule


### 2026-08-13: The panel's own fold round is new surface — both capstone HIGHs were interactions BETWEEN the panel's folds [tag: drafting-cycle]


- **Suggested action:** Add capstone-seat/fold-set-reader clause to DRAFTING_CYCLE.md §2.6: a panel round that folds is closed only when a capstone seat (or the scripted inter-seat battery) has read the FOLD SET as its artifact — per-seat commit diffs as the handoff, probe-vs-fold cross-checks, the freeze checklist re-run against the folded state. Add the corresponding new-surface handoff slot to PANEL_SEAT_TEMPLATE.md. Part of the drafting-cycle pair-cluster with entry 326 — both extend the same doctrine surfaces (§2.6 capstone + §2.0/§3 record discipline).
- **Reasoning:** Entry describes how both capstone HIGH findings at the dc-coldfront panel (plan 373) were defects the panel round itself had just created — the fold set was new surface that no seat had read. The 'How to apply' prescribes a mechanism: a capstone seat must read the fold set (per-seat commit diffs, probe-vs-fold cross-checks, freeze checklist re-run) before the round is closed. This is a documentary rule change to DRAFTING_CYCLE.md §2.6, making the fold-set reading an explicit gate rather than an implicit assumption. The entry cites panel-scale replay of the warm-walk fact (~a third of findings are previous round's folds) with a sharper edge: panel folds land denser and later.
- **Confidence:** high

### 2026-08-13: The record could not license the panel — walk 3 ran dry but was never recorded; strike, don't tidy [tag: drafting-cycle]


- **Suggested action:** Add per-walk-commit record-clock rule to DRAFTING_CYCLE.md §2.0/§3: the per-walk commit IS the record's clock — a dry walk is a row, not a non-event. Codify the strike-not-tidy discipline for lagging records (explicit lateness note with dating evidence, never backfill as if contemporaneous). Add a mechanized record-coherence check (rows vs per-walk commits) to the walk-0 battery in the walk-register schema. Part of the drafting-cycle pair-cluster with entry 325 — both extend the same doctrine surfaces (§2.6 capstone + §2.0/§3 record discipline); Gate 1 should route them together.
- **Reasoning:** Entry describes walk 3 running dry at dc-coldfront (plan 373) but having no register row, leaving the record unable to license the cold panel — seat 4 (Integration) flagged it HIGH (S4-2). The 'How to apply' prescribes two mechanisms: (1) per-walk commit as the record's clock (a dry walk is a row), and (2) a mechanized record-coherence check in the walk-0 battery. Both are documentary rule changes to DRAFTING_CYCLE.md §2.0/§3, codifying the strike-not-tidy discipline and adding an automated coherence check. The entry cites the record-decay pattern: 'attention converges on the artifact while the record starves.'
- **Confidence:** high

### 2026-08-13: cwd reset between Bash calls reaches OPS compounds too — a daemon relaunch fired from the wrong directory [tag: operational-recovery]


- **Suggested action:** Extend the commit-compound cd-absolute + location-assert rule in PLANNER_TEMPLATE.md to cover all state-changing ops compounds (restarts, kills, nohup launches, log rotations, db backups): open with cd to absolute path plus location assert (git rev-parse --show-toplevel or explicit pwd check), close by verifying the post-condition (pid is up, startup log line appeared) — never the launcher's exit code.
- **Reasoning:** Entry extends the phase-commits class (cwd resets between Bash calls) to ops compounds, citing session 40's daemon restart #2 where cwd reset put the relaunch elsewhere and the daemon was down ~1 minute before an absolute-path relaunch brought it up (pid 3969). The 'How to apply' prescribes extending the commit compound's cd-absolute + location-assert pattern to all state-changing ops compounds, with post-condition verification. Currently operator practice (discipline); the mechanism candidate is a PLANNER_TEMPLATE.md clause codifying the ops-compound open/close contract alongside the existing commit-compound rule.
- **Confidence:** medium

## Instrumentation


### 2026-08-13: A transcribed census row transposed two column values and stayed well-formed — spot-check rows against their cited sources [tag: verification]


- **Suggested action:** Add a paired-value source spot-check procedure: any hand-transcribed table that pairs values per row gets a sample of rows diffed against their cited sources before it is consumed — the check is cheap (open the citation, compare the pair) and it is the only instrument that sees transposition defects. When a defect is found in a closed artifact, record it in the consuming verdict/register with a pointer to the source; the closed artifact stays byte-stable.
- **Reasoning:** Entry describes plan 370's Item-7 spot-check finding census row #9 of labelled-instances.md carrying its inherited/actual category values swapped relative to its cited source. The row was perfectly well-formed — right shape, both values legal, plausible in either order — so no structural check fires. The 'How to apply' prescribes a new procedural safeguard: spot-check paired values against their cited sources before consumption. This is an instrumentation-class fix — a new verification instrument — rather than a documentary rule change. The mechanism candidate is a standing QA-row convention in RULE_20's orbit.
- **Confidence:** medium
