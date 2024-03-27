# Write your MySQL query statement below
with newq as (
    select *,
    sum(weight) over(order by turn) as cumSum 
    from queue
)

select person_name
from newq
where cumSum<=1000
order by cumSum desc
limit 1


