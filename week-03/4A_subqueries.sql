use northwind;
-- 1. What is the product name(s) of the most expensive products?
SELECT PRODUCTNAME 
FROM products
WHERE unitprice = (select max(unitprice) from products);
-- 2. What is the product name(s) and categories of the least expensive products?
select productname 
from products 
where unitprice = (select min(unitprice) from products);
-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
select  ShipperID 
from shippers
where shipperid = 3;
SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = 3;
-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT ProductID
FROM Products
WHERE ProductName = 'Sasquatch Ale';
SELECT OrderID
FROM `Order Details`
WHERE ProductID = 34;
-- 5. What is the name of the employee that sold order 10266?
select e. firstname, e.lastname 
FROM orders o
join employees e on O.employeeID = e.employeeID
WHERE O.orderid = 10266;
-- 6. What is the name of the customer that bought order 10266
select ContactName
from orders o
join customers c on o.customerID = c.customerID
where O.ORDERID = 10266;