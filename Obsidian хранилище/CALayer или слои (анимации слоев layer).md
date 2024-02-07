#слои #calayer #animation 

_**CALayer**_ — это класс, который концептуально очень похож на _UIView_. _Layers_ (слои), как и _views_, — это прямоугольные объекты, которые можно расположить в виде иерархического дерева. Как и _views_, они могут хранить в себе контент (такой как, например, картинка, текст или цвет фона) и управлять позицией своих _sublayers_.  
Слои имеют методы и свойства для выполнения анимаций и преобразований. Единственная важная функция _UIView_, которая не обрабатывается _CALayer_, — это **взаимодействие с пользователем** (_user interaction_). _CALayer_ **не знает** о **_responder chain_** (механизм, который _iOS_ использует для распространения событий касания через иерархию представлений) и поэтому не может реагировать на события, хотя он предоставляет методы, помогающие определить, находится ли конкретная точка касания в пределах слоя. 

_CALayer_ является частью фреймворка _CoreAnimations_.

_UIView_ обрабатывает множество вещей, включая _layout_ и _touch events_. Однако он не управляет непосредственно рисованием или анимацией. _UIKit_ делегирует эту задачу фреймворку _CoreAnimations_, который включает в себя класс _CALayer_. **_UIView_**, по сути, — это просто обертка над _CALayer_. 

## Создадим новый проект.

Добавьте на сториборд _UIView_, закрепите его на экране посередине и создайте аутлет в классе `ViewController`, для `UIView` имя будет `someView`.

Теперь, когда у нас есть объект `UIView`, мы можем получить доступ к его слою следующим образом:

someView.layer

У нас есть доступ к слою, но что мы можем с этим сделать? На самом деле, возможностей очень много! Работа со слоями будет вестись в методе жизненного цикла `viewDidAppear()`.

## **Закругленные углы**

Помните, когда мы делали закругленные углы у view, мы использовали такой код:

someView.layer.cornerRadius = 15

То есть мы обращались к свойству слоя, чтобы изменить закругленность углов. За закругленные углы отвечает свойство cornerRadius.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8c47570c5115e44c49c3db1e3f8ed8f9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u5_p1.png)

## **Эффект теней**

Вы также можете создать эффект теней. Для этого нужно воспользоваться рядом методов: shadowOffset, shadowOpacity, shadowColor. По необходимости ещё и shadowRadius.
```swift
    // 1. Смещение тени относительно someView
        someView.layer.shadowOffset = CGSize(width: 3, height: 4)
        // 2. Непрозрачность тени
        someView.layer.shadowOpacity = 0.4
        // 3. Радиус тени
        someView.layer.shadowRadius = 10
        // 4. Цвет тени
        someView.layer.shadowColor = UIColor.gray.cgColor
```
    

1. Мы установили смещение тени слоя: она будет смещена на три точки вправо и на четыре точки вниз относительно someView.
2. Установили непрозрачность тени на 0.4.
3. Установили радиус тени слоя. Это так называемый _радиус размытия_. Чем больше этот радиус, тем более размытая тень, но менее заметная.
4. Установили цвет тени слоя. Данное свойство имеет тип CGColor, поэтому нам необходимо UIColor преобразовать к CGColor.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/93157ae9f53a694f47fa9538ffbe4426/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u5_p2.png)

## **Обводка**

Мы можем обозначить границы нашего слоя посредством обводки слоя и добавить тень: 
```swift
someView.layer.borderColor = UIColor.gray.cgColor    //    1. Цвет обводки
someView.layer.borderWidth = 2    //    2. Ширина линии обводки
 
someView.layer.shadowOffset = CGSize(width: 3, height: 4) //    3. Смещение тени относительно someView
someView.layer.shadowOpacity = 0.4    // 4. Непрозрачность тени
someView.layer.shadowRadius = 10    // 5. Радиус тени
someView.layer.shadowColor = UIColor.gray.cgColor     // 6. Цвет тени

```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b0f4277e3590da98cb77d3d19fb068aa/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u5_p3.png)

## **Цвет фона**

Мы можем также установить цвет фона слоя. За это отвечает свойство backgroundColor:
```swift
someView.layer.backgroundColor = UIColor.red.cgColor

// MARK: Закругление углов
        // Закругление углов
        someView.layer.cornerRadius = 15
        // MARK: Тень
        // Смещение тени относительно someView
        someView.layer.shadowOffset = CGSize(width: 5, height: 5)
        // Непрозрачность тени
        someView.layer.shadowOpacity = 0.4
        // Радиус тени
        someView.layer.shadowRadius = 0
        // Цвет тени
        someView.layer.shadowColor = UIColor.gray.cgColor
        // MARK: Обводка
        someView.layer.borderColor = UIColor.gray.cgColor
        someView.layer.borderWidth = 2
        // MARK: Цвет фона
        someView.layer.backgroundColor = UIColor.red.cgColor
```

 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7d7b0c678dd006e87d5d92b2cd703376/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u5_p4.png)

