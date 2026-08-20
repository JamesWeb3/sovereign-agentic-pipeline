# Contributing

This is a public, open-notebook project. The point is that anyone can check our working
— so how we commit matters as much as what we commit.

## Two rules above all others

1. **Commit little and often.** Small commits that show the thinking beat one big drop.
   Half-finished analysis, a notebook that doesn't reach a conclusion yet, a dead end you
   want on record — all of it goes in. The commit history *is* the research trail.
2. **Every number gets a source or a calculation.** A figure you can't trace back to a
   primary source (with a URL and a retrieval date) or to a calculation in this repo is a
   figure we delete. No exceptions. See [docs/methodology.md](docs/methodology.md).

## Workflow

- Branch off `main`, open a pull request, keep the diff small.
- Reference the plan Step your change serves (the directory READMEs name it).
- CI runs `ruff check` and `pytest` on every push and PR — keep it green.
- Run `make lint` and `make test` locally before you push.

## What must NEVER be committed

This repo is public. Before every commit, check you are not adding:

- **Secrets** — API keys, tokens, passwords, `.env`. Only `.env.example` belongs here.
- **Gitignored data** — anything under `data/raw/`. Register its provenance in
  [data/README.md](data/README.md) instead and keep the bytes out of git.
- **Anything you can't redistribute** — content under a licence that forbids
  redistribution. When in doubt, link to the source rather than copying it in.

If you commit a secret by accident, rotate it immediately — rewriting history is not
enough once it is public.

## Style

- Python: 3.12, formatted and linted with `ruff` (config in `pyproject.toml`).
- Sources: one Markdown file per primary source in `research/sources/`, with the
  frontmatter schema documented in that directory's README.
- Commit messages: imperative mood, say what changed and why in one line.
