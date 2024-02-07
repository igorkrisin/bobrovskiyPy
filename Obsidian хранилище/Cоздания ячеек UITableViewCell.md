
#ios #swift #UITableCell 

## **Ячейка UITableViewCell  (динамическая ячейка)**

Так как создание ячеек в _TableView_ немного отличается от _UITableViewController_ тем, что вы сами добавляете её, а если используете коробочное решение, то ячейка уже идёт «в комплекте»

Давайте создадим ячейку, используя в нашем примере _TableView_. Данная процедура проста, но нужно обладать небольшими знаниями, чтобы все прошло легко и просто.

Первый шаг, который нам предстоит сделать:

Перейдите в _Storyboard_ → Выберите _TableView_, который все так же расположен на _ViewController_ → В правом верхнем углу нажмите на плюсик (_+ - Library_) → В поисковом запросе введите _**Table View Cell**_ — это и есть ячейка. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1550de632a28466a9f4dfc138dbb3840/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p1.png)

  

Затем перетащите её на табличное представление:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0d9291356734d0c3948f0dd02b6b2b82/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p2.png)

  

Всё, теперь у вас есть ячейка на таблице, которая будет выполнять роль контейнера данных. 

Всю иерархию _UI_ вы можете увидеть слева в выезжающем окне:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6cbbabdc6ad434f75a52d3fc61c72b5c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p3.png)

  

У вас есть ячейка _TableViewCell_, её можно настраивать как вам угодно и перетаскивать те элементы _UI_, которые вам понадобятся в работе внутри ячейки.

Давайте добавим в неё _UILabel_ слева по центру. Чтобы это сделать, откройте _Library_ (все точно так же, как делали раньше) и введите в поисковике _UILabel,_ а затем перетащите в левый угол.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f660d23481f1d817b8f8a14cb4f1478f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p4.png)

  

Теперь нужно выставить констрейны для этого элемента. Слева выбираем отступ 10, сверху — 0, снизу — 0, справа — 10. То есть наш _Label_ растянется на всю ячейку.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1be334854e66ceafa958bda0d9b5f501/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p5.png)

  

Мы закостамизировали ячейку, но как с ней работать дальше? Вам необходимо задать новый файл, как вы делали ранее, для того, чтобы связать нашу ячейку, опять же, как вы делали ранее.

Создаем файл _Cocoa Touch Class_ → Имя у ячейки будет _MyCell (Subclass of_ – будет _UITableViewCell_) → _Next_ → _Create_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0ac5af115193fea7f7aa1d2bc0bccafb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p6.png)

  

Этот класс _MyCell_ и будет являться связующим элементом ячейки и кода.

Теперь выбираем _Table View Cell_ в _Storyboard_ → Открываем _Identity Inspector_ → В поле _Class_ добавляем _MyCell_, тем самым мы свяжем класс с ячейкой.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5a68fee33708e57e6176d23b3a021de4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_pp7.png)

  

Переключитесь на _Attributes Inspector_ и в поле _Identifier_ также введите _MyCell_ (вы можете ввести любой идентификатор ячейки, но практика подсказывает, что лучше использовать название класса, с которым связана ячейка). _MyCell_ нам пригодится, когда мы начнём помещать данные для _UILabel_ в ячейку.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a2ef6c5c11448dc84d84d65029d315df/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p8.png)

  

Следующее, что нам нужно — это создать ссылку на _UILabel_, как мы делали ранее с _TableView_. Для этого мы:

Открываем ассистент → Выбираем добавленный _UILabel_ → Открываем нужный файл, если он не открылся автоматически (такое иногда бывает).

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3022fb6e2bc9650b6604132adc05db2e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p9.png)

  

После этого перетащите ссылку в класс и назовите _"userName":_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d5991792ec28a70a9866d13e45311c08/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p10.png)

  

Теперь все готово для того, чтобы начать работу по отображению ячеек в таблице.

Возвращаемся в класс _MyViewController_ и создаем там массив из студентов `[Евгения, Николай, Катерина, Станислав, Артур, Марина, Вячеслав, Перт]`. Именно эти имена должны вывестись списком в вашей таблице.

 let userArray = ["Евгения", "Николай", "Катерина", "Станислав", "Артур", "Марина", "Вячеслав", "Перт"]

Чтобы сказать табличному представлению, сколько у нас будет строк в таблице, нам необходимо вернуть в методе `tableView (:numberOfRowsInSection:)` количество элементов в массиве.
```swift
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
// берем массив и получаем общее значение данных которые хранятся в нем
    return userArray.count
  }

```

Теперь ваше приложение знает, сколько строк нужно будет показать. Следующий этап — это нужно поместить данные из массива в строки. Нет ничего проще, вам для этого нужен метод, который вы создали ранее (помните про заглушку, которую оставили, чтобы приложение запустилось без ошибок?). В любом случае, нам нужен метод также из _UITableViewDataSource:_

tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath)

Нужно внутри этого метода создать константу, которая будет ассоциироваться с _MyCell_ по идентификатору, о котором мы говорили ранее. В противном случае, если такого идентификатора не будет, вернется пустая ячейка (та самая заглушка).

Когда константа будет «проассоциирована», вы сможете получить доступ к полям из класса _MyCell_, а именно к _UILabel_. (Проще говоря, на каждую ячейку создается новая константа, и этой константе будет принадлежать своя переменная из массива).

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    guard let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath) as? MyCell else { return UITableViewCell() }
    cell.userName.text = userArray[indexPath.row]
    return cell
  }
```


Теперь запустите приложение и посмотрите, что у вас получилось.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/40efbb9a09d1de5610dc882138bdb173/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p12.png)

  

Это просто замечательно! Вы смогли написать свое первое приложение в _UITableView_!

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2ecb97eba7b257811b9781d684bcc016/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p13.png)

Источник: [risovach.ru](https://risovach.ru/upload/2018/06/mem/gordyy-kozlenok_178337901_orig_.jpg)

Давайте рассмотрим функционал _UITableViewDelegate_, к примеру, увеличим высоту ячеек.

Для этого нам понадобится метод `tableView(heightForRowAt indexPath:)`, высоту ячеек зададим 135.

func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
    return 134
  }

Посмотрим, что получилось:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d5dcc661604c7a610f4053ebededdf27/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p14.png)

  

Расстояние между строк значительно увеличилось, установим значение на 60, чтобы оно не шокировало, и давайте добавим название секции вверху, для этого есть прекрасный метод `tableView(: titleForHeaderInSection section: )`
```swift
func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
    return "Names"
  }
```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2f612b8f523a9059612d45856b17b554/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p15.png)

  

Также можно добавить какой-либо текст в конце секции.

**Важно!** Секций, как и строк, может быть любое количество.

Не удивляйтесь, есть метод и для этого — `tableView(titleForFooterInSection section: )`
```swift
func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -> String? {
    return "END THE SECTION"
  }
```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/74ad3ff3b74c129a8812c4d71194e48f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u5_p16.png)

  

Вы понимаете, насколько обширен функционал таблиц? Чтобы его изучить, нужно много **практиковаться** и писать приложения.

С динамическим ячейками для конкретной таблицы вы разобрались, теперь вы понимаете, как их создавать и заполнять. Давайте рассмотрим, что такое [[Статические ячейки]].