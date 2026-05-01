use sample_sales;
select * from sample_sales.management;
--- 4a. What is total revenue overall for sales in the assigned territory, plus the start date and end datethat tell you what period the data covers?
select
SUM(Sale_Amount) as total_revenue,
MIN(Transaction_Date) as start_date,
MAX(Transaction_Date) as end_date
from store_sales 
where store_ID between 840 and 851;
describe store_sales;
-- 4b. What is the month by month revenue breakdown for the sales territory?
describe store_locations;
SELECT StoreId, State, StoreLocation
FROM Store_Locations;
 -- this 2 querries above are not part of this specific question they are me troubleshooting in the middle
 SELECT  
    YEAR(Transaction_Date) AS year,
    MONTH(Transaction_Date) AS month_number,
    SUM(Sale_Amount) AS monthly_revenue
FROM store_sales
WHERE Store_ID BETWEEN 840 AND 851
GROUP BY YEAR(Transaction_Date), MONTH(Transaction_Date)
ORDER BY year, month_number;
-- 4c. Provide a comparison of total revenue for the specific sales territory and the region it belongs to.
 SELECT 
    'Territory (840–851)' AS level,
    SUM(Sale_Amount) AS total_revenue
FROM store_sales
WHERE Store_ID BETWEEN 840 AND 851

UNION ALL

SELECT 
    'Full New York Region' AS level,
    SUM(s.Sale_Amount) AS total_revenue
FROM store_sales s
JOIN store_locations l
    ON s.Store_ID = l.StoreId
WHERE l.State = 'New York';
-- 4d. What is the number of transactions per month and average transaction size by product category for the sales territory
-- transaction per month
select 
	   Date_FORMAT(transaction_date, '%Y-%m') AS month,
       count(*) as transaction,
       avg(sale_amount) as avg_transaction_size
from store_sales
where store_id between 840 and 851
group by
 DATE_FORMAT(transaction_date, '%Y-%m')
order by  month; 
-- avg transaction size by product category
SELECT 
    prod_num AS product_category,
    AVG(sale_amount) AS avg_transaction_size
FROM store_sales
WHERE store_id BETWEEN 840 AND 851
GROUP BY prod_num
ORDER BY avg_transaction_size DESC;
 -- 4e.provide a ranking of in-store sales performance by each store in the sales territory, or a ranking of online sales performance by state within an online sales territory
 select 
    store_id, 
    sum(sale_amount) as total_revenue
from store_sales
where store_id between 840 and 851
group by Store_ID
order by total_revenue desc;
-- 4f . What is your recommendation for where to focus sales attention in the next quarter?
-- Based on my analysis of the New York territory (Store_ID 840–851), the highest performing stores are 850 and 847, while the lowest revenue comes from 851 and 844. I recommend focusing more attention on improving the lower-performing stores by checking issues like sales activity, customer flow, or inventory.
 -- Also, products 105248-IT and 105250-IT show the highest transaction values, so these should be promoted more and kept well stocked.
-- Overall, the next quarter should focus on boosting weaker stores while maximizing sales from top products and high-performing locations.
