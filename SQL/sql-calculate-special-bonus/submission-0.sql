-- Write your query below

SELECT employee_id,
Case 
    when employee_id % 2 = 1 and name not like 'M%' then salary 
    else 0 
    end as bonus  
FROM employees 
ORDER BY employee_id