## **Анимация**

Теперь перейдем к тому, как сделать анимацию слоя. Для этого мы будем использовать CABasicAnimation — класс для создания объектов, которые помогут анимировать свойства наших слоев.

Для того, чтобы создать анимацию, нужно написать очень простой код:
```swift
let animation = CABasicAnimation(keyPath: "position")
```



- keyPath — свойство, которое хотим анимировать

Допустим, мы хотим создать анимацию изменения расположения (позиции) какого-либо объекта на экране. Для этого можно использовать position.

Итак, мы создали CABasicAnimation. Стоит отметить, что на данный момент анимация не добавлена, а лишь создана, и, по сути, сейчас никакой анимации у нас нет. Откуда ей взяться? Ведь мы просто указали то, **какую** анимацию мы хотим сделать — _анимацию изменения расположения_, но не задали конечную точку, к которой должны прийти, не задали какие-то свойства. 

У CABasicAnimation есть ряд свойств, которые _можно и нужно_ использовать для создания анимации.

## **Рассмотрим основные свойства _CABasicAnimation_:**

  
fromValue — стартовое значение, _от которого будет стартовать анимация._

Рассмотрим основные свойства CABasicAnimation:
```swift
animation.fromValue = CGPoint(x: 50, y: 50)
```


В нашем случае, так как мы ранее создали анимацию изменения расположения, это начальное расположение объекта по _х_ и по _у_. Задать его мы можем и по-другому:
```swift
animation.fromValue = view.center
```


Таким образом, начальным положением объекта, который мы анимируем, будет середина экрана.

  
toValue — значение, до которого будем анимировать это свойство (от 0 до 1)
```swift
animation.toValue = CGPoint(x: 100.0, y: 100.0)

```

В нашем случае — это конечное объекта по _х_ и по _у_.

Вы могли подумать, что fromValue и toValue отвечают за начальное и финальное расположение объектов по _х_ и по _у_, но это не совсем так. В данном случае мы анимируем изменение положения объекта на экране, но если это будет анимация исчезновения объекта (изменения opacity-свойства), то начальное и конечное значения будут другими. На этом мы остановимся отдельно после того, как рассмотрим основные свойства.

  
duration — продолжительность анимации в секундах.
```swift
animation.duration = 3.0
```


  
autoreverses — возвращает в исходное значение либо плавно, либо нет (true/false).

```swift
animation.autoreverses = true
```


  
repeatCount — количество повторений анимации.
```swift
animation.repeatCount = 2
```


  
add(CAAnimation, forKey: String) — функция добавления анимации, где первый параметр — это CAAnimation, в нашем случае — CABasicAnimation. forKey — ключ, который в дальнейшем вами может быть использован, то есть это не тот ключ, который мы указывали в CABasicAnimation.

В данном случае мы хотим добавить написанную анимацию для someView. Обращаемся к свойству layer и вызываем метод add(:forKey):
```swift
someView.layer.add(animation, forKey: "animatePosition")
```


В результате у нас получился следующий код:
```swift
let animation = CABasicAnimation(keyPath: "position");
        animation.fromValue = view.center
        animation.toValue = CGPoint(x: 100.0, y: 100.0)
        animation.duration = 3.0
        animation.autoreverses = true
        animation.repeatCount = 2
        someView.layer.add(animation, forKey: "animatePosition")
```
        
 

## Теперь давайте напишем анимацию плавного исчезновения объекта с экрана.

Делать это мы будем посредством уменьшения прозрачности.
```swift
let animation = CABasicAnimation(keyPath: "opacity")
```


В качестве keyPath укажите opacity-свойство, которое отвечает за прозрачность (максимальное значение — 1, минимальное — 0).

Соответственно начальным значением будет 1, финальным — 0.
```swift
animation.fromValue = 1
animation.toValue = 0
```


Укажем время длительности анимации:
```swift
animation.duration = 1
```


Сделаем плавное возвращение в начальную позицию:
```swift
animation.autoreverses = true
```


И добавим анимацию:
```swift
someView.layer.add(animation, forKey: "changeOpacity")
```
