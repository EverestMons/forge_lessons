"""
Forge — Lessons Forge module tests.

Step 2: schema verification tests for lesson_entries and lesson_proposals tables.
Step 3: parser and ingestion tests for parse_lessons_md and ingest_lesson_entries.
"""
from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import db
from src.lessons_forge import (
    parse_lessons_md, ingest_lesson_entries, insert_proposal,
    set_proposal_route,
    get_unclassified_entries, detect_duplicates,
    run_full_lessons_cycle,
    generate_lessons_report,
    _normalize_for_hash,
    _TERMINAL_STATUSES,
)


def _setup() -> sqlite3.Connection:
    """Create in-memory DB with full schema."""
    conn = sqlite3.connect(":memory:")
    db.init_db(conn)
    return conn


def test_lesson_entries_schema():
    """PRAGMA table_info on lesson_entries — correct columns, types, NOT NULL."""
    conn = _setup()
    rows = conn.execute("PRAGMA table_info(lesson_entries)").fetchall()
    cols = {row[1]: row for row in rows}

    assert "id" in cols
    assert "source_file" in cols
    assert "source_heading" in cols
    assert "entry_date" in cols
    assert "raw_content" in cols
    assert "content_hash" in cols
    assert "tags" in cols
    assert "ingested_at" in cols

    # NOT NULL checks (PRAGMA column index 3 = notnull)
    assert cols["source_file"][3] == 1, "source_file should be NOT NULL"
    assert cols["source_heading"][3] == 1, "source_heading should be NOT NULL"
    assert cols["raw_content"][3] == 1, "raw_content should be NOT NULL"
    assert cols["content_hash"][3] == 1, "content_hash should be NOT NULL"
    assert cols["ingested_at"][3] == 1, "ingested_at should be NOT NULL"
    assert cols["entry_date"][3] == 0, "entry_date should be nullable"
    assert cols["tags"][3] == 0, "tags should be nullable"

    conn.close()


def test_lesson_proposals_schema():
    """PRAGMA table_info on lesson_proposals — correct columns, FK to lesson_entries."""
    conn = _setup()
    rows = conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()
    cols = {row[1]: row for row in rows}

    expected_cols = [
        "id", "entry_id", "category", "subcategory", "suggested_action",
        "reasoning", "confidence", "status", "target_layer", "target_artifact",
        "duplicate_of", "proposed_at", "status_updated_at", "status_updated_by",
    ]
    for col_name in expected_cols:
        assert col_name in cols, f"Missing column: {col_name}"

    # NOT NULL checks
    assert cols["entry_id"][3] == 1
    assert cols["category"][3] == 1
    assert cols["suggested_action"][3] == 1
    assert cols["reasoning"][3] == 1
    assert cols["confidence"][3] == 1
    assert cols["status"][3] == 1
    assert cols["proposed_at"][3] == 1

    # Nullable columns
    assert cols["subcategory"][3] == 0
    assert cols["target_layer"][3] == 0
    assert cols["target_artifact"][3] == 0
    assert cols["duplicate_of"][3] == 0
    assert cols["status_updated_at"][3] == 0
    assert cols["status_updated_by"][3] == 0

    # FK enforcement: inserting a proposal with nonexistent entry_id should fail
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, proposed_at) "
            "VALUES (99999, 'structural', 'action', 'reason', 'high', '2026-04-23')"
        )

    conn.close()


def test_check_constraints_reject_invalid():
    """INSERT into lesson_proposals with invalid category/status/confidence raises IntegrityError."""
    conn = _setup()

    # Seed a valid lesson_entries row for FK
    conn.execute(
        "INSERT INTO lesson_entries (source_file, source_heading, raw_content, content_hash, ingested_at) "
        "VALUES ('LESSONS.md', '2026-04-01 — Test', 'content', 'hash123', '2026-04-23')"
    )
    entry_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Invalid category
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, proposed_at) "
            "VALUES (?, 'bogus_category', 'action', 'reason', 'high', '2026-04-23')",
            (entry_id,),
        )

    # Invalid confidence
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'ultra', '2026-04-23')",
            (entry_id,),
        )

    # Invalid status
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'invalid_status', '2026-04-23')",
            (entry_id,),
        )

    # Invalid target_layer
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, target_layer, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'bad_layer', '2026-04-23')",
            (entry_id,),
        )

    # Invalid status_updated_by
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, status_updated_by, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'robot', '2026-04-23')",
            (entry_id,),
        )

    # Valid insert should succeed
    conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, suggested_action, reasoning, confidence, proposed_at) "
        "VALUES (?, 'structural', 'action', 'reason', 'high', '2026-04-23')",
        (entry_id,),
    )

    conn.close()


# --- Synthetic LESSONS.md fixture ---

SYNTHETIC_LESSONS = """\
# Eluvian Lessons Notepad
**Purpose:** Test fixture.

---

## Active entries (awaiting categorization or integration)

## 2026-04-10 — First test lesson about planning

**Source:** Unit test fixture.

**Lesson:** Plans should be small and focused.

**Tag:** planner-discipline, governance-meta

---

## 2026-04-12 — Second lesson with no tags

**Source:** Another test fixture.

**Lesson:** Agents need clear instructions.

---

## Archived entries (integrated into permanent homes)

## 2026-03-01 — Archived lesson that should NOT appear

**Source:** Should be filtered out by parser.

**Tag:** archived-tag
"""


def _write_fixture(content: str) -> str:
    """Write content to a temp file and return the path."""
    fd, path = tempfile.mkstemp(suffix=".md", prefix="test_lessons_")
    os.write(fd, content.encode("utf-8"))
    os.close(fd)
    return path


# --- Parser tests ---

