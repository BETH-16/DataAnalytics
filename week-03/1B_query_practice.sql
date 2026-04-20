USE northwind;
-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT productId, productname, unitprice
FROM PRODUCTS; 
-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT productId, productname, UnitsInStock
FROM products
where unitprice <=7.50;
-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?
SELECT  productname, unitsInstock, unitsonorder
FROM products
where UnitsInStock = 0
AND UnitsOnOrder >= 1;
-- 4. Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries ending with seafood items.
SELECT productid, productname, categoryID
FROM products;
-- VIEW all categories
 SELECT *
 FROM categories;
 -- get seafood caregoryID
 SELECT categoryID, categoryname
 FROM categories
 WHERE CategoryName = 'seafood';
 -- list all seafood products
 select productID, productname, unitprice
 FROM products
 WHERE CategoryID = (
 SELECT categoryID
 FROM categories
 WHERE CategoryName = 'seafood' );
 -- 5. Examine the products table again. How do you know what supplier each product comes from? Find Tokyo Traders products.
 -- View supplier IDs in Products
SELECT ProductID, ProductName, SupplierID
FROM Products;
-- Find Tokyo Traders supplier ID
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';
-- All products from Tokyo Traders
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE SupplierID = (
    SELECT SupplierID
    FROM Suppliers
    WHERE CompanyName = 'Tokyo Traders' );
-- 6. How many employees work at Northwind? What employees have "manager" in their job title?
-- Count employees
SELECT COUNT(*) AS TotalEmployees
FROM Employees;

SELECT EmployeeID, LastName, FirstName, Title
-- Employees with manager in title
FROM Employees
WHERE Title LIKE '%Manager%';