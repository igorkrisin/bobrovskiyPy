#ячейки #UITableCell #Xib 

Теперь для своих экспериментов будем использовать созданный ранее _ViewController!_ На нём уже есть таблица с ячейкой, с которой мы уже поработали ранее.

Давайте запустим снова этот экран, чтобы удостовериться, что ничего не сломалось и осталось без изменений.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d9bf8f8a0a3e1e174806d338be703141/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p33.png)

  

Все осталось в том виде, в котором мы оставили этот код.

## Приступим к экспериментам над ячейкой.

Пока не будем вносить новых изменений в старую ячейку. В первую очередь создадим «кастомную ячейку» при помощи _.xib._

Как это сделать? Идем по проторенной дорожке:

- Создаем _Cocoa Touch Class:  File → New → File…_ → В открывшемся окне выбираем _Cocoa Touch Class_ → Жмем _Next_ _→_ В окне создания класса пишем имя класса _(UniversalCell)_, _Subclass of: UItableViewCell_ _→_ Нажимаем на поле _Also create XIB file._ 
- Язык — Swift.
- Next → Create

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/abdb2867d102bae3674b614d9c419cdd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p34.png)

  

Теперь у вас есть два файла: _UniversalCell.xib_ и _UniversalCell.swift_

_**UniversalCell.xib**_ — это «заготовка» под ячейку (пустой контейнер), который мы заполним.

_**UniversalCell.swift**_ —  это класс, связанный с _UniversalCell.xib_, с которым мы в дальнейшем будем работать.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2e4845c0018718a392632a68a0957432/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p35.png)

  

Перейдем в _UniversalCell.xib_ и добавим _UILabel_, как в нашей старой ячейке. Мы будем отображать массив имен, который создавали ранее. Помните его? 

let userArray = ["Евгения", "Николай", "Катерина", "Станислав", "Артур", "Марина", "Вячеслав", "Перт"]

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a82f3e233cb8183923cc655c3455151c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p36.png)

  

_Label_ добавили. Теперь, как и раньше, нам нужно сказать классу _UniversalCell_, что нас есть этот _Label_. Для этого откройте класс _UniversalCell_ и создайте вручную слабую ссылку на _Label_, это делается вот так:

@IBOutlet weak var userName: UILabel!

## После этого вернитесь в _XIB_ и свяжите _Label_, находящийся на _XIB_ с _Label_ в коде, это делается вот так:

**1**

  
Выделяем _Label_ в меню слева (на ксибе) и жмёте на первую кнопку мыши, появляется диалоговое окно, в котором вы должны выбрать _"new referencing outlet"_ и перетянуть на _label_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ecae0517ca8c9d25a61344828ddd933d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p37.png)

  

**2**

  
Когда вы перетянули, у вас откроется второе диалоговое окно, в котором вы должны выбрать тот _Outlet_, который вы создали ранее с именем _userName_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b4749ee5b21357411bf55808e2552c48/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p38.png)

  

После того, как вы выбрали этот элемент, у вас появится связь между _Label_ из класса и _Label_ из _XIB_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1f66e9bafc1f55664a30c5d694926be1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p39.png)

  

Итак, у нас есть ячейка и _Label_, которые уже связаны в коде.

## Теперь нужно поменять старую ячейку на новую, только что созданную. Как это сделать:

#### Первый этап:

1. Удалите файл _MyCell.swift_
2. Удалите ячейку (TableViewCell) из _TableView (само TableView не удаляйте!) 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3076b236c1f0a6407de931dc1d571cf0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p40.png)

  

#### Второй этап:

Вам нужно «зарегистрировать» созданный _XIB_ в _TableView_, чтобы приложение понимало, где и что ему искать (нужные файлы).

Это делается в методе:
```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) → UITableViewCell
```


Сам процесс регистрации прост — при помощи идентификаторов, это значит, что вам нужно установить идентификатор в _XIB_, как вы делали ранее:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/69b8c8dbb6e67bde0a8ddf49bb6e3b25/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p41.png)

  

Идентификатор установлен, а это значит, что в следующем методе...
```swift

func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell
```
...вы можете создать регистрацию _XIB_ ячейки:
```swift

tableView.register(UINib(nibName: "UniversalCell", bundle: nil), forCellReuseIdentifier: "UniversalCell")
```




Весь код метода:
```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    tableView.register(UINib(nibName: "UniversalCell", bundle: nil), forCellReuseIdentifier: "UniversalCell")
 
    guard let cell = tableView.dequeueReusableCell(withIdentifier: "UniversalCell", for: indexPath) as? UniversalCell else { return UITableViewCell() }
    cell.userName.text = userArray[indexPath.row]
    return cell  }

```

Если вдруг вы забудете зарегистрировать файл, тогда увидите вот такую ошибку:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b5f81943642800b17fb5ed7ced9d9d09/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p42.png)

  

Вот и все, путь немного тернист, но пройдя его несколько раз, вы запомните все этапы.


Все готово для тестирования. Запустите приложение, вы должны увидеть точно такую же картинку, что и раньше, как со «старой» ячейкой, которую мы добавляли непосредственно на _TableView_. Только теперь у нас не осталось и следа от старых файлов, мы используем все «новое».