USE northwind;
-- 1. Write a query to list the product id, product name, and unit price of every product. This time, display them in ascending order by price.
SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC;
-- 2. What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price.
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;
-- 3. What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price. If two or more have the same price, list those in ascending order by product name.
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;
-- 4. Write a query against the orders table that displays the total number of distinct customers who have placed orders.
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;
-- 5. Write a query against the orders table that displays the total number of distinct customers by country, ordered by CustomerCount largest to smallest.
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;
-- 6. What are the products where we have less than 25 units on hand, but 1 or more units are on order? Order by quantity on order (high to low), then product name.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;
-- 7. List each job title in employees, along with a count of how many employees hold each job title.
SELECT Title, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;
-- 8. What employees have a monthly salary between $2000 and $2500? Order them by job title.
SELECT EmployeeID, FirstName, LastName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;
