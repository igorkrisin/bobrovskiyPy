#tableViewController #ios #swift #storyboard 

Так же можно создовать кастомный [[TableView создаем через storyboard ]]


Первым по очереди в обучении будет **_UITableViewController_**, так как его проще всего реализовать. Все потому, что _Apple_ думает о своих разработчиках и старается упростить им жизнь всеми доступными способами, особенно тем, кто только начинает первые шаги в программировании под _iOS_.

Почему _UITableViewController_ проще в изучении чем _TableView_?

Дело в том, что _UITableViewController_ «из коробки» содержит много полезных и уже подключенных вещей, которые вам не придется подключать вручную.

Как говорится: все познается в сравнении — вы увидите отличия при создании _UITableViewController_ по сравнению с созданием _TableView_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5e258f72b4a1ef67522cf9ba56e1f023/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p1.png)

Источник: [www.meme-arsenal.com](https://www.meme-arsenal.com/memes/7a8e30bacaf533fd7c26aab31acc1c2f.jpg)

## Приступаем к работе.

В качестве контроллера у нас сейчас используется стандартный, созданный _IDE ViewController_. Для наших целей он не нужен, и поэтому нам необходимо его удалить.

Удаляем из _Main.storiboard_ стандартный _ViewController:_ Выделим его и нажмем _Delete:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0663cd160cc23d49a747441b42607113/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_pp2.png)

  

Такую манипуляцию нужно проделать и с файлом _ViewController.swift_, без долгих прощаний удаляем и его. 

Когда выберете нужный файл и попытаетесь его удалить, то _Xcode_ спросит у вас, как удалить этот файл, вы должны удалить его **полностью**, для этого нужно выбрать _"Move to Trash":_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7cae7aa3bd5957687ded6eb8917704ba/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p3.png)

  

Тем самым мы полностью избавились от ненужных нам элементов.

Дальше вы должны перейти в _Main.storyboard_, нажать на плюсик в правом верхнем углу экрана, ввести в строке поиска _UITableViewController_ и перетащить этот элемент на экран, где только что был _UIViewController_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d650674de80b7aa28ad5f2bae99a3758/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p5.png)

  

После того, как вы перетащили новое табличное представление вместо того, что было ранее _(__UIViewController)_, вы увидите _UITableViewController_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/080c41c340833197a446633402c75ff4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p6.png)

  

Теперь у нас есть _UITableViewController_ в нашем _Storyboard_.

Давайте рассмотрим, что нам предоставляет _UITableViewController_ из коробки. На самом _UITableViewController_ у нас есть:

1. _**Table View**_ — таблица, в которой мы и будем размещать весь список того, что нам нужно (все элементы, помещенные в таблицу).
2. **_Table View Cell_** — это некоторая программируемая ячейка, в которую мы будем помещать данные. О ней мы поговорим чуть позже.
3. **_Content View_** — это настраиваемая _view_, в которую мы можем получить любые элементы _UI_ (к примеру, это может быть _ImageView_, _Label_ или _Button_)

Для того, чтобы начать хоть какую-то работу, нам необходимо создать дополнительный файл, который будет связан с нашим табличным представлением (помните, немного выше мы удалили файл _ViewController_, вот он был связан с _UIViewController_).

Для этого нужно создать новый _Cocoa Touch Class:  File_ → _New_ → _File…_ В открывшемся окне выбираем _Cocoa Touch Class_ и жмем _Next_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/365db0a172b2b44eae9e4ed6869eae49/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p7.png)

  

Называем наш класс говорящим именем и желательно в конце указываем или _TableViewController,_ или аббревиатуру _TVC_. Тем самым мы указываем, на то, что наш класс будет связан непосредственно с каким-то _UI_ (в будущем, когда у вас будет множество файлов, понять, какой класс отвечает за контроллер, будет легче).

А также (и это очень **важно**) вы должны выбрать из _(Subclass of:)_ тот тип, что вам нужен. У вас это _UITableViewController_.

Чекбокс с _.Xib_, оставляем пустым.

Язык, естественно, _Swift_.

Когда настройка завершена, ждем кнопку _Next_. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/03d20514640a0e73bdfafb3c5a992433/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p8.png)

  

Не забываем указать, в каком месте нам нужно создать наш файл.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/897912696704ff7291dcbef9b0fc3e8d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p9.png)

  

Готово! _Xcode_ создал для нас новый файл. Давайте перейдем в него и посмотрим, что же за файл был создан.

В классе _MyTableViewController_ мы сразу видим много закомментированного кода. Не стоит пугаться, это не какой-то лишний код, им вы будете пользоваться по мере роста своих навыков. Но пока он не нужен, смело удаляем его (а вот код, закомментированный в шапке, лучше оставить). Вот, что у вас должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f88f57c620041a0f5f18b808dad82516/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p10.png)

  

Все почти готово. Последнее, что осталось сделать, это связать наш новый созданный класс _MyTableViewController_ с нашим контроллером _UITableViewController_.

Это делается достаточно просто. Вам нужно перейти в _Storyboard_, выбрать ваш контроллер _UITableViewController_, открыть вкладку _identity_ _inspector_ и в поле _class_ ввести имя нашего только что созданного класса _MyTableViewController_, тем самым вы связываете контроллер с классом.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d5f287a0c1474c297d65ea9b869fb389/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p11.png)

  

Давайте перейдем к следующему шагу.

Так как мы удалили первый «стандартный» _ViewController_, который шел из коробки, вместе с ним мы удалили и «указатель» — с какого _UI_ нужно запускать приложение. Проще говоря, если вы сейчас запустите приложение в симуляторе, то у вас будет черный экран, а в консоли будет вот такая надпись:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/868acfdbdc2eeb5187d473495e6cae56/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p12.png)

  

Этой ошибкой приложение говорит, что оно не знает, с какого экрана нужно стартовать приложение. Данную проблему очень просто исправить.

Перейдите в _Attributes Inspector_, видите под текстовым полем _"Title"_ чекбокс "_is initial View Controller"_?

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/554da7013b6047305cb81cf9a438c85a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p13.png)

  

Нажмите на него и вы увидите, как перед вашим _UITableViewController_ появится стрелочка, которая показывает, что приложение будет запущено именно с этого экрана.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4d4e036d25e47f407b21dc07b5c9a6c6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p14.png)

  

Запустите приложение на симуляторе. Вы должны увидеть на экране пустой список, который может скроллиться вверх и вниз.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fe15aef0fae7f360c37577affa130f04/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p15.png)

  

## Фух! Теперь все готово.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fd41a3fb09e437d4fdbea19db4e6fb36/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m22_u2_p16.png)

Источник: [memesmix.net](http://memesmix.net/media/created/9icavf.jpg)

С созданием _UITableViewController_ мы закончили и показали вам весь путь, чтобы вы понимали, с чем вам придется столкнуться. Не пугайтесь, этот процесс только кажется сложным и долгим, когда вы набьете руку, вы не будете его замечать.