# Write your MySQL query statement below
with tmp as (
    select *,
    count(employee_id) over(partition by employee_id) as employeecount
    from employee
)

select employee_id, department_id
from tmp
where employeecount =1 or primary_flag = 'Y'