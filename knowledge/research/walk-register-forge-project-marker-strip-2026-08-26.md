# Walk register — `forge-project-marker-strip-2026-08-26` (lessons-forge)

**schema_version:** `0.3`

**Plan:** `lessons-forge/knowledge/decisions/drafts/executable-forge-project-marker-strip.md`
**Tier:** T1 (Small — one regex arm + two tests; class shop-infra by content: lessons-forge CODE). **Panel: none** (T1 two-walk; direction-class escalates).
**Opened:** 2026-08-26

---

## Walk 0 — context pin (REAL, measured 2026-08-26)

1. **CEO ruling (this session):** LESSONS.md entries may carry an ADDITIVE `[project: <name>]` heading bracket ("the project name would just be an additional tag, not a replacement to anything") enabling per-project sweeps ("mechanize lessons for invoice pulse").
2. **The diagnostic ground (measured from the code, this session):** `_DATED_HEADING_RE` passes any heading bracket through into `source_heading`; entry IDENTITY is `_key_heading`, which strips ONLY `[status:]`/`[target:]` — an unstripped `[project:]` would join the identity key, so retro-tagging an existing entry would orphan its ingest row; the `**Tag:**` line is the machine tag channel and must NOT carry project names (tag-overlap dedup would cross-match unrelated same-project lessons).
3. **The design that follows:** add `project` to the strip alternation — the bracket becomes pure greppable metadata: new entries tag at authoring; backfill becomes SAFE (key unchanged); the tags column untouched.
4. **Target pins:** `src/lessons_forge.py` L52 the exact regex line count-1; suite baseline **63 passed** (measured green this authoring); the two existing `_key_heading` tests at L1590+ unaffected by the change (they assert tag-marker preservation and status/target stripping — neither involves `project`).
5. **id prediction:** id_sequence read 549.

⚠️ Walk 0 carries no fold rows. Walks 1–2 appended AFTER the draft exists, from real passes.

---

## Walk 1 — five-lens sequential walk (post-draft, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| G1 | 1 | 2 Destruction | 2.2 | — | The single resume probe conflated arm-landed with tests-landed — a death between Tasks B and C would skip the tests and commit without them (caught only at QA, one full round late). | `1 → already landed, skip to Task D` | Folded: two-probe branch table (arm, tests) with four arms incl. the impossible-state HALT. |

**Walk 1 total: one finding, folded.** (Weak spots dry — probe pairs earnable, 65 = measured-63 + deterministic-2; Vulnerabilities dry — `[project:` count in live LESSONS.md MEASURED 0, so the widened strip re-keys nothing; Integration-record dry — tags-column exclusion with dedup rationale, real-pytest gate engaged; ACID dry.)

---

## Walk 2 — five-lens sequential walk (confirming pass, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| W2-1 | 2 | 1 Weak spots | 1.2 | — | DRY — branch arms re-read; probes re-verified against the live tree. | — | No fold. |
| W2-2 | 2 | 2 Destruction | 2.2 | — | DRY — arms partition all death states. | — | No fold. |
| W2-3 | 2 | 3 Vulnerabilities | 3.3 | — | DRY. | — | No fold. |
| W2-4 | 2 | 4 Integration-record | 4.1 | — | DRY. | — | No fold. |
| W2-5 | 2 | 5 ACID | 5.2 | — | DRY. | — | No fold. |

**Walk 2 total: 0 findings — all five lenses dry. BAR MET; T1, no panel escalation.**
