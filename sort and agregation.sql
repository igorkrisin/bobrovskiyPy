5.4.1. SELECT * FROM Employees ORDER BY BirthDate DESC, Country;
5.4.2. SELECT * FROM Employees WHERE Region IS NOT NULL ORDER BY BirthDate DESC, Country;
5.4.3. SELECT AVG(UnitPrice) FROM [Order Details]; средняя цена
	   SELECT MIN(UnitPrice) FROM [Order Details]; минимальная 
	   SELECT MAX(UnitPrice) FROM [Order Details]; максимальная
5.4.4  SELECT COUNT(DISTINCT City) FROM Customers;

рефлексия к заданию 4.3.2:
при выводе сиран поставщиков можно использовать более короткую запись  (ShipCountry IN ('France','USA'))
вместо (ShipCountry = 'USA' OR ShipCountry = 'France')