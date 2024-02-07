#swift 
_**UIResponder**_ — суперкласс, от которого наследуется _UIView_ и все _view_-элементы.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6ae259bc821ed7d7f5975048c58e308b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p1.png)

Источник: [Coursera](https://www.coursera.org/lecture/user-interface/uiview-i-iegho-sabklassy-chast-1-ACUHS)

Классы, которые наследуются от _UIResponder_, участвуют в обработке событий _UIKit_. А что это за такие события? Этими событиями могут быть события движения (встряхивание устройства) или сенсорные события (нажатие на экран).

Перед тем, как углубляться дальше в теоретическую часть, давайте подумаем — где эти события мы можем наблюдать в реальной жизни. Например, вы пишете заметку в приложении _Notes_ и случайно встряхнули экран. В это время на экране вылезло предупреждение о двух вариантах — либо удалить текст, либо оставить в покое. Вряд ли каждый трясёт айфон, чтобы удалить текст. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4721b8e6b7a547cf3d7192b006fb231f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p2.jpeg)

  

Другой пример более близок к прикладному применению. Заходим в приложение _Notes_, создаём новую заметку и открывается вот такой экран:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/133abf6fbef0255e75a709eb25d097ef/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p3.jpeg)

  

В момент, когда мы нажали на кнопку _“Add New Note”_, произошло событие нажатия. И уже на экране работы с текстом клавиатура появилась как бы автоматически. Клавиатура появилась, потому что обработалось нажатие на кнопку “_Add New Note”,_ и сработала логика, которая отвечает за обработку событий. Следовательно:  
Нажатие обработано → Запустился метод, который показывает клавиатуру.

Вот нажатие произошло → _firstResponder_ зарегистрировал его. Этот _firstResponder_ — первый _UIResponder_, который записал это событие. Затем _UIKit_ создаёт из _firstResponder_ связный список _Responder Chain._

В _Responder Chain_ классы-наследники от _UIResponder_ выстраиваются в связный список респондеров.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fdfee10d4ac1b94fddafb1d9956425b5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p4.png)

Источник: [coursera.org](https://www.coursera.org/lecture/user-interface/uiview-i-iegho-sabklassy-chast-1-ACUHS)

1. _UIKit_ пробегается по списку, чтобы проверить, сможет ли _responder_ работать с конкретным методом. Делает он это через свой встроенный метод `canPerformAction`:
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/952a1de0ba17d080f336a820d8017fc8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p05.png)
    
      
    
2. Если _responder_ не способен работать с таким методом, _UIKit_ рекурсивно отправляет действия к следующему _responder_ с помощью метода `target`:
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c78b8e5b1a44393a164ef2f26bc4402e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p06.png)
    
      
    

_*Кстати, мы можем сами выбирать респондер. Делается это ручками, через код. Об этом мы подробно поговорим в практической части юнита._

Этот «подкапотный» и невидимый невооружённым глазом процесс будет повторяться до тех пор, пока:

- не найдётся один из _UIResponder’ов_ в цепочке, который сможет работать с нужным нам методом,
- связный список закончится и система проигнорирует событие,

Упрощая всю эту историю, хочется сказать пару слов о принципе:

- Нажали на экран.
- Отправился своего рода сигнал на поиск ответчика (респондера), который первым ответит на сигнал и что-то сделает.
- В случае успеха — ответчик найден, что-то происходит — мы видим результат.
- В случае если ответчик не найден — система забивает и все живут дальше как жили раньше.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3c9255eb43587eef081e6e7dee59dca9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p5.png)

Источник: [developer.apple.com](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/using_responders_and_the_responder_chain_to_handle_events)

_Apple_ в официальной документации описывает _Responder Chain_ немного иначе — сверху вниз, но принцип тот же. В большинстве своём _Responder Chain_ в _iOS_ — связной список _subview_-элементов. 

Наверное, пока не совсем понятно, что нам это даёт в прикладном аспекте и чем может быть полезно. Так как в этом юните мы плавно подходим к теме жестов, то _Responder Chain_ отлично поможет нам подготовиться к  [[UIGestureRecognizer Жесты]]. Ведь _Responder Chain_ участвует при нажатиях, касаниях экрана и движениях.

Перед тем, как мы перейдём к методам _UIResponder_, стоит взглянуть на то, как работа с _UIResponder_ выглядит на минималках, так сказать, «под капотом». В нашем полу-практическом обзоре будут задействованы дефолтные элементы, которые мы получаем от _Xcode_ из коробки при создании проекта. Мы не будем добавлять ничего, просто посмотрим на поведение _UIWindow_. Для трекинга будем пользоваться обычным методом `print()`.

## **Заглянем под капот**

Создадим отдельный новый проект для наших экспериментов. Всё, что нас будет волновать, это _AppDelegate.swift_ и _ViewController.swift._ Сгруппируем их поближе друг к другу для удобства:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3ee36c7d53b9d0bbf33af3078d8ae78f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p6.png)

  

