#coreData #swift 

[[core data вручную поставить, если забыл установить галочку]]

План действий:

![[Screenshot 2024-01-28 at 19.35.05.png | 500]]



1.  Делаем модель BD, создаем поля.
![[Screenshot 2024-01-28 at 19.44.22 1.png | 500]]

- проставляем всем полям типы, id - String!

![[Screenshot 2024-01-28 at 19.48.04.png]]

- меняем в инспекторе Codegen на manual/None

![[Screenshot 2024-01-28 at 19.50.40.png]]


- идем в настройки в editor и выбираем пункт с картинки

![[Screenshot 2024-01-28 at 19.52.29.png]]

- после создания получаем 2 расширения и отправляем их в одну папку

![[Screenshot 2024-01-28 at 19.55.13.png]]

- создаем файл swift coreManager
![[Screenshot 2024-01-28 at 19.56.34.png]]

- Создаем в файле class CoreManager и делаем из него singleton, что бы контексты не смешивались, что бы мог существовать только один экземпляр класса и <mark style="background: #FF5582A6;">импортируем coreData</mark>. Создаем инициализатор.


![[Screenshot 2024-01-28 at 19.58.30.png]]

- переносим этот код из appdelegate в coreManager в качестве имени контейнера используем <mark style="background: #FF5582A6;">название файла data base!!!!</mark>


![[Screenshot 2024-01-28 at 20.07.03.png]]

- удаляем из sceneDelegate эту ф-ю. Что бы он не ссылался на appDelegate

![[Screenshot 2024-01-28 at 20.05.49.png]]
Модель базы данных готова!

2. Начнем писать функционал 
- Первая ф-я получения информации, 

![[Screenshot 2024-01-28 at 20.15.20.png]]

- так же создадим массив для хранения информации

![[Screenshot 2024-01-28 at 20.15.43.png]]

Следующая функция добавления информации:

- Присваиваем все поля и в конце сохраняем и получаем все элементы

![[Screenshot 2024-01-28 at 20.37.39.png]]

- далее пишем удаление и обновление будем делать через extensions 

![[Screenshot 2024-01-28 at 20.45.43.png]]

Модель полностью написана.

во ViewControllere создаем экземпляр CoreManager и добавляем в NumberOfRowsSection  количество его timers, а в cellForRowAt выводим информацию из базы данных.

![[Screenshot 2024-01-28 at 20.53.26.png]]

- во viewDidLoad устанавливаем constraints и растягиваем на весь view таблицу 

![[Screenshot 2024-01-28 at 20.58.35.png]]

ниже в viewDidLoad пишем добавление нового viewCintroller 

![[Screenshot 2024-01-28 at 21.01.41.png]]


- Далее идем на созданную только что страницу addViewController и пишем там менеджер и пишем поля для ввода


![[Screenshot 2024-01-28 at 21.05.23.png]]
- создаем менеджер и экземпляр данных и кнопки с полями

![[Screenshot 2024-01-28 at 21.26.33.png]]


- Прописываем action для кнопки сохранения в базу
![[Screenshot 2024-01-28 at 21.08.08.png]]
 

- прописываем вывод на экран view

![[Screenshot 2024-01-28 at 21.11.10.png]]


-  и констрейнты для них тоже во viewDidLoad 

![[Screenshot 2024-01-28 at 21.12.00.png]]

далее прописываем background для view и его title во viewDidLoad

- во viewWillAppear ViewControler обновляем таблицу 


![[Screenshot 2024-01-28 at 21.16.00.png]]

