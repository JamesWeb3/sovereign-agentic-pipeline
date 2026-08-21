// Question: what does the corpus claim about a given facility, and on whose authority?
// Set $facility_id to the facility you care about (e.g. the Southland data-centre site).
// Returns each claim about it, the sources backing it, and the camp those sources sit in.
MATCH (c:Claim)-[:ABOUT]->(f:Facility {id: $facility_id})
MATCH (c)-[:SUPPORTED_BY]->(s:Source)
RETURN f.name    AS facility,
       c.id      AS claim,
       c.topic   AS topic,
       collect(DISTINCT s.publisher) AS sources,
       collect(DISTINCT s.camp)      AS camps
ORDER BY claim;
