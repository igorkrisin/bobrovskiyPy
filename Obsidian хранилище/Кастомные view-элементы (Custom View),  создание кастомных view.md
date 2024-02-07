#UIView #custom_element #custom_view

**Кастомные _view_-элементы** — элементы интерфейса, создаваемые разработчиком, которые помогают ему создавать сложные интерфейсы.

Философия кастомного элемента состоит в том, чтобы разработчик мог не ограничивать себя одним лишь _UIKit_. Стоит запомнить, что _UIKit_ даёт нам базу, с которой мы сможем работать так, как нам хочется. Это и называется «выходить за рамки».

Бывают такие абсурдные ситуации, когда новички смотрят на какие-нибудь библиотеки с космическими интерфейсами и думают, что это невозможно, что это какая-то заоблачная графика, что не обойтись без _3D_ и ещё куча таких тем появляются из потока сознания. Потом, заглянув под капот, новичок берёт себя в руки и понимает, что ему нужно лишь _время_ на продумывание и реализацию таких кастомных интерфейсов.

В реальности коммерческой разработки есть **три ситуации**: 

- нужен переиспользуемый элемент для одного и более экранов;
- нужен сложный элемент, аналогов которому нет в _UIKit_;
- нужен сложный переиспользуемый элемент, чтобы эффективно решать поставленную задачу — комбо предыдущих двух вариантов;

Как мы помним, _UIKit_ предоставляет **основу**, а остальное в работе с кастомными элементами зависит от нас.

Переиспользуемые элементы создаются через _xib_-файлы. Что это такое?

_Xib_-файл — это файл _XML Interface Builder_. Такое определение не закрывает полностью вопрос понимания. Простыми словами, это **усечённая версия** **сториборда** для создания отдельных элементов, то есть кастомных вью.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/444bea1797e9fe3e102a41eb9b8186cf/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_001.png)

Интерфейс для работы с кастомными _view_

Кстати, если мы меняем _xib_-файл на его родном экране, то есть на мини-сториборде для создания кастомных _view_, то этот элемент будет обновляться везде, где он используется. Например, мы делаем в _xib_-файле кнопку, она по задумке круглая и зелёная. Кнопка используется на пяти экранах. Следовательно, на всех пяти экранах эта кнопка будет круглой и зелёной. На следующей итерации было принято решение изменить форму кнопки на квадратную, а цвет сделать серым. Если мы меняем эти параметры в _xib_-файле, то элемент обновится на всех экранах → на пяти экранах кнопка станет квадратной и серой.

Предположим, нам нужен более сложный _UI_-элемент, который переиспользуется несколько раз на одном экране или на нескольких экранах. При этом мы не хотим несколько раз писать один и тот же код или устанавливать одни и те же элементы несколько раз.

Решением будет создание собственного _UI_-элемента для переиспользования его в нескольких местах. Почему это важно? Ответ «Во-первых, хоть это и сложно, но это удобно» здесь не работает.

Вот представим, что у нас есть функция, которая принимает какое-то конкретное значение на вход, а на выходе мы получаем увеличенное значение, потому что в нашей функции происходит определённая обработка значения. И теперь, когда мы вызываем функцию, чтобы произвести какие-то вычисления, мы получаем на выходе изменённое значение:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ed9edf4dfd25dc175edc6a501f342cba/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_002.png)

Есть конкретный случай: дизайнер захотел немного изменить внешний вид. Чтобы для нас, разработчиков, даже небольшое изменение дизайна не оказалось большой болью, мы создадим один элемент и будем использовать его многократно. И когда дизайнер попросит нас внести изменения, мы выберем настройки элемента либо в сториборде, либо в коде и изменим нужные параметры. Чуда не случится, а время сэкономим.

## **Ещё немного теории о свойствах кастомных View**

Перед тем, как мы перейдём к практике, хотелось бы сказать пару слов про два атрибута кастомных _view_-элементов. Речь идёт о **@IBInspectable** и **@IBDesignable**.

