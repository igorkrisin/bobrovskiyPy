#UIControl #swift 

Перед тем, как мы будем создавать свой кастомный _UIControl_, мы сначала познакомимся с _UIControl_ в теории. 

**_UIControl_** — это класс для реализации поведения визуальных элементов, которые реагируют определённым образом на действия пользователя. 

Такое определение нам даёт документация. Если начать искать _UIControl_ в панели _UIKit_-элементов, то мы ничего не найдём. Да, так и есть. Дело в том, что это такой класс, который объединяет в себе элементы типа **_UIButton_**, **_UISegmentedControl_**, **_UISlider_** и другие подобные элементы контроля. Ведь если рассуждать логически: слайдер — контроллер для громкости, следовательно, он осуществляет контроль. Поэтому он и находится в этом классе **_UIControl_**.

Картинка внизу наглядно отражает, какие элементы включает в себя _UIControl,_ и что он из себя в принципе представляет:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2e99ba4f20c812521c2cf77c700cb6be/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p1.png)

Источник: [Coursera](https://lms.skillfactory.ru/xblock/%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8)

Как мы видим, _UIControl —_ это сабкласс _UIView_, который работает с пользовательскими действиями через _UI_-элементы контроля.

В предыдущем юните мы уже отчасти делали кастомный контроллер — круглая кнопка из стандартного приложения «Калькулятор» на _iOS_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9c4e00128c42f6058f786430190ffc4f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p2.png)

  

С наследованием от класса _UIControl_ ситуация будет обстоять немного иначе — мы создаём новый элемент для работы с интерфейсом, наследуясь от класса _UIControl_. При этом система будет распознавать наш кастомный контрол-элемент в качестве самостоятельной единицы.

## **Собственный мини-контроллер**

Давайте сделаем собственный _UISegmentControl_, который не будет иметь ничего общего с его оригинальным классом, но при этом работать будет абсолютно так же. Мы не просто соберём контроллер в стиле «чтобы был», а найдём ему применение. Вот так будет выглядеть результат нашего контроллера:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/38998feba1ccbc6dcd2e94175d958a75/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p3.png)

Вроде _UISegmentControl_, но не он  

0. Давайте создадим новый проект. Тут всё стандартно, вы знаете, как это делать. Перед нами снова наш привычный _tabula rasa_ сториборд:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c054f54c466f3f6e8051bfa77701d0bb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p4.png)

  

Сейчас нам очень не хватает одной детали — класса для нашего будущего контроллера. Создадим пустой _.swift_-файл, назовём его _CustomSegment_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2218743fdba4021d543ba64d872dda91/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p5.png)

  

В пустом файле мы видим только импортированный внутренний фреймворк _Foundation_, чего нам недостаточно. Добавим недостающий фреймворк — _UIKit_, а также создадим класс для нашего кастомного контрол-элемента:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9ceb68699eac66f8ddb7eb1ce42d427c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p6.png)

  

Как видите, мы наследуем класс от _UIControl._

1  

Учитывая, что в нашем элементе есть три надписи — _Daily, Weekly_ и _Monthly_, — нам нужно сделать для них переменные. Для удобства внутри класса сделаем массив `[UILabel]`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8b62bd52cad951124b84e4d2f0802fd5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p7.png)

  

2  

Помимо массива надписей [UILabel]создадим ещё _UIView_ для работы с визуальной частью нашего контроллера. Пока создадим и забудем о нём ненадолго:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3de36f33543f9829ae00a8b227158cbe/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p8.png)

  

3  

Далее, внутри этого же класса делаем _closure_ с массивом трёх элементов:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3721971414c5c2bcf2e5522a19590a6d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p9.png)

  

4  

Мы снова пошли через _closure_ и наблюдатель `didSet`. Внутри замыкания с наблюдателем мы будем вызывать функцию `setLabels()`. Пока что _IDE_ ругается, так как не видит эту функцию в коде. Окей, но мы позже создадим функцию `setLabels()` для работы с надписями в контрол-элементе. 

Сейчас нам важно задать параметр `selectedIndex` нашему контроллеру. Для этого снова идём через _closure_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ef76b1f20685fb13b1959c9f2ff74101/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p10.png)

  

Как мы видим, _IDE_ снова ругается на несуществующий метод в коде. Мы уже должны целых две функции! По крайней мере, благодаря красным ворнингам мы точно не забудем создать эти методы. Давайте с ними разберёмся.

5  

