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