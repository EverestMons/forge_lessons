# Forge heading-key migration census — 2026-08-25

**Diagnostic:** 528 | **Produced:** 2026-08-25 | **DB mode:** `file:///Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`

---

## Central finding

**No heading migration is needed.** Plans 499 and 500 (both 2026-08-21) added `_key_heading()` to `src/lessons_forge.py` which strips `[status: …]` and `[target: …]` markers from headings before DB lookup or insert. The ingest code already normalizes headings transparently — the relabel campaign's suffix additions are invisible to the corpus.

The Planner's F1 dry-run numbers (parsed 345 / would_insert 331 / unchanged 14 / db-only 356) are **SUPERSEDED** — they were measured without the `_key_heading` normalization that was already committed to the codebase at measurement time.

---

## F-pin re-derivation

| Pin | Planner value | Re-derived value | Source |
|---|---|---|---|
| F1 | parsed 345 / would_insert 331 / unchanged 14 / db-only 356 | **parsed 345 / would_insert 32 / would_update 0 / unchanged 313 / db-only 57** | Full ingest dry-run with `_key_heading` normalization (see M-1/M-3) |
| F2 | DB heading EXTENDS to file heading | **Correct direction but irrelevant** — `_key_heading` strips the extension at ingest time; DB stores canonical form | `_STATUS_TARGET_MARKER_RE` at `src/lessons_forge.py:52`; `_key_heading` at `:55` |
| F3 | UNIQUE(source_file, source_heading); proposals FK on entry_id | **Confirmed.** `lesson_proposals.entry_id REFERENCES lesson_entries(id) ON DELETE CASCADE`. FK direction: proposals point to entries by id, not by heading. Heading changes cannot break the FK. | `.schema lesson_entries`; `.schema lesson_proposals` |
| F4 | 378 proposals | **378** confirmed | `SELECT COUNT(*) FROM lesson_proposals` → 378 |
| F5 | trailing-separator hash trap ROOT-CAUSE-FIXED 2026-07-16 | **Confirmed.** `_normalize_for_hash` at `:34` strips trailing blank lines + `---` separators. `_TERMINAL_STATUSES` guard at `:178-191` prevents staling `implemented`/`rejected`/`superseded`/`reference`. NEXT_SESSION.md documents the fix arc (plans 203-208). | `src/lessons_forge.py:34-49`; NEXT_SESSION.md |
| F6 | MAX(ingested_at) = 2026-08-19T17:18:13 | **2026-08-19T17:18:13.712877+00:00** confirmed | `SELECT MAX(ingested_at) FROM lesson_entries` |
| F7 | DB at absolute live path, untracked | **Confirmed.** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` exists, not in any worktree. | CLAUDE.md shop policy |

---

## M-1 — the mapping census

### Method

For every DB entry: compute `_key_heading(source_heading)` (identity for DB rows since they were stored via `_key_heading`). For every parsed file entry: compute `_key_heading(source_heading)` (strips `[status: …]` and `[target: …]`). Match by exact key equality + source_file.

### The `_key_heading` normalization (plans 499/500)

```python
# src/lessons_forge.py:52-56
_STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target):[^\]]*\]', re.IGNORECASE)

def _key_heading(heading: str) -> str:
    return _STATUS_TARGET_MARKER_RE.sub('', heading).rstrip()
```

Strips `[status: …]` and `[target: …]` markers. **Preserves** `[tag: …]` markers. Introduced in commit `7e8b2a2` (plan 499, 2026-08-21), refined in `dd54b33` (plan 500, 2026-08-21). The `ingest_lesson_entries` function at line 146 calls `_key_heading` before both SELECT lookup and INSERT.

### Suffix grammar measured in LESSONS.md

All 345 entries have at least one marker:
- `[status: …]`: 331 entries. Values: `codified` (225), `pending` (92), `learned` (14).
- `[target: …]`: 239 entries. Values: `PLANNER_TEMPLATE.md` (148), `DRAFTING_CYCLE.md` (87), `RULE_20_SELF_CHECK_BLOCK.md` (2), `FORGE_QA.md` (1), `PANEL_SEAT_TEMPLATE.md` (1).
- `[tag: …]`: 334 entries. 61 unique tag values.
- Entries with zero markers: **0**.
- Other bracket markers: **none found**. The grammar is exactly `[status: …]`, `[target: …]`, and `[tag: …]`.

### Classification

**Total: 345 parsed + 370 DB = 715 rows. All classified. Zero unexplained.**

#### Matched (313 entries)

DB heading == `_key_heading(file heading)`. Content hash equal in all 313 cases. Zero hash drift. These are the core corpus entries (June 2026 onwards) whose headings were annotated with `[status: …]`/`[target: …]` by the relabel campaign, but the markers are stripped by `_key_heading` at ingest time, so they match perfectly.

#### DB-only (57 entries, IDs 1–57)

All from April–May 2026 vintage. These entries have been **removed from LESSONS.md entirely** — not reformatted, not archived, simply absent. The file now begins at `## 2026-06-02:`. No `## Archived` section exists.