def test_parse_lessons_md_basic():
    """Parser returns 2 entries from synthetic fixture with correct headings and dates."""
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        assert len(entries) == 2

        assert entries[0]["source_heading"].startswith("2026-04-10")
        assert entries[0]["entry_date"] == "2026-04-10"
        assert "Plans should be small" in entries[0]["raw_content"]

        assert entries[1]["source_heading"].startswith("2026-04-12")
        assert entries[1]["entry_date"] == "2026-04-12"
        assert "Agents need clear instructions" in entries[1]["raw_content"]
    finally:
        os.unlink(path)


def test_parse_lessons_md_tags():
    """Parser extracts tags correctly; entries without tags get None."""
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        assert entries[0]["tags"] == "planner-discipline, governance-meta"
        assert entries[1]["tags"] is None
    finally:
        os.unlink(path)


def test_parse_lessons_md_archived_stop():
    """Parser stops at ## Archived — archived entries are not returned."""
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        headings = [e["source_heading"] for e in entries]
        assert not any("Archived lesson" in h for h in headings)
        assert len(entries) == 2
    finally:
        os.unlink(path)


def test_parse_lessons_md_hash_deterministic():
    """Same input produces identical content_hash on repeated parse."""
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries1 = parse_lessons_md(path)
        entries2 = parse_lessons_md(path)
        for e1, e2 in zip(entries1, entries2):
            assert e1["content_hash"] == e2["content_hash"]
    finally:
        os.unlink(path)


# --- Ingestion tests ---

def test_ingest_fresh_insert():
    """Fresh ingest of 2 entries returns inserted=2."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        result = ingest_lesson_entries(conn, entries)
        assert result["inserted"] == 2
        assert result["updated"] == 0
        assert result["unchanged"] == 0
        assert result["stale_proposals_marked"] == 0

        count = conn.execute("SELECT COUNT(*) FROM lesson_entries").fetchone()[0]
        assert count == 2
    finally:
        os.unlink(path)
        conn.close()


def test_ingest_unchanged_noop():
    """Re-ingest same entries returns unchanged=2, no writes."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries)
        conn.commit()

        result = ingest_lesson_entries(conn, entries)
        assert result["inserted"] == 0
        assert result["updated"] == 0
        assert result["unchanged"] == 2
        assert result["stale_proposals_marked"] == 0
    finally:
        os.unlink(path)
        conn.close()


def test_ingest_updated_entry():
    """Edit an entry's content, re-ingest: updated=1, hash changes in DB."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries)
        conn.commit()

        old_hash = entries[0]["content_hash"]

        # Mutate first entry
        entries[0]["raw_content"] = "Completely new content.\n"
        import hashlib
        entries[0]["content_hash"] = hashlib.sha256(
            entries[0]["raw_content"].encode("utf-8")
        ).hexdigest()

        result = ingest_lesson_entries(conn, entries)
        assert result["updated"] == 1
        assert result["unchanged"] == 1

        # Verify DB hash changed
        row = conn.execute(
            "SELECT content_hash FROM lesson_entries WHERE source_heading = ?",
            (entries[0]["source_heading"],),
        ).fetchone()
        assert row[0] != old_hash
        assert row[0] == entries[0]["content_hash"]
    finally:
        os.unlink(path)
        conn.close()


def test_ingest_stale_proposals():
    """Seed a proposal, edit entry, re-ingest: proposal marked stale."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries)
        conn.commit()

        # Get the first entry's ID
        entry_id = conn.execute(
            "SELECT id FROM lesson_entries WHERE source_heading = ?",
            (entries[0]["source_heading"],),
        ).fetchone()[0]

        # Seed a proposal for this entry
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'proposed', '2026-04-23')",
            (entry_id,),
        )
        conn.commit()

        # Mutate the entry's content
        import hashlib
        entries[0]["raw_content"] = "Modified content for stale test.\n"
        entries[0]["content_hash"] = hashlib.sha256(
            entries[0]["raw_content"].encode("utf-8")
        ).hexdigest()

        result = ingest_lesson_entries(conn, entries)
        assert result["updated"] == 1
        assert result["stale_proposals_marked"] == 1

        # Verify proposal is now stale
        status = conn.execute(
            "SELECT status FROM lesson_proposals WHERE entry_id = ?",
            (entry_id,),
        ).fetchone()[0]
        assert status == "stale"
    finally:
        os.unlink(path)
        conn.close()


# --- get_unclassified_entries tests ---

def test_get_unclassified_entries():
    """Helper returns entries with no proposal or only stale proposals, excludes implemented."""
    conn = _setup()

    # Entry 1: no proposal at all
    conn.execute(
        "INSERT INTO lesson_entries "
        "(source_file, source_heading, raw_content, content_hash, ingested_at) "
        "VALUES ('LESSONS.md', '2026-05-01 — No proposal', 'body1', 'h1', '2026-05-01')"
    )
    id_no_proposal = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Entry 2: only a stale proposal
    conn.execute(
        "INSERT INTO lesson_entries "
        "(source_file, source_heading, raw_content, content_hash, ingested_at) "
        "VALUES ('LESSONS.md', '2026-05-02 — Stale only', 'body2', 'h2', '2026-05-02')"
    )
    id_stale_only = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
        "VALUES (?, 'structural', 'action', 'reason', 'high', 'stale', '2026-05-02')",
        (id_stale_only,),
    )

    # Entry 3: has an implemented proposal — should be excluded
    conn.execute(
        "INSERT INTO lesson_entries "
        "(source_file, source_heading, raw_content, content_hash, ingested_at) "
        "VALUES ('LESSONS.md', '2026-05-03 — Implemented', 'body3', 'h3', '2026-05-03')"
    )
    id_implemented = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
        "VALUES (?, 'governance_rule', 'action', 'reason', 'high', 'implemented', '2026-05-03')",
        (id_implemented,),
    )

    result = get_unclassified_entries(conn)
    assert result == [id_no_proposal, id_stale_only], (
        f"Expected [{id_no_proposal}, {id_stale_only}], got {result}"
    )
    conn.close()


