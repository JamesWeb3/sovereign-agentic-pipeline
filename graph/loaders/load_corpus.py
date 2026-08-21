"""Load the source register (research/corpus.csv) into the Neo4j knowledge graph.

Upserts one (:Source) node per row, keyed on `source_id`, so re-running is idempotent.
As the corpus grows, extend this to also create the Claim/Number nodes each source backs
(the `claim_ids` column already lists them).

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

from neo4j import GraphDatabase

CORPUS_CSV = Path(__file__).resolve().parents[1].parent / "research" / "corpus.csv"

UPSERT_SOURCE = """
MERGE (s:Source {id: $source_id})
SET s.title      = $title,
    s.publisher  = $publisher,
    s.pub_date   = $pub_date,
    s.url        = $url,
    s.retrieved_at = $retrieved_at
RETURN s.id AS id
"""


def read_corpus(path: Path = CORPUS_CSV) -> list[dict[str, str]]:
    """Return the corpus rows as dicts. Raises if the file or its header is missing."""
    if not path.exists():
        raise FileNotFoundError(f"corpus not found at {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if rows and "source_id" not in rows[0]:
        raise ValueError("corpus.csv is missing the required 'source_id' column")
    return rows


def load(rows: list[dict[str, str]], driver) -> int:
    """Upsert each row as a :Source node. Returns the number of sources written."""
    written = 0
    with driver.session() as session:
        for row in rows:
            session.run(
                UPSERT_SOURCE,
                source_id=row["source_id"],
                title=row.get("title", ""),
                publisher=row.get("publisher", ""),
                pub_date=row.get("pub_date", ""),
                url=row.get("url", ""),
                retrieved_at=row.get("retrieved_at", ""),
            )
            written += 1
    return written


def main() -> None:
    uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD", "sovereign_dev_pw")

    rows = read_corpus()
    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        count = load(rows, driver)
    finally:
        driver.close()
    print(f"Upserted {count} source(s) from {CORPUS_CSV}")


if __name__ == "__main__":
    main()
