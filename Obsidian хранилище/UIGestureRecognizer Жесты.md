
#UIGestureRecognizer #swift #жесты

Немного предыстории. Как мы знаем, _iPhone_ изначально был задуман как устройство, которое реагирует исключительно на жесты. Стив Джобс отвергал стилусы, ещё на презентации в далёком 2007 году. Со временем появился _Apple Pencil,_ но сейчас не о нём. Так как основная философия _iPhone_ — пальцы и ничего лишнего, то и управление задумывалось соответственно. И сегодня в айфонах мы видим разного рода жесты — свайпы, обычные нажатия, долгие «залипания» по экрану. Более того, теперь можно жесты создавать самостоятельно.

В предыдущем юните мы вскользь коснулись работы с жестами. Этот юнит мы полностью посвятим возможностям **_UIGestureRecognizer_**, рассмотрим его максимально — в теории, с примерами, визуально и в коде, в общем, как мы любим.

## **Сначала о жестах**

Чтобы у нас было больше понимания, как эти жесты используются в прикладном аспекте, то мы рассмотрим каждый на примере. 

Сразу хочется поблагодарить [QATestLab](https://training.qatestlab.com/blog/technical-articles/basic-touch-gestures/) за предоставление сегментированной информации о жестах в свободном доступе! Материалы в виде картинок были взяты из этой [статьи](https://training.qatestlab.com/blog/technical-articles/basic-touch-gestures/%20).

## **Тапы**

Тап считается одним из самых популярных жестов и используется везде. Например, тапы — это нажатия на элемент типа _UIButton_, нажатия на _UITextField_, чтобы всплыла клавиатура, нажатия по кнопкам клавиатуры и ещё много разных вариантов. Основные тапы делятся на четыре вида:

- **Одиночные тапы (single taps)** — обычные одиночные нажатия на экран с целью нажать кнопку и так далее:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/51be3ddc20af8393e681e2aa60d046b2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p1.jpg)
    
      
    
- **Двойные тапы (double taps)** — двойной тап, почти без отрыва, чтобы таким образом приблизить изображение:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ee6be09d1f801124e89cc1a23f4ea141/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p2.jpg)
    
      
    
- **Одиночный тап _двумя_ пальцами** — можно встретить в _Apple Maps_, при сильном увеличении карты достаточно коснуться экрана двумя пальцами, чтобы уменьшить масштаб:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ea541839d47b0d372f6a5a671731eaea/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p3.jpg)
    
      
    
- **Двойной тап двумя пальцами** — это такой же одинарный двойной тап, только первый раз мы можем тапнуть указательным пальцем, второй раз — средним. И если мы проделаем такой жест с картинкой, то результат не изменится: жест сработает — изображение увеличится, как в случае с двойным тапом выше:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3d6c36ed029f8b5d72ed757ef43609a9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p4.jpg)
    
      
    
      
      
    

## **Щипки**

- **Обычный «щипок»** — используется для уменьшения масштаба изображения при работе с фото, а также в приложениях с картами:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d71623ac88bb303a3e75626451f21789/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p5.jpg)
    
      
    
- **Сведение пятью пальцами** (для больших экранов) — на больших экранах типа _iPad_ этим жестом можно быстро выйти из приложения:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c4bba0c0e054fd7b95e73c1961890f47/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p6.jpg)
    
      
    
      
      
    

## **Растяжение (spread)**

- **Обычное растяжение** — работает с картинками, картами и прочими элементами, у которых можно менять масштаб. Этот жест увеличивает масштабируемый контент:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b1d2762f3a03413f907718d5aa612885/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p7.jpg)
    
      
    
- **Спрэд пятью пальцами** — чистит рабочий стол _iPad_, «выбрасывая» программы за его пределы. Чтобы это сработало, нужно коснуться экрана пятью пальцами одновременно и развести:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/072367388429cd3e7f6db79ff575a76e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p8.jpg)
    
      
    
      
      
    

## **Повороты двумя пальцами**

Касательно поворотов пальцами — про них нет смысла много говорить, но есть смысл посмотреть, какими они бывают. Возможно, половину этих жестов с картинок ниже мы вообще не используем, но они распознаются системой и позволяют делать разные манипуляции. Например, вертеть картинку так, как вздумается. На картинках внизу вы найдёте пять вариантов работы двумя пальцами на экране _iPhone/iPad:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1fa3775bc7116d913f7796591056babc/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p9.jpg)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b106747035e4a7e29440518fc5ea694d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p10.jpg)

  