# --- insert_proposal tests (Phase 1B Step 2) ---

def _seed_entry(conn: sqlite3.Connection, heading: str = "2026-04-01 \u2014 Test entry",
                tags: str | None = None) -> int:
    """Insert a minimal lesson_entries row and return its id."""
    conn.execute(
        "INSERT INTO lesson_entries "
        "(source_file, source_heading, raw_content, content_hash, tags, ingested_at) "
        "VALUES ('LESSONS.md', ?, 'body', 'hash_placeholder', ?, '2026-04-23')",
        (heading, tags),
    )
    return conn.execute("SELECT last_insert_rowid()").fetchone()[0]


def test_insert_proposal_basic():
    """Insert one proposal with all fields, verify DB values and returned ID."""
    conn = _setup()
    entry_id = _seed_entry(conn)

    pid = insert_proposal(
        conn, entry_id=entry_id, category="structural",
        suggested_action="Fix the tool", reasoning="Tool is broken",
        confidence="high", status="proposed", target_layer="structure",
        target_artifact="PLANNER_TEMPLATE.md", duplicate_of=42,
        subcategory="tooling",
    )
    assert isinstance(pid, int) and pid > 0

    row = conn.execute(
        "SELECT entry_id, category, subcategory, suggested_action, reasoning, "
        "confidence, status, target_layer, target_artifact, duplicate_of "
        "FROM lesson_proposals WHERE id = ?", (pid,)
    ).fetchone()
    assert row[0] == entry_id
    assert row[1] == "structural"
    assert row[2] == "tooling"
    assert row[3] == "Fix the tool"
    assert row[4] == "Tool is broken"
    assert row[5] == "high"
    assert row[6] == "proposed"
    assert row[7] == "structure"
    assert row[8] == "PLANNER_TEMPLATE.md"
    assert row[9] == 42
    conn.close()


def test_insert_proposal_minimal_fields():
    """Insert with only required args, verify defaults."""
    conn = _setup()
    entry_id = _seed_entry(conn)

    pid = insert_proposal(
        conn, entry_id=entry_id, category="narrative",
        suggested_action="Archive it", reasoning="No action needed",
        confidence="low",
    )
    assert isinstance(pid, int) and pid > 0

    row = conn.execute(
        "SELECT status, target_layer, target_artifact, duplicate_of, subcategory "
        "FROM lesson_proposals WHERE id = ?", (pid,)
    ).fetchone()
    assert row[0] == "proposed"
    assert row[1] is None
    assert row[2] is None
    assert row[3] is None
    assert row[4] is None
    conn.close()


# --- detect_duplicates tests (Phase 1B Step 2) ---

SYNTHETIC_REF_CONTENT = """\
## Lessons Learned

| Date | Lesson |
|---|---|
| 2026-03-06 | Always read specialist files before source code. |
| 2026-03-13 | planner-discipline is important for governance-meta work. |

**Tag:** planner-discipline

## Some Other Section

This section talks about planning and governance topics.
Plans should be small and focused on delivery.
"""


def _write_ref_file(content: str) -> str:
    """Write a synthetic reference file to /tmp/ and return path."""
    fd, path = tempfile.mkstemp(suffix=".md", prefix="test_ref_", dir="/tmp")
    os.write(fd, content.encode("utf-8"))
    os.close(fd)
    return path


def test_detect_duplicates_empty_list():
    """Empty entry_ids returns empty list."""
    conn = _setup()
    result = detect_duplicates(conn, [], reference_files=["/tmp/nonexistent.md"])
    assert result == []
    conn.close()


def test_detect_duplicates_no_match():
    """Entry with tags not present in reference file returns empty list."""
    conn = _setup()
    entry_id = _seed_entry(conn, heading="2026-04-01 \u2014 Unique heading xyz",
                           tags="zzz-nonexistent-tag")
    ref_path = _write_ref_file("This file has no matching content at all.")
    try:
        result = detect_duplicates(conn, [entry_id], reference_files=[ref_path])
        assert result == []
    finally:
        os.unlink(ref_path)
        conn.close()


def test_detect_duplicates_tag_match():
    """Entry with a tag that appears in reference file is detected."""
    conn = _setup()
    entry_id = _seed_entry(conn, heading="2026-04-01 \u2014 Some unique heading",
                           tags="planner-discipline, other-tag")
    ref_path = _write_ref_file(SYNTHETIC_REF_CONTENT)
    try:
        result = detect_duplicates(conn, [entry_id], reference_files=[ref_path])
        assert len(result) == 1
        assert result[0]["entry_id"] == entry_id
        assert result[0]["matched_source"] == ref_path
        assert result[0]["match_reason"].startswith("tag_match:")
        assert "planner-discipline" in result[0]["match_reason"]
    finally:
        os.unlink(ref_path)
        conn.close()


def test_detect_duplicates_heading_match():
    """Entry with heading text appearing as substring in reference file is detected."""
    conn = _setup()
    # Heading title "read specialist files before source code" appears in SYNTHETIC_REF_CONTENT
    entry_id = _seed_entry(
        conn,
        heading="2026-04-01 \u2014 read specialist files before source code",
        tags=None,
    )
    ref_path = _write_ref_file(SYNTHETIC_REF_CONTENT)
    try:
        result = detect_duplicates(conn, [entry_id], reference_files=[ref_path])
        assert len(result) == 1
        assert result[0]["entry_id"] == entry_id
        assert result[0]["match_reason"] == "heading_substring_match"
    finally:
        os.unlink(ref_path)
        conn.close()