Ранее мы добавляли в код @IBOutlet и @IBAction. Добавление @IBInspectable и @IBDesignable имеет свои нюансы. Говоря вкратце, эти атрибуты способны перенести в _Interface Builder_ свойства кастомного _view_-элемента, которые доступны в коде. Согласитесь, что это прикольно — создать свойство в коде, а редактировать его визуально, ползунками в сториборде.

Что нам стоит знать в рамках этого небольшого теоретического блока про эти новые атрибуты:

- **@IBDesignable** относится к классу _view_-элемента в целом. Означает, что _Interface Builder_ сможет обновлять прямо на сториборде элемент с этим свойством. То есть, чтобы увидеть изменения, нам не нужно сто раз запускать симулятор.
- **@IBInspectable** применяется к свойству элемента в классе (который @IBDesignable), чтобы мы могли менять это свойство в сториборде — к примеру, в стандартных условиях мы не можем закруглить углы нашего _UIView_ без кода. @IBInspectable отправляет свойство в сториборд и мы можем настроить скругленность ползунками.

В дальнейшем мы детально рассмотрим работу этих атрибутов. Такое минимальное представление о них нам нужно, чтобы в дальнейшем мы работали с ними, имея минимальное представление.

**Пять важных принципов кастомных _view_:**

1. Создание кастомных _view_-элементов — смесь _xib_-файлов и кода. В _xib_-файле мы расставляем элементы визуально, как при добавлении на _ViewController_. В коде же мы прописываем логику работы элементов, вытаскиваем параметры для управления через _Inspector_, а также можем добавлять дополнительные _view_-элементы, _constraints_ и так далее. В итоге, что мы напишем в коде, то увидим при редактировании элемента на сториборде. Стоит помнить, что _xib_ мы не создадим через код.
2. Кастомные _view_-элементы управляются через код подобно _ViewController’у_. Помните, как в модуле «[Знакомство с UIKit](https://lms.skillfactory.ru/courses/course-v1:SkillFactory+iOS-4+14SEP2020/courseware/4248fe4a0e5545d49ddcbfe9fefc51e5/90de46f8502641e59a41e9410472d51f/1?activate_block_id=block-v1%3ASkillFactory%2BiOS-4%2B14SEP2020%2Btype%40vertical%2Bblock%404b1dbbc553124ea6b71cf0e07fc376e5)» мы создавали для каждого _ViewController’а_ собственные классы? Аналогичная история происходит и здесь: чтобы мы могли работать с нашими кастомными _view_-элементами, система должна их видеть. Видеть она их будет через такой же кастомный класс. То есть, например, в коде у нас класс со всей логикой элемента, а на канвасе — красивая кнопка как результат.
3. C кастомными вьюшками можно работать через код. Это такие же _view_-элементы, только сделанные под наши задачи и нужды. Значит, главный принцип не меняется: менять параметры можно где угодно.
4. Кастомные _view_-элементы наследуются от своих «родительских» элементов. Нормально это можно показать только на примере. Если мы делаем кастомный _UIView_, то его класс будет наследоваться от _UIView_:  
    `class MyCustomView: UIView { }`
5. Вне зависимости от своей сложности элемент будет доступен сразу на канвасе. При этом все изменения состояния элемента будут видны в реальном времени, как это происходит со стандартными _UIKit-_элементами в целом.

Эти принципы будут сопровождать нас на всём практическом пути.

## Давайте уже создавать

В этом разделе мы начнём с малого — с создания кастомного _view_-элемента в общем виде, чтобы у нас было понимание, как это вообще происходит. Затем будем усложнять себе задачу, чтобы набивать руку.

### Этап 0. Подготовка

Запускаем _Xcode_, в окне приветствия выбираем _Create a new Xcode project:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/49a3e68a213f76b98cb7db6bb269ff6a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p2.png)

  

В окне _Choose a template for your new project_ выбираем _App_ и нажимаем _Next_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ed0bd0e286ef47a42d2520f9f842308e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p3.png)

  

Далее появляется привычное окно, которое запрашивает имя проекта. Назовём его _MyCustomViewProject_ и нажмём _Next_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4a0cc799f4f9f611aa37f555c0343b24/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p4.png)

  

Теперь остаётся выбрать директорию, где проект будет храниться, и нажать _Create_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/751b08157d81535bd4c9bb9b95b9f066/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p5.png)

  

