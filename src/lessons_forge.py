"""
Forge — Lessons Forge module.

Phase 1A: parser and ingestion for LESSONS.md entries.
Phase 1B: duplicate detection, insert_proposal helper, orchestrator,
          report generator.

Segments by dated headings, extracts tags, computes content hashes,
and upserts into the lesson_entries table with idempotency.
Detects duplicates against reference files via tag keyword overlap
and heading substring matching. Orchestrates full cycle and generates
human-readable reports.
"""
from __future__ import annotations

import hashlib
import os
import re
import sqlite3
import subprocess
from datetime import datetime, timezone


# Heading patterns
_DATED_HEADING_RE = re.compile(r"^## (20\d\d.+)")
_ARCHIVED_HEADING_RE = re.compile(r"^## Archived")
_TAG_LINE_RE = re.compile(r"^\*\*Tags?:\*\*\s*(.+)", re.IGNORECASE)


def parse_lessons_md(path: str) -> list[dict]:
    """
    Parse LESSONS.md into a list of entry dicts.

    Segments by dated heading pattern (^## 20\\d\\d). Stops at ^## Archived.
    Extracts tags from **Tag:** / **Tags:** lines. Computes SHA-256 content_hash
    over raw_content body (excluding the heading line).

    Returns:
        List of dicts with keys: source_heading, entry_date, raw_content,
        content_hash, tags.
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entries: list[dict] = []
    current_heading: str | None = None
    current_body_lines: list[str] = []

    def _flush():
        if current_heading is None:
            return
        raw_content = "".join(current_body_lines)
        # Extract tags
        tags = None
        for line in current_body_lines:
            m = _TAG_LINE_RE.match(line.strip())
            if m:
                tags = m.group(1).strip()
                break
        # Extract date (first 10 chars of heading text, e.g. "2026-04-14")
        entry_date = None
        if len(current_heading) >= 10:
            candidate = current_heading[:10]
            if re.match(r"^\d{4}-\d{2}-\d{2}$", candidate):
                entry_date = candidate
        content_hash = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
        entries.append({
            "source_heading": current_heading,
            "entry_date": entry_date,
            "raw_content": raw_content,
            "content_hash": content_hash,
            "tags": tags,
        })

    for line in lines:
        # Stop at Archived section
        if _ARCHIVED_HEADING_RE.match(line):
            _flush()
            break

        # Check for dated heading
        m = _DATED_HEADING_RE.match(line)
        if m:
            _flush()
            current_heading = m.group(1).strip()
            current_body_lines = []
        elif current_heading is not None:
            current_body_lines.append(line)
    else:
        # EOF without hitting Archived
        _flush()

    return entries


def ingest_lesson_entries(conn: sqlite3.Connection, entries: list[dict],
                          source_file: str = "LESSONS.md") -> dict:
    """
    Upsert parsed lesson entries into the lesson_entries table.

    Idempotency: lookup by (source_file, source_heading). If hash unchanged,
    skip. If hash changed, update and mark downstream proposals stale.
    Does NOT call conn.commit().

    Returns:
        Dict with keys: inserted, updated, unchanged, stale_proposals_marked.
    """
    now = datetime.now(timezone.utc).isoformat()
    result = {"inserted": 0, "updated": 0, "unchanged": 0, "stale_proposals_marked": 0}

    for entry in entries:
        row = conn.execute(
            "SELECT id, content_hash FROM lesson_entries "
            "WHERE source_file = ? AND source_heading = ?",
            (source_file, entry["source_heading"]),
        ).fetchone()

        if row is None:
            # New entry — INSERT
            conn.execute(
                "INSERT INTO lesson_entries "
                "(source_file, source_heading, entry_date, raw_content, content_hash, tags, ingested_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (source_file, entry["source_heading"], entry["entry_date"],
                 entry["raw_content"], entry["content_hash"], entry["tags"], now),
            )
            result["inserted"] += 1
        elif row[1] == entry["content_hash"]:
            # Unchanged — skip
            result["unchanged"] += 1
        else:
            # Changed — UPDATE
            entry_id = row[0]
            conn.execute(
                "UPDATE lesson_entries "
                "SET raw_content = ?, content_hash = ?, tags = ?, entry_date = ?, ingested_at = ? "
                "WHERE id = ?",
                (entry["raw_content"], entry["content_hash"], entry["tags"],
                 entry["entry_date"], now, entry_id),
            )
            result["updated"] += 1

            # Mark downstream proposals as stale
            cur = conn.execute(
                "UPDATE lesson_proposals SET status = 'stale', "
                "status_updated_at = ?, status_updated_by = 'auto' "
                "WHERE entry_id = ? AND status != 'stale'",
                (now, entry_id),
            )
            result["stale_proposals_marked"] += cur.rowcount

    return result


_VALID_ROUTES = frozenset(('codify', 'backlog', 'reference'))


def insert_proposal(conn: sqlite3.Connection, entry_id: int, category: str,
                    suggested_action: str, reasoning: str, confidence: str,
                    status: str = 'proposed', target_layer: str | None = None,
                    target_artifact: str | None = None,
                    duplicate_of: int | None = None,
                    subcategory: str | None = None,
                    route: str | None = None) -> int:
    """
    Insert a single proposal row into the lesson_proposals table.

    Thin DB-insert helper. Does NOT call conn.commit() — callers manage
    transactions. Category, confidence, status, and target_layer values
    are validated implicitly by SQLite CHECK constraints on the
    lesson_proposals table (see Phase 1A schema DDL).

    Args:
        conn: SQLite connection with lesson_proposals table created.
        entry_id: FK to lesson_entries(id). Must reference an existing entry.
        category: One of: structural, instrumentation, governance_rule,
                  language, narrative, duplicate.
        suggested_action: Natural-language recommendation for this entry.
        reasoning: Classifier's reasoning for the category assignment.
        confidence: One of: low, medium, high.
        status: Proposal status. Default 'proposed'. One of: proposed,
                accepted, rejected, ambiguous, stale, superseded, implemented,
                reference.
        target_layer: Optional routing layer. One of: structure, governance,
                      language, none. NULL if not determined.
        target_artifact: Optional target file (e.g. "PLANNER_TEMPLATE.md").
        duplicate_of: Optional identifier for category='duplicate' entries.
        subcategory: Reserved for Phase 2; pass None in Phase 1.

    Returns:
        int: The id (primary key) of the newly-inserted proposal row.

    Raises:
        sqlite3.IntegrityError: If category/status/confidence/target_layer
            violates CHECK constraints, or if entry_id doesn't reference
            an existing lesson_entries row (FK violation).
    """
    if route is not None and route not in _VALID_ROUTES:
        raise ValueError(f"route must be one of {sorted(_VALID_ROUTES)} or None, got {route!r}")
    now = datetime.now(timezone.utc).isoformat()
    cur = conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, subcategory, suggested_action, reasoning, "
        "confidence, status, target_layer, target_artifact, duplicate_of, route, proposed_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (entry_id, category, subcategory, suggested_action, reasoning,
         confidence, status, target_layer, target_artifact, duplicate_of, route, now),
    )
    return cur.lastrowid


def set_proposal_route(conn: sqlite3.Connection, proposal_id: int,
                       route: str | None) -> None:
    """Set the route on an existing proposal (disposition-time capture)."""
    if route is not None and route not in _VALID_ROUTES:
        raise ValueError(f"route must be one of {sorted(_VALID_ROUTES)} or None, got {route!r}")
    conn.execute(
        "UPDATE lesson_proposals SET route = ? WHERE id = ?",
        (route, proposal_id),
    )


def get_unclassified_entries(conn: sqlite3.Connection) -> list[int]:
    """Return entry IDs that need (re)classification this cycle.

    An entry needs classification if it has NO proposal whose status is
    anything other than 'stale'. This includes (a) entries with no proposal
    at all and (b) entries whose only proposal(s) are 'stale' — the state the
    ingestion update path leaves an edited entry in (old proposal staled, entry
    requeued). Entries with a 'proposed'/'accepted'/'implemented'/'rejected'/
    'superseded' proposal are excluded (active or dispositioned).

    This is the canonical work list. As of 2026-07-02, run_full_lessons_cycle()
    delegates its needs_classification field to this helper, so the two are
    consistent. This helper remains the canonical source (Rule #47).
    Do NOT use `NOT EXISTS (any proposal)` — it drops stale-only entries and
    silently skips re-queued edits.
    """
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT e.id FROM lesson_entries e "
        "WHERE NOT EXISTS ("
        "  SELECT 1 FROM lesson_proposals p "
        "  WHERE p.entry_id = e.id AND p.status != 'stale'"
        ") ORDER BY e.id"
    ).fetchall()
    return [r[0] for r in rows]


_EM_DASH_SEP = " \u2014 "


def detect_duplicates(conn: sqlite3.Connection, entry_ids: list[int],
                      reference_files: list[str] | None = None) -> list[dict]:
    """
    Detect duplicate lesson entries by scanning reference files.

    For each entry ID, reads the entry row from lesson_entries, then scans
    each reference file for two match types:
      1. Structural tag overlap: each tag from the entry's comma-separated tags
         column is checked against the set of tags extracted from **Tag:** /
         **Tags:** lines in the reference file. Reference files without
         structured tag lines yield no tag matches (clean no-op).
      2. Exact substring match on the entry's source_heading descriptive title
         (portion after the date + em-dash separator) in the reference file
         content, case-insensitive.

    First match wins: if an entry matches any reference file via either
    criterion, it is included in the result once. Non-matched entries are
    absent from the returned list.

    Reference files are read via subprocess.run(["cat", path]) rather than
    open(). Rationale: reference files live outside the Forge project scope;
    bash subprocess avoids Python filesystem coupling to paths that may move.

    Args:
        conn: SQLite connection with lesson_entries table populated.
        entry_ids: List of lesson_entries.id values to check. May be empty.
        reference_files: List of absolute paths to reference files to scan.
            Defaults to ["/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md"]
            if None.

    Returns:
        List of dicts, one per matched entry:
          {"entry_id": int, "matched_source": str, "match_reason": str}
    """
    if not entry_ids:
        return []

    if reference_files is None:
        reference_files = ["/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md"]

    # Cache reference file contents and structured tag sets (read each file once)
    ref_contents: dict[str, str] = {}
    ref_tag_sets: dict[str, set[str]] = {}
    for ref_path in reference_files:
        try:
            result = subprocess.run(
                ["cat", ref_path], capture_output=True, text=True, check=True,
            )
            ref_contents[ref_path] = result.stdout.lower()
            # Extract structured tags from **Tag:**/**Tags:** lines
            tags_found: set[str] = set()
            for line in result.stdout.splitlines():
                m = _TAG_LINE_RE.match(line.strip())
                if m:
                    tags_found.update(
                        t.strip().lower() for t in m.group(1).split(",")
                    )
            ref_tag_sets[ref_path] = tags_found
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    if not ref_contents:
        return []

    matches: list[dict] = []

    for eid in entry_ids:
        row = conn.execute(
            "SELECT source_heading, tags FROM lesson_entries WHERE id = ?",
            (eid,),
        ).fetchone()
        if row is None:
            continue

        source_heading, tags = row
        matched = False

        # Extract descriptive title from heading
        if _EM_DASH_SEP in source_heading:
            heading_title = source_heading.split(_EM_DASH_SEP, 1)[1].strip()
        else:
            heading_title = source_heading.strip()
        heading_title_lower = heading_title.lower()

        # Extract tags
        tag_list: list[str] = []
        if tags:
            tag_list = [t.strip() for t in tags.split(",") if t.strip()]

        for ref_path, ref_lower in ref_contents.items():
            if matched:
                break

            # Criterion 1: exact tag-set overlap (structural **Tag:** lines)
            for tag in tag_list:
                if tag.lower() in ref_tag_sets.get(ref_path, set()):
                    matches.append({
                        "entry_id": eid,
                        "matched_source": ref_path,
                        "match_reason": f"tag_match: {tag}",
                    })
                    matched = True
                    break

            if matched:
                break

            # Criterion 2: heading substring match
            if heading_title_lower and heading_title_lower in ref_lower:
                matches.append({
                    "entry_id": eid,
                    "matched_source": ref_path,
                    "match_reason": "heading_substring_match",
                })
                matched = True

    return matches


_OVERLAP_STOP = frozenset({
    'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can',
    'has', 'had', 'have', 'was', 'were', 'been', 'will', 'may',
    'shall', 'should', 'would', 'could', 'must', 'need',
    'that', 'this', 'what', 'with', 'when', 'from', 'into',
    'they', 'them', 'than', 'their', 'there', 'these', 'those',
    'which', 'where', 'while', 'about', 'after', 'before',
    'between', 'does', 'doing', 'during', 'each', 'every',
    'more', 'most', 'other', 'some', 'such', 'only', 'also',
    'just', 'very', 'already', 'being', 'add', 'new', 'any',
})

_OVERLAP_WORD_RE = re.compile(r'[a-z]{3,}')


def _tokenize_for_overlap(text: str) -> set[str]:
    """Extract lowercase keyword tokens (3+ alpha chars, stop-words removed)."""
    return {w for w in _OVERLAP_WORD_RE.findall(text.lower())
            if w not in _OVERLAP_STOP}


def detect_recently_implemented_overlaps(
    conn: sqlite3.Connection,
    entry_ids: list[int],
    recency_days: int = 45,
) -> list[dict]:
    """
    Detect entries overlapping recently-implemented proposals (advisory-only).

    For each entry_id, computes keyword overlap between the entry's heading/tags
    and each recently-implemented proposal's suggested_action/reasoning/category/
    target_artifact. Returns matches above a recall-oriented threshold.

    Read-only: never writes to the DB.

    Args:
        conn: SQLite connection with lesson_entries and lesson_proposals tables.
        entry_ids: List of lesson_entries.id values to check. May be empty.
        recency_days: How far back to look for implemented proposals (default 45).

    Returns:
        List of dicts, one per match:
          {"entry_id": int, "proposal_id": int, "implemented_at": str,
           "overlap_reason": str}
    """
    if not entry_ids:
        return []

    impl_rows = conn.execute(
        "SELECT id, suggested_action, reasoning, category, target_artifact, "
        "status_updated_at FROM lesson_proposals "
        "WHERE status = 'implemented' "
        "AND status_updated_at >= date('now', '-' || ? || ' days')",
        (recency_days,),
    ).fetchall()

    if not impl_rows:
        return []

    impl_data = []
    for pid, sa, reasoning, cat, ta, impl_at in impl_rows:
        kw = _tokenize_for_overlap(sa or '')
        kw |= _tokenize_for_overlap(reasoning or '')
        if cat:
            kw |= _tokenize_for_overlap(cat)
        if ta:
            kw |= _tokenize_for_overlap(ta)
        full_text = ' '.join(filter(None, [sa, reasoning, cat, ta])).lower()
        impl_data.append((pid, kw, full_text, impl_at))

    results: list[dict] = []

    for eid in entry_ids:
        row = conn.execute(
            "SELECT source_heading, tags FROM lesson_entries WHERE id = ?",
            (eid,),
        ).fetchone()
        if row is None:
            continue

        source_heading, tags = row

        entry_kw: set[str] = set()
        entry_tags: list[str] = []
        if tags:
            for t in tags.split(','):
                t_clean = t.strip().lower().strip('`')
                if t_clean:
                    entry_tags.append(t_clean)
                    entry_kw |= _tokenize_for_overlap(t_clean)
        if _EM_DASH_SEP in source_heading:
            heading_text = source_heading.split(_EM_DASH_SEP, 1)[1]
        else:
            heading_text = source_heading
        entry_kw |= _tokenize_for_overlap(heading_text)

        if not entry_kw:
            continue

        for pid, prop_kw, prop_full_text, impl_at in impl_data:
            if not prop_kw:
                continue

            intersection = entry_kw & prop_kw
            if not intersection:
                continue

            union = entry_kw | prop_kw
            jaccard = len(intersection) / len(union)

            tag_hits = [t for t in entry_tags if t in prop_full_text]
            score = jaccard
            if tag_hits:
                score = max(score, 0.15)

            if score < 0.08:
                continue

            parts: list[str] = []
            if tag_hits:
                parts.append(f"tag overlap: {', '.join(tag_hits[:3])}")
            kw_sample = sorted(intersection)[:5]
            if kw_sample:
                parts.append(f"keyword overlap: {', '.join(kw_sample)}")
            reason = '; '.join(parts) if parts else f"jaccard={jaccard:.2f}"

            results.append({
                "entry_id": eid,
                "proposal_id": pid,
                "implemented_at": impl_at or "unknown",
                "overlap_reason": reason,
            })

    return results


def run_full_lessons_cycle(conn: sqlite3.Connection,
                           lessons_md_path: str = "/Users/marklehn/Developer/GitHub/LESSONS.md") -> dict:
    """
    Execute the deterministic steps of a Lessons Forge cycle.

    Per ADR-002 (amended 2026-04-23), this function runs:
      1. parse_lessons_md(lessons_md_path) — segment LESSONS.md into entries
      2. ingest_lesson_entries(conn, entries) — upsert into lesson_entries
      3. detect_duplicates(conn, candidate_ids) — scan reference inputs
      4. For each detected duplicate, insert a proposal via insert_proposal()
         with category='duplicate', status='proposed', confidence='high'.

    Classification (the agent-driven step) is NOT executed here. The returned
    dict includes needs_classification — the list of entry IDs that require
    agent-driven classification in a subsequent cycle plan step.

    Idempotency: before inserting a duplicate proposal, checks whether an
    existing proposal with category='duplicate' already exists for that
    entry_id. If so, skips insertion (no duplicate-of-duplicate).

    Does NOT call conn.commit() — caller is responsible for committing.

    Args:
        conn: SQLite connection with lesson_entries and lesson_proposals
              tables created (via db.init_db).
        lessons_md_path: Absolute path to LESSONS.md. Defaults to the
                         governance root location.

    Returns:
        dict with keys:
          - ingested_count: int — entries newly inserted this cycle
          - updated_count: int — entries updated (content changed)
          - unchanged_count: int — entries unchanged (hash match, skipped)
          - duplicates_marked_count: int — new duplicate proposals inserted
          - needs_classification: list[int] — entry IDs requiring classification,
            computed via get_unclassified_entries(conn) after duplicate-proposal
            insertion. DB-wide (not parse-scoped); matches the canonical Rule #47
            work list.
          - cycle_timestamp: str — ISO 8601 UTC timestamp of cycle execution
    """
    cycle_timestamp = datetime.now(timezone.utc).isoformat()

    # Step 1: parse
    entries = parse_lessons_md(lessons_md_path)

    # Step 2: ingest
    ingestion = ingest_lesson_entries(conn, entries)

    # Collect all entry IDs (not just inserted/updated) for duplicate check
    candidate_ids = []
    for entry in entries:
        row = conn.execute(
            "SELECT id FROM lesson_entries WHERE source_file = ? AND source_heading = ?",
            ("LESSONS.md", entry["source_heading"]),
        ).fetchone()
        if row:
            candidate_ids.append(row[0])

    # Step 3: detect duplicates
    duplicates = detect_duplicates(conn, candidate_ids)

    # Step 4: insert duplicate proposals with idempotency check
    duplicates_marked_count = 0
    for match in duplicates:
        eid = match["entry_id"]
        # Idempotency: skip if a duplicate proposal already exists
        existing = conn.execute(
            "SELECT 1 FROM lesson_proposals WHERE entry_id = ? AND category = 'duplicate'",
            (eid,),
        ).fetchone()
        if existing:
            continue
        insert_proposal(
            conn,
            entry_id=eid,
            category="duplicate",
            suggested_action=f"Already captured in {match['matched_source']}",
            reasoning=match["match_reason"],
            confidence="high",
            duplicate_of=None,
        )
        duplicates_marked_count += 1

    # Step 5: detect recently-implemented overlaps (advisory-only, read-only)
    recently_implemented_overlaps = detect_recently_implemented_overlaps(
        conn, candidate_ids,
    )

    needs_classification = get_unclassified_entries(conn)

    return {
        "ingested_count": ingestion["inserted"],
        "updated_count": ingestion["updated"],
        "unchanged_count": ingestion["unchanged"],
        "duplicates_marked_count": duplicates_marked_count,
        "needs_classification": needs_classification,
        "recently_implemented_overlaps": recently_implemented_overlaps,
        "cycle_timestamp": cycle_timestamp,
    }


def generate_lessons_report(conn: sqlite3.Connection, cycle_date: str,
                            output_dir: str = "reports") -> str:
    """
    Generate a human-readable lessons report from proposals.

    Queries lesson_proposals WHERE status IN ('proposed', 'ambiguous') joined
    with lesson_entries. Groups proposals by category. Writes a markdown
    report to {output_dir}/lessons-report-{cycle_date}.md.

    Creates output_dir if it doesn't exist. Returns the absolute path of
    the written report.

    Args:
        conn: SQLite connection with lesson_entries and lesson_proposals
              tables populated.
        cycle_date: Date string for the report filename (e.g. "2026-04-23").
        output_dir: Directory to write the report file. Default "reports"
                    (relative to CWD, which is the forge root).

    Returns:
        str: Absolute path of the written report file.
    """
    rows = conn.execute(
        "SELECT p.category, p.suggested_action, p.reasoning, p.confidence, "
        "p.duplicate_of, e.source_heading, e.entry_date, p.route, p.entry_id "
        "FROM lesson_proposals p "
        "JOIN lesson_entries e ON p.entry_id = e.id "
        "WHERE p.status IN ('proposed', 'ambiguous') "
        "ORDER BY p.category, e.entry_date DESC",
    ).fetchall()

    overlap_map: dict[int, list[dict]] = {}
    if rows:
        entry_ids_set = list({r[-1] for r in rows})
        for ov in detect_recently_implemented_overlaps(conn, entry_ids_set):
            overlap_map.setdefault(ov["entry_id"], []).append(ov)

    lines: list[str] = []
    lines.append(f"# Lessons Report \u2014 {cycle_date}\n")
    lines.append("")

    if not rows:
        lines.append("## Summary\n")
        lines.append("")
        lines.append("No proposals pending review.\n")
    else:
        # Group by category
        grouped: dict[str, list] = {}
        for row in rows:
            cat = row[0]
            grouped.setdefault(cat, []).append(row)

        # Summary
        lines.append("## Summary\n")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|---|---|")
        for cat in sorted(grouped.keys()):
            lines.append(f"| {cat} | {len(grouped[cat])} |")
        lines.append("")
        total = sum(len(v) for v in grouped.values())
        lines.append(f"**Total proposals:** {total}\n")
        lines.append("")

        # Per-category sections
        for cat in sorted(grouped.keys()):
            lines.append(f"## {cat.replace('_', ' ').title()}\n")
            lines.append("")
            for row in grouped[cat]:
                _, suggested_action, reasoning, confidence, duplicate_of, source_heading, entry_date, route, entry_id = row
                lines.append(f"### {source_heading}\n")
                lines.append("")
                lines.append(f"- **Suggested action:** {suggested_action}")
                lines.append(f"- **Reasoning:** {reasoning}")
                lines.append(f"- **Confidence:** {confidence}")
                if route is not None:
                    lines.append(f"- **Route:** {route}")
                if cat == "duplicate" and duplicate_of is not None:
                    lines.append(f"- **Duplicate of:** {duplicate_of}")
                for ov in overlap_map.get(entry_id, []):
                    lines.append(
                        f"- ⚠️ **Recently-implemented overlap:** "
                        f"proposal #{ov['proposal_id']} "
                        f"(implemented {ov['implemented_at']}) "
                        f"— {ov['overlap_reason']} "
                        f"— verify not already subsumed before codifying."
                    )
                lines.append("")

    content = "\n".join(lines)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"lessons-report-{cycle_date}.md")
    with open(output_path, "w") as f:
        f.write(content)

    return os.path.abspath(output_path)
