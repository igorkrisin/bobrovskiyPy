6.3.1. 
SELECT [ContactType], 
	COUNT([ContactType]) as CountField
FROM Contacts 
GROUP BY [ContactType] 
ORDER BY ContactType; 

6.3.2.  
SELECT CategoryID, 
	AVG(UnitPrice) as UNIT_PRICE
FROM Products
GROUP BY CategoryID
ORDER BY UNIT_PRICE; 

рефлексия по 5 му заданию 
в 3ей задаче можно было написать все 3 функции в одном выражении: 
SELECT AVG(UnitPrice), MIN(UnitPrice), MAX(UnitPrice)
FROM [Order Details]
я сделал 3 разные