def test_detect_duplicates_first_match_wins():
    """Entry matches via both tag AND heading — only one dict returned."""
    conn = _setup()
    # Both tag "planner-discipline" and heading "read specialist files" match
    entry_id = _seed_entry(
        conn,
        heading="2026-04-01 \u2014 read specialist files before source code",
        tags="planner-discipline",
    )
    ref_path = _write_ref_file(SYNTHETIC_REF_CONTENT)
    try:
        result = detect_duplicates(conn, [entry_id], reference_files=[ref_path])
        assert len(result) == 1
        # Tag match is checked first, so it should be the winner
        assert result[0]["match_reason"].startswith("tag_match:")
    finally:
        os.unlink(ref_path)
        conn.close()


def test_detect_duplicates_tag_substring_not_flagged():
    """Tag appearing only in reference prose (no **Tag:** line) does NOT trigger match."""
    conn = _setup()
    entry_id = _seed_entry(conn, heading="2026-04-01 \u2014 Unique heading no dup",
                           tags="planner-discipline")
    # Reference contains the tag in prose but has NO **Tag:** line
    ref_content = """\
## Rules

Rules for planner-discipline are documented below.
All governance work should follow planner-discipline standards.
"""
    ref_path = _write_ref_file(ref_content)
    try:
        result = detect_duplicates(conn, [entry_id], reference_files=[ref_path])
        assert result == [], (
            "Tag appearing only in prose should not trigger tag_match "
            "under structural **Tag:** extraction"
        )
    finally:
        os.unlink(ref_path)
        conn.close()


# --- Orchestrator tests (Phase 1B Step 3) ---

# Synthetic LESSONS.md with NO tags that match SYNTHETIC_REF_CONTENT
SYNTHETIC_LESSONS_NO_DUPS = """\
# Eluvian Lessons Notepad
**Purpose:** Test fixture.

---

## Active entries (awaiting categorization or integration)

## 2026-04-10 \u2014 Completely unique lesson alpha

**Source:** Unit test fixture.

**Lesson:** This is a unique lesson with no matches.

**Tag:** zzz-unique-alpha

---

## 2026-04-12 \u2014 Completely unique lesson beta

**Source:** Another test fixture.

**Lesson:** Another unique lesson.

**Tag:** zzz-unique-beta

---

## Archived entries (integrated into permanent homes)

## 2026-03-01 \u2014 Archived
"""

# Synthetic LESSONS.md where first entry has a tag matching SYNTHETIC_REF_CONTENT
SYNTHETIC_LESSONS_ONE_DUP = """\
# Eluvian Lessons Notepad
**Purpose:** Test fixture.

---

## Active entries (awaiting categorization or integration)

## 2026-04-10 \u2014 Lesson with matching tag

**Source:** Unit test fixture.

**Lesson:** This lesson has a tag that matches the reference file.

**Tag:** planner-discipline

---

## 2026-04-12 \u2014 Completely unique lesson gamma

**Source:** Another test fixture.

**Lesson:** This lesson has no matches.

**Tag:** zzz-unique-gamma

---

## Archived entries (integrated into permanent homes)

## 2026-03-01 \u2014 Archived
"""


def test_run_full_lessons_cycle_fresh():
    """Synthetic LESSONS.md with 2 entries, no duplicates."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_NO_DUPS)
    ref_path = _write_ref_file("No matching content here at all.")
    try:
        # Monkey-patch the default reference files via explicit arg not available,
        # so we use detect_duplicates directly. Instead, use a wrapper approach:
        # run_full_lessons_cycle uses default ref files, but we can't control that.
        # Instead, we'll call with a synthetic lessons file and rely on no matches.
        # The reference file default points to PLANNER_TEMPLATE.md which won't match
        # our zzz-unique tags.
        result = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        assert result["ingested_count"] == 2
        assert result["updated_count"] == 0
        assert result["unchanged_count"] == 0
        assert result["duplicates_marked_count"] == 0
        assert len(result["needs_classification"]) == 2
        assert "cycle_timestamp" in result
    finally:
        os.unlink(lessons_path)
        os.unlink(ref_path)
        conn.close()


def test_run_full_lessons_cycle_with_duplicates():
    """Synthetic LESSONS.md with 2 entries, one matching tag in PLANNER_TEMPLATE."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_ONE_DUP)
    try:
        # "planner-discipline" tag will match against real PLANNER_TEMPLATE.md
        # (which contains "planner-discipline" as it's a common concept).
        # If PLANNER_TEMPLATE.md is unavailable, duplicates_marked_count=0.
        result = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        assert result["ingested_count"] == 2

        # Check that at most 1 duplicate was marked (depends on PLANNER_TEMPLATE availability)
        # The important invariant: needs_classification + duplicates = total entries
        total = len(result["needs_classification"]) + result["duplicates_marked_count"]
        assert total == 2

        if result["duplicates_marked_count"] == 1:
            assert len(result["needs_classification"]) == 1
            # Verify the duplicate proposal exists in DB
            dup_count = conn.execute(
                "SELECT COUNT(*) FROM lesson_proposals WHERE category = 'duplicate'"
            ).fetchone()[0]
            assert dup_count == 1
    finally:
        os.unlink(lessons_path)
        conn.close()


def test_run_full_lessons_cycle_idempotent():
    """Second call with same inputs: unchanged, no re-inserted duplicate proposals."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_ONE_DUP)
    try:
        # First run
        result1 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        conn.commit()
        dups_first = result1["duplicates_marked_count"]

        # Second run — same inputs
        result2 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        assert result2["unchanged_count"] == 2
        assert result2["ingested_count"] == 0
        assert result2["updated_count"] == 0
        # Idempotency: no new duplicate proposals inserted on re-run
        assert result2["duplicates_marked_count"] == 0

        # Total duplicate proposals in DB should still equal first run's count
        dup_count = conn.execute(
            "SELECT COUNT(*) FROM lesson_proposals WHERE category = 'duplicate'"
        ).fetchone()[0]
        assert dup_count == dups_first
    finally:
        os.unlink(lessons_path)
        conn.close()


# --- needs_classification regression tests ---

def test_needs_classification_excludes_dispositioned_entry():
    """Entry with a pre-existing non-stale proposal (e.g. 'implemented') is
    excluded from needs_classification on a subsequent cycle run."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_NO_DUPS)
    try:
        result1 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        conn.commit()
        assert len(result1["needs_classification"]) == 2

        entry_id = result1["needs_classification"][0]
        insert_proposal(
            conn, entry_id=entry_id, category="governance_rule",
            suggested_action="Add rule", reasoning="Needed",
            confidence="high", status="implemented",
        )
        conn.commit()

        result2 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        assert entry_id not in result2["needs_classification"]
        assert len(result2["needs_classification"]) == 1
    finally:
        os.unlink(lessons_path)
        conn.close()