Removal appears to have occurred during the 2026-08-21 reconciliation session (git log: `89cc869 docs: session wrap 2026-08-21 (SESSION 58b) — lessons-corpus arc: memory audited to zero, LESSONS.md reconciled, corpus snapshotted`).

**Proposals on these 57 entries: 62 total.** All in terminal status:
- `implemented`: 32
- `superseded`: 24
- `rejected`: 6
- `proposed`: 0 | `stale`: 0 | `ambiguous`: 0

No active work is keyed on any orphaned entry.

**Classification: removed-from-file.** No heading-migrated, no heading-migrated+content-drifted, no ambiguous entries exist. The suffix-stripped matching (stripping `[tag: …]` in addition to `[status: …]`/`[target: …]`) finds zero additional matches — the 57 are genuinely absent from the file.

#### File-only / genuinely new (32 entries)

Post-F6 entries added to LESSONS.md between 2026-08-19 and 2026-08-25. All have unique canonical headings (no collisions among themselves or with DB headings).

| Date | Count | Entries |
|---|---|---|
| 2026-08-19 | 7 | Clone-diff three passes, anchor path for git, shipped rule wrong action, declaration/consumer pair, correction opens gap, malformed sqlite3 URI, periodic task exception guard |
| 2026-08-21 | 4 | Hand-building vs system registries, mechanized workflow wrong destination, content_hash not identity, CEO glossary.md decision |
| 2026-08-22 | 3 | Single-arm probe uninterpretable, lookup key identity, regression guard before fix |
| 2026-08-23 | 4 | Derives-its-own-terms identity, read checker implementation, mechanism self-insufficiency, session wrap mid-flight append |
| 2026-08-24 | 10 | Tool verdict channel, folding not adopting, described-vs-measured fold, print-not-branch check, watched directory predicate, date-keyed affirmation gate, predicted id not identity, review file-list vs consumers, observer window start, schema enum feature claim |
| 2026-08-25 | 4 | Context boundary precedent, shared deposit filename collision, correct instruction three encounters, resurrect code with hardening history |

---

## M-2 — the migration mechanics

### No migration needed

Because `_key_heading()` already strips `[status: …]` and `[target: …]` at ingest time (line 146), the DB's stored headings are canonical and match the key-stripped file headings exactly. The `ingest_lesson_entries` function's SELECT lookup at line 147–150 finds the correct row for every matched entry. **No UPDATE of `source_heading` is required.**

### FK verification

`lesson_proposals.entry_id REFERENCES lesson_entries(id) ON DELETE CASCADE`. Direction: proposals reference entries by integer `id`, not by heading text. A heading change on an `lesson_entries` row would not affect any FK relationship. Verified from `.schema lesson_proposals`.

### Proposal-staling side effect trace

The ingest update path (lines 167–202) runs when `content_hash` differs. It:
1. Flags terminal-status proposals (`_TERMINAL_STATUSES`: implemented, rejected, superseded, reference) via `terminal_proposals_flagged` — **does not demote them** (the F5 fix).
2. Marks non-terminal, non-stale proposals as `stale` via `UPDATE … SET status = 'stale' … WHERE status != 'stale' AND status NOT IN (…_TERMINAL_STATUSES)`.

Since all 313 matched entries have **equal hashes** (would_update = 0), the update path **never fires**. Zero proposals at risk.

### Drifted-arm handling (hypothetical)

Not applicable — would_update = 0. If content had drifted, the ingest would update `raw_content`, `content_hash`, `tags`, and `entry_date`, then stale non-terminal proposals. The heading stays unchanged (it was already canonical). The `_normalize_for_hash` function ensures trailing-separator changes don't flip hashes (F5 fix).

