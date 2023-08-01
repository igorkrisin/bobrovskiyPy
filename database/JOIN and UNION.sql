11.5.1

SELECT *, Orders.OrderID FROM Customers 
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID AND Orders.CustomerID IS NULL
ORDER BY Customers.CompanyName;

11.5.2.

SELECT 'Customer' As Type, ContactName, City, Country FROM Customers 
UNION 
SELECT 'Supplier' As Type, ContactName, City, Country FROM Suppliers 
ORDER BY City; 
