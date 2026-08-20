# 1. Record architecture decisions

Date: 2026-08-20
Status: Accepted

## Context

This project makes a chain of architectural choices — a knowledge graph over a document
store, an MCP server as the tool boundary, self-hosting over hosted inference — and the
reasons matter as much as the choices. A public, open-notebook project needs those
reasons on the record so a reader (or a future contributor, or Karl six weeks from now)
can see *why*, not just *what*.

## Decision

We keep Architecture Decision Records (ADRs) in `docs/decisions/`, one Markdown file per
decision, numbered sequentially (`0001-...`, `0002-...`). Each records the context, the
decision, and its consequences. Superseded ADRs are kept, not deleted, and marked as
superseded — the trail of thinking is part of the deliverable.

The format follows Michael Nygard's ADR pattern
(<https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>).

## Consequences

- Every non-obvious architectural choice gets a short, linkable record.
- The overriding project constraint — **no foreign API anywhere in the pipeline, because
  the moment one layer is hosted the sovereignty and energy claims both collapse** — is
  the backdrop against which future ADRs are judged. Any proposal that reaches for a
  hosted service must argue against that constraint explicitly in its own ADR.