def test_needs_classification_includes_stale_only_entry():
    """Entry whose only proposal has status 'stale' IS included in
    needs_classification (re-queued-edit path)."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_NO_DUPS)
    try:
        result1 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        conn.commit()

        entry_id = result1["needs_classification"][0]
        insert_proposal(
            conn, entry_id=entry_id, category="structural",
            suggested_action="Fix it", reasoning="Broken",
            confidence="high", status="stale",
        )
        conn.commit()

        result2 = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        assert entry_id in result2["needs_classification"]
    finally:
        os.unlink(lessons_path)
        conn.close()


def test_needs_classification_plus_duplicates_equals_total():
    """On a fresh DB, needs_classification + duplicates_marked_count == total
    parsed entries (invariant preserved after delegation to helper)."""
    conn = _setup()
    lessons_path = _write_fixture(SYNTHETIC_LESSONS_ONE_DUP)
    try:
        result = run_full_lessons_cycle(conn, lessons_md_path=lessons_path)
        total_parsed = result["ingested_count"]
        assert total_parsed == 2
        assert (
            len(result["needs_classification"]) + result["duplicates_marked_count"]
            == total_parsed
        )
    finally:
        os.unlink(lessons_path)
        conn.close()


# --- Report generator tests (Phase 1B Step 3) ---

def test_generate_lessons_report_empty():
    """No proposals — report has placeholder text."""
    conn = _setup()
    report_dir = tempfile.mkdtemp(prefix="test_reports_")
    try:
        path = generate_lessons_report(conn, "2026-04-23-test", output_dir=report_dir)
        assert os.path.isfile(path)
        with open(path) as f:
            content = f.read()
        assert "No proposals pending review." in content
        assert "# Lessons Report" in content
    finally:
        os.unlink(path)
        os.rmdir(report_dir)
        conn.close()


def test_generate_lessons_report_multi_category():
    """Seed 3 proposals across 3 categories — report has 3 sections."""
    conn = _setup()
    report_dir = tempfile.mkdtemp(prefix="test_reports_")

    # Seed 3 entries with different dates
    e1 = _seed_entry(conn, heading="2026-04-15 \u2014 Entry A")
    e2 = _seed_entry(conn, heading="2026-04-10 \u2014 Entry B")
    e3 = _seed_entry(conn, heading="2026-04-20 \u2014 Entry C")
    # Update entry_date for sorting verification
    conn.execute("UPDATE lesson_entries SET entry_date = '2026-04-15' WHERE id = ?", (e1,))
    conn.execute("UPDATE lesson_entries SET entry_date = '2026-04-10' WHERE id = ?", (e2,))
    conn.execute("UPDATE lesson_entries SET entry_date = '2026-04-20' WHERE id = ?", (e3,))

    insert_proposal(conn, e1, "structural", "Fix it", "Broken", "high")
    insert_proposal(conn, e2, "governance_rule", "Add rule", "Missing", "medium")
    insert_proposal(conn, e3, "language", "Rephrase", "Unclear", "low")

    try:
        path = generate_lessons_report(conn, "2026-04-23-multi", output_dir=report_dir)
        with open(path) as f:
            content = f.read()

        # 3 category sections
        assert "## Structural" in content
        assert "## Governance Rule" in content
        assert "## Language" in content

        # Summary counts
        assert "| structural | 1 |" in content
        assert "| governance_rule | 1 |" in content
        assert "| language | 1 |" in content
        assert "**Total proposals:** 3" in content
    finally:
        os.unlink(path)
        os.rmdir(report_dir)
        conn.close()


def test_generate_lessons_report_writes_file():
    """Returned path points to an existing non-empty file."""
    conn = _setup()
    report_dir = tempfile.mkdtemp(prefix="test_reports_")
    try:
        path = generate_lessons_report(conn, "2026-04-23-write", output_dir=report_dir)
        assert os.path.isfile(path)
        assert os.path.getsize(path) > 0
        assert os.path.isabs(path)
    finally:
        os.unlink(path)
        os.rmdir(report_dir)
        conn.close()


# --- Route column tests ---

@pytest.mark.parametrize("route_val", ["codify", "backlog", "reference"])
def test_insert_proposal_with_valid_route(route_val):
    """Insert with each valid route value persists and reads back."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    pid = insert_proposal(
        conn, entry_id=entry_id, category="structural",
        suggested_action="action", reasoning="reason",
        confidence="high", route=route_val,
    )
    row = conn.execute(
        "SELECT route FROM lesson_proposals WHERE id = ?", (pid,)
    ).fetchone()
    assert row[0] == route_val
    conn.close()


def test_insert_proposal_route_none_default():
    """Insert without route keyword leaves route NULL."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    pid = insert_proposal(
        conn, entry_id=entry_id, category="structural",
        suggested_action="action", reasoning="reason",
        confidence="high",
    )
    row = conn.execute(
        "SELECT route FROM lesson_proposals WHERE id = ?", (pid,)
    ).fetchone()
    assert row[0] is None
    conn.close()


def test_insert_proposal_invalid_route_raises():
    """Invalid route value raises ValueError at the Python layer."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    with pytest.raises(ValueError, match="route must be one of"):
        insert_proposal(
            conn, entry_id=entry_id, category="structural",
            suggested_action="action", reasoning="reason",
            confidence="high", route="invalid_route",
        )
    conn.close()


