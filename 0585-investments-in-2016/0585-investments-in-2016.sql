WITH newTable AS (
    SELECT pid
    FROM insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
),
newTable1 AS (
    SELECT pid
    FROM insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) = 1
)
SELECT round(SUM(tiv_2016),2) as tiv_2016
FROM insurance
WHERE pid IN (SELECT pid FROM newTable)
AND pid NOT IN (SELECT pid FROM newTable1);