## **Свайпы**

Свайп тоже достаточно популярный жест. Раньше ему не придавали особого значения — ну скроллишь себе галерею фотографий, листаешь странички в браузере и ладно. Позднее появился _Tinder_, интерфейс которого заточен под следующую механику: нравится анкета человека — свайпаем вправо, чтобы смэтчиться и начать общение, а если не понравилось — свайпаем влево, чтобы перейти к другим рандомным вариантам.

На самом деле, свайпы достаточно стары и с ними работает больше количество приложений — от стандартных до сторонних. Самые простые свайпы мы видим каждый день — в _Photos_, в браузерах, в том же _Instagram_ и ещё много где. Плюс этими же свайпами мы листаем рабочие столы в _iOS_, когда ищем приложение.

У свайпов несильно меняется суть в зависимости от количества пальцев, которые участвуют в одном свайпе. Это зависит от платформы: например, свайп из четырёх пальцев нецелесообразно применять на _iPhone_ — экран не такой большой.

Свайпы тоже имеют свои градации:

- **Основные одиночные свайпы** — пролистывание страничек в браузере или фотографий:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1980910c6afc0df9603e3f8337c32e41/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p11.jpg)
    
      
    
- **Двойные** — самый частый двойной свайп на это свайп двумя пальцами вниз. Будучи на одном из рабочих столов, мы можем сделать этот свайп по экрану и получить быстрый доступ к настройкам:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/70c42ccb6e3f61c8c9e1179149881082/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p12.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3447eec2c59fa81ca01d46a5fa65c15e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p13.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/eef5c4dd130651ead45accc8cbc7b33a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p14.jpg)
    
      
    
- **Тройные** — тремя пальцами можно на _iPad_ переключаться между приложениями, то есть свайп тремя пальцами влево или вправо:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6a8845547096138f1c3f8456a3250ecb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p15.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5eaab605d3852db4196f818b169fd838/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p16.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6dc5afd19bd635d97d74f63a4a9e9a3a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p17.jpg)
    
      
    
- **Свайпы для четырёх пальцев** — четырьмя пальцами можно на _iPad_ переключаться между приложениями, то есть свайп такой же свайп четырьмя пальцами влево или вправо, как это было в случае с тройным свайпом:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1e034ccd3a70bccec6f0b47ed8143faf/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p18.jpg)
    
      
    
      
      
    

## **Долгие нажатия (press and hold)**

Этот тип жестов можно сгруппировать в две категории, по два жеста на каждый:

- **Обычные долгие нажатия** — здесь мы просто нажимаем и держим палец или пальцы на экране дольше, чем при обычном нажатии. При этом мы не знаем, сколько секунд мы держим — мы можем держать три секунды, можем держать десять секунд — всё равно получим тот результат, который задан на _long press:  
    _  
    
     _![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0908e95eab2c73333faf966ffb24ae5a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p19.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/64a3040edb39f82d44b5033785f9b6e5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p20.jpg)_
    
      
    
- **Долгие нажатия с таймером** — к обычным долгим нажатиям и удержанию добавился таймер. Похожее мы смотрели бегло в _UIResponder_, когда задавали время удержания пальца на каком-либо _view_-элементе. Только здесь мы уже сможем оперировать со временем:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8a900d7c00104eff0af9215e58465903/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p21.jpg) ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/89a03b2c1731a92c1f01d34c94a10997/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p22.jpg)
    
      
    
      
      
    

## **Drag-жесты**

Эти жесты помогают нам перенести какие-то элементы между приложениями (если мы работаем с _iPad_ в _Split View_) или изменить порядок каких-либо предметов, например, изменить порядок задач в каком-нибудь _todoList_. Эти жесты делятся на два типа:

- _**Drag-and-Drop** —_ жест, с помощью которого можно захватить какой-то элемент (ячейка таблицы, ячейка коллекции), чтобы перенести его внутри приложения, либо перенести его в другое приложение:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c6f6699641dd4266a3161ca63e8b876c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p23.jpg)
    
      
    
