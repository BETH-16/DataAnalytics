USE sample_sales;
-- 2. Which transactions had a sale amount greater than $500? Display the transaction date, store ID, product number, and sale amount 
SELECT  date,  prodnum, SalesTotal
from online_sales
where SalesTotal > 500;
describe online_sales;
describe store_sales;
select transaction_date, store_id, prod_num, sale_amount
from store_sales
where Sale_Amount > 500;
-- 4. What is the total sales revenue across all transactions? What is the average transaction amount?
select 
    sum(salestotal) as total_revenue,
    avg(salestotal) as average_transaction
from ( 
   select salestotal from online_sales
   union all 
   select sale_amount from store_sales
) AS all_sales;
-- 13. Write a query that shows total sales by region. Which region generates the most revenue? 
select 
    shiptostate as region, 
    sum(salestotal) as total_sales
from online_sales
group by ShiptoState
order by total_sales desc;  

select 
     Store_ID as store,
     sum(Sale_Amount) as total_sales
from store_sales
group by Store_ID
order by total_sales desc;
-- 19. Find the top 5 highest-grossing stores, then use that result to look up their city and state from Store_Locations.
select store_ID, sum(sale_amount) as total_revenue
from store_sales
group by store_ID
order by total_revenue desc
limit 5;
select bt.Storeid, bt.StoreLocation, bt.state, top.total_revenue
from store_locations bt 
join (
     select Store_ID, sum(sale_amount) as total_Revenue
     FROM Store_sales
     group by Store_ID
     order by total_Revenue DESC 
     limit 5 ) 
     TOP
     ON bt.StoreID = top.Store_ID;
describe store_locations;