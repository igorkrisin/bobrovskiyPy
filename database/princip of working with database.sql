1 SELECT ProductName, UnitsInStock FROM Products 
2 SELECT * FROM Products WHERE (UnitPrice < 20); 
3 SELECT * FROM Orders WHERE (Freight >= 11.7) AND (Freight <= 98.1);
4 SELECT * FROM Employees WHERE (TitleOfCourtesy = 'Dr.') OR (TitleOfCourtesy = 'Mr.');
5 SELECT * FROM Suppliers WHERE (Country = 'Japan');
6 SELECT * FROM Orders WHERE (EmployeeID = 2) OR (EmployeeID = 4) OR (EmployeeID = 8);
7 SELECT * FROM [Order Details] WHERE (UnitPrice > 40) AND (Quantity < 10);

Рефлексия по прошлому заданию.

Categories->Products - один ко многим\\ правильно
Contacts ->один к одному \\ таблица контактов отдельная таблица без связи, как я понял
CustomerDemographic->Customers - многие ко многим, \\такой связи нет
Customers->Orders - один ко многим \\ правильно
Employees->Territories - многие ко многим ,поскольку у сотрудников может быть несколько территорий и у территорий несколько сотрудникоа есть сводная таблица идентификаторов
Orders->Employees - один к множеству \\ поменять местами
Orders->Details один ко многим  \\такой связи нет
Product->Details одни ко многим \\ такой связ нет
Customers->Orders один ко многим \\ правильно
Employees->Orders один ко многим\\ правильно
Shippers->Orders один ко многим\\ правильно
Products->Suppliers один комногим \\поменять местами таблицы
Region->Territories один ко многим\\ правильно
\\ надо добавить Orders	многие ко многим(через OrderDetails) Products я такой связи не увидел

Из основного не увидел одну связь Orders	многие ко многим(через OrderDetails) Products 
и увидел лишних 2 связи Contacts ->один к одному и CustomerDemographic->Customers
в некоторых местах спутал направление.

