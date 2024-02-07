#swift #animation #createAnimation #анимации

[Перейти к основному содержимому](https://lms.skillfactory.ru/xblock/block-v1:SkillFactory+iOS-2.0+2021+type@vertical+block@cfe2d479a18847c2bfdd27ee7b20e2e8?show_title=0&show_bookmark_button=0&recheck_access=1&view=student_view&format=Homework#main)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/71b83d68b00a5104adea1947587859cc/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m25_intro2.svg)

## **В этом юните мы изучим:**

- свойства, которые можно анимировать у _UIView_,
- анимации с задержкой,
- анимацию c _keyFrame_,
- анимацию _constraints_,
- _UIViewAnimationOptions._

Анимировать _iOS_ приложения на самом деле очень просто. Нужно написать буквально несколько строчек, чтобы анимировать какой-либо объект. Начнем с того, как создать анимацию _UIView_.

## **Рассмотрим методы и свойства класса _UIView_**

Нажмите правой кнопкой мыши по `UIView` в коде и выберите _Jump to Definition:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7f47a0b03066eea8163acaa8a7b4814f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p1.png)

Вы перейдете в `open class UIView`, который имеет множество свойств и методов. Вы можете с ними ознакомиться. В одном из расширений (`extension`) `UIView` вы можете обнаружить функции для её анимации:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/019331d59dc9a1cd68d21c0b183135c6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p2.png)

Это методы класса `UIView`, которые будут работать со всеми `UIView`, вне зависимости от экземпляров.

## **Анимации с задержкой, UIViewAnimationOptions (options)**

Основной метод, который мы можем использовать для анимации `UIView`, — это метод `animate()`. 

open class func animate(withDuration duration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions = [], animations: @escaping () -> Void, completion: ((Bool) -> Void)? = nil)

Методов с названием animate несколько, отличаются они лишь своими параметрами, в которых вы можете задавать определенный интервал задержки, длительности, опции анимации. Для того, чтобы создать анимацию при помощи функции animate(), нужно обязательно определить её продолжительность. Продолжительность и другие свойства анимации задаются в параметрах функции. Внутри функции пишется код, который анимирует какой-либо объект.

**Рассмотрим параметры более детально:**

- duration: — определяет продолжительность анимации (в секундах). Укажите отрицательное значение или 0, чтобы код был выполнен без анимации.
- delay: — задержка перед началом анимации, измеряемая в секундах. Укажите 0, чтобы сразу начать выполнение анимации.
- options: — параметры, указывающие на то, как вы хотите выполнить анимацию.
- animations: — блок кода, где вы программно изменяете любые свойства view в иерархии представлений. То есть здесь вы пишете код, который будет анимировать объекты.
- completion: — блок кода, который будет выполнен после завершения анимации.

**Основные опции анимации (_options_):**

- .curveEaseIn — анимация начинается медленно и ускоряется по мере продвижения.
- .curveEaseOut — анимация начинается быстро и замедляется по окончании.
- .curveEaseInOut — анимация начинается медленно и ускоряется в средней фазе и замедляется по завершении (комбинация двух вышеперечисленных).

[Здесь](https://medium.com/@apmason/uiview-animation-options-9510832eedba) вы можете ознакомиться с подробным разбор всех свойств.

## Давайте создадим проект, в котором будем анимировать `UIView`.

Начнем с подготовительных действий. Нам нужно `UIView`, которое мы будем анимировать, и кнопка, нажав на которую мы запустим анимацию.

Добавьте на сториборд `UIView`. Измените цвет фона на желтый (или любой другой).

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9e384b9aab0242c9c478446775744158/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p3.png)

Добавьте на сториборд кнопку (_Button_). Закрепите её и _view_ на экране при помощи констрэйнтов: задайте ширину, высоту, расположите посередине как по вертикали, так и по горизонтали.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2c2a85c61dadb445ff69ae2181f69128/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p4.png)

