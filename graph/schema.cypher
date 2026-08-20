// Sovereign Agentic Pipeline — knowledge graph schema (Neo4j Community).
//
// Applied by `make graph`. Every statement is IF NOT EXISTS, so this file is idempotent:
// run it as many times as you like. Neo4j is schema-optional, so "the schema" here is the
// set of uniqueness constraints and indexes that keep the graph honest, plus the node and
// relationship model documented in comments below.
//
// The model exists to make the core methodology rule STRUCTURAL: a Claim links to the
// Source it came from and a Number links to the Claim it supports, so an untraceable
// number cannot be represented.
//
// ----------------------------------------------------------------------------------------
// NODE LABELS
//   (:Source)   a primary source — coverage, submission, official statement, dataset, report
//   (:Claim)    an assertion drawn from one or more sources
//   (:Number)   a specific quantitative value backing a claim (with unit + as-of date)
//   (:Entity)   an organisation, agency, or company in the debate
//   (:Facility) a physical site — a data centre, a power station, a substation
//   (:Policy)   a regulation, consent, submission process, or official position
//   (:Person)   a named individual (author, spokesperson, submitter)
//
// RELATIONSHIPS (created at load time by graph/loaders/load_corpus.py)
//   (:Claim)    -[:SUPPORTED_BY]->   (:Source)     a claim traces to its source(s)
//   (:Number)   -[:EVIDENCES]->      (:Claim)      a number backs a claim
//   (:Number)   -[:FROM_SOURCE]->    (:Source)     a number traces to its source
//   (:Claim)    -[:ABOUT]->          (:Entity|:Facility|:Policy)   what the claim concerns
//   (:Source)   -[:AUTHORED_BY]->    (:Person)     byline / submitter
//   (:Person)   -[:AFFILIATED_WITH]->(:Entity)     who someone speaks for
//   (:Entity)   -[:OPERATES]->       (:Facility)   who runs a site
//   (:Facility) -[:LOCATED_IN]->     (:Entity)     region / territorial authority
//   (:Policy)   -[:APPLIES_TO]->     (:Facility)   which consent/rule governs a site
//   (:Source)   -[:TAKES_POSITION]-> (:Policy)     climate-first / growth-first stance
// ----------------------------------------------------------------------------------------

// --- Uniqueness constraints (each also creates a backing index) ---
CREATE CONSTRAINT source_id   IF NOT EXISTS FOR (s:Source)   REQUIRE s.id   IS UNIQUE;
CREATE CONSTRAINT claim_id    IF NOT EXISTS FOR (c:Claim)    REQUIRE c.id    IS UNIQUE;
CREATE CONSTRAINT number_id   IF NOT EXISTS FOR (n:Number)   REQUIRE n.id    IS UNIQUE;
CREATE CONSTRAINT entity_id   IF NOT EXISTS FOR (e:Entity)   REQUIRE e.id    IS UNIQUE;
CREATE CONSTRAINT facility_id IF NOT EXISTS FOR (f:Facility) REQUIRE f.id    IS UNIQUE;
CREATE CONSTRAINT policy_id   IF NOT EXISTS FOR (p:Policy)   REQUIRE p.id    IS UNIQUE;
CREATE CONSTRAINT person_id   IF NOT EXISTS FOR (p:Person)   REQUIRE p.id    IS UNIQUE;

// --- Indexes for the fields we filter and search on most ---
CREATE INDEX source_publisher IF NOT EXISTS FOR (s:Source)   ON (s.publisher);
CREATE INDEX source_camp      IF NOT EXISTS FOR (s:Source)   ON (s.camp);
CREATE INDEX source_date      IF NOT EXISTS FOR (s:Source)   ON (s.pub_date);
CREATE INDEX claim_topic      IF NOT EXISTS FOR (c:Claim)    ON (c.topic);
CREATE INDEX number_unit      IF NOT EXISTS FOR (n:Number)   ON (n.unit);
CREATE INDEX entity_name      IF NOT EXISTS FOR (e:Entity)   ON (e.name);
CREATE INDEX facility_region  IF NOT EXISTS FOR (f:Facility) ON (f.region);

RETURN "schema applied" AS status;
