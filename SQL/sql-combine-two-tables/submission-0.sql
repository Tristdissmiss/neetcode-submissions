-- Write your query below 
select p.first_name, p.last_name, a.city, a.state
From person p 
LEFT JOIN address a on a.person_id = p.person_id 
