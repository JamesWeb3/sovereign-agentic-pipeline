"""Structural tests for the three evidence registers and the loader that reads them.

`research/corpus.csv` says which Sources exist, `research/claims.csv` which Claims, and
`research/numbers.csv` which Numbers and where each one came from. These tests enforce
the methodology rule in prose form — every number traces to a source or it is deleted —
as a build failure, so an untraceable figure cannot sit in the register unnoticed.

They import `load_corpus` for its readers and `check_references`, which is deliberately
possible without a database: the module defers its `neo4j` import into `main()`, and CI
installs only ruff and pytest.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "graph" / "loaders"))

import load_corpus  # noqa: E402  (path must be set before the import)

RESEARCH = ROOT / "research"

EXPECTED_CLAIMS_HEADER = [
    "claim_id",
    "topic",
    "statement",
    "about_type",
    "about_id",
]

EXPECTED_NUMBERS_HEADER = [
    "number_id",
    "claim_id",
    "source_id",
    "value",
    "unit",
    "as_of",
    "basis",
    "note",
]


def _rows(name: str) -> list[dict[str, str]]:
    with (RESEARCH / name).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _header(name: str) -> list[str]:
    with (RESEARCH / name).open(newline="", encoding="utf-8") as fh:
        return next(csv.reader(fh))


def test_registers_exist():
    for name in ("corpus.csv", "claims.csv", "numbers.csv", "entities.csv"):
        assert (RESEARCH / name).exists(), f"research/{name} is missing"


def test_headers_are_exact():
    assert _header("claims.csv") == EXPECTED_CLAIMS_HEADER
    assert _header("numbers.csv") == EXPECTED_NUMBERS_HEADER


def test_ids_are_unique():
    for name, key in (
        ("corpus.csv", "source_id"),
        ("claims.csv", "claim_id"),
        ("numbers.csv", "number_id"),
    ):
        ids = [r[key] for r in _rows(name)]
        dupes = {i for i in ids if ids.count(i) > 1}
        assert not dupes, f"duplicate {key} in {name}: {sorted(dupes)}"


def test_every_reference_resolves():
    """The whole evidence base, checked the way the loader checks it before writing."""
    load_corpus.check_references(
        _rows("corpus.csv"), _rows("claims.csv"), _rows("numbers.csv")
    )


def test_every_number_carries_a_source():
    """No URL, no source; no source, no number. This is the methodology rule itself."""
    for row in _rows("numbers.csv"):
        assert row["source_id"].strip(), f"{row['number_id']} has no source_id"


def test_every_number_value_is_numeric():
    """A Number whose value is prose cannot be compared, which is the point of a Number."""
    for row in _rows("numbers.csv"):
        try:
            float(row["value"])
        except ValueError:  # pragma: no cover - the assert carries the message
            pytest.fail(f"{row['number_id']} has non-numeric value {row['value']!r}")


def test_every_number_states_its_basis():
    """Two figures for one claim are usually two quantities, not a contradiction.

    The `basis` column is what stops the graph flattening a consent limit and an
    operator's expectation into a disagreement, so it is mandatory.
    """
    for row in _rows("numbers.csv"):
        assert row["basis"].strip(), f"{row['number_id']} does not state its basis"


def test_every_claim_is_backed_by_at_least_one_source():
    """A Claim nothing supports is an assertion, and the corpus does not hold assertions."""
    backed: set[str] = set()
    for row in _rows("corpus.csv"):
        backed.update(load_corpus.claim_ids_for(row))
    unbacked = sorted({r["claim_id"] for r in _rows("claims.csv")} - backed)
    assert not unbacked, f"claims with no source behind them: {unbacked}"


def test_about_types_are_known_labels():
    for row in _rows("claims.csv"):
        label = row["about_type"].strip()
        if label:
            assert label in load_corpus.ABOUT_LABELS, (
                f"{row['claim_id']} points at unknown label {label!r}"
            )


def test_check_references_rejects_an_untraceable_number():
    """The guard has to actually fire, or it is decoration."""
    corpus = _rows("corpus.csv")
    claims = _rows("claims.csv")
    bad = [
        {
            "number_id": "num-untraceable",
            "claim_id": claims[0]["claim_id"],
            "source_id": "",
            "value": "1",
            "unit": "L",
            "as_of": "2026-01-01",
            "basis": "invented",
            "note": "",
        }
    ]
    with pytest.raises(ValueError, match="no source_id"):
        load_corpus.check_references(corpus, claims, bad)


def test_check_references_rejects_an_unknown_claim():
    corpus = _rows("corpus.csv")
    claims = _rows("claims.csv")
    bad = [
        {
            "number_id": "num-orphan",
            "claim_id": "claim-does-not-exist",
            "source_id": corpus[0]["source_id"],
            "value": "1",
            "unit": "L",
            "as_of": "2026-01-01",
            "basis": "invented",
            "note": "",
        }
    ]
    with pytest.raises(ValueError, match="not in claims.csv"):
        load_corpus.check_references(corpus, claims, bad)


EXPECTED_ENTITIES_HEADER = ["entity_id", "label", "name", "kind", "region"]


def test_entities_header_and_labels():
    assert _header("entities.csv") == EXPECTED_ENTITIES_HEADER
    for row in _rows("entities.csv"):
        assert row["label"] in load_corpus.ABOUT_LABELS, (
            f"{row['entity_id']} has unknown label {row['label']!r}"
        )
        assert row["name"].strip(), f"{row['entity_id']} has no name"


def test_every_claim_points_at_a_registered_entity():
    """A Claim ABOUT an unregistered id would make claims_about_facility return nulls."""
    load_corpus.check_references(
        _rows("corpus.csv"),
        _rows("claims.csv"),
        _rows("numbers.csv"),
        _rows("entities.csv"),
    )


def test_every_corpus_source_has_frontmatter_camp():
    """`camp` reaches the graph from the source file, not from a second copy in the CSV.

    Source nodes carry camp so `sources_by_camp` and `claims_about_facility` can group by
    it; both returned nulls before the loader read the frontmatter.
    """
    attrs = load_corpus.source_attributes()
    for row in _rows("corpus.csv"):
        attr = attrs.get(row["source_id"])
        assert attr is not None, f"{row['source_id']} has no source file"
        assert attr["camp"], f"{row['source_id']} has no camp in its frontmatter"