- _**Press and drag**_ — в _iOS_ 14 этот жест позволяет как минимум изменить режим отображения фотографий в галерее — сделать плитку помельче или же покрупнее:  
      
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ba844faaacfedcfeffdead3c59535d12/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p24.jpg)
    
      
    

## **Жесты на симуляторе**

Мы привыкли к жестам на устройстве с физическим экраном, с возможностью прикасаться пальцами. В любом случае, стоит подготовиться к ситуации, когда у нас не всегда будет возможность тестировать приложение на устройстве. Мало ли что может произойти: в офисе устройства для тестирования отправились в ремонт, или тестировщик работает на удалёнке, а на личном устройстве тестировать запрещено (_NDA,_ все дела). И выход только один — понять, как производить симуляцию жестов на виртуальном устройстве прямо на _Mac_-компьютере.

В плане жестов наличие одной лишь _Apple Mouse_ сильно ограничивает разработчика при тестировании. _Apple Mouse_ поддерживает максимум работу с двумя пальцами, в то время как _TrackPad_ даёт больше возможностей разгуляться. _TrackPad_ — это здорово, но вряд ли он есть у каждого, даже на работе. Поэтому мы готовимся к худшим условиям, когда у нас только клавиатура и мышь. 

Клавиатура в такой ситуации способна помочь. Всё упирается в клавиши _Alt_ (которая _Option_) и _Shift_. Например, если удерживать _Option + Shift,_ то можно сымитировать мультитач-прокрутку. 

## Скринкаст на тему: «Жесты в симуляторе.‎»

А ещё у _Apple_ есть человекопонятный гайд на тему «Тач-жесты через мышь и клавиатуру», в котором есть вот такая таблица соотношений:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a70ca79a9dd2255bd50fe10a861645c9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p25.png)