def test_route_check_constraint_rejects_invalid_sql():
    """Direct SQL INSERT with an invalid route is rejected by the CHECK constraint."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, route, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'bogus', '2026-07-06')",
            (entry_id,),
        )
    conn.close()


def test_migration_idempotence_double_init():
    """init_db() twice on one DB does not error."""
    conn = sqlite3.connect(":memory:")
    db.init_db(conn)
    db.init_db(conn)
    cols = {row[1] for row in conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()}
    assert "route" in cols
    conn.close()


def test_migration_adds_route_to_pre_existing_db():
    """init_db() against a DB created WITHOUT the route column adds it."""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS lesson_entries (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file     TEXT    NOT NULL,
            source_heading  TEXT    NOT NULL,
            entry_date      TEXT,
            raw_content     TEXT    NOT NULL,
            content_hash    TEXT    NOT NULL,
            tags            TEXT,
            ingested_at     TEXT    NOT NULL,
            UNIQUE(source_file, source_heading)
        );
        CREATE TABLE IF NOT EXISTS lesson_proposals (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
            category            TEXT    NOT NULL,
            subcategory         TEXT,
            suggested_action    TEXT    NOT NULL,
            reasoning           TEXT    NOT NULL,
            confidence          TEXT    NOT NULL,
            status              TEXT    NOT NULL DEFAULT 'proposed',
            target_layer        TEXT,
            target_artifact     TEXT,
            duplicate_of        INTEGER,
            proposed_at         TEXT    NOT NULL,
            status_updated_at   TEXT,
            status_updated_by   TEXT
        );
    """)
    cols_before = {row[1] for row in conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()}
    assert "route" not in cols_before

    db.init_db(conn)
    cols_after = {row[1] for row in conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()}
    assert "route" in cols_after
    conn.close()


def test_set_proposal_route_persists():
    """set_proposal_route updates the route on an existing proposal."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    pid = insert_proposal(
        conn, entry_id=entry_id, category="governance_rule",
        suggested_action="Add rule", reasoning="Needed",
        confidence="high",
    )
    assert conn.execute("SELECT route FROM lesson_proposals WHERE id = ?", (pid,)).fetchone()[0] is None

    set_proposal_route(conn, pid, "codify")
    assert conn.execute("SELECT route FROM lesson_proposals WHERE id = ?", (pid,)).fetchone()[0] == "codify"

    set_proposal_route(conn, pid, "backlog")
    assert conn.execute("SELECT route FROM lesson_proposals WHERE id = ?", (pid,)).fetchone()[0] == "backlog"

    set_proposal_route(conn, pid, None)
    assert conn.execute("SELECT route FROM lesson_proposals WHERE id = ?", (pid,)).fetchone()[0] is None
    conn.close()


def test_set_proposal_route_invalid_raises():
    """set_proposal_route with an invalid value raises ValueError."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    pid = insert_proposal(
        conn, entry_id=entry_id, category="structural",
        suggested_action="action", reasoning="reason",
        confidence="high",
    )
    with pytest.raises(ValueError, match="route must be one of"):
        set_proposal_route(conn, pid, "not_a_route")
    conn.close()


def test_report_renders_route_where_present():
    """Report includes route for proposals that have one, omits for NULL."""
    conn = _setup()
    report_dir = tempfile.mkdtemp(prefix="test_reports_")
    e1 = _seed_entry(conn, heading="2026-07-01 — Routed entry")
    e2 = _seed_entry(conn, heading="2026-07-02 — Unrouted entry")
    conn.execute("UPDATE lesson_entries SET entry_date = '2026-07-01' WHERE id = ?", (e1,))
    conn.execute("UPDATE lesson_entries SET entry_date = '2026-07-02' WHERE id = ?", (e2,))

    insert_proposal(conn, e1, "structural", "Fix it", "Broken", "high", route="codify")
    insert_proposal(conn, e2, "structural", "Fix that", "Also broken", "medium")

    try:
        path = generate_lessons_report(conn, "2026-07-06-route", output_dir=report_dir)
        with open(path) as f:
            content = f.read()
        assert "- **Route:** codify" in content
        assert content.count("**Route:**") == 1
    finally:
        os.unlink(path)
        os.rmdir(report_dir)
        conn.close()


# --- Reference status migration tests ---

def test_reference_status_migration_idempotence():
    """init_db() twice: reference status CHECK present, no error."""
    conn = sqlite3.connect(":memory:")
    db.init_db(conn)
    db.init_db(conn)
    schema = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'"
    ).fetchone()[0]
    assert "'reference'" in schema
    conn.close()