В результате должен получиться следующий сториборд:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9c21ea22a723a46d02d1525fa9282cd9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p5.png)

Добавьте IBAction кнопки и IBOutlet `UIView` — назовите её, например, `someView`.

В результате код нашего _ViewController’a_ должен выглядеть так:

import UIKit
 ```swift
 class ViewController: UIViewController {
 
    @IBOutlet weak var someView: UIView!
    override func viewDidLoad() {
        super.viewDidLoad()
    }
 
    @IBAction func viewAnimate(_ sender: Any) {
    }
}
```


Итак, писать код мы будем в функции viewAnimate(). Срабатывает она при нажатии на кнопку на _ViewController’e._

Будем использовать функцию animate(), которую мы детально рассмотрели ранее:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ef4e9eecd1f1be51c6e62a4394e4261e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p6.png)

Для того, чтобы развернуть блок animations, нажмите левой кнопкой мыши два раза по серой области после animations. На скриншоте ниже она выделена синим:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/984307c5c59a21b01be57cc5e3dfd0d2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p7.png)

Блок animations раскроется, и внутри него можно будет писать код:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2c99d90e67301d41b022e454111e1875/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p8.png)

Для начала давайте зададим значение параметрам функции animate():

- withDuration: — продолжительность анимации — три секунды.
- delay: — задержка перед началом анимации — пять секунд.
- options: — функционал анимации — .curveLinear.
- animations: — блок анимации — изменяем непрозрачность на ноль (делаем плавное исчезновение someView).
- completion: — блок завершения — nil, так как при завершении анимации нам ничего не нужно делать.

     @IBAction func viewAnimate(_ sender: Any) {
        UIView.animate(withDuration: 3,
                       delay: 5,
                       options: .curveLinear,
                       animations: {
                        self.someView.alpha = 0.0
        },
                       completion: nil)
    }

Таким образом, анимация будет осуществляться на протяжении трёх секунд, перед началом анимации будет задержка в пять секунд, а непосредственно сама анимация — это плавное исчезновение someView с экрана (так как мы изменяем ей значение свойства alpha,которое отвечает за прозрачность).

Свойство alpha отвечает за прозрачность someView. Максимальное значение — 1.0, минимальное значение — 0.0. 

Мы хотим плавно убрать someView с экрана. Для этого выставляем продолжительность анимации в три секунды, а в блоке анимации пишем код, где ставим значение alpha у someView равным 0.0. На протяжении трёх секунд someView будет плавно пропадать с экрана.

Теперь мы знаем, что один из способов анимации `UIView` — это метод animate(), которому мы задаем определенные параметры и внутри которого мы пишем код анимации.

Если такие параметры, как задержка, опции, _completion_ вам не нужны, то вы смело можете использовать следующий метод animate():

UIView.animate(withDuration: 0.5) {
      self.someView.alpha = 0.0
}

Здесь вам нужно выставить лишь продолжительность анимации, а внутри написать код анимации. Это еще раз подтверждает, что анимировать _iOS_ приложение на самом деле очень просто!


Идём дальше.

## **Анимация с keyframe**

Если вам необходимо комбинировать анимации с течением времени, используйте _keyframe_-анимацию. Вы можете добавлять неограниченное количество ключевых кадров, которые имеют время начала и время продолжительности. Вы также предоставляете каждому ключевому кадру анимацию. При запуске _iOS_ объединяет их все вместе, плавно переходя из одной анимации в другую.

**_Keyframe_** — ключевой кадр, следовательно **_keyframe animations_** — анимация по ключевым кадрам.

Можно сказать, что анимация по ключевым кадрам — это последовательности поданимаций, которые объединяются в большую сложную анимацию.

Перейдем к практике. Вы можете продолжить писать код в действующем проекте, где мы уже анимировали someView, а можете создать новый. Не забудьте удалить код старых анимаций, если продолжите писать код в прошлом проекте. Он нам больше не нужен.