`setLabels()` — метод для работы с нашими лейблами, будет также следить за тем, чтоб массив надписей не принял слишком много элементов и не сломал нашу задумку. Метод состоит из двух важных частей — чистка массива от лишних элементов + установка первичных настроек:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3f3ae00ff31133e571b53bbfdb1db034/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p11.png)

  

**Суть:** мы очищаем наш массив для того, чтобы положить туда три настроенных лейбла

6  

Касательно `showNewSelectedIndex()`, создадим его прямо после `setLabels()`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4a110377b3bc9f4df7fbb040174f7902/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p12.png)

  

**Суть:** мы достаём из массива лейбл по `selectedIndex`, а наш `simpleView` получает фрейм лейбла.

7  

Вернёмся к `selectedIndex` в коде и под ним создадим инициализатор + IDE попросит нас добавить `required init`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/39021937cd61b4d410cfaafaf80ccb52/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p13.png)

  

8  

Далее, уже чуть ниже `required init` создадим метод `setView` для нашего `simpleView`. В нём мы добавим необходимые визуальные настройки для _view_ через код — потому что всё по хардкору:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/10cfe06f6684e76b31a99e3b6e6d3a09/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p14.png)

  

Мы покрасили наш _view_ и задали ему форму, поставили в него надписи благодаря функции `setLabels()` и добавили наш элемент как _subView_ самым первым — то есть с индексом 0.

9  

Теперь мы будем отслеживать нажатия. Стоит сразу предупредить, что никаких сложностей с жестами в этом юните не предвидится. Максимум мы познакомимся с жестами как с существующими элементами, но подробно рассматривать мы их будем в следующем юните.

После метода `setLabels` вызовем метод `beginTracking`. Суть нашего трекера нажатий в том, чтобы пробегаться по массиву лейблов и искать там _CGPoint_ как локацию. У нас есть одна константа `location`, опциональная переменная `calculatedIndex`, цикл с двумя параметрами, плюс проверка `selectedIndex` на `nil`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2ee794b363b5b1bb4f7bb451b5628424/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p15.png)

  

10  

Сейчас вернёмся к методу `beginTracking` и над ним вызовем метод `layoutSubviews()`. В этом методе мы сделаем условие-проверку, при выполнении которого наши лейблы получат дополнительные параметры:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/30661bb296dde5e14958c817f718c0fb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p16.png)

  

`selectedLabelColor` и `thumbColor` пока не существуют, но это «задел на будущее», в дальнейшем мы сделаем редактируемые свойства.

11  

Спустимся под функцию `beginTracking` и сделаем два метода — `setSelectedColors` — для цветов, и `setFont` — для шрифта соответственно:

Методы достаточно простые. `setSelectedColors` пробегается по массиву лейблов и красит их в стандартный цвет (который мы пока не сделали). Плюс он делает проверку - если у нас есть лейблы в массиве, то они выбранный лейбл получает другой цвет (который тоже ожидает создания). Ну и также этот метод красит `simpleView`. Практически аналогичные вещи делает `setFont`, только со шрифтами:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/99a8e3e00e48783a83aa45342135d073/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p17.png)

  

Спойлер: четыре несуществующих параметра станут @IBInspectable-свойствами. Скоро…

12  

Добавим @IBInspectable-свойства, чтобы ими можно было управлять не только из кода, но и через _Interface_ _Builder_. Ну и чтоб _IDE_ перестала ругаться. После _closure_ с `selectedIndex` добавим шесть свойств, четыре из которых @IBInspectable:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ef86348ccf1298083617787601713551/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p18.png)

  

И да — ворнинги пропали! Как же я люблю @IBInspectable-свойства, вот они сверху вниз. Ничего не напоминает?

Единственное, в рамках этого шага дополним `showNewSelectedIndex`: добавим цикл с двумя параметрами, чтобы покрасить невыбранные элементы; подкрасим выбранный элемент — у нас ведь есть теперь инструменты:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cb7cc185cb2b1720771744523dfb266e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p20.png)

  

Всё? На самом деле, мы забыли добавить один важный параметр, без которого реальный пользователь не сказал бы нам «спасибо», а тестировщик отдал бы задачу назад.

_**Attention:**_ сейчас мы сделаем простую анимацию, без которой этот контроллер невозможно переваривать. Более подробно с анимацией вы познакомитесь в следующем модуле, а здесь мы разберём простейший её вид для красоты нашего _UI_-элемента.

В методе `showNewSelectedIndex` пропишем анимацию для _UIView_. Сразу увидим четыре новых параметра с типом _CGFloat_, а внутрь кода с анимацией поместим выражение с размером нашего _superView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4d61220f91fe4534b832f7bdeef665ff/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p21.png)

  