Источник: [help.apple.com](https://help.apple.com/simulator/mac/current/#/deva6cdf367f)

## **Что такое UIGestureRecognizer**


**_UIGestureRecognizer_** — базовый абстрактный класс, реализующий в себе всю логику работы с жестами. При помощи _UIGestureRecognizer_ можно «обучить» _view_-элементы распознавать разные жесты. Как инструмент интерфейса, _UIGestureRecognizer_ отсутствует в списке элементов, которые можно перетянуть и положить на контроллер, что логично → он абстрактный.

У _UIGestureRecognizer_ есть несколько стандартных реализаций для семи типов основных жестов. В отличии от количества жестов, которое мы видели в теории по жестам, это довольно скудный список. В то же время эти семь типов позволяют разгуляться нашей фантазии в работе с жестами. И мы можем пощупать их визуально (достаточно вбить в поиске по _UIKit_):

- Тапы — _UITapGestureRecognizer_
- Два пальца по экрану как щипок, тот же зум — _UIPinchGestureRecognizer_
- Поворот двумя пальцами — _UIRotationGestureRecognizer_
- Свайп в любом направлении — _UISwipeGestureRecognizer_
- Смахивание от края экрана как жест возврата к предыдущему экрану — _UIScreenEdgePanGestureRecognizer_
- Скролл в любом направлении — _UIPanGestureRecognizer_
- Долгое нажатие, «залипание» пальца — _UILongPressGestureRecognizer_
- Собственный жест — _UICustomGestureRecognizer_

Уточнение: _UIScreenEdgePanGestureRecognizer_ нигде ранее нам не встречался. Дело в том, что иными словами он называется **сложный скролл**, то есть скролл от конкретной области экрана. Например, в _iPhone X_ и выше (кроме _SE_ 2020) есть экранный аналог кнопки _Home_. Это скролл от самого нижнего края экрана вверх, это движение позволяет нам вернуться на рабочий стол из приложения, тем самым отправив приложение в «ожидание».

У одного вью может быть несколько _UIGestureRecognizer_-элементов. То есть сколько для него _UIGestureRecognizer’ов_ установлено, столько жестов он может обрабатывать, реагировать на них и так далее. Естественно, если мы задали в коде настройки и условия для этого множества жестов, то и элемент будет вести себя соответственно. У картинки в стандартной фотогалерее на _iOS_ стоит как минимум три распознавателя жестов, которые обрабатывают множества движений из своих наборов: _UITapGestureRecognizer_, _UIPinchGestureRecognizer_, _UISwipeGestureRecognizer_.

В предыдущем юните мы вывели для себя логическую цепочку, как работают жесты в _iOS_ на основе методов. Стоит углубиться в понимание процесса работы самих жестов.

**Важно:** _UIGestureRecognizer_ первым получает право обрабатывать _UITouch_-ивенты.

Мы привыкли, что для нас тот же свайп — один жест, с помощью которого мы можем листать фотографии в стандартном приложении _Photo_. Для системы жест разделён на несколько ключевых точек и выглядит как **цепочка событий**.

## **События**

В прошлом юните мы затронули тему событий, и в коде у нас был тип _UIEvent_. _UIEvent_ мы тоже не найдём среди элементов _UIKit_. Как мы знаем, в _iOS_ есть три типа событий:

1. Сенсорные события (касания экрана)
2. События движения (те же встряхивания)
3. События дистанционного управления (прибавление громкости физическими кнопками)

Событие _UIEvent_ как раз уже содержит в себе касания — одно или более, — которые связаны с этим событием. Когда сенсорное событие происходит, система адресует его соответствующему _responder’у_ и вызывает соответствующий метод типа `touchesBegan()`. Далее респондер использует нажатия для определения конкретного действия: один раз ткнули по _view_ — он изменил цвет на синий, зажали палец на _view_ на две секунды — всплыло специальное меню.

## **Немного о UITouch**

_UIKit_ предоставляет нам _UITouch_ для создания жестов — это такой объект, отражающий информацию о локации, размере, передвижении и силе нажатия на экране. Наследуется он от класса _NSObject_.

Если верить документации, то _UITouch_ включает в себя методы доступа к _view_ или _window_, в котором касание произошло. Также предоставляется возможность узнать:

- когда произошло это касание,
- коснулся ли пользователь двумя пальцами одновременно (спасибо мультитач),
- сильно ли нажал на экран.

Плюс _UITouch_ отслеживает фазу касания — начало касания, движение пальца по экрану, конец жеста, или жест вовсе отменён. Более того, данные о нажатиях можно хранить. Об этом и других нюансах мы побольше поговорим в практической части.

**Как видят жесты обычные пользователи:** единое действие (да в реальности мы не задумываемся — нажимаем, свайпаем и всё)

**Как видит жесты iOS** — цепочкой событий: палец коснулся экрана → палец идёт по экрану → палец оторвался от экрана.

В системе эта цепочка событий обрабатывается так: 

- пользователь коснулся экрана,
- в этот момент система создаёт _UITouch_-объект,
- этот _UITouch_-объект будет ассоциирован с текущим касанием на всё время его жизни → то есть пока палец не оторвётся от экрана.

Пояснение: 

1. На время всей цепочки событий для каждого пальца, который касается экрана, есть свой уникальный _UITouch_-объект.
2. Затем система определяет _view_-элемент, фрейм которого содержит точку касания экрана.
3. Этот _view_-элемент становится тем самым _firstResponder._
4. Этот _view_-элемент, ставший _firstResponder_, получает уведомления о _UITouch_-объекты.
5. Дальше этот _view_-элемент пробрасывает _UITouch_-объекты по responderChain.

Вот такая развёртка одного жеста происходит в системе, когда мы хотим просто перелистнуть фотку. Конечно, это всё недоступно глазу обычного пользователя и он видит это всё как «должно быть». В это время в системе происходят процессы распознавания жестов по отдельности. И всё это за то время, что мы пролистываем фотографию, а это даже меньше секунды.

После того, как мы рассмотрели _UIEvent_ и _UITouch_, вернёмся к нашим жестам. Как мы уже знаем, _UIKit_ предоставляет нам семь инструментов для распознавания жестов. Если в поиске по _UIKit_-элементам забить _gesture_, то мы увидим семь стандартных элементов + 1 для полёта фантазии:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d1bc96512b8aa0a9e5eea599ef0e7167/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p27.png)

  

Ещё раз пробежимся по уже знакомым нам _UI_-элементам для работы с жестами:

- Тапы — UITapGestureRecognizer
- Два пальца по экрану как щипок, тот же зум — _UIPinchGestureRecognizer_
- Поворот двумя пальцами — _UIRotationGestureRecognizer_
- Свайп в любом направлении — _UISwipeGestureRecognizer_
- Смахивание от края экрана как жест возврата к предыдущему экрану — _UIScreenEdgePanGestureRecognizer_
- Скролл в любом направлении — _UIPanGestureRecognizer_
- Долгое нажатие - «залипание» пальца — _UILongPressGestureRecognizer_
- Собственный жест — _UICustomGestureRecognizer_

