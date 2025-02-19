-- delete from Person where id not in (select MIN(id) from Person group by email)

delete p from Person p
left join (select MIN(id) as id from Person GROUP BY email) AS Ids
ON p.id = Ids.id
WHERE Ids.id IS NULL;