-- Lists all shows sorted by their rating in descending order
SELECT 
    ts.title AS show_title,
    SUM(tr.rating) AS rating_sum
FROM 
    tv_shows ts
JOIN 
    tv_show_ratings tr ON ts.id = tr.show_id
GROUP BY 
    ts.title
ORDER BY 
    rating_sum DESC;
