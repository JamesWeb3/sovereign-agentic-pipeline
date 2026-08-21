# graph/queries/ — named example queries

Each `.cypher` file answers one question, stated in a comment at the top. Run them in the
Neo4j Browser (http://localhost:7474) or with `cypher-shell` against a loaded graph.

- `sources_by_camp.cypher` — how the corpus splits across the climate-first / growth-first
  divide.
- `untraceable_numbers.cypher` — the methodology check: any Number not tied to a Source.
- `claims_about_facility.cypher` — every claim (and its sources) about a given facility.

Add a new file per question; keep the leading comment so the folder stays self-describing.
