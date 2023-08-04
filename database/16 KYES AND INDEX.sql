Я в прошлом занятии неправильно сформировал таблицу Region в RegionID установил территориальный 
ID а в описаниии региона установил ID региона, что бы поменять данные поля я написал команду

USE MyDB
UPDATE Region
SET RegionID = 1, RegionDescription = 'Eastem';

Затем установил индексы для поля RegionID

USE MyDB
CREATE CLUSTERED INDEX RegionIDIndex ON Region (RegionID);
CREATE CLUSTERED INDEX TerritoryesIndex ON Territories (TerritoryID);
