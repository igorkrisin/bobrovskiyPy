Categories->Products - один ко многим
Contacts ->один к одному
CustomerDemographic->Customers - многие ко многим, потому как покупателям может принадлежать не один регион и регионам не один покупатель, есть сводная таблица идентификаторов
Customers->Orders - один ко многим
Employees->Territories - многие ко многим ,поскольку у сотрудников может быть несколько территорий и у территорий несколько сотрудникоа есть сводная таблица идентификаторов
Orders->Employees - один к множеству
Orders->Details один ко многим 
Product->Details одни ко многим
Customers->Orders один ко многим
Employees->Orders один ко многим
Shippers->Orders один ко многим
Products->Suppliers один комногим
Region->Territories один ко многим


