# agent/ — LangChain agent + exported Dify workflows

**Plan Step:** Step 8 (Part B — pipeline) · **Lead:** James
**Status:** scaffolded only. Part B starts week 10; do not implement ahead of that.

## What this will be

The agent logic in **LangChain**, calling the MCP tools (Step 7) over the retrieval layer
(Step 6), with orchestration authored in **Dify** and its workflows **exported into this
repo** so the pipeline is reproducible from git rather than trapped in a running instance.

Local model, local tools, local orchestration — no hosted inference.

**Done** when the agent answers NZ-domain questions end to end using the local model and
the MCP tools, with the Dify workflow exported here.