Распознаватели можно поделить условно на два типа:

1. Дискретные — _UITapGestureRecognizer_, _UILongPressGestureRecognizer_, _UISwipeGestureRecognizer._
2. Непрерывные — _UIPinchGestureRecognizer_, _UIRotationGestureRecognizer_, _UIPanGestureRecognizer_, _UIScreenEdgePanGestureRecognizer._

Дискретные распознаватели в своём исполнении похожи чем-то на _UIButton_: Задали _action_, который будет вызван один раз → Как только наступит требуемое событие.

Непрерывные же какие-то неуёмные ребята в самом деле — вызывают _action_-метод много раз, при каждом значимом изменении для распознаваемого ими жеста. То есть если у нас в процессе жеста палец съехал хотя бы на один пиксель на экране, но непрерывный распознаватель _UIPanGestureRecognizer_ орёт и бьёт тревогу — чтобы обработать движение и обновить интерфейс.

Основное свойство непрерывного рекогнайзера — **state**, **UIGestureRecognizer.State**. Обрабатывается оно в _action_-методе и может принимать следующие значения:

- `possible` — распознаватель готов работать
- `began` — распознаваемый жест начался
- `changed` — происходит изменение состояния - движется палец при скролле
- `recognized` (или `ended`) — жест закончился
- `cancelled` — жест отменился
- `failed` — жест не получилось распознать: ожидали скролл двумя пальцами, но экрана коснулся лишь один палец

## **Как работать с жестами в сториборде и в коде**

## **Сториборд как начало начал**

Создадим новый проект для работы с жестами. На _ViewController_ добавим два разных _UIView_. Убедимся, что в настройках _view_-элементов стоит галочка на _User Interaction Enabled:_

_![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c3dc7d45ad4d9f73f178525a09d48a35/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p28.png)_

  

Теперь покрасим их:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b9ed324c660fee5cb657ee2c1e7d3104/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p29.png)

  

Найдём _Pan Gesture Recognizer_ и перетащим его на тёмно-синий _view_-элемент. В верхней плашке _ViewController_ появится иконка жеста, что будет означать, что жестовый элемент успешно добавлен. То же мы увидим в иерархии вьюшек:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c0285f19e41c9f678c7b57b414065dd8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p30.png) → ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4804f796c8960dd4c72feb6c52ec7a8b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p31.png) → ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a3317a8d1f8d405cdd618c72803a4ad6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p32.png)

  

А что сейчас собственно произошло? Ведь никаких особенных изменений не случилось. Мы подвязали _Pan Gesture Recognizer_ к одному нашему _view_-элементу. Это значит, что теперь любые движения внутри него будут распознаваться. В теории да, но мало просто добавить элемент — надо ещё и написать функцию, которая будет делать два действия:

- проверять, трогают ли вьюшку,
- реагировать соответственно.

Кстати, распознаватель жестов можно связать с кодом. Необязательно создавать аутлет, можно сделать сразу @IBAction. Потянем его в код по классике — зажмём _Ctrl_, левой кнопкой мыши тянем соединитель на _ViewController.swift:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1830b9adfa40a00a0b2f25effb459313/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p33.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5629b38aba6a4ba0804b6da512a10d8b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p34.png) → ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/27b90b4be1fc0b133802af3984cc570b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p35.png)

Единственно только для собственного удобства, в @IBAction изменим `sender` на `gesture`, чтобы понимать, к чему мы обращаемся:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/03206c51fcad1c406457b8936d1bf1e4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p36.png)

  

В плане жестов _Xcode_ ленится добавлять делегаты. Если мы добавили рекогнайзер, то делегат нам придется тоже добавлять самостоятельно. Выберем рекогнайзер, зажмем _Ctrl_, нажмем левой кнопкой мыши и поведем ниточку от рекогнайзера к _ViewController_ в иерархии элементов до появления окошечка с пустым делегатом:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ccd06951828ebfee67b4cffe9d6c3fee/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p37.png)

  

Нам остается только выбрать делегат, чтобы рядом с ним в этом окошечке появилась точка:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f7928272da40066d375e7a33ed0a0861/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p38.png)

  

