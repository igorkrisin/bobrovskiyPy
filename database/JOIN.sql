10.4.1 

SELECT Products.ProductName, Products.UnitPrice
FROM Products JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20
ORDER BY UnitPrice;


10.4.2
Выдача при запросе FULL JOIN объемнее из-за того что эта команда выдает объединение множеств,
то будут выданы варианты с обоих таблиц соотвествующих запросу?
 а в таблицах есть поля которые не запонениы по данному ID противоположной таблицы поэтому и 
 результатов будет больше чем в INNER. 
 
10.4.3. думаю что после условия для CROSS JOIN нужно дописаать условие после комнады WHERE:
таблица1 CROSS JOIN таблица2 WHERE условие 


10.4.4 
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID



					рефлекия по заданию 9
в задании 9.4.1. 
Найдите все пары из разных заказчиков (Customers), для которых не задан регион (поле Region).

SELECT t1.ContactName, t2.ContactName, t1.Region
FROM Customers t1, Customers t2 
WHERE (t1.Region IS NULL) AND (t2.Region IS NULL) AND
      (t1.CustomerID <> t2.CustomerID)
	  
я не указал условия  (t1.CustomerID <> t2.CustomerID), поэтому будут
 попадаться пары с однаковыми заказчиками
