select email from person group by email having count(*)>1

select email from (select email, count(*) as email_count from Person group by email) as email_count where email_count>1