Профит. Нас интересует сториборд в этом проекте. Поэтому перейдём туда, чтобы увидеть привычный пустой _ViewController_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/079a65515282299ed049670f9c1a0930/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p6.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/48755395a65607b429ed8a6f130becaa/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p7.png)

  

Выберем наш пустой ViewController левой кнопкой мыши, затем нажмём «плюсик» в правом верхнем углу сториборда и увидим весь набор элементов, который нам предлагает _UIKit_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5eb370924b28336623390b887c894a59/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p8.png)

  

Найдём _UIView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d7d31d1339bf169a7bb761d256108d62/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p9.png)

  

И перетащим его на наш пустой _ViewController_. Как мы помним, вьюшки по умолчанию белого цвета, белое на белом теряется, и работать в таком режиме не совсем удобно. Поэтому в свойстве _Background_ меняем цвет. У нас это будет зелёный:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/566f85dcd648849ce8c1829686067571/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p10.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e6ee5a9f3439ff7e630be038dcf824e7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p11.png)

  

Также для удобства добавим _constraints_ — пока что по классике: собственные _width,_ _height_ и четыре ограничителя для расположения на _ViewController’е_:

- Собственные _Constraints у UIView_ — выбираем нашу вьюшку, зажимаем _Ctrl_ и нажимаем левой кнопкой мыши на вьюшку. Появится вот такой синий связующий элемент. Тянем его исключительно в районе вьюшки и отпускаем левую кнопку мыши:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3ed59ba3a7ffdd21d775cf44cd2cea77/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p12.png)

  

У нас появятся на выбор две _Constraints_ — _width_ и _height_. Поэтому выбираем обе — зажав клавишу _Command_, нажимаем левой кнопкой мыши по каждой:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4c4e401fd2855d101a2cda3afd72b03d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p13.png)

  

У нас появятся _Constraints_, которые будут подсвечиваться красным цветом. Мы помним, что это говорит об ошибке, и что _ViewController_ хочет больше ограничений. Окей:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5dcd2373cf86b10f03f324b75b495154/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p14.png)

  

Теперь идём вниз, находим _Add New Constraints_ ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ed1138d7d691af1964f0710ba261dd5c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p114.png)  добавляем стандартные ограничители для расположения на _ViewController’е_. Их может быть как 3, так и 4 — это исключительно на ваше усмотрение. В зависимости от экрана симулятора элемент может изменяться до определённых размеров — ведь мы не фиксировали размер. На скриншотах внизу установлены 4 ограничителя, но это не значит, что нужно ИМЕННО 4. Можно 3, главное — чтобы не было интерфейсных “сдвигов”:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bfaa56234d9f4f9402cd522c420742b4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p15.png)

  

Нажимаем _Add Constraints:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/baf2d95f1df3e8288d58888193b7b2d4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p16.png)

  

Что в итоге? Всё очень неплохо — _ViewController_ не ругается, систему всё устраивает:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1d1cbbf1d8bfde374590ea0d26f21682/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p17.png)

  

### Этап 1. Визуальная сборка

Теперь когда у нас основа положена, мы можем переходить к созданию того самого _xib_-файла, о котором мы говорили в теоретическом блоке. Вверху экрана _Xcode_ выбираем _File_ → _New_ → _File_… :

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d0e293a167ac4e06fa5707a672be05e4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p18.png)

  

И в окне _Choose a template for your new file_ спустимся до секции _User Interface_. В ней лежит нужный нам шаблон — _Empty_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ee956a7f3d2191826194b4372c2271b2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p19.png)

  

Выберем его, нажмём _Next_, назовём _MyCustomView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ad5c7098b453a2b7525ce8a4d73ee0a5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p20.png)

  

После того, как мы нажмём _Create_, в иерархии проекта появится ещё один файл _MyCustomView.xib:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f13b5cb2a81d22cac238fb113aeee975/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p21.png)

  

Кстати, после создания _MyCustomView.xib_ абсолютно пустой:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/06676f7fe9b28ae3333e588b91b15fbb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p22.png)

  

