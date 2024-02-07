#transition #переход #переходы


У `UIView` есть метод _**transition()**_, при помощи которого можно создавать анимации перехода. 

Изучая данный метод, мы напишем приложение с анимацией игральных карт. Создадим новый проект. И сразу переходим на сториборд.

**<mark style="background: #BBFABBA6;">1</mark>**

  
Первое, что нужно сделать, — это добавить _UIView_ на экран, задать ширину, высоту и закрепить посередине.

**<mark style="background: #BBFABBA6;">2</mark>**

  
Второе — добавить внутрь ранее созданной _UIView_ еще два _UIView_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/dca9c245cc0185b7aec594cac07d6b2a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p1.png)

  

Их в дальнейшем, перетягивая в класс как `IBOutlet`, мы назовем как `firstView` и `secondView`.

Эти две _view_ нужны нам для того, чтобы, при переворачивании `firstView`, нам после анимации показывалась secondView. `firstView` имеет желтый цвет, secondView — зеленый.

**1**

  
Третье — внутрь secondView добавьте _label_, закрепите его посередине secondView. Удалите текст. По умолчанию _label_ пустой.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5b5b3c17a70797f901ec15c71d0c904a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p2.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/25bf49d3396efb98428dc8e914f19c22/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p3.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3a6b3bbd6ee5ffc2cf9e5c4acc2b6b57/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p4.png)

  

**1**

  
Четвертое — добавьте кнопку «‎Посмотреть предсказание».

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a3411d0870e2318b0b6d1022277c77cd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p5.png)

  

  
Вот, что у нас должно получиться в результате:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/863815c9f0dac301adbe3b4fe5567007/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p6.png)

  

Добавьте `firstView`, secondView, _label_ в класс в качестве IBOutlet:
```swift
// MARK: IBOutlets
    @IBOutlet weak var firstView: UIView!
    @IBOutlet weak var secondView: UIView!
    @IBOutlet weak var secondViewLabel: UILabel!
```
    

Далее добавьте IBAction для кнопки «‎Посмотреть предсказание»:
```swift
// MARK: IBAction
    @IBAction func transitionCard(_ sender: Any) {
}
```


Суть приложения, которое мы сейчас напишем, состоит в том, чтобы показывать предсказания на карточке. Изначально у нас показывается пустая карточка. При нажатии на кнопку происходит анимация переворота карточки, на которой будет написано предсказание.

Поэтому нам нужны две переменные:
```swift
// MARK: Public properties
    var isFlipped = false
    var predictions = ["Уже через несколько месяцев ты будешь крепким джуном!",  "Завтра будет солнце!", "Удача на твоей стороне"]
```
    

- isFlipped — повернулась ли карта
- predictions — предсказания, для отображения которых на одной из view мы добавили label

Для того, чтобы карточки смотрелись более красивыми, округлим им углы. Для этого напишем соответствующий код в методе жизненного цикла viewWillAppear():
```swift
override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        firstView.layer.cornerRadius = 10
        secondView.layer.cornerRadius = 10
    }
```
    

В результате у вас должен был получиться следующий код:

import UIKit
 
class ViewController: UIViewController {
 ```swift
  // MARK: IBOutlets
    @IBOutlet weak var firstView: UIView!
    @IBOutlet weak var secondView: UIView!
    @IBOutlet weak var secondViewLabel: UILabel!
 
    // MARK: Public properties
    var isFlipped = false
    var predictions = ["Уже через несколько месяцев ты будешь крепким джуном!", "Завтра будет солнце!", "Удача на твоей стороне"]
 
    // MARK: Public methods
    override func viewDidLoad() {
        super.viewDidLoad()
    }
 
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        firstView.layer.cornerRadius = 10
        secondView.layer.cornerRadius = 10
    }
 
    // MARK: IBAction
    @IBAction func transitionCard(_ sender: Any) {
    }
}
```
   

Итак, для анимации `firstView` и secondView мы будем использовать метод transition:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9043a4670f89ac14f7b86e24bd39a606/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios__25_u4_p7.png)

  

Параметры данного метода:

- from: — от какой view начинается анимация перехода (начальное view перехода).
- to: — к какой view переходим (конечное view перехода).
- duration: — длительность анимации.
- options: — опции анимации.
- completion: — блок, который будет выполнен по окончании последовательности анимации.

Если в параметр from мы зададим `firstView`, а в параметр to зададим secondView, то у нас всегда будет одна и та же анимация: переход от `firstView` к secondView.  
Нам же нужно, чтобы такого ограничения не было. И, если мы перешли к `firstView`, то следующий переход должен быть к secondView, если перешли к secondView, то следующий переход — к `firstView`.

**Но главный вопрос — как это сделать?**

Всё на самом деле очень просто. Чуть раньше мы создали переменную isFlipped. 

В начале функции transitionCard нам нужно менять ее параметр на противоположный. С true на false. То есть с «‎карта была перевернута» на «‎карта не была перевернута». И в зависимости от значения этой булевой переменной совершать какие-то действия.

```swift
isFlipped = !isFlipped
```


Или же более элегантный вариант:
```swift
isFlipped.toggle()
```


Метод toggle() **инвертирует значение булевой переменной**. То есть из true делает false, а из false — true.

Дальше нужно создать две константы: firstCard, secondCard. Они также будут постоянно меняться.
```swift
let firstCard = isFlipped ? firstView : secondView
let secondCard = isFlipped ? secondView : firstView
```


- firstCard: если карта перевернута, то присвоить `firstView`, иначе — secondView.
- secondCard^ если карта перевернута, то присвоить secondView, иначе — `firstView`.

Таким образом, в from и to у нас всегда будут разные view, они будут постоянно меняться местами: то `firstView`, то secondView. Зависеть это будет от значения переменной isFlipped, которая также постоянно меняется.

Заполняем параметры метода transition:
```swift
UIView.transition(from: firstCard!,
         to: secondCard!,
         duration: 0.5,
         options: [.transitionFlipFromRight, .showHideTransitionViews],
         completion: nil)

- .transitionFlipFromRight — анимация переворота view вправо.
- .showHideTransitionViews — скрывает fromView, но не удаляет его из иерархии представлений.
```


Код в результате должен получиться следующий:
```swift
// MARK: IBAction
    @IBAction func transitionCard(_ sender: Any) {
        isFlipped = !isFlipped
        let firstCard = isFlipped ? firstView : secondView
        let secondCard = isFlipped ? secondView : firstView
 
        UIView.transition(from: firstCard!,
         to: secondCard!,
         duration: 0.5,
         options:[.transitionFlipFromRight,
                                    .showHideTransitionViews],
         completion: nil)
    }
```
    

Сейчас мы близки к тому, что хотели сделать изначально. Единственное, что осталось добавить, — появление рандомного предсказания.

Но и тут всё предельно просто. Внутри замыкания _animation_ функции transition нужно добавить константу, которая будет генерировать случайное число в диапазоне от 0 до количества предсказаний (predictions.count).

Затем соответствующее предсказание мы присваиваем лэйблу:
```swift
        UIView.transition(from: firstCard!,
                          to: secondCard!,
                          duration: 0.5,
                          options: [.transitionFlipFromRight, .showHideTransitionViews]) { _ in
let randomInt  = Int.random(in: 0..<self.predictions.count)
self.secondViewLabel.text = self.predictions[randomInt]
        }
```

Ну что же, самую сложную часть этого модуля мы прошли. И, считаем, что прошли успешно! Давайте закрепим полученные знания посредством теста и пойдем дальше.