`withDuration` — время анимации в секундах  
`delay` — задержка во времени анимирования, тоже в секундах  
`usingSpringWithDamping` — частота затухающих колебаний (интервал от 0.0 до 1.0)  
`initialSpringVelocity` — начальная скорость анимации

Вот так мы случайно частично познакомились с анимацией. В следующем модуле вам будет легче её понять.

13  

Последний шаг в файле класса — _constraints_. По логике у нашего кастомного контроллера три кнопки. Поэтому _constraints_ мы будем добавлять при помощи цикла, который будет бегать по массиву `items`. Добавим собственный метод `addIndividualItemConstraints` с двумя входными параметрами - `items` как массив _UIView_ и `mainView` как _UIView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c1094372bb8be61a1df0a00545bb10c8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p22.png)

  

Наш метод будет выглядеть просто: цикл, затем две проверки на `index,` и в каждой проверке выражения при несоблюдении условий. 

В реальности, пока рано подводить итоги, потому что с появлением новых методов нам придётся дополнить наш код. И начнём мы с класса _CustomSegment_. Тут ничего трудного, вы знаете, как сделать его @_IBDesignable_.

В цикле с двумя параметрами мы сразу добавим верхние и нижние ограничители:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1ef890724b61931787b983dfe5b4c0f8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p23.png)

  

Затем следует проверка: что если индекс у нас нулевой (выбрали самый первый элемент), плюс условия — что, если нет:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4129cf9d4a17f426d63d57a253ad0a03/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p24.png)

  

И наконец — проверяем индекс элемента и распределяем _constraints_ на оставшиеся кнопки при двух условиях:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/05cd5276e21891e7f831b0eb7982670d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p25.png)

  

В итоге, так выглядит наш метод с _constraints_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7881258b2ab1005a097e4f16b02ed01a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p26.png)

  

А вот дальше интереснее. В _closure_ массива `items: [String]` внутри наблюдателя `didSet` сделаем условие, а внутри условия поставим `setLabels`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ce71aef0bebb21558a18dc87aad9eb95/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p27.png)

  

Перейдём к инитам — в них тоже пропишем `setView`: в `init(frame: CGRect)` и в `required init`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0a334e95961d3ab99b6bc2157c2e99b4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p28.png)

  

Теперь поправим сам метод `setLabels` — там не хватает шрифта цвета фона элемента, а также надо отключить `autoresizing mask` и поправить `textColor` — ведь у нас есть два ситуативных цвета:

- В `textColor` применим тернарный оператор
- Цвет фона сделаем прозрачным
- За параметр шрифта у нас будет отвечать аналогичная переменная, она ещё и _IBInspectable_
- Отключим авторесайзинг у лейблов
- Добавим _individual constraints,_ иначе целый блок кода написан, а что с ним делать…

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ed3aa59383e61d99964ac3123d3ff49a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p29.png)

  

Метод `setLabels` теперь не узнать. В общем-то это были наши финальные штрихи. Дело теперь за интерфейсом. Переходим в сториборд.

## **Что по визуалу**

Давайте покрасим наш контроллер в серый цвет, чтобы было лучше видно. _Light Gray Color_ вполне хватит:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cbdabf9ca21098050b2a892bbf25a8f9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p30.png)

  

Перетащим _UIView_ на наш контроллер и сделаем сам элемент длинным и узким:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8b5e04fd4559f48ec25addab0b51f5fb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p31.png)

  

Зададим в _Identity Inspector_ кастомный класс. В нашем случае это _CustomSegment_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5252182e84468a57899f58b14443abdd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p32.png)

  

Буквально за несколько секунд сториборд отрисовал нам кастомный элемент и отдал нам четыре @IBInspectable-свойства на изменение при помощи визуального редактора. Все четыре свойства имеют значение _default_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/474e6cec1577d8850b05d5b982cbcf78/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p33.png)

  

Кстати, если сториборд не прогрузил _view_-элемент, — это не страшно, мы всё равно можем увидеть его в симуляторе. Обычно такая проблема решается путём рандомного перехода по файлам — из сториборда в код и обратно. Если же не грузит совсем и появляется красный ворнинг, то можно сделать _**clean up**_ — Cmd + K → Выйти из _Xcode_ и снова открыть проект.

Поиграем с настройками, которые мы вывели сами для себя, приятно же:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/026473bd957f984ca93144c6ffeed264/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p34.png)

  