Уменьшим ширину и высоту someView до 150, чтобы она при перемещении по оси _x_, y влезала в область видимости экрана.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4fe47f1f7571c68334e004fe5fee2660/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p9.png)

Код мы по-прежнему пишем внутри функции viewAnimate(), которая срабатывает при нажатии на кнопку. 

Начните вводить `UIView.animate` внутри функции viewAnimate() и выберите animateKeyframes():

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7bbcd760c0359ab74f813d2e6ed2449a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p10.png)

animateKeyframes() создает анимацию по ключевым кадрам. Далее, внутри блока animations, мы должны добавить непосредственно сами ключевые кадры.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cee2c305667ebfe4d399d7bab1b33cc4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p11.png)

Со всеми параметрами мы ознакомились ранее, когда изучали метод animate(). Здесь никаких изменений нет.

Вспомним _назначение параметров функции:_

- duration: — определяет продолжительность анимации (в секундах). Укажите отрицательное значение или 0, чтобы код был выполнен без анимации.
- delay: — задержка перед началом анимации, измеряемая в секундах. Укажите 0, чтобы сразу начать выполнение анимации.
- options: — параметры, указывающие на то, как вы хотите выполнить анимацию.
- animations: — блок кода, где вы программно изменяете любые свойства view в иерархии представлений. То есть здесь вы пишете код, который будет анимировать объекты.
- completion: — блок кода, который будет выполнен после завершения анимации.

Теперь внутри анимации необходимо добавить **ключевые кадры.**

Добавлять мы их будем внутри animations-замыкания. Для того, чтобы добавить ключевой кадр, используем метод addKeyframe():

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7b1f05768a8d442078f2cb55a3862907/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p12.png)

Как мы видим, появились новые параметры, которые ранее мы не затрагивали:

- withRelativeStartTime — время запуска указанных анимаций. Это значение должно находиться в диапазоне от 0 до 1, где 0 представляет собой начало общей анимации, а 1 — конец общей анимации. Например, для анимации длительностью в две секунды указание времени начала 0,5 приведёт к тому, что анимация начнёт выполняться через одну секунду после начала общей анимации. То есть 0,5 —  это середина общей анимации.
- relativeDuration — продолжительность времени, в течение которого анимация должна быть выполнена до заданного значения. Это значение должно находиться в диапазоне от 0 до 1 и указывать на количество времени относительно общей длины анимации.  
    Так, если вы зададите значение 0, то все свойства, заданные в блоке анимации, будут немедленно обновлены в указанное время запуска. Если вы зададите ненулевое значение, свойства будут анимироваться в течение этого периода времени.  
      
    Например, для анимации длительностью в две секунды указание relativeDuration равным 0,5 приводит к длительности этой анимации в одну секунду.

Теперь, когда мы познакомились со всеми составляющими _keyframe-_анимации, давайте её создадим, добавим несколько ключевых кадров, и получим полноценную анимацию.

Первое, что мы должны сделать, — это создать _keyframe_-анимацию:

UIView.animateKeyframes(withDuration: 5, delay: 0, options: .calculationModeCubic, animations: {
}

Время анимации сделаем равным пяти секундам, время задержки — 0, опцию анимации — calculationModeCubic.

Перед кодом анимации добавим константу, в которую поместим первоначальное (то есть нынешнее, стартовое) расположение по центру. Это нужно для того, чтобы в конце анимации мы вернулись туда, откуда начинали.

let start = self.someView.center

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1f77c24d03ccbfb2c992113eaf58e774/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p13.png)

Теперь нужно добавить несколько ключевых кадров внутри блока animations.

**1**

  
Первое движение someView будет вниз.

Время начала относительно общей анимации будет 0, а продолжительность анимации относительно общей будет 0,125. То есть время выполнения данного ключевого кадра равняется ⅛ от общей анимации. Напоминаем, что минимальное значение 0, максимальное — 1.

