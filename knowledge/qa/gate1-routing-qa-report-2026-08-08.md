# Gate 1 Routing QA Report — 2026-08-08

## Task Q0 — Re-Pin

### Q0.1 — Evidence file git pin
```
git -C /Users/marklehn/Developer/GitHub/lessons-forge log -1 --oneline -- knowledge/development/gate1-routing-dev-log-2026-08-08.md knowledge/development/gate1-pre-dump-2026-08-08.txt knowledge/development/gate1-post-dump-2026-08-08.txt
9f4bcb4 [326] gate1 routing DEV — proposals 223–273 (44 accepted/codify, 7 reference/backlog)
```
**Gate: PASS — newest commit is Step 1's (`9f4bcb4`).**

### Q0.2 — Proposed count post-state
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';"
0
```
**Gate: PASS (0 — no verdict-window write re-opened the batch).**

---

## Item 1 — Read-Only Re-Verification (from DB)

### 1(a) — Proposed = 0
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';"
0
```
**PASS.**

### 1(b) — Accepted/codify ids diffed against CODIFY-44
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT id FROM lesson_proposals WHERE status='accepted' AND route='codify' AND id BETWEEN 223 AND 273 ORDER BY id;"
223
224
225
226
227
228
229
230
231
232
234
235
236
237
239
240
241
242
243
244
245
248
249
250
251
252
253
254
255
256
257
260
261
262
263
264
265
266
267
268
269
270
272
273
```
```
diff /tmp/codify44-expected.txt /tmp/codify44-actual.txt
(no output — exact match)
```
**PASS — 44 ids, exact match with CODIFY-44 list.**

### 1(c) — Reference/backlog ids diffed against PARK-7
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT id FROM lesson_proposals WHERE status='reference' AND route='backlog' AND id BETWEEN 223 AND 273 ORDER BY id;"
233
238
246
247
258
259
271
```
```
diff /tmp/park7-expected.txt /tmp/park7-actual.txt
(no output — exact match)
```
**PASS — 7 ids, exact match with PARK-7 list.**

