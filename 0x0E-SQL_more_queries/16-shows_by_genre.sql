-- Lists all shows and their genres (if any)
SELECT 
    ts.title AS show_title, 
    IFNULL(tg.name, 'NULL') AS genre_name
FROM 
    tv_shows ts
LEFT JOIN 
    tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN 
    tv_genres tg ON tsg.genre_id = tg.id
ORDER BY 
    ts.title ASC, tg.name ASC;