Откроем _AppDelegate.swift._ Тут уже есть «заготовки» в виде нескольких методов, но трогать мы их не будем. Кстати, заметьте, что _AppDelegate_ наследуется от _UIResponder_ и _UIApplicationDelegate_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/48045d435b6adc74b933bd2f04f96e0d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p7.png)

  

Добавим в самое начало класса `AppDelegate` переменную `window` с опциональным типом `UIWindow`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0fe9c9bcf3b8b826b315517e3a658cce/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p8.png)

  

Под методом didFinishLaunchingWithOptions переопределим метод touchesBegan():

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2ce4d82c9eb597b58aa7123e2383933d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p9.png)

  

И в этом методе добавим print(“AppDelegate: touchesBegan”), чтобы видеть подтверждение работы метода в виде логов в консоли:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5e9c2746da4a3bd8c0c67bc69f512f5b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p10.png)

  

Запустим наше тестовое приложение в симуляторе и тапнем по экрану (мышкой, насколько это возможно :D). И мы увидим в консоли заветное сообщение, потому что мы вызвали метод touchesBegan():

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/13b13dc49b2288cd372641f2b2aef23a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p11.png)

  

О чём это говорит? AppDelegate — это вообще последний респондер в цепочке, который принимает события. И мы можем это проверить. У нашего приложения ведь всего один _ViewController_: значит, главный _View_ первым принимает события. Идём в _ViewController.swift_ — будем делать extension для _UIView_ как для класса:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ee1557f0d76d43c93d0e65d11760bdae/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p12.png)

  

В нашем extension вызовем touchesBegan(), чтобы также вывести логи в консоль:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5802c8b062a2514cfbaf798f941b0f2f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p13.png)

  

И да _UIView_ — первый, кто принимает события:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3625488d2345ed86bf9245f00d721d3d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p14.png)

  

И ежели это так, то по логике _UIView_ может работать с этим методом, поэтому событие не было проброшено дальше остальным участникам цепочки, поэтому мы не видим в консоли _AppDelegate_, так как его нет надобности «тормошить». Но мы ведь можем так сделать? Можем!

Всё в том же методе, который у нас в extension прописываем выражение для передачи события следующему участнику _Responder Chain:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ee7dd8d418b375773ea46ffc55da329b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p15.png)

  

Забавный результат, не находите?

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8b07932af714497197696bfbcbb246eb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p16.png)

  

Дело в том, что здесь ещё участвует _UIWindow_ (вернее, его инстанс), отсюда и такие многочисленные логи. И да, мы не ошиблись — _AppDelegate_ стоит последним в цепочке, так как у нас есть _UIView_ и _UIWindow_, чтобы получать события. Ну и посмотрим, как у нас себя ведёт в таких ситуациях _ViewController_ — перенесём код из extension прямо после viewDidLoad:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/426617d81014e97fa1469e85a50589a4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p17.png)

  

В результате у нас первым так и идёт _UIView_, потом уже _ViewController_, затем _UIView_ уже как инстанс _UIWindow_ и в самом конце _AppDelegate_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ef366e5bd384e3523f7afc92cdfdea23/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p18.png)

  

И для полноты картины сделаем extension для _UIWindow_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/701e1caa34523fc7a891aa53e0bda776/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p19.png)

  

Теперь нашей цепочке отобразился _UIWindow_ нормально:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6e646537b3a00aa55a0094e0275c642f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p20.png)

  

К нашей гипотезе напрашивается вывод, что главный _View_ в _Responder Chain_ получает события первым. Затем уже _ViewController_, который перебрасывает событие на _UIWindow_. В итоге событие доходит до _AppDelegate_, но максимально в последнюю очередь. Конечно, _Responder Chain_ изменится, если мы добавим на _ViewController_ какие-то ещё _view_-элементы, но это уже совсем другая история.

## **Методы UIResponder**

Те методы, с которыми нам предстоит работать, лучше знать в лицо. Здесь мы пробежимся вкратце по каждому методу несмотря на то, что они описаны в документации. Потом будет проще понимать, что, где и когда использовать.

