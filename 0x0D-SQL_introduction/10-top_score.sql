-- show best
SELECT score, name 
FROM second_table
GROUP BY score, name
ORDER BY score DESC;
