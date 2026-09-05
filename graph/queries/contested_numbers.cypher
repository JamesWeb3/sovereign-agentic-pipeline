// Question: which claims carry more than one number, and do those numbers actually disagree?
//
// This is the query the whole graph exists for. A spreadsheet forces one value per cell;
// here every figure survives with the `basis` that says what it measures.
//
// `comparable` is the column that matters. Two numbers on one claim are only a candidate
// disagreement when they share a unit — 220,752,000 L/yr against 66,000,000 L/yr is a
// real question, while 84 units and 10,000 L are simply two attributes of the same claim.
// Karl's contradiction table found that most apparent contradictions in this corpus are
// the second kind: 550 people, 1,200 roles and 5,751 jobs/yr are three sources answering
// three different questions, and flattening them into a disagreement is the mistake.
MATCH (n:Number)-[:EVIDENCES]->(c:Claim)
MATCH (n)-[:FROM_SOURCE]->(s:Source)
WITH c, n, s
ORDER BY n.value DESC
WITH c,
     collect({
       value: n.value,
       unit: n.unit,
       basis: n.basis,
       as_of: n.as_of,
       source: s.publisher
     }) AS figures,
     count(DISTINCT n.unit) AS units
WHERE size(figures) > 1
RETURN c.id    AS claim,
       c.topic AS topic,
       size(figures) AS how_many,
       units < size(figures) AS comparable,
       figures
ORDER BY comparable DESC, how_many DESC, claim;
