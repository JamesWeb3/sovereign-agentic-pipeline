// Question: how does the source corpus split across the debate's two camps?
// Gives a quick read on whether we are steel-manning both sides or leaning one way.
MATCH (s:Source)
RETURN s.camp AS camp, count(*) AS sources
ORDER BY sources DESC;
