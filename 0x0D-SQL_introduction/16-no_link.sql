-- LIST RECORDS BASED ON SOME INFO
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