def test_reference_status_migration_pre_existing_db():
    """init_db() against a DB with old status CHECK (no 'reference') rebuilds correctly."""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS lesson_entries (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file     TEXT    NOT NULL,
            source_heading  TEXT    NOT NULL,
            entry_date      TEXT,
            raw_content     TEXT    NOT NULL,
            content_hash    TEXT    NOT NULL,
            tags            TEXT,
            ingested_at     TEXT    NOT NULL,
            UNIQUE(source_file, source_heading)
        );
        CREATE TABLE IF NOT EXISTS lesson_proposals (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
            category            TEXT    NOT NULL CHECK(category IN ('structural', 'instrumentation', 'governance_rule', 'language', 'narrative', 'duplicate')),
            subcategory         TEXT,
            suggested_action    TEXT    NOT NULL,
            reasoning           TEXT    NOT NULL,
            confidence          TEXT    NOT NULL CHECK(confidence IN ('low', 'medium', 'high')),
            status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')),
            target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure', 'governance', 'language', 'none')),
            target_artifact     TEXT,
            duplicate_of        INTEGER,
            route               TEXT    CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference')),
            proposed_at         TEXT    NOT NULL,
            status_updated_at   TEXT,
            status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))
        );
        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_entry ON lesson_proposals(entry_id);
        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_status ON lesson_proposals(status);
        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_category ON lesson_proposals(category);
    """)

    # Seed data to verify preservation
    conn.execute(
        "INSERT INTO lesson_entries (source_file, source_heading, raw_content, content_hash, ingested_at) "
        "VALUES ('LESSONS.md', '2026-07-01 — Test', 'body', 'hash1', '2026-07-01')"
    )
    conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, suggested_action, reasoning, confidence, status, route, proposed_at) "
        "VALUES (1, 'structural', 'Fix it', 'Broken', 'high', 'implemented', 'codify', '2026-07-01')"
    )
    conn.commit()

    # Verify old schema lacks 'reference' in status CHECK
    schema_before = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'"
    ).fetchone()[0]
    assert "'implemented', 'reference'" not in schema_before

    db.init_db(conn)

    # Verify schema now includes 'reference' in status CHECK
    schema_after = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'"
    ).fetchone()[0]
    assert "'implemented', 'reference'" in schema_after

    # Verify data preserved
    row = conn.execute(
        "SELECT category, status, route FROM lesson_proposals WHERE id = 1"
    ).fetchone()
    assert row == ('structural', 'implemented', 'codify')

    conn.close()


def test_reference_status_check_accepts_reference():
    """INSERT with status='reference' succeeds."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    conn.execute(
        "INSERT INTO lesson_proposals "
        "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
        "VALUES (?, 'structural', 'action', 'reason', 'high', 'reference', '2026-07-07')",
        (entry_id,),
    )
    row = conn.execute(
        "SELECT status FROM lesson_proposals WHERE entry_id = ?", (entry_id,)
    ).fetchone()
    assert row[0] == "reference"
    conn.close()


def test_reference_status_check_still_rejects_invalid():
    """INSERT with status='bogus' still raises IntegrityError after rebuild."""
    conn = _setup()
    entry_id = _seed_entry(conn)
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'bogus_status', '2026-07-07')",
            (entry_id,),
        )
    conn.close()


def test_reference_status_migration_preserves_row_count():
    """Table rebuild preserves all rows and data across migration."""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS lesson_entries (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file     TEXT    NOT NULL,
            source_heading  TEXT    NOT NULL,
            entry_date      TEXT,
            raw_content     TEXT    NOT NULL,
            content_hash    TEXT    NOT NULL,
            tags            TEXT,
            ingested_at     TEXT    NOT NULL,
            UNIQUE(source_file, source_heading)
        );
        CREATE TABLE IF NOT EXISTS lesson_proposals (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
            category            TEXT    NOT NULL CHECK(category IN ('structural', 'instrumentation', 'governance_rule', 'language', 'narrative', 'duplicate')),
            subcategory         TEXT,
            suggested_action    TEXT    NOT NULL,
            reasoning           TEXT    NOT NULL,
            confidence          TEXT    NOT NULL CHECK(confidence IN ('low', 'medium', 'high')),
            status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')),
            target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure', 'governance', 'language', 'none')),
            target_artifact     TEXT,
            duplicate_of        INTEGER,
            route               TEXT    CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference')),
            proposed_at         TEXT    NOT NULL,
            status_updated_at   TEXT,
            status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))
        );
    """)

    # Seed multiple rows
    for i in range(1, 6):
        conn.execute(
            "INSERT INTO lesson_entries (source_file, source_heading, raw_content, content_hash, ingested_at) "
            "VALUES ('LESSONS.md', ?, 'body', ?, '2026-07-01')",
            (f"2026-07-0{i} — Entry {i}", f"hash{i}"),
        )
        conn.execute(
            "INSERT INTO lesson_proposals "
            "(entry_id, category, suggested_action, reasoning, confidence, status, proposed_at) "
            "VALUES (?, 'structural', 'action', 'reason', 'high', 'implemented', '2026-07-01')",
            (i,),
        )
    conn.commit()

    count_before = conn.execute("SELECT COUNT(*) FROM lesson_proposals").fetchone()[0]
    assert count_before == 5

    db.init_db(conn)

    count_after = conn.execute("SELECT COUNT(*) FROM lesson_proposals").fetchone()[0]
    assert count_after == 5

    # Verify all IDs preserved
    ids = [r[0] for r in conn.execute("SELECT id FROM lesson_proposals ORDER BY id").fetchall()]
    assert ids == [1, 2, 3, 4, 5]

    conn.close()


def test_report_renders_proposal_details():
    """Report renders per-proposal heading and suggested-action line."""
    conn = _setup()
    report_dir = tempfile.mkdtemp(prefix="test_reports_")

    eid = _seed_entry(conn, heading="2026-07-01 — Unique topic xyz")
    conn.execute(
        "UPDATE lesson_entries SET entry_date = ? WHERE id = ?",
        ("2026-07-01", eid),
    )
    insert_proposal(
        conn, eid, "structural",
        "Fix something unique", "It is broken", "high",
    )

    try:
        path = generate_lessons_report(
            conn, "2026-07-09-details", output_dir=report_dir,
        )
        with open(path) as f:
            content = f.read()
        assert "### 2026-07-01" in content
        assert "- **Suggested action:** Fix something unique" in content
    finally:
        os.unlink(path)
        os.rmdir(report_dir)
        conn.close()


# --- Hash normalization tests (plan 204) ---


def test_hash_trailing_separator_invariant():
    """Regression: body with and without trailing separator produces identical hash."""
    body = "**Source:** Unit test.\n\n**Lesson:** Plans should be small.\n\n**Tag:** planner-discipline\n"
    body_with_sep = body + "\n---\n\n"
    assert _normalize_for_hash(body) == _normalize_for_hash(body_with_sep)

    import hashlib
    h1 = hashlib.sha256(_normalize_for_hash(body).encode("utf-8")).hexdigest()
    h2 = hashlib.sha256(_normalize_for_hash(body_with_sep).encode("utf-8")).hexdigest()
    assert h1 == h2


def test_hash_substantive_edit_changes_hash():
    """A real content edit still produces a different hash."""
    body_a = "**Lesson:** Plans should be small.\n"
    body_b = "**Lesson:** Plans should be large and ambitious.\n"
    assert _normalize_for_hash(body_a) != _normalize_for_hash(body_b)


def test_raw_content_stored_verbatim_with_separator():
    """Normalization does not leak into stored raw_content."""
    body_with_sep = (
        "\n**Source:** Unit test.\n\n**Lesson:** Plans should be small.\n"
        "\n**Tag:** planner-discipline\n\n---\n\n"
    )
    md = (
        "# Lessons\n\n"
        "## 2026-04-10 — Test entry\n"
        + body_with_sep
        + "## Archived entries\n"
    )
    path = _write_fixture(md)
    try:
        entries = parse_lessons_md(path)
        assert len(entries) == 1
        assert entries[0]["raw_content"].rstrip().endswith("---"), (
            "raw_content must retain the trailing separator verbatim"
        )
    finally:
        os.unlink(path)


@pytest.mark.parametrize("terminal_status", sorted(_TERMINAL_STATUSES))
def test_terminal_status_guard(terminal_status):
    """Entry with a genuinely changed body and a terminal-status proposal:
    proposal stays in its terminal status and appears in terminal_proposals_flagged."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries)
        conn.commit()

        entry_id = conn.execute(
            "SELECT id FROM lesson_entries WHERE source_heading = ?",
            (entries[0]["source_heading"],),
        ).fetchone()[0]

        pid = insert_proposal(
            conn, entry_id=entry_id, category="governance_rule",
            suggested_action="Add rule", reasoning="Needed",
            confidence="high", status=terminal_status,
        )
        conn.commit()

        entries[0]["raw_content"] = "Genuinely different content for guard test.\n"
        import hashlib
        entries[0]["content_hash"] = hashlib.sha256(
            _normalize_for_hash(entries[0]["raw_content"]).encode("utf-8")
        ).hexdigest()

        result = ingest_lesson_entries(conn, entries)
        assert result["updated"] == 1
        assert result["stale_proposals_marked"] == 0

        status_after = conn.execute(
            "SELECT status FROM lesson_proposals WHERE id = ?", (pid,)
        ).fetchone()[0]
        assert status_after == terminal_status

        flagged = result["terminal_proposals_flagged"]
        assert len(flagged) == 1
        assert flagged[0]["entry_id"] == entry_id
        assert flagged[0]["proposal_id"] == pid
        assert flagged[0]["status"] == terminal_status
    finally:
        os.unlink(path)
        conn.close()


