use northwind;
-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write asecond query to find the name of the product that has that price.
select MIN(unitprice) as cheapestprice
FROM products;
-- 2. Write a query to find the average price of all items that Northwind sells.
select  AVG(unitprice) AS Averageprice
from products;
select round(avg(unitprice), 2) as averageprice
from products;
-- 3.Write a query to find the price of the most expensive item that Northwind sells. Then write asecond query to find the name of the product with that price, plus the name of the supplier for that product;
select MAX(UNITPRICE) AS mostexpensiveprice 
from products;
select p.productname, s.companyname as suppliername  
from products P
join suppliers s on p.supplierid = s.supplierid
where p.unitprice = (
select max(unitprice)
from products 
);
-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;
-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)
SELECT 
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;
-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here
SELECT 
    s.SupplierID,
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;
-- 7. Write a query to find the list of all category names and the average price for items in each category
SELECT 
    c.CategoryName,
    AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;
-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.
SELECT 
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;
-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units onhand). Sort the results in descending order by value. If two or more have the samevalue, order by product name. If a product is not in stock, leave it off the list.
SELECT 
    ProductID,
    ProductName,
    UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY 
    InventoryValue DESC,
    ProductName ASC;