Пугаться этого не нужно. Этот пустой канвас ещё раз подтверждает, что _Xcode_ даёт свободу для нашего творчества.

Кстати, давайте сразу по ходу дела создадим _.swift_-файл, в котором в дальнейшем опишем логику для нашего кастомного _view_. Вверху экрана _Xcode_ выбираем _File → New → File…_ :

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d0e293a167ac4e06fa5707a672be05e4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p23.png)

  

И в окне _Choose a template for your new file_ остановимся на _Source_, выберем _Cocoa Touch Class_ и кликнем _Next_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f23b5df43480618eb88534e726d6508a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p24.png)

  

Назовём этот файл так же, как у нас называется _xib_-файл — в данном случае это _MyCustomView_. Ничего не меняем — _Subclass of_ оставляем _UIView_ и нажимаем _Next_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4a06d7ff541e692d73df664785915f82/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p25.png)

  

Здесь мы тоже ничего не меняем — _Xcode_ предложил сохранить наш _Cocoa Touch Class_ в основной директории приложения, а мы соглашаемся и нажимаем _Create_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/108275a1711715da0d454206f7c8da2b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p26.png)

  

Иерархия проекта снова обновилась:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6b04895c45aecc53823c9b7129b2a62a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p27.png)

  

А в файле уже создан класс:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/eec5ef0b9a43d4d265f2ee96f3fbdeec/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p28.png)

  

Вернёмся в наш пустой _MyCustomView.xib_ и перетащим на его канвас _UIView_. Вот что мы увидим:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/395f9b75f1f67ce0cd2ba42e4b2ee4be/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p29.png)

  

В _Attributes Inspector_ на параметр _Size_ выставляем _Freeform,_ чтобы отвязаться от строгих рамок:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a7133002ad94d9eef195396b7e42613c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p30.png)

  

А в _Size Inspector_ выставим размер _240x128_, чтобы сделать размер нашего кастомного вью таким же, какой он у зелёного вью-элемента на _ViewController’е_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fe92591a3ee71bd46191d7a9e7bd640c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p31.png)

  

Что мы имеем в результате:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/444bea1797e9fe3e102a41eb9b8186cf/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p32.png)

  

Теперь системе надо сообщить, к какому классу относится наш _xib_-файл. Так как мы в начале уже создали одноимённый класс, нам остаётся подвязать визуальную часть нашего элемента к коду. Для этого в сториборде нашего _xib_-файла выбираем _File’s Owner_, переходим в _Identity Inspector_ и в графе _Class_ выставляем наш класс — в данном случае это _MyCustomView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c20e9df1f5be46b0edf8286a70740f66/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p33.png)       →       ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e13f368109eb8717326759d0848e560a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p34.png)

  

**Лайфхак:** чтобы не листать весь дропдаун, просто начните вводить название класса в графе и система сама предложит вам класс с похожим названием. Так как название у класса уникальное, то в 99% случаев _Xcode IDE_ выставит в графу кастомный класс.

Теперь наш элемент имеет полное право называться кастомным:

- он сделан разработчиком на основе имеющихся в _UIKit_ средств,
- у него есть кастомный класс, который наследуется от _UIView,_
- он связан с кодом.

Посмотрим, как он работает с канвасом. Суть в том, что для этого нам и нужен зелёный _UIView_, который мы положили на _ViewController_ в самом начале этого юнита. Дело в том, что сейчас мы увидим, как наш _xib_-файл повлияет на тот зелёный вью-элемент. 

Возвращаемся на _Main.storyboard_ _→_ Выбираем левой кнопкой мыши наш зелёный _UIView_. В _Identity Inspector_ зелёного вью-элемента выставляем _MyCustomView_ в качестве класса:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/39e3fdb77cbbc8b05f794b4fd7cf8675/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p35.png)

  

Сейчас мы не увидим значительных изменений, потому что это только малая часть всей «магии» с кастомными элементами. Этим шагом мы сделали минимальное соединение двух вью-элементов — нашего зелёного и кастомного вью, который лежит в _xib_-файле.

