-- show the number of appearance of a record
SELECT `score`, COUNT(*) AS number
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
