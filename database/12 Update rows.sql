12.3.1. 
SET IDENTITY_INSERT dbo.Employees ON;
INSERT INTO Employees(EmployeeID, LastName, FirstName,  Country) 
VALUES (10, 'Ivanov', ' Piter', 'Russia'); 
SET IDENTITY_INSERT dbo.Employees OFF;

12.3.2 

INSERT INTO EmployeeTerritories(EmployeeID, TerritoryID) 
VALUES (10, '03049'); 

12.4.2

SET IDENTITY_INSERT dbo.Orders ON;
INSERT INTO Orders(OrderID , EmployeeID, ShipName) 
VALUES (11078, '9' , 'Russia Today'); 

Сначала была ошибка по IDENTITY_INSERT, что он имеет значение OFF (с такой проблемой я столкнулся еще в 
задании 12.3.1), я переключил данный идентификатор и появилась ошибка о том, что явно идентификатор задать нельзя
я убрал явное присваивание значению идентификатора и заказ добавился. Могу предположить что присвоени происходит 
автоматически данного поля (другим механизмом), либо мной были выбраны недопустимые символы Идентификатора.

											Рефлексия по заданию 11
											
Я неправильно указал условия отбора при выполении LEFT JOIN тем самым получив значение в котором FK 
ключ таблицы Orders пустой из обоих таблиц левой и правой, правильно было написать уловия отбора через WHERE 
как результат меньше итоговый выод и он затрагивает только правую таблицу

SELECT *, Orders.OrderID FROM Customers 
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID AND Orders.CustomerID IS NULL
ORDER BY Customers.CompanyName;


правильно так:
SELECT * FROM Customers LEFT JOIN Orders
  ON Orders.CustomerID = Customers.CustomerID
  WHERE Orders.CustomerID IS NULL