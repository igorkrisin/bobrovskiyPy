#TableView #storyboard #ios #UITableView

## **Что это такое?**

_**UITableView**_ — это то же табличное представление, что и _UITableViewController_, за одним исключением: у нашего _UITableView_ нет своего контроллера, это значит, что вам предстоит «накладывать» табличное представление на какой-то контроллер, например, на _UIViewController_.

## **Для чего UITableView нужен?**

Он нужен для тех же целей, что и _UITableViewController —_ отображать какие-то данные в виде некоего списка. В основном _UITableView_ накладывают на уже готовые экраны, на которых уже что-то есть, но также можно создавать какие-либо кастомные элементы.

## Приступаем к созданию _UITableView._

Вам не нужно создавать новый проект, помните «стрелочку», которая «объясняла» приложению, с какого экрана нужно запускаться?

Теперь вам нужно отключить «указатель» на запуск приложения с _UITableViewController_. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f63839920ae7b7c870878590add749e0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p1.png)

  

Делается это для того, чтобы мы могли создать новый _UIViewController_ и сказать приложению, что оно должно стартовать с другого экрана.

Следующим этапом будет добавление _UIViewController_ на экран _Storyboard_. Как и раньше, переходим в _main.storyboard_ и в правом экране нажимаем на «+», после этого вводим в поисковой строке _ViewController_.

Перетягиваем _ViewController_ в _Storyboard_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/18d09df6f1ba311db99cff852aaf4761/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p2.png)

  

Теперь у нас есть пустой _ViewController_, вы можете разместить его где угодно (разместим его под _TableViewController_):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b93d5c5946919459fc5217cb675b4d1f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p3.png)

  

Следующее, что нам нужно будет сделать, — это сказать приложению, что мы будем стартовать с этого _ViewController_ экрана: 

Выбираем _ViewController_ → Переходим во вкладку _Attribute_ _Inspector_, которая располагается в выезжающем меню справа (ранее вы уже это делали несколько раз) → Ставим галочку напротив _initial View Controller:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/19f414715a72cbc617931370ce611350/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_pp4.png)

  

Все готово для того, чтобы добавить новое табличное представление. Также, находясь в _Storyboard_, нажимаем на «+» и в поисковой строке вводим _TableView_. Вы должны увидеть следующее:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2a736106e8a878d74a87064aa6cb3000/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p5.png)

  

Перетягиваем _TableView_ в наш _ViewController_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1147429c30d4dc067c894b3e0a70766b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p6.png)

  

Когда вы перетянули _TableView_ на _ViewController_, ваша таблица выглядит маленькой, её следует растянуть (в зависимости от того, как вам нужно), в нашем случае давайте растянем её по всему экрану. Для этого:

Выберите _TableView_ в нижнем правом углу экрана → Нажмите на кнопку _"Add New Constrains"_  → Установите все _Constrains_ в ноль.

Тем самым наше табличное представление растянется по всему экрану, в независимости от того, какого размера у нас экран, и на каком он устройстве.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7df58e5b227d2f3544a9546e5d67359a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p7.png)

  

Итак, таблица растянута на _ViewController_. Теперь настала очередь создания файла, который будет **проассоциирован** (связан) с _ViewController_.

**Внимание!** Вы проходили этот процесс ранее при создании _**UITableViewController**_.  
Как и раньше, нам нужно создать новый _Cocoa Touch Class:  File -> New -> File…_ в открывшемся окне выбираем _Cocoa Touch Class_ и жмем _Next_.

Называем наш класс говорящим именем и, желательно, в конце указываем _ViewController_ или аббревиатуру _VC_. Тем самым мы указываем на то, что наш класс непосредственно будет связан с каким-то _UI_.

А также (и это очень **важно**) вы должны выбрать из _(Subclass of:)_ тот тип, что вам нужен, у вас это _UIViewController_.

Чекбокс с _.Xib_, оставляем пустым.

Язык, естественно, _Swift_.

Когда настройка завершена, жмем кнопку _Next_. 

Сохраняем файл в директорию с проектом.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/608a9d445d77af0302d95b41b5bdcd28/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p8.png)

  

У вас есть файл, который вы должны связать с _ViewController_. Для этого перейдем в _Storyboard_, выберем _ViewController_, перейдем в _"identity inspector"_ и свяжем ваш созданный файл с контроллером, как показано на скриншоте ниже.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c3823cb387853faf711807980af51806/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p9.png)

  

### Готово!

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/dcb0813844c1a31eddb8b6ea77f5f667/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p10.png)

Источник: [cmates.blob.core.windows.net](https://cmates.blob.core.windows.net/cmmaterial/image_2019_7_12_22_33_4_432.jpeg)

Сейчас у вас есть _TableView_, лежащий на _ViewController_, но ваш только что созданный файл ничего не знает про табличное представление и не может работать с ним. Для того, чтобы вы смогли работать с таблицей, нужно создать ссылку на эту таблицу. Это делается так:

Выбираем _ViewController_ → В правом верхнем углу жмем на кнопку _"Editor Options"_ → В появившемся меню нам нужен _"Assistant"_ для того, чтобы открыть экран файла с кодом (_MyViewController_) и _Storyboard_ одновременно.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7e62c03a69bf1e51b9d3b15b297e7710/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p11.png)

  

