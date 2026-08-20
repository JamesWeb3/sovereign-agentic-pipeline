"""Structural tests for the scaffold.

These guard the invariants a contributor relies on: the corpus format, the graph schema
covering every node label, every Step directory carrying a README, and the protected eval
warning being present. They also unit-test the one piece of real logic in Part A so far
(the scheduling simulation).
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_CORPUS_HEADER = [
    "source_id",
    "title",
    "publisher",
    "pub_date",
    "url",
    "retrieved_at",
    "claim_ids",
]

NODE_LABELS = ["Source", "Claim", "Number", "Entity", "Facility", "Policy", "Person"]

STEP_DIRS = [
    "research",
    "graph",
    "grid",
    "energy",
    "scheduling",
    "model",
    "retrieval",
    "mcp_server",
    "agent",
    "voice",
    "roi",
    "report",
]


def test_corpus_header_is_exact():
    with (ROOT / "research" / "corpus.csv").open(newline="", encoding="utf-8") as fh:
        header = next(csv.reader(fh))
    assert header == EXPECTED_CORPUS_HEADER


def test_corpus_has_at_least_one_example_row():
    with (ROOT / "research" / "corpus.csv").open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) >= 1
    assert rows[0]["source_id"]


def test_schema_models_every_node_label():
    schema = (ROOT / "graph" / "schema.cypher").read_text(encoding="utf-8")
    for label in NODE_LABELS:
        assert f":{label}" in schema, f"schema.cypher does not model :{label}"


def test_schema_is_idempotent_style():
    schema = (ROOT / "graph" / "schema.cypher").read_text(encoding="utf-8")
    # Every constraint/index must be IF NOT EXISTS so `make graph` can re-run cleanly.
    for line in schema.splitlines():
        stripped = line.strip()
        if stripped.startswith(("CREATE CONSTRAINT", "CREATE INDEX")):
            assert "IF NOT EXISTS" in stripped, f"not idempotent: {stripped}"


def test_at_least_three_named_queries():
    queries = list((ROOT / "graph" / "queries").glob("*.cypher"))
    assert len(queries) >= 3
    for q in queries:
        assert q.read_text(encoding="utf-8").lstrip().startswith("//"), (
            f"{q.name} should open with a comment saying what it answers"
        )


def test_every_step_dir_has_a_readme():
    for d in STEP_DIRS:
        assert (ROOT / d / "README.md").is_file(), f"{d}/ is missing a README.md"


def test_protected_eval_warning_present():
    text = (ROOT / "model" / "eval" / "README.md").read_text(encoding="utf-8")
    assert "never used for training" in text
    assert "protected" in text.lower()


def test_no_gitkeep_placeholders():
    assert not list(ROOT.rglob(".gitkeep"))


def test_scheduling_simulation_math():
    from scheduling.simulate import simulate

    series = [0.5, 0.9, 0.9]
    result = simulate(series, threshold=0.8)
    # Two of three periods clear the threshold, so one third of work is deferred.
    assert round(result.deferred_fraction, 4) == round(1 / 3, 4)
    # Scheduled share averages the two eligible periods (0.9), beating the baseline.
    assert result.scheduled_renewable_share == 0.9
    assert result.clean_energy_gain > 0