В целом эти методы представляют собой функции, которые берут два значения на вход (кроме `remoteControlReceived)`:

  
touchesBegan сообщает объекту, что на контроллере (_UIView, UIWindow_) начались касания — кто-то тапнул по экрану:

```swift
open func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?)
```

  
touchesMoved сообщает респондеру, что кто-то тапнул по экрану и стал делать перемещение:

```swift
open func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?)
```


  
touchesEnded сообщает респондеру, что процесс нажатия на экран прекратился — пользователь убрал пальцы от экрана, то есть отпустил пальцы:
```swift
open func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?)

```

  
touchesCancelled сообщает респондеру об отмене конкретного события из-за другого системного события — мало памяти:

```swift
open func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?)
```


  
pressesBegan сообщает объекту, что началось нажатие на физическую кнопку (кнопка громкости):
```swift
open func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```


  
pressesChanged сообщает объекту, значение, связанное с нажатием на физическую кнопку, изменилось:

```swift
open func pressesChanged(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

  
pressesEnded сообщает объекту, кнопку отпустили и нажатие благополучно закончилось как процесс:

```swift
open func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

  
pressesCancelled сообщает объекту, что из-за системного события (мало памяти) процесс нажатия на физическую кнопку прерван/отменён:
```swift
open func pressesCancelled(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```


  
motionBegan сообщает получателю, что началось событие движения — то есть айфон стали встряхивать, запустился процесс встряхивания:

```swift
open func motionBegan(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```


  
motionEnded сообщает получателю, что закончилось событие движения — то есть айфон перестали трясти, процесс встряхивания закончился:

```swift
open func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```


  
motionCancelled сообщает получателю, что событие движения отменилось:
```swift
open func motionCancelled(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```


  
remoteControlReceived сообщает объекту, что получен удалённый доступ, например, к аксессуару:
```swift
open func remoteControlReceived(with event: UIEvent?)
```

[Документация по _UIResponder_ подробно](https://developer.apple.com/documentation/uikit/uiresponder%C2%A0)

## **Что можем делать с UIResponder**

В реальности не стоит пугаться тех теоретических терминов, с которыми мы столкнулись в самом начале. У _Responder Chain_ есть адекватный способ применения, по которому проще всего понять пользу этого класса. 

Что ж, создадим новый проект. Времени это займёт немного, но мы создадим вью для экспериментов и немного потрогаем тему жестов.

**1.** Создадим пустой .swift-файл. В нём сделаем новый класс, который будет наследоваться от _UILabel_. Если вдруг _IDE_ будет ругаться на _UILabel_, значит вы просто не импортировали _UIKit_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4383593a0e1144383cd7309cf3855189/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_22.png)

  

**2.** Добавим булеву переменную canBecomeFirstResponder — её не надо объявлять, просто вводим название, _Xcode_ сам определит её и предложит нам. Эту переменную создали за нас, спасибо _Apple_ за упрощение. Делаем из этой переменной _closure_, который будет нам возвращать _true_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a72786cde653d51e99764db6c9019129/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p23.png)

  

**3.** Переходим на _ViewController_. Создадим объект нашего _ResponsiveView_ там:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6ad0ce7bbb01e3dc6236f12a69c97908/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p24.png)

  

**4.** Теперь зададим параметры нашему лейблу. Обратите внимание на скриншот — у нас две группы параметров. Обязательные предлагаем добавить как они есть, а с необязательными поработать самостоятельно, на усмотрение вашей фантазии. Возможно, вы добавите что-то от себя:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b809dbe107c74889cf675e987054f5ee/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p25.png)

  

**5.** Мы хотим обрабатывать событие долгого нажатия, но у нас нечем его распознавать. Разрешим пользовательское взаимодействие и создадим распознаватель жестов:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fbd787373eae3369685f410306854454/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p26.png)

  

Ворнинг не страшен, потому метод для долгого нажатия мы создадим. Скоро…

**6.** За пределами `viewDidLoad` сделаем _@objc-_метод с названием `longPressHandler`. Пока _IDE_ успокоится и не будет донимать нас ошибкой:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7ab8d1d483ee2cf020c76b8a6d4319a6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p27.png)

  

**7.** Вернёмся к нашему рекогнайзеру и под ним выставим минимальное время нажатия, сделаем 0.2. Мы же должны сколько-то подождать перед тем, как появится предложение действия:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cda56e749fbaf4d85f07ca040fe352be/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p28.png)

  

**8.** Теперь под `minimumPressDuration` добавим наш рекогнайзер на наш лейбл:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b476dde75d1f9109e11fb5ae8f6c8461/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p29.png)

  

**9.** А сейчас то, о чём мы говорили в начале юнита: в методе `longPressHandler` мы попросим _UIKit_ сделать наш лейбл первым респондером. В этом нам поможет :

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8ecd95c1736932ef4c04dce764c1b96f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p30.png)

  

**10.** После этого мы можем сделать контроллер меню и настроить его:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/38ae0bf4e6740256e6c8bd0b9e5279af/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p31.png)

  

_*Жёлтые ворнинги сейчас не так страшны, как в реальном проекте. Поэтому тут мы можем их себе позволить. Два метода более не используются в iOS 13+ → IDE жалуется._

**11.** Создаём элемент меню и добавляем его в массив menuItems:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6d53040d861c3e74e9965efc76e429da/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p32.png)

_Xcode, не ругайся, метод сейчас завезут._  

**12.** Добавляем метод saveClicked. Его суть проста — снимать с нашего лейбла статус первого респондента стандартным методом resignFirstResponder и выдавать в консоль значение _“Saved”:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9c40da5cde83600e579d30390ad06a5d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p33.png)

  

Запустим приложение в симуляторе, выберем наш лейбл, нажмём на него и подержим какое-то время. В результате увидим это:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3ec681406158ff8d3872bcaa211b6462/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u4_p34.png)

  

Такой результат означает, что мы всё сделали правильно, несмотря на небольшие ворнинги и что мы смогли обработать нажатие. Ну и нажав _Save_ мы увидим в консоли _Saved_.