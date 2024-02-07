#UIView #custom_element 

## **Использование кастомных _view_**

Собственно, использовать кастомный вью-элемент можно как через сториборд, так и через код. В сториборде можно копировать, размещать, добавлять ограничители — как и со всеми обычными вьюшками. В коде делается всё то же самое, только вне визуального формата (спасибо, кэп).


То есть в коде можно создавать и вызывать кастомные элементы, применять к ним ограничители — в общем всё как с обычными _view_-элементами. Давайте как раз попробуем это сделать. 

В первую очередь мы удалим наш красивый кастомный вью с _ViewController’а:_ выберем его и нажмём _backspace_ на клавиатуре. Ничего плохого не случилось и не случится — этот элемент опознаётся системой, у нас есть его код.

Теперь идём в _ViewController.swift_. В самом начале файла создадим переменную, назовём её _customViewElement_ и пропишем ей основные параметры через _CGRect_ — координаты и размер:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/134e4c57dac636deadd65aeffeff95c8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p68.png)

  

Наша переменная написана по всем канонам:

- Название.
- Тип данных — _MyCustomView._
- Обращение к _MyCustomView_ для заполнения _CGRect._

Добавим её на _ViewController_ через код. Для этого в методе `viewDidLoad()` добавим знакомое нам `addSubview`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/241c8900d76aa5de249ed919129e6e34/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p69.png)

  

Напоминание: так как у _ViewController’а_ есть свой основной _view_, то добавление происходит на него.

Мы не увидим изменений на сториборде, потому что мы удалили наш элемент оттуда. Если же мы запустим симулятор, то увидим кастомизированный элемент:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9af8fca600bdc5c93589ae13a80f45b5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p70.png)


  

Всё логично: заданные размеры отобразились, координаты тоже.

Посмотрим теперь, как получить доступ к отдельным элементам нашей кастомной вьюшки. Например, изменим текст внутри надписи. Для этого в методе `viewDidLoad` пропишем выражение, в котором мы обращаемся к `labelText` внутри нашего `customViewElement`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a0d3e0fb70ba205648f3666d056ed42e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p71.png)

  

Подсказка

Такой результат мы увидим на симуляторе:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/057d6b4eb3cc1844ecb3bf29b4fbd1f0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p72.png)

  

Чтобы почувствовать разницу, мы изменим цвет составного элемента вьюшки — `workingView`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6ed297ae81528432117cbf9a9f4c44f5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p73.png)

  

Мы обратились к нему как к обычному параметру, потому что не делали отдельную логику для него, как в случае с лейблом и его текстом.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0830055dc4aeb5cc6838e1bb64898afc/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p74.png)

 

**Как мы понимаем, у нас есть два варианта создания нового _view_-элемента на базе кастомного класса:**

1. Скопировать в сториборде.
2. Создать через код.

## **Работа с формой вьюшки**

Нюанс: Мы можем изменять форму наших _view_-элементов. Например, нам захотелось сделать кастомный вью в виде кружочка и ничего больше. Давайте ради этого изменим размеры _view_-элемента до _240x240._

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5e21f4c90ef39ad2d2d600c76fd38eaa/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p75.png)

  

А теперь удалим или деинсталлируем (как вам удобнее) элемент _Label_ из вьюшки в _MyCustomView.xib_. При удалении придётся очистить код от упоминаний о лейбле и сделать то же в инспекторе связей, а при снятии галочки в параметре _Installed_ в самом низу _Attribute Inspector_ не придётся чистить код:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/235b5f8e10552fe3f8eb58f467859adc/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p76.png)

  

_Label_ виден в иерархии и подсвечен слабо, потому что не удалён, а **деинсталлирован**.

На главном сториборде нас тоже будет ждать жёлтый квадрат. Переходим в _MyCustomView.swift,_ находим метод `setCustomView()` и добавляем в него код для изменения параметра закругленности углов:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ca9609d6f9fa1bf14973729ca1614610/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p77.png)

  

Здесь нам пришлось сначала обратиться к `layer`, затем мы нашли параметр `cornerRadius` и установили его фрейму значение ширины, которое мы делим на два. Так система максимально закруглит наш кастомный вью настолько, что он станет полноценным кружочком.

Симуляторе мы увидим наш кружок вместо квадрата:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/29aa4a7cd1439750aa1411cbf07c4be7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p78.png)

  

