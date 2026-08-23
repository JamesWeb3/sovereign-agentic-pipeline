# Sovereign Agentic Pipeline

A fully open-source **Sovereign Agentic Pipeline for New Zealand**: an AI system a NZ
business can run end to end on NZ renewable compute, built entirely from open-source
parts, where no data ever leaves the country and every layer is inspectable and
swappable. This repo is the research trail and the build — worked in the open, commit
by commit, from August to December 2026.

> **The binding constraint on every design decision here:** the moment one layer is a
> foreign API, the sovereignty claim dies and so does the energy claim — because you no
> longer know what grid the compute ran on. Everything self-hosted, everything open
> source, no hosted inference anywhere in the pipeline.

## The research question

> **What is the most viable way to build data centres that support the massive growth of
> AI and inference, while simultaneously building out renewable energy infrastructure,
> and could New Zealand lead on this model?**

Two proofs sit on top of the pipeline:

1. **It can run clean here.** The first published, checkable number for what a token of
   inference costs in NZ and on what electricity — plus whether compute can be scheduled
   to follow renewable generation while holding SLAs.
2. **It is worth paying for.** ROI cases for four NZ business types (law firm, healthcare
   provider, local council, accounting firm) with break-even points against hosted
   commercial APIs.

## The stack (all open source)

| Layer | Tool | Lead |
|---|---|---|
| Knowledge graph | Neo4j Community | James → Karl |
| Model | Mistral open weights + LoRA | James |
| Retrieval | RAGFlow (graph-aware, over Neo4j) | James → Karl |
| Tool protocol | MCP — own server, 4 tools | James → Karl |
| Agent logic | LangChain | James |
| Orchestration | Dify | Karl |
| Interface | Open WebUI | Karl |
| Voice | Whisper STT + Piper/Kokoro TTS, all local | Karl |

## Quickstart

You need [Docker](https://docs.docker.com/get-docker/) (Desktop is fine) and `make`.
Nothing else — no Python install required to bring up the graph.

```bash
cp .env.example .env      # the default dev password is fine for local work
make up                   # starts Neo4j Community in Docker
make graph                # applies graph/schema.cypher to the running database
```

Then open the Neo4j Browser at **http://localhost:7474** (Bolt on `:7687`) and sign in
with the credentials from your `.env` (`neo4j` / the `NEO4J_PASSWORD` you set).

`make down` stops everything. `make graph` is idempotent — every constraint and index is
declared `IF NOT EXISTS`, so you can re-run it safely.

## Repo map

Each directory carries its own `README.md` stating which plan Step it serves, who leads
it, and what "done" means. `[A]` = Part A (evidence, weeks 1–9, Karl leads). `[B]` =
Part B (pipeline, weeks 10–18, James leads engineering — scaffolded only for now).

```
sovereign-agentic-pipeline/
├── README.md                  # this file
├── LICENSE                    # Apache-2.0
├── CONTRIBUTING.md            # commit little and often; every number gets a source
├── docker-compose.yml         # Neo4j now; RAGFlow/Dify/Open WebUI stubbed + commented
├── Makefile                   # make up | down | graph | lint | test
├── pyproject.toml             # Python 3.12, ruff + pytest; deps grouped per part
├── .env.example               # copy to .env
├── .github/                   # CI (ruff + pytest) and the Step issue template
├── docs/                      # methodology, architecture decisions, weekly log
├── research/     [A] Step 1   # Southland landscape from primary sources — KARL
├── graph/        [A] Step 1   # Neo4j schema + corpus loader + example queries — KARL
├── grid/         [A] Step 2   # EMI half-hourly NZ generation data
├── energy/       [A] Step 3   # measured watt-hours per 1000 tokens
├── scheduling/   [A] Step 4   # can compute follow renewable generation?
├── model/        [B] Step 5   # Mistral + LoRA (dataset + protected held-out eval)
├── retrieval/    [B] Step 6   # RAGFlow over the graph
├── mcp_server/   [B] Step 7   # own MCP server, 4 tools
├── agent/        [B] Step 8   # LangChain + exported Dify workflows
├── voice/        [B] Step 9   # Whisper STT + Piper/Kokoro TTS, local only
├── roi/          [B] Step 10  # four NZ business ROI cases
├── report/       [B] Step 11  # the published write-up
├── notebooks/                 # exploratory analysis, one per evidence step
└── data/                      # provenance register; data/raw is gitignored
```

## The evidence rules

This is a research repo before it is a code repo. The non-negotiables — every number
gets a source or a calculation, negative results count, primary sources only, the
protected held-out eval — live in **[docs/methodology.md](docs/methodology.md)**. Read
them before you add a figure.

## Contributors

- **James Oldham** — Sentry AI (sponsor, engineering lead for Part B)
- **Karl Belleza** — researcher (leads Part A)

## Licence

[Apache-2.0](LICENSE). This repo is public from commit one; keep it that way (see
[CONTRIBUTING.md](CONTRIBUTING.md) on what must never be committed).


## Karl's Description of the project

This is a project/research based on figuiring out if New Zealand can build AI data centres on renewable energy (research) and building an AI agent system under sovereign and energy constraints in order to work alongside renewable energy and not go against it

The project is split into two parts, the first part is the evidence which Karl will be in charge of building upon the research corpus and implementing techniques from Neo4j knowledge graph linkiing sources, causes and people affected in the data center crisis.

The second part is the pipeline phase which actually tries out the agent stack, using Mistral open-weights model, LoRA fine tune, RAGFlow retrieval over the graph, a custom MCP tool server, LangChain agent logic, Dify orchestration, Open WebUI interface, local Whisper/Piper voice.

Overall the first part of this project will be mostly gathering evidence and fuelling the research corpus, in which Karl's evidence will be supplemented with learning how to use Neo4j properly and being able to hopefully implement a system design which can later on be used into the pipeline stages.