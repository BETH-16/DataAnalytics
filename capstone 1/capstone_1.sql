use sample_sales;
select * from sample_sales.management;
--- 1. What is total revenue overall for sales in the assigned territory, plus the start date and end datethat tell you what period the data covers?
select
SUM(Sale_Amount) as total_revenue,
MIN(Transaction_Date) as start_date,
MAX(Transaction_Date) as end_date
from store_sales 
where store_ID= '1';
describe store_sales;
WITH territory_sales AS (
    SELECT *
    FROM store_sales
    WHERE Store_ID = 1
)
SELECT 
    SUM(Sale_Amount) AS total_revenue,
    MIN(Transaction_Date) AS start_date,
    MAX(Transaction_Date) AS end_date
FROM store_sales;
-- 2. What is the month by month revenue breakdown for the sales territory?
select 
month,
sum(sale_amount) as monthly_revenue  
from (
select 
transaction date 
sale_amount,

 
 
