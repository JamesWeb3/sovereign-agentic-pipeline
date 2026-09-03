"""Load the evidence base (research/*.csv) into the Neo4j knowledge graph.

Three registers, loaded in dependency order, all idempotent so re-running is safe:

    research/corpus.csv   one row per Source, plus the claim_ids it backs
    research/claims.csv   one row per Claim, and what the claim is about
    research/numbers.csv  one row per Number, tied to its Claim and its Source

The point of splitting them is the methodology rule in docs/methodology.md: a figure
that cannot be traced is a figure we delete. Here that rule is structural rather than
aspirational, because a Number row carries a mandatory `source_id` and the loader
refuses the file if any reference does not resolve. `graph/queries/untraceable_numbers.cypher`
should therefore always return nothing; if it ever returns a row, this loader has a bug.

The second reason for a separate numbers register is that **a Claim may carry more than
one Number, and that is the normal case rather than an error**. Datagrid's Makarewa
consent allows 220,752,000 L/yr while Datagrid says it expects to use 66,000,000. Those
are not a contradiction to resolve by deleting one, they are a consent limit and an
operator expectation, which is why every Number carries a `basis` describing what it
actually measures. Picking a winner would throw away the finding.

Usage:
    pip install -e ".[part-a]"
    make up && make graph          # database up, schema applied
    python graph/loaders/load_corpus.py

Connection is read from the environment (see .env.example):
    NEO4J_URI (default bolt://localhost:7687), NEO4J_USER, NEO4J_PASSWORD
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

# `neo4j` is imported inside main() rather than here on purpose: CI installs only ruff
# and pytest, so the register-validation tests must be able to import this module
# without a database driver present. Everything above main() is pure Python.

RESEARCH = Path(__file__).resolve().parents[2] / "research"
CORPUS_CSV = RESEARCH / "corpus.csv"
CLAIMS_CSV = RESEARCH / "claims.csv"
NUMBERS_CSV = RESEARCH / "numbers.csv"

# A Claim points at whatever it concerns. The label is chosen per row rather than
# hard-coded, so a claim about the grid and a claim about the site both work; the
# schema constrains all four on `id`.
ABOUT_LABELS = {"Facility", "Entity", "Policy", "Person"}

UPSERT_SOURCE = """
MERGE (s:Source {id: $source_id})
SET s.title      = $title,
    s.publisher  = $publisher,
    s.pub_date   = $pub_date,
    s.url        = $url,
    s.retrieved_at = $retrieved_at
RETURN s.id AS id
"""

UPSERT_CLAIM = """
MERGE (c:Claim {id: $claim_id})
SET c.topic     = $topic,
    c.statement = $statement
RETURN c.id AS id
"""

# The about-node label is interpolated, never the values. ABOUT_LABELS gates it, so a
# bad register cannot inject a label — an unknown one raises before we reach Cypher.
LINK_CLAIM_ABOUT = """
MATCH (c:Claim {{id: $claim_id}})
MERGE (t:{label} {{id: $about_id}})
MERGE (c)-[:ABOUT]->(t)
"""

LINK_CLAIM_SOURCE = """
MATCH (c:Claim {id: $claim_id})
MATCH (s:Source {id: $source_id})
MERGE (c)-[:SUPPORTED_BY]->(s)
"""

UPSERT_NUMBER = """
MATCH (c:Claim {id: $claim_id})
MATCH (s:Source {id: $source_id})
MERGE (n:Number {id: $number_id})
SET n.value = $value,
    n.unit  = $unit,
    n.as_of = $as_of,
    n.basis = $basis,
    n.note  = $note
MERGE (n)-[:EVIDENCES]->(c)
MERGE (n)-[:FROM_SOURCE]->(s)
RETURN n.id AS id
"""


def _read(path: Path, key: str) -> list[dict[str, str]]:
    """Read a register, raising rather than returning junk if it is missing a key column."""
    if not path.exists():
        raise FileNotFoundError(f"register not found at {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if rows and key not in rows[0]:
        raise ValueError(f"{path.name} is missing the required '{key}' column")
    return rows


def read_corpus(path: Path = CORPUS_CSV) -> list[dict[str, str]]:
    return _read(path, "source_id")


def read_claims(path: Path = CLAIMS_CSV) -> list[dict[str, str]]:
    return _read(path, "claim_id")


def read_numbers(path: Path = NUMBERS_CSV) -> list[dict[str, str]]:
    return _read(path, "number_id")


def claim_ids_for(row: dict[str, str]) -> list[str]:
    """Split a corpus row's semicolon-separated claim_ids, dropping blanks."""
    return [c.strip() for c in (row.get("claim_ids") or "").split(";") if c.strip()]


