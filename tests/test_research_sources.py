"""Structural tests for the evidence base in research/.

These enforce the rules research/sources/README.md states in prose, so that a source which
cannot be traced fails the build rather than sitting unnoticed in the corpus:

  * every source file carries complete frontmatter, with `url` and `retrieved` non-empty
    ("no URL, no source")
  * `type` and `camp` stay inside their controlled vocabularies
  * the camp subfolder a file lives in matches its `camp` frontmatter
  * `id` matches the filename, and every source has exactly one corpus.csv row

Frontmatter is parsed with a deliberately small hand-rolled reader rather than a YAML
dependency: the schema is flat `key: value` lines and nothing here needs more.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "research" / "sources"
CORPUS = ROOT / "research" / "corpus.csv"

REQUIRED_FIELDS = ["id", "title", "publisher", "date", "url", "retrieved", "type", "camp"]
MANDATORY_NON_EMPTY = ["id", "url", "retrieved", "type", "camp"]

TYPES = {"coverage", "submission", "official-statement", "dataset", "report", "other"}
CAMPS = {"climate-first", "growth-first", "neutral", "official"}

# Not sources: the directory READMEs, and the format template that deliberately has no
# corpus row (a live row would inject an "Example Publisher" node into the graph).
TEMPLATE = "example-0001-template.md"


def source_files() -> list[Path]:
    """Every markdown file under research/sources/ that claims to be a source."""
    return sorted(p for p in SOURCES.rglob("*.md") if p.name != "README.md")


def read_frontmatter(path: Path) -> dict[str, str]:
    """Parse the leading `---` fenced block into a dict. Empty dict if absent."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.split("#")[0].strip().strip('"')
    return fields


def corpus_rows() -> list[dict[str, str]]:
    with CORPUS.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def test_every_source_has_frontmatter():
    missing = [p.name for p in source_files() if not read_frontmatter(p)]
    assert not missing, f"source files with no frontmatter block: {missing}"


def test_every_source_has_all_required_fields():
    for path in source_files():
        fields = read_frontmatter(path)
        if not fields:
            continue  # reported by test_every_source_has_frontmatter
        absent = [f for f in REQUIRED_FIELDS if f not in fields]
        assert not absent, f"{path.name} is missing frontmatter fields: {absent}"


def test_url_and_retrieved_are_present():
    """The core methodology rule: no URL, no source."""
    for path in source_files():
        fields = read_frontmatter(path)
        if not fields:
            continue
        for key in MANDATORY_NON_EMPTY:
            assert fields.get(key), f"{path.name} has an empty '{key}' - untraceable"


def test_type_and_camp_use_controlled_vocabularies():
    for path in source_files():
        fields = read_frontmatter(path)
        if not fields:
            continue
        if fields.get("type"):
            assert fields["type"] in TYPES, f"{path.name}: unknown type {fields['type']!r}"
        if fields.get("camp"):
            assert fields["camp"] in CAMPS, f"{path.name}: unknown camp {fields['camp']!r}"


def test_camp_folder_matches_frontmatter():
    """The folder is a view onto `camp`; the frontmatter stays authoritative."""
    for path in source_files():
        folder = path.parent.name
        if folder not in CAMPS:
            continue  # top-level files are covered by test_sources_live_in_a_camp_folder
        camp = read_frontmatter(path).get("camp")
        assert camp == folder, f"{path.name} is in {folder}/ but declares camp: {camp}"


def test_sources_live_in_a_camp_folder():
    stray = [p.name for p in source_files() if p.parent == SOURCES and p.name != TEMPLATE]
    assert not stray, f"sources not filed under a camp folder: {stray}"


def test_id_matches_filename():
    for path in source_files():
        if path.name == TEMPLATE:
            continue  # the template's id is a placeholder, not its filename
        fields = read_frontmatter(path)
        if not fields.get("id"):
            continue
        assert fields["id"] == path.stem, f"{path.name} declares id {fields['id']!r}"


def test_every_source_file_has_a_corpus_row():
    ids = {row["source_id"] for row in corpus_rows()}
    orphans = [
        p.name
        for p in source_files()
        if p.name != TEMPLATE and read_frontmatter(p).get("id") not in ids
    ]
    assert not orphans, f"source files with no corpus.csv row: {orphans}"


def test_every_corpus_row_has_a_source_file():
    stems = {p.stem for p in source_files()}
    missing = [row["source_id"] for row in corpus_rows() if row["source_id"] not in stems]
    assert not missing, f"corpus.csv rows with no source file: {missing}"


def test_corpus_source_ids_are_unique():
    ids = [row["source_id"] for row in corpus_rows()]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    assert not duplicates, f"duplicate source_id in corpus.csv: {duplicates}"


def test_corpus_rows_carry_url_and_retrieved_at():
    for row in corpus_rows():
        assert row["url"], f"{row['source_id']}: empty url in corpus.csv"
        assert row["retrieved_at"], f"{row['source_id']}: empty retrieved_at in corpus.csv"


def test_corpus_rows_list_at_least_one_claim():
    for row in corpus_rows():
        claims = [c for c in row["claim_ids"].split(";") if c.strip()]
        assert claims, f"{row['source_id']}: no claim_ids - backs nothing"