Нам нужно, чтобы someView двигалось по _х_ ровно посередине экрана, а по _y_ — в самый низ экрана. Для этого используем следующие свойства _bounds_:

**_Bounds_** — местоположение и размер представления (view) с использованием его собственной системы координат.

- maxY — это максимальная координата по оси _У_. Например, на _iPhone_ 8 — это 667.0, на _iPhone 12 Pro_ — 884.0.  
    Всё зависит от родительской _view_, которая в свою очередь по размерам, конечно, зависит в том числе от размеров экрана устройства.
- midX — это середина (_middle_) по оси _Х,_ то есть середина экрана.

При помощи maxY и midX мы можем определить середину и низ _view_, а значит и экрана.
```swift
UIView.addKeyframe(withRelativeStartTime: 0, relativeDuration: 0.25) {
     self.someView.center = CGPoint(x: self.view.bounds.midX,
     y: self.view.bounds.maxY)
}
```


Для того, чтобы задать _x_ и _y_, используем структуру CGPoint.

_Преимущество анимации по ключевым кадрам_ заключается в том, что каждый отдельный ключевой кадр _независим_, поэтому вы всегда можете запустить его отдельно и посмотреть, нравится ли вам анимация, прежде чем добавлять другую.

**2**

  
Следующее движение someView вправо.

Здесь всё просто. Время старта — 0.25. То есть сразу после предыдущего ключевого кадра стартует этот. Продолжительность времени, в течение которого анимация должна быть выполнена до заданного значения, — 0.25. 

someView мы перемещаем на 50 точек вправо.

UIView.addKeyframe(withRelativeStartTime: 0.25, relativeDuration: 0.25) {
       self.someView.center.x += 50
}

**3**

  
И заключительный ключевой кадр возвращает нас в то место, откуда мы начинали.

Помните, мы создавали константу start, которой присвоили начальную позицию someView? Сейчас мы присваиваем текущему положению someView константу start, тем самым говорим: верни someView туда, откуда мы начинали.

Время начало анимации относительно общей здесь — 0,5. Продолжительность по-прежнему — 0.25

UIView.addKeyframe(withRelativeStartTime: 0.50, relativeDuration: 0.25) {
        self.someView.center = start
}

Весь код:

```swift
    @IBAction func viewAnimate(_ sender: Any) {
        let start = self.someView.center
 
        UIView.animateKeyframes(withDuration: 5, delay: 0, options: .calculationModeCubic, animations: {
            UIView.addKeyframe(withRelativeStartTime: 0, relativeDuration: 0.25) {
                self.someView.center = CGPoint(x: self.view.bounds.midX,
      y: self.view.bounds.maxY)
            }
 
            UIView.addKeyframe(withRelativeStartTime: 0.25, relativeDuration: 0.25) {
                self.someView.center.x += 50
            }
 
            UIView.addKeyframe(withRelativeStartTime: 0.50, relativeDuration: 0.25) {
                self.someView.center = start
            }
        })
    }```



## **Анимация constraints**

С тем, что такое _constraints_, для чего они нужны и как их добавлять, вы знакомы. Но их можно еще и анимировать!

Когда нам это может понадобиться? На самом деле, кейсов, когда может понадобиться анимация констрэйнтов достаточно много. Предположим, у нас снизу выезжает клавиатура, которая закрывает какие-то важные элементы: _textField_ или кнопку. Вместе с выездом клавиатуры будет изменяться расположение _textField_.

Давайте напишем появление _label’a_ с левой стороны экрана при запуске приложения.

## Создадим новый проект.

На _Storyboard_ добавим _label_, закрепим его сверху и посередине.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9b6c6e0dbf7e54d544d4a21f44e13ee1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p14.png)

Теперь необходимо выделить _constraint_, который закрепляет _label_ посередине. 