Это нужно для того, чтобы создать ссылку на _TableView_ в файле _MyViewController_.

Как **создать ссылку** на _TableView_: Выбираем табличное представление → Зажимаем правую кнопку мыши и тянем в наш файл _MyViewController_, после чего отпускаем.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c75884c36dcdae376b65b757663d87b3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p12.png)

  

В появившемся окне вы увидите пять строк:

- _Connection_ — вам нужен _outlet_. Это и будет наша «связь» _TableView_, который лежит на _VIewController_, с файлом _MyViewController_ (для работы с таблицей).
- _Object_ — тот файл, куда мы перемещаем нашу ссылку.
- _Name_ — название нашей ссылки.
- _Type_ — тип того элемента, «лежащего» на _VIewController_.
- _Weak_ — это свойство ссылки (ссылки бывают _weak_ и _strong_, дальше в курсе вы узнаете, что это такое) .

В вашем случае мы ничего не меняем, кроме имени, это будет _"tableView",_ затем жмем кнопку _Connect_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/35a73cd5b7ad592b0565a0a197975646/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p13.png)

  

Теперь в файле _MyVIewController_ вы увидите такой код, который означает, что элемент с именем _tableView_ и типом _UITableView_ имеет слабую (_weak_) связанную ссылку с _TableView_, которая лежит на _VIewController_. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/abc829f1e31d7ce830c9d1d46300b11b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p14.png)

  

Чтобы удостовериться, что вы действительно привязали именно тот элемент, который вам нужен, наведите курсор на круг напротив `@IBOutlet` с открытыми экранами _Storyboard_ и _MyVIewController._ При наведении на круг напротив @IBOutlet у нас подсветится тот элемент, который соответствует вашей слабой ссылке.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/195ec8832c6d9ca2ba03e00ff35ebe15/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p15.png)

  

Итак, вы прошли часть пути, дальше вам нужно подключить протоколы _UITableView_ для того, чтобы вы могли брать методы, отвечающие за работу _UITableView_ (которые придумал за вас _Apple_). Что касается _UITableViewController_, то вам не нужно было это делать, так как все было подключено за вас «из коробки». Здесь же мы делаем это «руками».

Напротив _UIViewController_ ставим запятую, затем пишем _UITableViewDataSource_ и _UITableViewDelegate_.

**_UITableViewDataSource_** — методы для работы с данными таблицы

**_UITableViewDelegate_** — методы для работы с компоновкой (отображением) таблицы, а также действия, выполняемые пользователем.

О [[UITableViewDataSource и о UITableViewDelegate]] мы поговорим немного позже, сначала давайте научимся создавать таблицу.

После добавления протоколов (а они, как вы знаете, обязывают реализовать свойства и методы), вы увидите вот такую ошибку, говорящую о том, что вы не соответствуете протоколу (проще говоря, у вас не реализованы **обязательные** методы).

Давайте нажмем на кнопку _"FIX"_ для быстрого исправления этой проблемки:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/51a06ea479f27eaa7ffcd9772884fad1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p17.png)

  

Вы увидите, как добавились два новых метода:
```swift
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    <#code#>
  }
 
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    <#code#>
  }
```


Первый метод отвечает за количество секций в вашей таблице и должен вернуть некое целочисленное значение. Давайте вернём единицу.

Второй отвечает за создание ячейки (о которой мы поговорим немного позже). Давайте воспользуемся заглушкой и в качестве возвращаемого значения вернем пустую ячейку (заглушку) `UITableViewCell()`.


```swift
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return 1
  }
 
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    return UITableViewCell()
  }
```


Теперь попробуйте запустить приложение на симуляторе, у вас **не** должно быть никаких ошибок, вы должны увидеть пустой список, который можете скролить вверх и вниз. Это еще не все, у вас есть пролеченные протоколы, и вроде бы уже можно работать с таблицей, но нет. Вы помните о делегатах и как их реализовывать?

Для того, чтобы вы смогли использовать методы протоколов _UITableViewDelegate_ и _UITableViewDataSource_, вам нужно **подключить делегаты этих протоколов**. Это тоже просто:

Берем нашу слабую ссылку под именем _tableView_ (которую мы создали ранее) и в методе _viewDidLoad_ вызываем свойство этого соответствующего протокола.  
  
Для UITableViewDelegate — `tableView.delegate = self`  
Для UITableViewDataSource это будет — `tableView.dataSource = self`

Вот теперь мы точно можем сказать, что когда мы будем вызывать любые другие методы из _UITableViewDelegate_ или _UITableViewDataSource_, они точно сработают в этом конкретном табличном представлении.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cb22e88dfab0f1d1af8c7c5eb97352a3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u3_p19.png)

  

Еще раз запустите приложение, чтобы убедиться, что мы ничего не сломали :)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3c545b28f659bed25943c1230c2d60b8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_22_u3_withoutmistakes.gif)

Источник: [giphy.com](https://giphy.com/gifs/work-yeah-computer-WO59vdEqmMHOeMzpjb)

Теперь вы знаете, как создавать табличное представление непосредственно во _ViewController_. Это немного сложнее, чем _TableViewController_, потому что вам **вручную** нужно подключать элементы, которые в _TableViewController_ подключены за вас.
Перейдем к [[Cоздания ячеек UITableViewCell]]
