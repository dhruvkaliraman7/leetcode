WITH countTable AS (
    SELECT num, COUNT(*) AS countCount
    FROM mynumbers
    GROUP BY num
    ORDER BY num DESC
)

SELECT 
    CASE 
        WHEN (SELECT COUNT(*) FROM countTable) = 0 THEN NULL
        ELSE (SELECT num FROM countTable WHERE countCount = 1 LIMIT 1)
    END AS num;
