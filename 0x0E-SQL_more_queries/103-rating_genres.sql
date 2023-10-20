-- Lists all genres sorted by their rating in descending order
SELECT 
    tg.name AS genre_name,
    COALESCE(SUM(tr.rating_value), 0) AS rating_sum
FROM 
    tv_genres tg
LEFT JOIN 
    tv_show_genres tsg ON tg.id = tsg.genre_id
LEFT JOIN 
    tv_show_ratings tr ON tsg.show_id = tr.show_id
GROUP BY 
    tg.name
ORDER BY 
    rating_sum DESC;