И кстати, стоит поменять цвет фона в `setView()` на _white_. Тогда в симуляторе это будет смотреться нормально:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/94bab711e25770af2b998354753e82d2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p35.png)

  

## **Как работать с UIControl в коде**

Стоит снова напомнить, что мы имеем дело с таким же _view_-элементом. Значит, у нас всё плюс-минус одинаково, за исключением каких-нибудь особых методов. Но в целом вопрос хороший, потому что мы сделали составной элемент из нескольких таких элементов, а не просто обычную кнопку.

Отправляемся на _ViewController.swift,_ держим _Xcode_ в режиме двух половинок экрана (_Alt_ + левая кнопка мыши по любому файлу, который нужно открыть во втором окне). Делаем аутлет нашего кастомного контрола в класс _ViewController_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c6a6836aaf02367966046b317b2cb736/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p36.png)

  

Мы видим, что `customSegment` наследуется от `CustomSegment`, то есть от своего класса.

Дополнительно добавляем _UIImageView_ на _ViewController_, растягиваем его и в параметре _Image_ ставим какую-нибудь неяркую картинку. _Content Mode — Aspect Fill._ Мы добавили обои с горой _El Capitan:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f4c17cff27ad0bfee418b939f08c2c01/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p37.png)

  

Не забываем, что _UIImageView_ тоже надо связать с кодом.

Создадим ещё два лейбла — один будет просто транслировать надпись, а другой будет выдавать информацию в зависимости от переключения.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/99b25d0fec3cb15ee23df944580d875b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p38.png)

  

Свяжем их с кодом, это никогда не бывает лишним:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/33108b870e6b8219a4e7751d1780bbe3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p39.png)

  

**Attention:** так как в этом задании _Constraints_ не имеют столь высокого приоритета, нам важно, чтобы вы смогли сосредоточиться на обращении к кастомному контролу из кода. Поэтому мы расшариваем заготовку с проектом, где установлены максимально удобные _constraints_. С ограничителями не придётся ломать голову, потому что у нас не стоит задача вызвать у вас отторжение к обучению.

[Скачать проект CustomView](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f53de1fa7c9662032c60eb4501453325/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/CustomControllerWithConstraints.zip)

Если мы запустим проект в симуляторе, то увидим вот такую картину:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4f0051cd7903c4b9ab1c6dedc2f8c3a6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p40.png)

  

Давайте сделаем границу оранжевой:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c238afdff571d751ae11fee7c66c9e84/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p41.png)

  

Стоит немного поработать над кодом. Создадим _objc_-метод `segmentValueChange()` для связи между нижним лейблом и нашим контролом и сделаем в нём условия для каждого из трёх айтемов. Наша задача — выдавать конкретные значения при выборе одной из клавиш контрола. Пусть у нас элементу _DAILY_ соответствует $1,290, _WEEKLY_ — $34,736, _MONTHLY_ — $104,211. 

Кстати, числа абсолютно произвольные. Использовать свои варианты не возбраняется:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/724e3c301fd50a6425bd9170e749af24/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p42.png)

  

При помощи `viewDidLoad()` и нехитрых выражений настроим внешний вид нашего `customSegment`:

- Сделаем три опции при помощи массива.
- Изменим шрифт на _Avenir-Black_, 12.
- Выставим индекс кнопки, который будет срабатывать при запуске.
- Добавим отступов.
- Прикрутим метод addTarget для контроля событий.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/63f4d7e7c893fb92aaf5bee6e706d468/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p43.png)

  

Лейблы тоже не должны оставаться в стороне. Ведь мы их не по приколу создали. В том же viewDidLoad() изменим их шрифт и присвоим строковые значения по умолчанию. Ведь мы помним, что теперь при запуске мы будем видеть _WEEKLY_, а значит на запуске по умолчанию должно быть соответствующее число.:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/34af19d85c60b01c7649c1cdeba105b2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p44.png)

  

Теперь осталось только сделать пару настроек в _UIImageView_. Не забываем, что картинку пока лучше хранить в папке _Assets.xcassets_, а доступ к ней можно получить по имени:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5690fead925ec24403eeb96cc42e2e43/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p45.png)

  

Собственно, вот полная версия нашего _ViewController’а_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/26f6e3478409d2b89a1d9b0c15a5d936/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p46.png)

  

Запустим в симуляторе:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/22af15f58929d1eeaf94d61cfad4406e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u3_p47.png)

  

Да, всё запустилось согласно настройкам, а сам элемент кликабелен и работает хорошо — исправно выдаёт значения согласно нажатой кнопке.