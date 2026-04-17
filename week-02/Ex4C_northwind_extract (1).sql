/*
a) the table that holds the item northwind sells is called "products".
b) the table that holds the types/categories of items is called "categories".
 select *  from employees;
 USE NORTHWIND;
 SELECT COUNT(*) FROM Employees;
 SELECT * FROM Employees
 /*
 a) the employee whose name looks like a bird is nancy davolio because her last name sounds like "dove"
 SELECT * FROM Products;
 6. a)the query returns 77 records to retrive only 10 rows we can use "top 10" or set a row limit in the query editor.
 b) we can limit rows using SQL syntax
 SELECT TOP 10 * FROM products 
SELECT * FROM categories; 
/*
7.c) the category id for seafood is 8.
*/
SELECT 
ORDERID,
ORDERDATE,
SHIPNAME,
SHIPCOUNTRY
FROM ORDERS
LIMIT 50;