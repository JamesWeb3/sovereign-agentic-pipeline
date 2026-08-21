# retrieval/ — RAGFlow over the graph

**Plan Step:** Step 6 (Part B — pipeline) · **Lead:** James → Karl
**Status:** scaffolded only. Part B starts week 10; do not implement ahead of that.

## What this will be

Graph-aware retrieval with **RAGFlow**, querying over the Neo4j knowledge graph (`graph/`)
rather than a flat vector store — so an answer can walk `Claim → Source` and cite what it
leaned on. Self-hosted; no hosted embedding or inference API.

**Done** when RAGFlow retrieves over the graph and returns passages with their source
provenance intact, ready for the agent (Step 8) to consume.
