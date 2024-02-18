#swift #mvc #архитектура

- создаем папку Application и в нее помещаем AppDelegate и SceneDelegate 

![[Screenshot 2024-02-05 at 19.05.10.png]]

 - далее SupportingFiles в нее переносим LunchScreen и Info.plistRe, так же нужно настроить новый путь к Info.plist

![[Screenshot 2024-02-05 at 19.06.51.png]]

так же нужно настроить новый путь к Info.plist
переходим в Target->Build и в поле поиска вводим .plist и видим адрес расположения файла и указываем новый путь и ошибка уходит

![[Screenshot 2024-02-05 at 20.48.13 1.png]]

- далее Resourses  и помещаем Assets сюда помещаем переводы приложения и шрифты
- 
- и папка Screens и внутри нее делаем еще папку MainScreen и SecondScreen и переносим файлы в папки с соответствующим названием

 ![[Screenshot 2024-02-05 at 19.31.59.png]]

при использовании MVC внутри папок MainSecreen и SecondScreen нужно создать еще три папки Model, View, Controller в нашем проекте будет только Controller и в нее складываем файл VC и storyboard 

![[Screenshot 2024-02-05 at 19.38.43.png]]

В папке view лежат только  кастомные элементы (кнопки, лэйблы и тд)









