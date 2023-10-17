-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures 
WHERE MONTH(date_column) IN (7, 8) -- Assuming the column that stores the date is named "date_column"
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