def check_references(
    corpus: list[dict[str, str]],
    claims: list[dict[str, str]],
    numbers: list[dict[str, str]],
) -> None:
    """Fail before touching the database if any reference does not resolve.

    A half-loaded graph is worse than no graph: the untraceable-numbers query would
    come back clean simply because the offending rows never made it in.
    """
    source_ids = {r["source_id"] for r in corpus}
    claim_ids = {r["claim_id"] for r in claims}
    problems: list[str] = []

    for row in corpus:
        for cid in claim_ids_for(row):
            if cid not in claim_ids:
                problems.append(
                    f"corpus.csv: {row['source_id']} backs '{cid}', which is not in claims.csv"
                )

    for row in claims:
        label = (row.get("about_type") or "").strip()
        if label and label not in ABOUT_LABELS:
            problems.append(
                f"claims.csv: {row['claim_id']} has about_type '{label}'; "
                f"expected one of {sorted(ABOUT_LABELS)}"
            )

    for row in numbers:
        try:
            float(row["value"])
        except (KeyError, TypeError, ValueError):
            problems.append(
                f"numbers.csv: {row['number_id']} has non-numeric value "
                f"{row.get('value')!r}; a Number that cannot be compared is not a Number"
            )
        if row["claim_id"] not in claim_ids:
            problems.append(
                f"numbers.csv: {row['number_id']} evidences '{row['claim_id']}', "
                "which is not in claims.csv"
            )
        if not (row.get("source_id") or "").strip():
            problems.append(f"numbers.csv: {row['number_id']} has no source_id")
        elif row["source_id"] not in source_ids:
            problems.append(
                f"numbers.csv: {row['number_id']} cites '{row['source_id']}', "
                "which is not in corpus.csv"
            )

    if problems:
        raise ValueError(
            "evidence base does not resolve, nothing was loaded:\n  "
            + "\n  ".join(problems)
        )


def load(
    corpus: list[dict[str, str]],
    claims: list[dict[str, str]],
    numbers: list[dict[str, str]],
    driver,
) -> dict[str, int]:
    """Upsert sources, then claims and what they are about, then numbers.

    Order matters: a Number matches on an existing Claim and Source rather than
    creating them, so a typo fails loudly instead of quietly minting an empty node.
    """
    counts = {"sources": 0, "claims": 0, "numbers": 0, "claim_source_links": 0}
    with driver.session() as session:
        for row in corpus:
            session.run(
                UPSERT_SOURCE,
                source_id=row["source_id"],
                title=row.get("title", ""),
                publisher=row.get("publisher", ""),
                pub_date=row.get("pub_date", ""),
                url=row.get("url", ""),
                retrieved_at=row.get("retrieved_at", ""),
            )
            counts["sources"] += 1

        for row in claims:
            session.run(
                UPSERT_CLAIM,
                claim_id=row["claim_id"],
                topic=row.get("topic", ""),
                statement=row.get("statement", ""),
            )
            counts["claims"] += 1
            label = (row.get("about_type") or "").strip()
            about_id = (row.get("about_id") or "").strip()
            if label and about_id:
                session.run(
                    LINK_CLAIM_ABOUT.format(label=label),
                    claim_id=row["claim_id"],
                    about_id=about_id,
                )

        for row in corpus:
            for cid in claim_ids_for(row):
                session.run(
                    LINK_CLAIM_SOURCE, claim_id=cid, source_id=row["source_id"]
                )
                counts["claim_source_links"] += 1

        for row in numbers:
            session.run(
                UPSERT_NUMBER,
                number_id=row["number_id"],
                claim_id=row["claim_id"],
                source_id=row["source_id"],
                # float, not the raw string. Stored as text, Neo4j sorts a Number
                # lexically, which puts 66000000 above 604800 and makes every
                # comparison in the graph quietly wrong.
                value=float(row["value"]),
                unit=row.get("unit", ""),
                as_of=row.get("as_of", ""),
                basis=row.get("basis", ""),
                note=row.get("note", ""),
            )
            counts["numbers"] += 1

    return counts


def main() -> None:
    uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD", "sovereign_dev_pw")

    from neo4j import GraphDatabase

    corpus = read_corpus()
    claims = read_claims()
    numbers = read_numbers()
    check_references(corpus, claims, numbers)

    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        counts = load(corpus, claims, numbers, driver)
    finally:
        driver.close()

    print(
        f"Upserted {counts['sources']} source(s), {counts['claims']} claim(s), "
        f"{counts['numbers']} number(s), {counts['claim_source_links']} claim-source link(s)."
    )


if __name__ == "__main__":
    main()