---

## M-3 — the true ingestion batch

### Scratch-DB rehearsal

Copied DB to `/tmp/lessons-forge-scratch-528.db`. Ran `ingest_lesson_entries(conn, entries)` with the real parser output.

```
Pre:  entries=370  proposals=378
Post: entries=402  proposals=378

Result:
  inserted: 32
  updated: 0
  unchanged: 313
  stale_proposals_marked: 0
  terminal_proposals_flagged: []
```

**New entry ID band:** 371–402 (AUTOINCREMENT, sequential).

**Hash stability check:** All 370 pre-existing entries retained their original content_hash. Zero drift.

**Proposals:** 378 pre and post — no proposals created, staled, or flagged.

### Batch fingerprint

The true post-08-19 ingestion batch is **32 inserts, 0 updates**. Expected shape confirmed:
- would_insert (32) == genuinely-new count (32) ✓
- would_update (0) == drifted arm (0) ✓
- unchanged (313) == matched count (313) ✓

---

## M-4 — the executable spec

### Simplified by M-1 findings

Because no heading migration is needed, the follow-up executable reduces to a **clean ingest** with standard safeguards:

**Step 1 — Ingest the 32 new entries**

1. Pre-ingest backup: `cp lessons-forge.db pre-ingest-2026-08-25-<ts>.db`
2. Dry-run verification: run `ingest_lesson_entries` in a transaction, verify result matches batch fingerprint (inserted=32, updated=0, unchanged=313, stale_proposals_marked=0), print sentinels BEFORE commit.
3. Commit on match; rollback on mismatch.
4. Post-ingest verification: `SELECT COUNT(*) FROM lesson_entries` → 402; `SELECT COUNT(*) FROM lesson_proposals` → 378 (unchanged); `SELECT id, source_heading FROM lesson_entries WHERE id >= 371 ORDER BY id` → the 32 new entries; verify no proposals staled.

**Verification arms (397-precedent disciplines):**
- Parser-diff authority: the real `parse_lessons_md` + `_key_heading` output is the source of truth, not grep or manual heading comparison.
- ID-band statement: new entries occupy IDs 371–402 (AUTOINCREMENT from current MAX(id)=370).
- Batch fingerprint: inserted=32, updated=0, unchanged=313.
- Dry-run-then-live with rollback: transaction-wrapped, sentinel-gated.
- Pre-backup file: `pre-ingest-2026-08-25-<ts>.db` per house convention.

### What the executable does NOT need

- No `UPDATE lesson_entries SET source_heading = …` — the headings are already correct.
- No UNIQUE-collision pre-check for migration — there is no migration.
- No proposal manipulation — no content drift triggers the staling path.

---

## M-5 — the relabel-side residue

### Heading-keyed consumer search

```
/usr/bin/grep -rln -F "entry_heading" /Users/marklehn/Developer/GitHub/lessons-forge/
/usr/bin/grep -rln -F "entry_heading" /Users/marklehn/Developer/GitHub/governance/knowledge/research/
```

**lessons-forge consumers (excluding .git):**

| File | Classification |
|---|---|
| `knowledge/research/bare-entry-ruling-2026-08-23.tsv` | TSV with `entry_heading` column. All 14 entry_ids (59, 82, 88, 93, 104, 112, 116, 122, 123, 134, 328, 330, 331, 333) are in the MATCHED set. **NOT stale.** The `entry_heading` values are display-friendly excerpts keyed by `entry_id`; the FK to `lesson_entries.id` is the operative key, not the heading text. |
| `knowledge/research/learned-promotion-2026-08-23.tsv` | TSV with `entry_heading` column. All 17 referenced entry_ids are in the MATCHED set. **NOT stale.** Same structure — `entry_id` is the FK, heading is for human readability. |
| `knowledge/research/promotion-corrected-2026-08-23.tsv` | TSV with abbreviated `entry_heading` column. All entry_ids MATCHED. **NOT stale.** |
| `knowledge/decisions/Done/diagnostic-504.md` | Plan file referencing `entry_heading` in prose. Historical artifact. **NOT stale** (describes completed work). |
| `knowledge/decisions/Done/executable-507.md` | Plan file referencing `entry_heading` in prose. Historical artifact. **NOT stale.** |
| `knowledge/decisions/Done/diagnostic-506.md` | Plan file referencing `entry_heading` in prose. Historical artifact. **NOT stale.** |
| `knowledge/decisions/Done/diagnostic-503.md` | Plan file referencing `entry_heading` in prose. Historical artifact. **NOT stale.** |
| `knowledge/decisions/ready-diagnostic-forge-heading-key-migration.md` | This diagnostic's own plan file. Self-referential. **N/A.** |