Чтобы посмотреть на изменения в реальном времени, будет логично их внести. Давайте перейдём в _MyCustomView.xib_ _→_ Выберем наш кастомный вью и изменим его цвет через _Attributes Inspector,_ с белого на жёлтый:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c60f22dfdef45940d980aabd5cc6a0fe/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p36.png)

  

Также добавим на наш кастомный вью какой-нибудь элемент — тот же _UILabel_ для наглядности с белым фоном и фиолетовым шрифтом. При этом размер шрифта сделаем побольше, а выравнивание текста в _Label_ сделаем по центру:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f4e604a26cd9467e10b8fad1aa2abd5e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p37.png)          ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/94268502512502bc5f19eb02f5e18aa8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p38.png)

  

Подсказка

Добавим ещё две собственные _constraints_ — _width_ и _height_, а также четыре ограничительных: 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a1e0ea08fae95c06bffe2bd39ab238d9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p39.png)       _→_      ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/215638a60f20545ca7ed6824302e556d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p40.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7eaa4fa82665da6fdd06eb0700ee55ae/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p41.png)

  

**_Вы точно помните, как это делается, мы в вас верим!_**

В итоге у нас получится вот такой элемент:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/410bbce836595bd8481d988ddba0dcb7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p42.png)

  

Спойлер

### Этап 2. Код

Пришла пора прописать логику кастомного вью в коде. Идём в _MyCustomView.swift_ → Привязываем наш _UILabel_ через аутлет (_Ctrl_ + левая кн. мыши):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/186f41e063044ea2bc67148672d0bc6d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p43.png)

  

Называем его, как нам удобно:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/adb4f838832053ba2c0192f56e0aa213/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p44.png)

  

Наш аутлет готов:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b8561d784b4ae9a3ef2142e3b49b5a51/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p45.png)

  

Далее мы будем работать с файлом класса, то есть _MyCustomView.swift._ Если уж мы берёмся делать максимально кастомный элемент, то пройдёмся по свойствам элементов в составе нашего кастомного вью.

После аутлета добавим свойство для работы с текстом нашего лейбла:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1232e31b2de2c1c029ad62a37d2f7347/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p47.png)

  

Пояснение: мы сделали этот _closure_ с _get-_ и _set-_ параметрами для работы с текстом лейбла, который мы только привязали в код. `Get` будет **возвращать** **значение лейбла**. `Set` же будет **ставить новое значение** — поэтому мы создали `labelText`. И когда мы присваиваем значение в `labelText`, оно передаётся в качестве значения `labelForView.text`. Да, на словах оно может звучать не совсем понятно, но когда мы это увидим в практическом применении, то будет больше понимания, зачем нам такие заморочки.

Добавим ещё две переменные — `workingView` в качестве нашего кастомного вью и `xibName` как имя _xib_-файла:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e7e5e3b14234ea8f37bf8436fccd98c0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p48.png)

  

Пришло время инициализаторов. Добавляем инициализатор, который определит форму. У _frame_ тип данных _CGRect_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/736512d512823b19d4f8833452be5b67/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p49.png)

  

После добавления инициализатора _Xcode_ будет ругаться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a9450af9c8cd89ad183325a9798802e3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p50.png)

  

И правильно, ведь у нас нет _required init_. Нажмём на красный кружочек. Откроется полный текст, в котором система просит добавить недостающий элемент в код. Молча соглашаемся, нажав _Fix_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c70b90475336ae9a8470d7d7445068ca/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p51.png)

  

Теперь ошибок нет. Эта ошибка означает, что у нашего класса инициализатор может быть только при том условии, когда в классе будет прописан **обязательный** (_required init_) инициализатор. _Xcode_ обновил наш код, а ошибка исчезла:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/deec93244b344575eb7da12cf6bc19e7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p52.png)

  

Обновим наш обязательный инициализатор до следующего вида: поставим в него `super.init`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ec50afb070445f242cb04357e947f0cd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p53.png)

  

Пояснение: без инициализаторов мы не сможем работать с кастомным вью через код или сториборд. Поэтому сейчас мы подбираемся к важнейшей части нашего модуля. Ещё чуть-чуть и мы увидим обещанное удобство.