## **Код начинается здесь**

Теперь мы можем нормально работать с этим методом. В методе `panAction` у нас будет три основных шага, ориентированных на возможность распознавание жестов у конкретного view. Обратите внимание — мы можем не создавать аутлеты для наших _view_, потому что бОльший приоритет отдаётся жесту как экшену. И в этом экшене мы пойдём через `guard let` для дальнейшего обращения к _view_ и переиспользования.

**1.** Нам нужно интерпретировать жест. В методе создаём переменную `gestureTranslation`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b8fd7ebbc3fd2371ff70f4d2289a09c1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p39.png)

  

**2.** Так как мы без аутлета, у нас не объявлен вью. В то же время у него два развития событий для жеста — он либо есть, либо его нет. Поэтому привет, `guard let`. При этом мы находим наш переиспользуемый вью через знакомую переменную `gesture`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4d155afd627c67160d867497a352c397/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p40.png)

  

**3.** После того как мы сделали нашу переменную чистой через раскрытие опционала, мы зададим центр нашему _view_-элементу:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6c8a8a0e5ad4a13561d1b5c62a8d1302/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24.5.png)

Это важно, иначе мы не сможем воспользоваться распознаванием жестов.

**4.** Наш интерпретатор должен обнуляться, когда всё закончится, иначе с каждым разом наш блок будет улетать за пределы экрана. Обнулим интерпретатор через `setTranslation` для нашего _view_ и сделаем _unwrap_ для `gesture.state` через `guard let`. Нас интересует только законченная фаза `.ended`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/299eea27170d039521ecf213fcf6dc81/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p41.png)

  

**ATTENTION:** В _Xcode_ 12 при добавлении _Gesture Recognizer_ на _ViewController_ связь между ними устанавливается автоматически. В более ранних версиях приходилось настраивать связь между ними через _Ctrl_ + левая кнопка мыши. И если сделать такую комбинацию сейчас, то увидим, что за нас уже продумали — в _Sent_ _Actions_ уже стоит наш _panAction_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a75448fdb3fd9811e981ad86efc235f0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p42.png) → ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e73bba48f26640735959911b325746b1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p43.png)

  

А вот так будет выглядеть блок _Connection Inspector_ при добавленном _Gesture Recognizer_ на _ViewController_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0620f9a4d3082860b12d43851d57fd96/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p44.png)

  

Запустим в симуляторе. Если вы всё правильно сделали, то результат у вас будет такой же, как в этом коротком видео:



**4.** Добавим в наши рекогнайзеры привычный метод print. Для фиолетового вью метод будет выдавать в консоль _“Purple view panned”_, для синего — _“Blue view panned”:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d6dc9ce52ce525773948fcdb9c192154/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p46.png)      ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/42c3715afc9ec6b4d457dfa9554a284a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p47.png)

  

Если мы запустим и будем перетаскивать наши _view_-элементы, то увидим, что метод print срабатывает каждый раз, как мы передвигаем наши вьюшки. Стоит отметить, что при простом тапе по вьюшке print не вызывается (спасибо, Кэп, но это важно):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3244643e9cd44c373c7bbfbe6899a0fe/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p48.png)

  

**5.** Сейчас мы немного поиграем. Уменьшим наши вьюшки на _ViewController_. Создадим оранжевый вью, разместим его почти в самом верху экрана и сделаем ему стандартные ограничители:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b3f188269352870ded350e85ad243f99/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p49.png)

  

Результат на картинке внизу:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/273391eb2fcaba410252c7f7882f7160/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p50.png)

  

Зачем мы это собственно делаем? Мы выстраиваем черту, доходя до которой наши вьюшки будут исчезать.

**6.** А вот теперь нам реально понадобятся аутлеты. Сделаем аутлеты для всех трёх вью:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/94299d7d88a01b817bbaa89dc96cdc86/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p51.png)

  

**_By the way:_** в рамках практики мы будем создавать локальные переменные в методах жестов, чтобы не возиться с инициализаторами. Так будет быстрее и нагляднее.

**7.** У нас уже есть жестовые методы, поэтому остаётся их модифицировать. Нам нужны координаты наших вью-элементов. Добавим две переменные для фреймов в panAction:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ba61e71126d445f0542a6514dc284891/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p52.png)

  