**governance consumers:**

| File | Classification |
|---|---|
| `governance/knowledge/research/walk-register-executable-bare-entry-heading-bytes.md` | Walk register for plan 507. Historical. **NOT stale.** |
| `governance/knowledge/research/walk-register-executable-bare-entry-annotate.md` | Walk register. Historical. **NOT stale.** |
| `governance/knowledge/research/walk-register-diagnostic-learned-promotion.md` | Walk register. Historical. **NOT stale.** |
| `governance/knowledge/research/walk-register-diagnostic-forge-key-migration.md` | Walk register for this diagnostic. Self-referential. **N/A.** |
| `governance/knowledge/research/walk-register-diagnostic-bare-entry-ruling.md` | Walk register. Historical. **NOT stale.** |

**Verdict: zero stale consumers.** All TSV files use `entry_id` as their operative key. The `entry_heading` column in each is a display label, not a lookup key. Since the migration this diagnostic was designed to spec is unnecessary (the code already handles it), and all referenced entry_ids are in the matched set with stable headings, no consumer is broken by the relabel.

---

## M-6 — open questions

### Q1: disposition of the 57 removed-from-file entries (IDs 1–57)

The 57 entries from April–May 2026 are absent from LESSONS.md. They were removed during the 2026-08-21 reconciliation session. Their 62 proposals are all in terminal status (implemented=32, rejected=6, superseded=24). No active work references them.

**Options requiring a ruling:**

- **Keep as historical corpus.** The entries and their proposals remain queryable. The ON DELETE CASCADE FK means deleting entries would also delete their proposals. Since all proposals are terminal, there is no functional harm in keeping them — they simply won't appear in future ingest diffs. This is the zero-risk option.
- **Mark retired.** Add a `retired_at` column or equivalent to `lesson_entries` so queries can distinguish current-corpus from historical. Requires a schema migration — heavier than the value it provides for 57 terminal-only rows.
- **Delete.** `DELETE FROM lesson_entries WHERE id BETWEEN 1 AND 57` cascades to 62 terminal proposals. Irreversible (DB is untracked; the 2026-08-21 `corpus-snapshot-2026-08-21.sql` is the last backup). Not recommended without a fresh snapshot.

**Recommendation:** keep as historical corpus (the zero-risk default). The orphaned rows consume negligible space and do not interfere with ingest or classification. The `get_unclassified_entries` helper (line 275) correctly excludes them because they have terminal proposals. If a future audit requires clean separation, a `retired_at` column can be added then.

### Q2: none additional

No other forks surfaced. The ingest is straightforward — the heading-key hazard the diagnostic was designed to measure has already been resolved by plans 499/500.

---

## Rule 27 gap table — the executable's change sites

| # | Change site | Operation | Risk | Verification |
|---|---|---|---|---|
| 1 | `lesson_entries` table | INSERT 32 rows (IDs 371–402) | Low — pure append, no existing row touched | Post-ingest: `SELECT COUNT(*) = 402`; ID band 371–402; `SELECT COUNT(*) FROM lesson_proposals` = 378 |
| 2 | `lessons-forge.db` file | Modified on disk | Medium — untracked, no git safety net | Pre-backup to `pre-ingest-2026-08-25-<ts>.db`; scratch-DB rehearsal already validated |
| 3 | None — no heading UPDATE | N/A | N/A | The hazard this diagnostic was designed to settle does not exist; `_key_heading` (plans 499/500) already resolves it |

---

## Summary

The 2026-08-23 relabel campaign's `[status: …]`/`[target: …]` heading suffixes do NOT break the corpus — plans 499/500 (2026-08-21) added `_key_heading()` which strips those markers at ingest time. The Planner's dry-run measured a hazard that was already fixed in the codebase. The actual ingest batch is 32 new entries (2026-08-19 through 2026-08-25), 313 unchanged, 0 updates, and 57 historical entries removed from the file but safely orphaned in the DB with only terminal proposals. No migration executable is needed — only a standard ingest.