def test_nonterminal_still_stales():
    """A genuine body change with a 'proposed' proposal still marks it stale."""
    conn = _setup()
    path = _write_fixture(SYNTHETIC_LESSONS)
    try:
        entries = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries)
        conn.commit()

        entry_id = conn.execute(
            "SELECT id FROM lesson_entries WHERE source_heading = ?",
            (entries[0]["source_heading"],),
        ).fetchone()[0]

        insert_proposal(
            conn, entry_id=entry_id, category="structural",
            suggested_action="Fix it", reasoning="Broken",
            confidence="high", status="proposed",
        )
        conn.commit()

        entries[0]["raw_content"] = "Changed content for stale test.\n"
        import hashlib
        entries[0]["content_hash"] = hashlib.sha256(
            _normalize_for_hash(entries[0]["raw_content"]).encode("utf-8")
        ).hexdigest()

        result = ingest_lesson_entries(conn, entries)
        assert result["updated"] == 1
        assert result["stale_proposals_marked"] == 1
        assert result["terminal_proposals_flagged"] == []

        status = conn.execute(
            "SELECT status FROM lesson_proposals WHERE entry_id = ?",
            (entry_id,),
        ).fetchone()[0]
        assert status == "stale"
    finally:
        os.unlink(path)
        conn.close()


def test_trailing_separator_only_delta_zero_stales():
    """The catastrophic case: re-ingesting entries whose only delta is a
    trailing separator marks zero proposals stale and reports updated == 0."""
    body_core = (
        "\n**Source:** Unit test.\n\n**Lesson:** Plans should be small.\n"
        "\n**Tag:** planner-discipline\n"
    )
    md_v1 = (
        "# Lessons\n\n"
        "## 2026-04-10 — Test entry\n"
        + body_core + "\n"
        + "## Archived entries\n"
    )
    md_v2 = (
        "# Lessons\n\n"
        "## 2026-04-10 — Test entry\n"
        + body_core + "\n---\n\n"
        + "## Archived entries\n"
    )

    conn = _setup()
    path = _write_fixture(md_v1)
    try:
        entries_v1 = parse_lessons_md(path)
        ingest_lesson_entries(conn, entries_v1)
        conn.commit()

        entry_id = conn.execute(
            "SELECT id FROM lesson_entries WHERE source_heading = ?",
            (entries_v1[0]["source_heading"],),
        ).fetchone()[0]

        insert_proposal(
            conn, entry_id=entry_id, category="governance_rule",
            suggested_action="Add rule", reasoning="Needed",
            confidence="high", status="implemented",
        )
        conn.commit()
    finally:
        os.unlink(path)

    path2 = _write_fixture(md_v2)
    try:
        entries_v2 = parse_lessons_md(path2)
        result = ingest_lesson_entries(conn, entries_v2)
        assert result["updated"] == 0, "Trailing separator should NOT trigger an update"
        assert result["stale_proposals_marked"] == 0
        assert result["terminal_proposals_flagged"] == []
        assert result["unchanged"] == 1
    finally:
        os.unlink(path2)
        conn.close()
