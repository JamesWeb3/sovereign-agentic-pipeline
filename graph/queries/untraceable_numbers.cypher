// Question: are there any Numbers in the graph NOT tied back to a Source?
// This is the methodology guard rail made queryable — the result should always be empty.
// Any row returned is a figure we must trace or delete (docs/methodology.md).
MATCH (n:Number)
WHERE NOT (n)-[:FROM_SOURCE]->(:Source)
RETURN n.id AS number_id, n.value AS value, n.unit AS unit
ORDER BY number_id;