### 1(d) — All 51 rows carry status_updated_by='ceo' and status_updated_at matching transaction time
Transaction timestamp from dev log: `2026-08-09T01:20:01Z`
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE id BETWEEN 223 AND 273 AND status_updated_by='ceo' AND status_updated_at='2026-08-09T01:20:01Z';"
51
```
```
sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT id, status_updated_by, status_updated_at FROM lesson_proposals WHERE id BETWEEN 223 AND 273 AND (status_updated_by != 'ceo' OR status_updated_at != '2026-08-09T01:20:01Z') ORDER BY id;"
(no output — zero mismatches)
```
**PASS — all 51 rows carry `status_updated_by='ceo'` and `status_updated_at='2026-08-09T01:20:01Z'` (window test against the recorded transaction time, not a calendar-day test).**

### 1(e) — Consumer check (get_unclassified_entries equivalent)
```sql
SELECT e.id FROM lesson_entries e
WHERE NOT EXISTS (
  SELECT 1 FROM lesson_proposals p
  WHERE p.entry_id = e.id AND p.status != 'stale'
) ORDER BY e.id;
```
```
(no output — empty result set)
```
Entry ids associated with proposals 223–273:
```sql
SELECT DISTINCT p.entry_id FROM lesson_proposals p
WHERE p.id BETWEEN 223 AND 273 ORDER BY p.entry_id;
```
```
215
216
217
...
265
```
(51 entry ids spanning 215–265.)

**PASS — unclassified entries list is empty. No entry in the routed batch's entry set re-queued. Both `accepted` and `reference` proposals keep their entries dispositioned per the helper's docstring (`status != 'stale'` excludes both).**

---

## Item 2 — Untouched-Population Proof (independently re-derived)

### QA dump
- **Path:** `knowledge/qa/gate1-qa-dump-2026-08-08.txt`
- **Line count:** 273

### Diff against Step-1 PRE-dump
```
diff knowledge/development/gate1-pre-dump-2026-08-08.txt knowledge/qa/gate1-qa-dump-2026-08-08.txt
223,273c223,273
< 223|proposed|-|-
< 224|proposed|-|-
< 225|proposed|-|-
< 226|proposed|-|-
< 227|proposed|-|-
< 228|proposed|-|-
< 229|proposed|-|-
< 230|proposed|-|-
< 231|proposed|-|-
< 232|proposed|-|-
< 233|proposed|-|-
< 234|proposed|-|-
< 235|proposed|-|-
< 236|proposed|-|-
< 237|proposed|-|-
< 238|proposed|-|-
< 239|proposed|-|-
< 240|proposed|-|-
< 241|proposed|-|-
< 242|proposed|-|-
< 243|proposed|-|-
< 244|proposed|-|-
< 245|proposed|-|-
< 246|proposed|-|-
< 247|proposed|-|-
< 248|proposed|-|-
< 249|proposed|-|-
< 250|proposed|-|-
< 251|proposed|-|-
< 252|proposed|-|-
< 253|proposed|-|-
< 254|proposed|-|-
< 255|proposed|-|-
< 256|proposed|-|-
< 257|proposed|-|-
< 258|proposed|-|-
< 259|proposed|-|-
< 260|proposed|-|-
< 261|proposed|-|-
< 262|proposed|-|-
< 263|proposed|-|-
< 264|proposed|-|-
< 265|proposed|-|-
< 266|proposed|-|-
< 267|proposed|-|-
< 268|proposed|-|-
< 269|proposed|-|-
< 270|proposed|-|-
< 271|proposed|-|-
< 272|proposed|-|-
< 273|proposed|-|-
---
> 223|accepted|codify|ceo
> 224|accepted|codify|ceo
> 225|accepted|codify|ceo
> 226|accepted|codify|ceo
> 227|accepted|codify|ceo
> 228|accepted|codify|ceo
> 229|accepted|codify|ceo
> 230|accepted|codify|ceo
> 231|accepted|codify|ceo
> 232|accepted|codify|ceo
> 233|reference|backlog|ceo
> 234|accepted|codify|ceo
> 235|accepted|codify|ceo
> 236|accepted|codify|ceo
> 237|accepted|codify|ceo
> 238|reference|backlog|ceo
> 239|accepted|codify|ceo
> 240|accepted|codify|ceo
> 241|accepted|codify|ceo
> 242|accepted|codify|ceo
> 243|accepted|codify|ceo
> 244|accepted|codify|ceo
> 245|accepted|codify|ceo
> 246|reference|backlog|ceo
> 247|reference|backlog|ceo
> 248|accepted|codify|ceo
> 249|accepted|codify|ceo
> 250|accepted|codify|ceo
> 251|accepted|codify|ceo
> 252|accepted|codify|ceo
> 253|accepted|codify|ceo
> 254|accepted|codify|ceo
> 255|accepted|codify|ceo
> 256|accepted|codify|ceo
> 257|accepted|codify|ceo
> 258|reference|backlog|ceo
> 259|reference|backlog|ceo
> 260|accepted|codify|ceo
> 261|accepted|codify|ceo
> 262|accepted|codify|ceo
> 263|accepted|codify|ceo
> 264|accepted|codify|ceo
> 265|accepted|codify|ceo
> 266|accepted|codify|ceo
> 267|accepted|codify|ceo
> 268|accepted|codify|ceo
> 269|accepted|codify|ceo
> 270|accepted|codify|ceo
> 271|reference|backlog|ceo
> 272|accepted|codify|ceo
> 273|accepted|codify|ceo
```

### Partition
**(i) Within ids 223–273:** exactly 51 changes — 51 old lines (`proposed|-|-`) replaced by 51 new lines matching the routing spec (44 `accepted|codify|ceo` + 7 `reference|backlog|ceo`). No foreign writes to the routed batch.

**(ii) Outside ids 223–273:** ZERO differing lines. No concurrent activity touched any row outside the batch during the verdict window.

**PASS.**

---

## Item 3 — Test Suite

### Rule 21 justification (re-verified, not inherited)
The repo's suite is the single module `src/test_lessons_forge.py`. Running `pytest src/` is simultaneously targeted and full — the sixth data point of the CEO-tracked single-module precedent.

### Results
```
.......................................................                  [100%]
55 passed in 0.10s
```
**55 passed, 0 failed.** Actual (55) matches 311's measured expected (55). Full RAW output deposited at `knowledge/qa/full-suite.txt`.

---

## Item 4 — QA Verification Receipt

| # | Check | Status |
|---|-------|--------|
| Q0.1 | Evidence file git pin — newest commit is Step 1's (`9f4bcb4`) | ✅ |
| Q0.2 | Proposed count = 0 (post-state) | ✅ |
| 1a | Proposed = 0 (DB re-read) | ✅ |
| 1b | Accepted/codify ids exact match with CODIFY-44 (44 ids, diff empty) | ✅ |
| 1c | Reference/backlog ids exact match with PARK-7 (7 ids, diff empty) | ✅ |
| 1d | All 51 rows carry `status_updated_by='ceo'` and `status_updated_at='2026-08-09T01:20:01Z'` (window test) | ✅ |
| 1e | Consumer check — unclassified entries empty, no re-queued entries | ✅ |
| 2 | Untouched-population proof — 51 changes within 223–273, zero outside | ✅ |
| 3 | Test suite — 55 passed, 0 failed (matches 311's measured 55) | ✅ |

### Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: knowledge/qa/
Files verified: 2
```

---

### Status

**Complete**

### Deposits
- `knowledge/qa/gate1-routing-qa-report-2026-08-08.md`
- `knowledge/qa/gate1-qa-dump-2026-08-08.txt`
- `knowledge/qa/full-suite.txt`

### Ledger Updates

#### Forward Register
NONE

#### Prompt Feedback

No prompt feedback.