## **А можно без _XIB_? Спойлер: да**

То, что мы изучили в предыдущих разделах этого юнита, — теория + основные моменты работы с инструментами при создании кастомных вью-элементов. Как мы знаем, на одной только теории далеко не уедешь, поэтому мы будем практиковаться. 

Помните стандартное приложение «Калькулятор» на _iPhone_? Его кнопки, кстати, круглые. В этой части модуля сделаем что-нибудь нестандартное, причём 80% всей нашей «магии» придётся на код. Мы посмотрим, что ещё можно делать с кастомными элементами и как можно оптимизировать работу с ними.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ad4e2e81e099f9d6b44f2aa638d809e2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p79.jpeg)

  

Теперь, когда мы усвоили основные принципы работы с кастомными _view_-элементами, **мы создадим новый проект**. После создания проекта сразу идём на сториборд, где видим стандартный пустой _ViewController_, как обычно.

Перетащим кнопку на сториборд, сделаем её серой, зададим одинаковые размеры _100x100,_ добавим число 1 в надпись и слегка увеличим шрифт:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4e5c4252de918e16979e620729c1dc86/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p80.png)

  

Создадим файл из секции _Source_ типа _Cocoa Touch Class_. Вы знаете, как это сделать, мы в вас верим! В параметрах мы уже выбираем _UIButton_, вот как на скриншоте:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/16e126a953bf08331c8e74c73c7b41a9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p81.png)

  

Ничего кроме пустого класса после создания файла мы не увидим. Правда нам не нужно много кода в этой ситуации. Сразу сделаем наш класс @IBDesignable.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bb59161320e79936d11b32a404f9e3aa/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p82.png)

  

Также заведём булеву переменную. Но зачем? Мы проектируем себе удобство: закругленность можно будет включать и отключать. Сделаем вот такой _closure_ с наблюдателем `didSet`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5f139e4408dc34dc7eae59c208b70147/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p83.png)

  

**Хинт:** если вдруг вы подзабыли наблюдатели свойств, то почитать об этом можно по двум следующим ссылкам:

- _[swiftbook.ru](https://swiftbook.ru/content/languageguide/properties/)_ 
- _[proswift.ru](https://proswift.ru/nablyudateli-svojstv-v-swift-willset-i-didset/)_ 

Далее вызовем метод `prepareForInterfaceBuilder()`. Исходя из его названия, можно понять, что этот метод обновит нашу кнопку в _Interface Builder:_

_![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7dfebed0900f0595f0ed9e25dcd23b61/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p84.png)_

  

В нём как раз пропишем условие, при котором наша кнопка будет становиться круглой. А при каком условии она будет круглой? Правильно — если `roundButton` примет значение `true`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/882b2527a4767e09cd3c84c3b3496d9a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p85.png)

  

Как можем заметить, мы убрались в несколько строчек. Теперь идём на сториборд, возвращаемся к нашей кнопке: Выбираем нашу кнопку → Находим _Identity Inspector_ и помещаем _CircleButton_ как класс вместо пустого значения в графе _Class_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0daf0d1694c0628ad04f7b4b9413ba68/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p86.png)

  

Дальше система распознает, что мы только что сделали кастомный элемент. Ей не нужен _xib_-файл для этого. Перейдём в _Attributes Inspector_ нашей кнопки и увидим приятные обновления. Не зря же мы сделали булеву переменную:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a4d6e34188c233aaeaef77e2c89f34c2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p87.png)

  

Сейчас по дефолту она отключена. Посмотрите на свою кнопку и снова на _Round Button_ в _Attributes Inspector_. Сменим _off_ на _on_. Теперь снова посмотрите на кнопку. _Да, я на коне!_ То есть она круглая:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9c4e00128c42f6058f786430190ffc4f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p88.png)

  

Самое удобное, что мы можем «наплодить» таких кнопок через _Ctrl+C, Ctrl+V_ и какие-то сделать круглыми, а какие-то квадратными. При этом все они будут видны на сториборде сразу, а не только лишь при запуске симулятора:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a371f00c4d61a8d549487b13714d7b33/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p89.png)

  

В скринкасте мы расскажем про лайфхак, который решает проблему прогрузки сториборда при запуске _Xcode_ — когда заходишь в сториборд, а кастомные вью наотрез отказываются отображаться. Спойлер: это нормально.