# graph/ — the knowledge graph

**Plan Step:** Step 1 (Part A — evidence)
**Lead:** James → Karl
**Serves:** structured, traceable storage for every claim and number in the research;
the substrate the RAGFlow retrieval layer (Step 6) queries over.

## What this is

A Neo4j Community knowledge graph that models the Southland debate as
`Source → Claim → Number` chains, so that every number is structurally tied to the source
it came from. If it isn't traceable, it can't be represented — that is the whole point.

## Files

- `schema.cypher` — the node/relationship model, as uniqueness constraints and indexes.
  Idempotent (`IF NOT EXISTS` throughout). Applied by `make graph`.
- `loaders/load_corpus.py` — reads `research/corpus.csv` and upserts `Source` nodes (and,
  as the corpus grows, the claims/numbers linked to them) into the graph over Bolt.
- `queries/` — named `.cypher` files, each with a comment saying what question it answers.

## Quickstart

```bash
make up      # start Neo4j
make graph   # apply schema.cypher
# then, once you have Python deps (pip install -e ".[part-a]"):
python graph/loaders/load_corpus.py
```

Open the browser at http://localhost:7474 and run anything in `queries/`.

## The model

`Source, Claim, Number, Entity, Facility, Policy, Person` with the relationships
documented at the top of `schema.cypher`. The load order is: sources first (from
`corpus.csv`), then the claims and numbers extracted from them, each linked back.

## Definition of done (Step 1, graph half)

- `make graph` applies `schema.cypher` with no error on a clean clone.
- `load_corpus.py` populates `Source` nodes from `corpus.csv` idempotently (re-running
  does not duplicate).
- The example queries in `queries/` return sensible results against a loaded corpus.