Теперь напишем функцию, которая будет получать _UIView_ из _xib_-файла и возвращать нам этот _UIView_. Это нужно для отображения кастомного вью на сториборде:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9ccb850081db702a9832d28e86656107/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p54.png)

  

Скобки «краснеют», когда у возвратной функции отсутствует `return`.

Что будет делать эта функция:

- Получать сам проект через `bundle` — поэтому и делаем константу с `bundle`, чтобы система определила `bundle` автоматически.
- Получать название _xib_-файла при помощи двух параметров `nibName` и `bundle`.
- Получать вью как один элемент из массива, который у нас получился в результате вызова метода `instantiate` с `xib` — при этом в нашем массиве всего один элемент, а значит именно его нужно перевести в _UIView_ через _type casting._
- Возвращать вью.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6c3452a032bf0fb25af945b68548987c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p55.png)

Нюанс: в этом юните фигурирует _xib_-файл, но как мы видим из этой функции, то тип у него _UINib_. Дело в том, что _xib_ и _nib_ — это одно и то же.

Осталось только настроить этот кастомный вью. Создадим метод, назовём его `setCustomView`. В нём:

- получаем вью — переменная `workingView` забирает его с помощью метода `getFromXib()`
- определяем границы вью через `frame`
- определяем размещение в пределах заданных границ — `autoresizingMask` нам в помощь
- добавляем вью как `subview`

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/390b380f1318c77d6a0ab10e7d13e845/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p56.png)

Теперь `setCustomView()` нужно вызвать через инициализаторы:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3100d98fab74762fdd989da58ea5a9ed/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p57.png)

  

Если мы запустим этот проект в симуляторе, то мы увидим результат нашей работы:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8a0d797089555b63a281297a8e3fcce4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p58.png)

  

Тем не менее, в сториборде до сих пор глухо, но это окей. Помните, мы создали свойство для работы с текстом элемента `label`?

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1232e31b2de2c1c029ad62a37d2f7347/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p59.png)

  

Мы сделали это свойство, чтобы рассмотреть **@IBInspectable**.

## **@IBInspectable**

В теоретическом блоке мы рассматривали его как добавочное свойство для работы с параметрами кастомных _view_-элементов. На тот момент у нас не было достаточной практики, чтобы это понять. Сейчас мы знаем больше.

@IBInspectable добавляется для того, чтобы какое-то свойство кастомного вью мы могли редактировать прямо в сториборде. Всё в том же файле класса `MyCustomViewSwift` мы добавим @IBInspectable к свойству `labelText`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/094c3b1a7c81290b16d90f5caadc7c73/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p60.png)

  

Идём в главный сториборд и выбираем наш зелёный прямоугольник:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a915853b292884a9968aa1a6d4ac28c8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p61.png)

  

В _Attribute Inspector_ появилась новая секция, связанная с _MyCustomView_ с графой _Label Text:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d009d8f2e2cf79e97ef8c83a19b3749d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p62.png)

  

Впишем туда что-нибудь. Вьюшка на главном сториборде не реагирует опять:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/35dfa05d9f63cf19057c417e7f7046c3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p63.png)

  

Опять всё решает запуск в симуляторе:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/def7e56a62d859d599ac895517aca995/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p64.png)

  

## **@IBDesignable**

Снова возвращаемся в наш теоретический блок этого юнита. @IBDesignable относится к классу _view_-элемента в целом. По идее, он обеспечивает связь между _xib_-файлом и главным сторибордом, чтобы при редактировании кастомного вью все изменения отображались на сториборде. Чтобы лучше понять, как это работает, давайте добавим свойство @IBDesignable к нашему кастомному классу:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/10ee8f137103e85b8744279c2460f419/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p65.png)

  

Вроде ничего такого не сделали, а параметр принёс серьёзные изменения. Возвращаемся на _Main.storyboard:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c71fa43c58afe188d0affff235b11cfb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m24_u2_p66.png)

  

## Как говорится, _it works_!

Теперь в нашем арсенале есть кастомный вью, который можно переиспользовать сколько угодно раз, его можно также несколько раз разместить на экране и тому подобное — элемент есть, а дальше решит фантазия.

Перейдем к [[Использование кастомных view]] 