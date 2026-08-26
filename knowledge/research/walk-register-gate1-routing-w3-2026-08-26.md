# Walk register — `gate1-routing-w3-2026-08-26` (lessons-forge)

**schema_version:** `0.3`

**Plan:** `lessons-forge/knowledge/decisions/drafts/executable-gate1-routing-w3.md`
**Tier:** T1 (Small — three UPDATE rows under structural gates; class shop-infra per the 556 depositor precedent). **Panel: none.**
**Opened:** 2026-08-26

---

## Walk 0 — context pin (REAL, measured 2026-08-26)

1. **The Gate-1 record this plan executes:** 411 accept|codify ruled by the current Planner AS NON-AUTHOR (entry 403 authored by session c1f03a88; the 536/537 precedent; superset-class verified ABSENT from doctrine before ruling); 412 + 413 accept|codify ruled by the CEO via the in-session question UI (their entries are THIS session's authorship — the 459 law; both rulings verbatim in the conversation record and restated in this plan's CEO Context).
2. **Stamp law:** `status_updated_by` = 'planner' for 411, 'ceo' for 412/413 (the 378/389 packet precedent); one shared UTC stamp per run.
3. **Pins:** P=413; the band {411,412,413} all `proposed`/route-NULL (verified live); every id <= 410 terminal; g_pre x=3 (band proposed@NULL), g_post x=0 with accepted|codify=3 — structural CHECK gates under `-bail` (the 538–542 flip form; CHANGES_F the betrayer).
4. **id prediction:** 557.

⚠️ Walk 0 carries no fold rows. Walks 1–2 appended AFTER the draft exists, from real passes.

---

## Walk 1 — five-lens sequential walk (post-draft, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| R1 | 1 | 1 Weak spots | 1.2 | — | ⚠️ CRITICAL — the drafted structural gates used `CASE WHEN … ELSE CAST('FAILED' AS INTEGER)`, which SQLite evaluates to 0 SILENTLY: both gates were decorative (the print-don't-branch class, in SQL). A wrong pre-state would have COMMITTED. | `SELECT CASE WHEN (SELECT x FROM g_pre)=3 THEN 1 ELSE CAST('g_pre FAILED' AS INTEGER) END;` | Folded: the proven CHECK-constraint TEMP-TABLE form (`CREATE TEMP TABLE g(x INTEGER CHECK(...)); INSERT … SELECT COUNT(*)`) — the INSERT fails the CHECK, `-bail` aborts pre-COMMIT; the 552 EXECUTION seat rehearsed this exact abort live. |

**Walk 1 total: one finding (critical), folded.** (Destruction/Vulnerabilities/Integration-record/ACID dry — replay-abort at the g_pre INSERT; per-actor stamp split; rulings restated with sources; set-identity carried.)

---

## Walk 2 — five-lens sequential walk (confirming pass, real)

| id | walk | lens | sub_question | origin | finding | pre_fold_text | resolution |
|---|---|---|---|---|---|---|---|
| — | 2 | all five | — | — | DRY — the refit SQL traced statement-by-statement. | — | No folds. |

**Walk 2 total: 0 findings — all five lenses dry. BAR MET; T1, no panel escalation.**