Это можно сделать разными способами, один из которых — нажать на _label_. Затем зажать кнопку _option_ и нажать на _constraint:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c995bf3b79099e6309a90251ecf4c886/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u2_p15.png)

Назовите этот аутлет labelCenterConstraint.
```swift
@IBOutlet weak var labelCenterConstraint: NSLayoutConstraint!
```


Теперь пришло время освежить знания по жизненному циклу `UIViewController`. 

Нужно задать первоначальное значение для labelCenterConstraint, которое будет отличаться от того, которое мы задали на сториборде. Нам нужно, чтобы изначально labelCenterConstraint был за пределами экрана. Лучше всего это будет сделать в методе жизненного цикла viewWillAppear:

```swift
override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
}
```


У объекта класса NSLayoutConstraint есть такое свойство, как constant. Используя его, мы можем присвоить констрэйнту значение. Осталось решить, какое ему нужно присвоить значение, чтобы он находился за пределами экрана на совершенно любом устройстве, будь то _iPhone 12_ или _iPhone SE._

Для этого отлично подойдет view.bounds.width, который даст нам ширину _view_, а значит и ширину экрана. На _iPhone 8_ view.bounds.width = 375. И в таком случае изначально наш _label_ будет находиться далеко за пределами экрана.

Вычтем ширину экрана из текущего значения констрэйнта:
```swift
override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        labelCenterConstraint.constant -= view.bounds.width
}
```


Запускаем проект. Проверяем, что _label_ отсутствует на экране. Далее нам нужно написать анимацию появления _label’a_ слева направо.

Так как мы хотим, чтобы анимация воспроизводилась после запуска приложения, без нажатия кнопок, необходимо воспользоваться еще одним методом жизненного цикла, внутри которого мы и будем писать код анимации:
```swift
override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
}
```


Для анимации мы будем использовать метод `UIView` `UIView.animate()`:
```swift
    UIView.animate(withDuration: 0.5,
        delay: 0.0,
        options: [],
        animations: {
    })
```


Время анимации составляет 0.5 секунд.

Теперь напишем саму анимацию. Тут всё **очень** просто. Нужно всего лишь изменить значение констрэйнта внутри блока animations:

self.labelCenterConstraint.constant += self.view.bounds.width

Если на начальном этапе мы вычитали значение view.bounds.width, то сейчас прибавляем, чтобы _label_ у нас плавно «поехал‎» вправо, на середину. То есть мы прибавляем сейчас то, что в методе viewWillAppear отнимали, возвращаясь тем самым на стартовую позицию (посередине). Запускаем анимацию.

Кажется, что ничего не работает. В чём же дело? А дело всё в том, что мы не использовали метод layoutIfNeeded().

Метод layoutIfNeeded() сообщает системе, что нужно немедленно перерисовать _view_ и его _subviews_. layoutIfNeeded() вызывается для родительского представления, то есть для self.view.:
```swift
self.view.layoutIfNeeded()
```


Вот, что в результате должно получиться:
```swift
override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        view.layoutIfNeeded()
        UIView.animate(withDuration: 0.5,
                       delay: 0.0,
                       options: [],
                       animations: {
                        self.labelCenterConstraint.constant += self.view.bounds.width
                        self.view.layoutIfNeeded()
        })
    }
```

Запускаем приложение и наблюдаем за красивой анимацией.

Весь код:

 class ViewController: UIViewController {
 ```swift
 @IBOutlet weak var labelCenterConstraint: NSLayoutConstraint!
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
 
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        labelCenterConstraint.constant -= view.bounds.width
    }
 
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        UIView.animate(withDuration: 0.5,
                       delay: 0.0,
                       options: [],
                       animations: {
                        self.labelCenterConstraint.constant += self.view.bounds.width
                        self.view.layoutIfNeeded()
 
        })
    }
}

```
    
С тем, как анимировать `UIView`, мы разобрались, идём дальше!

[[transform трансформации UIView]] 