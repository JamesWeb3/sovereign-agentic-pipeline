# Sovereign Agentic Pipeline — developer entry points.
# Quickstart:  cp .env.example .env && make up && make graph

# Load .env if present (KEY=VALUE lines only) so recipes see NEO4J_PASSWORD etc.
-include .env

NEO4J_PASSWORD ?= sovereign_dev_pw
NEO4J_CONTAINER ?= sap-neo4j

.DEFAULT_GOAL := help
.PHONY: help up down graph wait-neo4j lint test fmt

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-12s %s\n", $$1, $$2}'

up: ## Start Neo4j (Docker) in the background
	docker compose up -d neo4j

down: ## Stop everything and remove the containers
	docker compose down

wait-neo4j: ## Block until Neo4j reports healthy
	@echo "Waiting for Neo4j to become healthy..."
	@for i in $$(seq 1 40); do \
		status=$$(docker inspect --format '{{.State.Health.Status}}' $(NEO4J_CONTAINER) 2>/dev/null || echo "starting"); \
		if [ "$$status" = "healthy" ]; then echo "Neo4j is healthy."; exit 0; fi; \
		sleep 3; \
	done; \
	echo "ERROR: Neo4j did not become healthy in time. Check 'docker compose logs neo4j'."; exit 1

graph: up wait-neo4j ## Apply graph/schema.cypher to the running database (idempotent)
	@echo "Applying graph/schema.cypher..."
	docker compose exec -T neo4j cypher-shell -u neo4j -p "$(NEO4J_PASSWORD)" < graph/schema.cypher
	@echo "Schema applied."

lint: ## Lint the Python with ruff
	ruff check .

fmt: ## Auto-format the Python with ruff
	ruff format .

test: ## Run the test suite
	python -m pytest -q
