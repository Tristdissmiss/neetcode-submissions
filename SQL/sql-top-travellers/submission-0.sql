-- Write your query below  
select u.name AS name,COALESCE(SUM(r.distance),0) AS travelled_distance 
From users u 
LEFT JOIN rides r on u.id = r.user_id 
GROUP BY u.name 
order by travelled_distance DESC


