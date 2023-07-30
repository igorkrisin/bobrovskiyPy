7.3.1 SELECT 'Discount%:', Discount*100 FROM [Order Details]
7.3.2
SELECT * FROM [Order Details]
WHERE ProductID IN 
	(SELECT ProductID FROM Products
	WHERE UnitsInStock > 40)
	ORDER BY ProductID

7.3.3
SELECT * FROM [Order Details]
WHERE ProductID IN 
	(SELECT ProductID FROM Products
	WHERE UnitsInStock > 40) AND
	OrderID IN
	(SELECT OrderID FROM Orders
	WHERE Freight < 50)
	ORDER BY ProductID;

