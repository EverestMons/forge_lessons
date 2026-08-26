# Walk register — `forge-cycle-w3-2026-08-26` (lessons-forge)

**schema_version:** `0.3`

**Plan:** `lessons-forge/knowledge/decisions/drafts/executable-forge-cycle-w3.md`
**Tier:** T1 (Small — a 3-entry ingest+classify cycle; clone of the 529/530 lineage, COMBINED into one plan as a DECLARED deviation justified by W=3). **Panel: none.**
**Opened:** 2026-08-26

---

## Walk 0 — context pin (REAL, measured 2026-08-26)

1. **CEO directive:** act on LESSONS.md — take items to their resting places. This plan is the pipeline's first leg (ingest+classify, NO routing); Gate 1 follows OUTSIDE it: the 08-25 entry routable by this Planner (prior-session author, the 536/537 precedent), the two 08-26 entries routable ONLY by the CEO (this session authored them — the 459 non-author law).
2. **Write-path facts READ from the code, not recalled:** ingest stores CANONICAL headings (`_key_heading` — `[project:]` stripped since 549), so the 22-entry backfill changes NOTHING at ingest (same key, same body hash); expected result EXACTLY `{inserted: 3, updated: 0, unchanged: 345}`; the upsert's update arm (the schema-shape-is-not-write-behavior trap) is unreachable for this batch and pinned to 0 fail-loud.
3. **Pins:** P0=410 proposals, ALL terminal (implemented 311 / reference 29 / rejected 38 / stale 3 / superseded 29 — zero proposed/accepted); E0=402; unclassified 0 now → 3 post-ingest → 0 post-classify (the 530 inversion); corpus 348 parsed entries, LESSONS.md sha-prefix `f80937e06472600872c2` (READ-ONLY — this plan must not write the corpus); reports 08-25 `0984fdd3521e682c3c0a` / 08-19 `7f9b283bf42a31eb9fca` (destructible, sha-pinned, tracked); author-conflict markers date-keyed `entry_date='2026-08-26'` → 2.
4. **Inherited halt-autopsy (459→530 lineage, restated):** the worktree absolute-path trap (425) — report output at `"$(pwd)/reports"`, absolute WITHIN the sandbox; `insert_proposal`/`ingest` do NOT commit — one commit, post-conditions on a FRESH read-only connection; the classify-inversion is the definitive proof.
5. **Corpus freeze inversion:** THIS plan is the deposited cycle plan — LESSONS.md appends are frozen from deposit until close (guard (a)); the deposit itself is the freeze.
6. **id prediction:** 556.

⚠️ Walk 0 carries no fold rows. Walks 1–2 appended AFTER the draft exists, from real passes.

---

## Walk 1 — five-lens sequential walk (post-draft, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| C1 | 1 | 1 Weak spots | 1.2 | — | New-row fetches keyed `id > <count>` — COUNT and MAX(id) can diverge (count-is-not-a-value-guard). | `WHERE id > 402` / `WHERE id > 410` | Folded: pre-flight-captured MAXE/MAXP, parameter-bound. |
| C2 | 1 | 2 Destruction | 2.2 | — | A post-commit death loses the in-memory M1 dict and M5 pre-set; the resume arm would either block or tempt fabrication. | `skip to Task C's commit-check` | Folded: labeled RECONSTRUCTED records with derivations — never presented as the run's own output. |

**Walk 1 total: two findings, both folded.** (Vulnerabilities dry — update-arm pinned 0 fail-loud from the read write-path, hash invariance from the docstring; Integration-record dry — authorship split + discharged-instance notes mandated into reasonings; ACID dry.)

---

## Walk 2 — five-lens sequential walk (confirming pass, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| — | 2 | all five | — | — | DRY — bound forms re-read; pins re-verified live. | — | No folds. |

**Walk 2 total: 0 findings — all five lenses dry. BAR MET; T1, no panel escalation.**