И две переменные в purpleViewPanAction:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9aab212a3fbac5211c0505c1a96b06f1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p53.png)

  

**8.** Механизм пожирания наших вьюшек очень простой — вьюшка попадает на оранжевую черту. У черты есть диапазон значений от минимального y до максимального y (x проверять не будем). Если y-координата перетаскиваемой вьюшки попадает в диапазон minY...maxY оранжевого вью, то наш перетаскиваемый элемент исчезает и перестаёт существовать. Если нет, то он живёт своей обычной жизнью. Цикл добавим в конец функции с жестом:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4cd73768ddaa29d6b76f88623313701f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p54.png)

  

**Суть цикла:**

- Делаем пробежку по диапазону _CGFloat_-значений, которые тут же приводим в _Int._
- Выдёргиваем из фрейма синей вьюшки координату y и сверяем её со значением из диапазона.
- В случае совпадения значений отключаем _blueView._

**9.** Аналогичную историю проделываем с другой нашей функцией распознавателя:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a2a3c35b3ba6dfbd28683699133b30f6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p55.png)



## **Как создавать собственные жесты**

Если со встроенными наборами жестов мы разобрались, теперь посмотрим, как и зачем создавать кастомные жесты. Вопрос зачем закрывается сразу — сделаем кастомный жест, в зависимости от движения одного элемента изменялся размер другого.

В рамках этой практики мы сделаем кастомный жест, с помощью которого можно будет потрясти один определённый _view_-элемент, а размер изменится у другого. В нашем случае, мы потрясём синий или фиолетовый _view_, а размер оранжевого либо увеличится, либо уменьшится.

Настало время _UIGestureRecognizer_ как такового, потому что это класс нашего _Custom Gesture Recognizer’а:_

_![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7ad5a581e68bdc6d12d0d0bc5d0498ca/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p56.png)_

  

**1.** По факту мы добрались до части, в которой мы получили возможность разгуляться в коде по полной. Ведь у нашего жеста будет свой класс, который наследуется от _UIGestureRecognizer_. Создадим новый файл типа _Cocoa Touch Class,_ сабкласс выберем _UIGestureRecognizer_ и назовём файл _MixGesture_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4e1200256aaf34e9bad9d5153372cff9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p57.png)

  

**2.** То, что мы увидим после создания файла — наш созданный класс наследуется от _UIGestureRecognizer_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a0c727d322022f84cc621af3d4b0ffa0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p58.png)

  

**3.** Теперь нужно подумать насчёт самого жеста. По идее мы трясём вью, значит тряска это сначала движение в одну сторону, потом в другую, следовательно у нас уже два направления и два необходимых движения. Также нам нужно обозначить дистанцию для жеста-тряски и загнать её в определённые рамки — дать тип _CGFloat_ и присвоить возможное значение, пусть это будет 35. Отразим это в коде — добавим две константы в класс:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cffae029dc029e863471257f42857d3f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p59.png)

  

**4.** Касательно направлений движения — тут нам поможет _enum_, в котором будет три направления. Почему три — одно из них неизвестное:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/54eb0050e2b9e012e017884880c85fd2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p60.png)

  

**5.** Далее нам нужно:

- Сосчитать количество встрясок пальцами нашего вью — сколько раз мы меняем направление жеста во время движения. Например, когда мы меняем направление движения три раза, то это считается за выполненный жест.
- Отталкиваться от стартовой позиции — это точка, в которой жест берёт своё начало. Мы обновляем её каждый раз, когда изменяется направление движения.
- Подходить к конечной точке — финальное направление движения пальца, которое начинается неизвестно где. После минимальных сдвигов, мы проверяем, где жест (влево или вправо) и, соответственно, обновляем нашу финальную точку.

Давайте создадим три переменные. Тут-то нам и поможет наш `case undefined`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ae0902895248c625e046b5e2718f5414/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p61.png)

_*finalDirection_ получает тип _MixingGestureDirection_ и принимает значение _undefined_  

**6.** А вот здесь начинается весь **экшн**. Состояние жеста должно обрабатываться. И мы не обойдёмся обычными параметрами, как это было в начале. Почему? У нас сложный жест, а не просто встроенный в систему свайп. Поэтому придётся прописать ряд методов, которые содержат _UIGestureRecognizer_. Эти методы мы рассматривали в начале юнита. Разобьём нашу дальнейшую работу над методами на логические блоки:

**Сброс** — в _reset_-методе у нас будет обнуляться mixingNumber, mixingStartPoint приобретёт значение .zero, а finalDirection станет .undefined. Также зададим условие для  state — если распознаватель в состоянии готовности, то он у нас будет фейлиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b3c208e9618d0c3e21e2df99465d0725/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p62.png)

  

**touchesBegan** — у нас происходит тап по экрану, значит, жест начинается. При этом mixingStartPoint должен обновляться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e1145748c9aab855208ffbf9b3f45f83/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p63.png)

  

**touchesMoved** — так как движение в нашем случае является базой кастомного жеста, то здесь помимо стандартной обработки нажатий, нам понадобится несколько переменных и условия для них:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7b86c3e1f7a86738c2af4251530ab959/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p64.png)

  

Вроде бы классика, но это не всё. Надо сделать внутри метода две константы, первая из которых будет отражать расположение жеста, а вторая будет считать разницу локации жеста и самой начальной точки жеста:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9857787e6bd3688d3d670e4f31fdb891/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p65.png)

  

Условие:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4f16f7ec29e439c4bd6d34bfa3e04c3d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p66.png)

  

Теперь создадим переменную типа _**MixingGestureDirection**:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d816fd7ec82bcb35e0fdce5b70baa7ae/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p67.png)

  

И дальше мы будем делать проверку у `horizontalDifference` на отрицательные значения:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b5300fd328a8b52f037582ff34c05004/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p68.png)

  

Потом проверим finalDirection на все значения энума, обновим внутри if-closure переменные, созданные в начале метода, а также state:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bb9b38e0d7d9299862d909448d931dea/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p69.png)

  

state в нашем случае проверяется на готовность рекогнайзера и на количество насчитанных движений при тряске вью-элемента. В итоге, если state принимает значение possible, а число движений насчитано больше, чем требовалось, то рекогнайзер отключается:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9e21cb70b8c7f848c8bbcbb636bfb81a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p70.png)

  

**touchesEnded** — здесь мы будем вызывать reset:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0e5f917c6cff2fb709284178b0601c4c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p71.png)

  

**touchesCancelled** — и здесь тоже будет вызываться сброс рекогнайзера:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5188d1150a872f91979174e0eb6c6379/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p72.png)

  

Есть две новости — хорошая и очень хорошая.  
**Хорошая:** мы собрали распознаватель кастомных жестов.  
**Очень хорошая:** распознаватель нужно интегрировать в код нашего _ViewController_, и он готов к этому полностью.

**7.** Переходим в файл _ViewController.swift._ Нас интересует метод viewDidLoad и тремя строчками кода устанавливаем туда наш рекогнайзер:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/496ba6b564640d211fcc18f0205be20e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p73.png)

  

Почему ошибка? Просто мы ещё не написали хэндлер для нашего рекогнайзера. Кстати, должно быть, вы помните, что это будет _objc_-функция. А так у нас объявлена переменная для рекогнайзера, делегат установлен и добавлен жест на _blueView_ (будто метод _view.addSubview_, но только для распознавателя). Ну, так создадим его:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a00197cd77bc87f4273b47bcaf232d3e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p74.png)

  

**8.** Теперь пропишем в функции, что мы хотели бы от неё. А именно изменение ширины оранжевого вью-элемента. Мы хотим, чтобы при каждой такой встряске наш оранжевый вью уменьшался в ширину на 10 единиц. Сделаем четыре локальные константы для нашего оранжевого вью и зададим параметр для фрейма — ширина (`orangeViewWidth`) должна терять 30 единиц каждый раз, когда мы трясём синий вью:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d21ded38772236fec68ee4a2587c7bbe/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p75.png)

  

**9.** Кстати, пока мы делали хэндлер, мы забыли о главном — наш класс `ViewController` должен также иметь параметры для работы с жестами. Отсюда и ошибка:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cf80dc4a2adac354e8d807fdc8f7da4f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p76.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2da9be4fdcbe22f99ddaa93fdc1dd622/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p77.png)

  

Мы просто пропустили один протокол у класса:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bfb057bc69d4ae5c2f98f99df4ba9695/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u5_p78.png)

  

И теперь эта ошибка благополучно исчезнет. В скринкасте мы запустим наш код.