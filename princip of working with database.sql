1 SELECT ProductName, UnitsInStock FROM Products 
2 SELECT * FROM Products WHERE (UnitPrice < 20); 
3 SELECT * FROM Orders WHERE (Freight >= 11.7) AND (Freight <= 98.1);
4 SELECT * FROM Employees WHERE (TitleOfCourtesy = 'Dr.') OR (TitleOfCourtesy = 'Mr.');
5 SELECT * FROM Suppliers WHERE (Country = 'Japan');
6 SELECT * FROM Orders WHERE (EmployeeID = 2) OR (EmployeeID = 4) OR (EmployeeID = 8);
7 SELECT * FROM [Order Details] WHERE (UnitPrice > 40) AND (Quantity < 10);

��������� �� �������� �������.

Categories->Products - ���� �� ������\\ ���������
Contacts ->���� � ������ \\ ������� ��������� ��������� ������� ��� �����, ��� � �����
CustomerDemographic->Customers - ������ �� ������, \\����� ����� ���
Customers->Orders - ���� �� ������ \\ ���������
Employees->Territories - ������ �� ������ ,��������� � ����������� ����� ���� ��������� ���������� � � ���������� ��������� ����������� ���� ������� ������� ���������������
Orders->Employees - ���� � ��������� \\ �������� �������
Orders->Details ���� �� ������  \\����� ����� ���
Product->Details ���� �� ������ \\ ����� ���� ���
Customers->Orders ���� �� ������ \\ ���������
Employees->Orders ���� �� ������\\ ���������
Shippers->Orders ���� �� ������\\ ���������
Products->Suppliers ���� �������� \\�������� ������� �������
Region->Territories ���� �� ������\\ ���������
\\ ���� �������� Orders	������ �� ������(����� OrderDetails) Products � ����� ����� �� ������

�� ��������� �� ������ ���� ����� Orders	������ �� ������(����� OrderDetails) Products 
� ������ ������ 2 ����� Contacts ->���� � ������ � CustomerDemographic->Customers
� ��������� ������ ������ �����������.

