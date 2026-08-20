# mcp_server/ — our own MCP server, 4 tools

**Plan Step:** Step 7 (Part B — pipeline) · **Lead:** James → Karl
**Status:** scaffolded only. Part B starts week 10; do not implement ahead of that.

## What this will be

Our own [Model Context Protocol](https://modelcontextprotocol.io) server exposing **four
tools** the agent calls — the clean boundary between the model layer and the data layer.
MCP is what lets us swap the model without touching the tools, and vice versa; that
decoupling is a teaching goal of the project, not just an implementation detail.

Self-hosted; the tools reach only local resources (the graph, retrieval, the grid/energy
data) — never a foreign API.

**Done** when the server runs locally and exposes four working, documented tools the agent
(Step 8) can call over MCP.
