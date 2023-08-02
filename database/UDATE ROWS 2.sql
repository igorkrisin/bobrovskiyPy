13.3.1

UPDATE [Order Details]
SET Discount = 0.20
WHERE Quantity > 50;

13.3.2

UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany' ;

13.3.3
SET IDENTITY_INSERT dbo.Shippers ON;
INSERT INTO Shippers (ShipperID, CompanyName)
VALUES (4, 'HH');
SET IDENTITY_INSERT dbo.Shippers OFF;


SET IDENTITY_INSERT dbo.Shippers ON;
INSERT INTO Shippers (ShipperID, CompanyName)
VALUES (5, 'HH');
SET IDENTITY_INSERT dbo.Shippers OFF;

DELETE FROM Shippers
WHERE ShipperID = 4;

DELETE FROM Shippers
WHERE ShipperID = 5;

Удалял по критерию ID поставщиков