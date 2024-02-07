#transformation #трансформация #трансформация 

У каждого `UIView` есть свойство _**transform**_, которое позволяет управлять его _размером_, _положением_ и _поворотом_, используя так называемое аффинное преобразование (**_CGAffineTransform_)**.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9c956342821c4da9ba50a5ac9579a0ef/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p1.png)

CGAffineTransform представляет собой матрицу размерностью 3 на 3. Немного окунемся в теорию по матрицам, чтобы лучше понимать происходящее. В них нет ничего сложного, поэтому не бойтесь :)

**Матрица** — это прямоугольная таблица элементов, состоящая из _m_ строк и _n_ столбцов. Число строк и столбцов задают **размерность матрицы** (_m×n_). Например, таблица размерностью 3×4 имеет 3 строки и 4 столбца. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/88dd00ce333d8881df9ce62ea12522c5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p2.png)

- _a11_ — элемент 1 строки и 1 столбца
- _a12_ — элемент 1 строки и 2 столбца
- _a1n_ — элемент 1 строки и n столбца
- _a21_ —  элемент 2 строки и 1 столбца…

Вернемся к CGAffineTransform. Как мы выяснили, это матрица размерностью 3 на 3.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8dd75f21c36741af7961f26fba86e4fe/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p3.png)

Источник: [developer.apple.com](https://docs-assets.developer.apple.com/published/8a0bbde8e5/equation01_2x_fabc9070-1967-4d6f-a086-17ab5fcfef6d.png)

В языке программирования _Swift_ CGAffineTransform реализована в качестве структуры.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/47cf9927807ed8d0da94f3801665cb2a/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p4.png)

Поскольку третий столбец матрицы всегда хранит в себе одно и то же значение _(0, 0, 1)_, структура CGAffineTransform содержит в себе значения _только для первых двух столбцов_. А именно такие значения как: _a, b, c, d, tx, ty_. Далее на конкретных примерах мы разберем каждое из этих значений, поймём, за что они отвечают, для чего нужны и какой результат дают.

Дополнительно можете прочитать документацию по [ссылке](https://developer.apple.com/documentation/coregraphics/cgaffinetransform).

## Еще немного подготовительных действий в проекте:

Внутрь someView добавим _label_, который поможет в дальнейшем нам отследить, повернулось ли someView, и если да, то в какую сторону.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c1ee9b08d7c4078bf3de0e904cc9f615/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p5.png)

При нажатии на кнопку по-прежнему срабатывает viewAnimate(), код мы будем писать именно внутри этой функции.

Начинаем с `UIView.animate()` и думаем: какие параметры нам нужны? Ведь функций animate() несколько и отличаются они именно параметрами. Нам нужно только _время выполнения анимации_, а значит, будем использовать следующую функцию:
```swift
UIView.animate(withDuration: 1) {
/// Тут будем писать код анимации
}
```


Теперь начинаем анимировать `UIView` !

## **Единичная матрица**

**Единичная матрица** _(identity matrix)_ — это квадратная матрица, в которой по диагонали расположены единицы, а во всех остальных элементах — ноль.

По умолчанию свойство `transform` представляет собой _единичную матрицу._ 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bc132f6c938091ddbbad9ba8936098cc/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/m25u3_image4.PNG)

Единичная матрица полезна для сброса положения, поворота или масштаба view. Если вы хотите, чтобы по окончании анимации все её параметры (положение, поворот, масштаб) сбросились, то используйте свойство identity.

```swift
self.someView.transform = CGAffineTransform.identity
```

Для чего это нужно? Чтобы, допустим, при каждом нажатии на кнопку у вас отрабатывала анимация. Если же вы не зададите единичную матрицу по окончании анимации, то не сможете использовать её повторно.

## **Изменение положения UIView** 

Для того, чтобы изменить положение `UIView`, используя `transform`, необходимо изменить у матрицы такие значения, как _tx, ty._

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2451cc27c3820af115fc14381858ee1b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/m25u3_image1.PNG)

Мы можем обратиться к tx и ty напрямую, чтобы изменить их. Изменим эти значения на -50:
```swift
self.someView.transform.tx = -50
self.someView.transform.ty = -50
```


Изменив значение tx на -50, мы сместили someView на 50 точек влево.

Это очень легко проверить:
```swift
print(self.someView.frame.origin.x)
self.someView.transform.tx = -50
print(self.someView.frame.origin.x)
```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/665757fbf2c05bbf58255536698d7c82/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p5.6.png)

Сначала расположение someView по _х_ было равно 112.5, затем стало равно 62.5. Разница как раз составляет 50 точек. Если бы мы изменили значение tx на 50, то someView сместилось бы на 50 точек вправо.

Аналогично и с ty: мы присвоили ty значение равное -50. Соответственно someView сместилось на 50 точек вверх. Если бы мы присвоили ty положительное значение, то someView сместилось бы вниз.

Делаем **вывод**: если хотим сместить `UIView` при помощи `transform` влево или вверх, используем отрицательные значения, вправо или вниз — положительные.

В результате смещения someView влево и вверх на 50 точек мы получили анимацию, при которой someView перемещается _по диагонали влево._ 

У CGAffineTransform есть функция CtranslatedBy(x:y:) и инициализатор CGAffineTransform(translationX:y:), которые также изменяют значения tx и ty. То есть до этого мы напрямую обращались к tx, ty и изменяли их. Но это можно сделать при помощи функции или инициализатора. Результат будет один и тот же во всех трёх случаях, но, тем не менее, знать о всех вариантах мы обязаны, поэтому рассмотрим их:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bb633ac30f714deb8b4ede1c9a3faf4e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p6.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7e46183a7845f1cbbb5358717a78c67d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p7.png)

Используя функцию или инициализатор, вы также можете изменить положение view по оси _x_ и по оси _y._ Давайте рассмотрим, как это можно сделать:

Используем функцию, чтобы сместить someView на 50 точек влево и вверх:

self.someView.transform = self.someView.transform.translatedBy(x: -50, y: -50)

Здесь мы обратились к свойству `transform`, чтобы вызвать функцию translatedBy и в её параметрах задать значения для tx, ty.

Используем инициализатор, чтобы сместить someView на 50 точек влево и вверх:

self.someView.transform = CGAffineTransform(translationX: -50, y: -50)

Здесь мы уже инициализируем значения структуры CGAffineTransform, прописывая параметрам инициализатора значения tx, ty.

Немного пояснений касательно инициализатора. Освежим теорию по данной теме.

CGAffineTransform(translationX: -50, y: -50)

Этот код равносилен тому, что у нас была бы создана какая-то структура и инициализатор, через который мы бы инициализировали какие-то значения структуры:
```swift
struct SomeStruct {
 
    init(x: CGFloat, y: CGFloat) {
        self.x = x
        self.y = y
    }
 
    let x: CGFloat
    let y: CGFloat
}
 
SomeStruct(x: 5, y: 5)
```


Или же:
```swift
struct CGAffineTransform {
 
    init(translationX: CGFloat, y: CGFloat) {
        self.translationX = translationX
        self.y = y
    }
 
    let translationX: CGFloat
    let y: CGFloat
}
CGAffineTransform(translationX: 5, y: 5)
```

 


**Узнали? Согласны?**

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/63dc3bf82481c8a9c7bda7ec2d44cf54/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p8.png)

Вы можете использовать любой из представленных вариантов изменения положения someView. Результат во всех случаях будет одинаковый — someView сместится на 50 строчек влево и на 50 строчек вверх.

Код всех трёх вариантов:
```swift
UIView.animate(withDuration: 3) {
            // Вариант 1
            self.someView.transform.tx = -50
            self.someView.transform.ty = -50
 
            // Вариант 2
            self.someView.transform = self.someView.transform.translatedBy(x: -50, y: -50)  
            // Вариант 3
            self.someView.transform = CGAffineTransform(translationX: -50, y: -50)
}

```


## **Масштабирование UIView**

Чтобы изменить высоту и ширину `UIView`, используя `transform`, необходимо изменить значения матрицы _a_ и _d_ , где _a_ — это _xScale_, а _d_ — _yScale_. По умолчанию эти значения равны 1.

_**Scale**_ в переводе с английского означает масштаб.

Вы можете индивидуально управлять _a_ и _d_, напрямую присваивая им какие-либо значения:
```swift
self.someView.transform.a = 2.0
self.someView.transform.d = 2.0
```

Для масштабирования view также можно использовать функцию scaleBy(x:y:) или инициализатор CGAffineTransform(scaleX:,y:).

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7479951b6108e66c78554fba193f094b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p9.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/042960412959e34466e3f96750ac02f3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p10.png)

Давайте напишем код, который будет увеличивать someView в два раза по обеим осям: по _x_ и по _y._ 

self.someView.transform = self.someView.transform.scaledBy (x: 2, y: 2)

Мы обращаемся к свойству `transform` и вызываем функцию scaleBy. Задавая иксу и игреку значение 2.0, мы указываем, что someView должна увеличиться по оси _x_ и по оси _y_ в два раза. Соответственно ширина и высота view увеличится в два раза.

Давайте увеличим размер someView другим способом — при помощи инициализатора:

self.someView.transform = CGAffineTransform(scaleX: 2.0, y: 2.0)

Таким образом, изменяя значения _a_ и _d_ у CGAffineTransform, вы масштабируете view по осям _x_ и _y_, изменяя при этом ширину и высоту view.

Код всех трёх вариантов:
```swift
UIView.animate(withDuration: 3) {
    // 1 вариант
    self.someView.transform = self.someView.transform.scaledBy (x: 2, y: 2)
    // 2 вариант
    self.someView.transform = CGAffineTransform (scaleX: 2.0, y: 2.0)
    // 3 вариант
    self.someView.transform.a = 2.0
    self.someView.transform.d = 2.0
}

```

## **Вращение UIView**

Для того, чтобы повернуть view на какой-либо угол, необходимо изменить значения матрицы _a, b, c, d_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8916a9e8b1b784a042e26562425b3ec9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/m25u3_image2.PNG)

Для поворота view можно использовать функцию rotated(by:) и инициализатор CGAffineTransform(rotationAngle:)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0d35f5a6282c018d4d21ba59130c2f95/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p11.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/379f9dc2cea38352477c94e80445cbbb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p12.png)

Важно отметить, что _**a**_**_ngle_** — это угол, на который вы хотите повернуть view, и он указывается в радианах! Сейчас разложим всё по полочкам. Не пугайтесь!

Начнем с определения:

**Радиан** — угол, соответствующий дуге, длина которой равна её радиусу. 1 радиан равен примерно 57 градусам.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/511ba25a55f1c958dedcc619580bdf79/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p13.png)

Не будем углубляться в теорию по геометрии, самое важное — это понять, зачем он (радиан) нам нужен в анимации. Нужен радиан нам для того, _чтобы указать, на какой угол должен повернуться объект._

Например, 180 градусов = 3,14 радиан = π (пи).

Для того, чтобы перевести градусы в радианы, нужно воспользоваться формулой. Давайте создадим константу с этой формулой:
```swift
let angle: CGFloat = градусы * CGFloat.pi / 180.0
```


Нужно градус, который вы хотите перевести в радианы, умножить на π (пи) и разделить на 180.

Давайте напишем код, который сделает поворот someView на 180 градусов. Как мы упомянули ранее, π (пи) = 180 градусов = 3,14 радиан. У CGFloat есть свойство, значение которого мы можем получить:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6d20821f9f0122aaccb68552573e4fbb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p14.png)
```swift
@IBAction func viewAnimate(_ sender: Any) {
         UIView.animate(withDuration: 1) {
             // Поворот на 180 градусов
             self.someView.transform = CGAffineTransform(rotationAngle: CGFloat.pi)
        }
}
```


Или же мы можем воспользоваться формулой перевода градуса в радианы, которую рассмотрели ранее. 

Здесь мы создадим отдельную константу типа CGFloat, чтобы дальше передать её в параметр инициализатора.

```swift
let angle: CGFloat = 180 * CGFloat.pi / 180.0
self.someView.transform = CGAffineTransform(rotationAngle: angle)
```

 

Результат будет соответственно такой же: someView повернется на 180 градусов.

То есть мы в параметр rotationAngle не можем сразу указать градус, на который мы хотим повернуть someView, так как rotationAngle принимает значение в радианах! Именно поэтому мы используем формулу перевода из градусы в радианы.


## **Искажение UIView**

Искажение _view_ можно получить путем изменения значений _b-_ и _c-_матрицы.

Давайте изменим значение c матрицы и посмотрим, что изменится:
```swift
UIView.animate(withDuration: 1) {
        let angle: CGFloat = 45.0 * CGFloat.pi / 180.0
        self.someView.transform.c = cos(angle)
}
```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/81430ad05c22d3bbf3e4e89dc1068bab/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p17.png)

Как мы видим, someView исказилось.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7ecc764d0eaf05e94df83da2ac49a2d3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/m25u3_image3.PNG)

Мы исказили someView на _cos(0,78)._ Необязательно использовать именно _cos_ или _sin,_ но более предпочтительно, поскольку по умолчанию _b = sin(0),_ как, собственно, и _с = sin(0)._

В замедленном видео анимация выглядит так:

Давайте теперь изменим значение _b-_матрицы:
```swift
UIView.animate(withDuration: 1) {
            let angle: CGFloat = 45.0 * CGFloat.pi / 180.0
            self.someView.transform.b = cos(angle)
}

```

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/52ea0b33e84f591fb19992b64ec1b7ea/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p18.png)

В замедленном видео анимация искажения выглядит так:

## **Комбинация анимаций**

Выполнение нескольких преобразований может привести к непредвиденному поведению и неожиданным результатам.

Рассмотрите предложенный код и ответьте для себя на вопрос: «‎Как сработает анимация?»
```swift
    @IBAction func viewAnimate(_ sender: Any) {
        UIView.animate(withDuration: 0.5) {
            let angle: CGFloat = 45.0 * CGFloat.pi / 180.0
            self.someView.transform = CGAffineTransform(rotationAngle: angle)
            self.someView.transform = CGAffineTransform(translationX: -50.0, y: -50.0)
            self.someView.transform = CGAffineTransform(scaleX: 2.0, y: 2.0)
        }
    }
```

Может показаться, что анимация сработает так: сначала someView повернется, потом переместится, потом масштабируется. И это неправильно. Тут всё немного хитрее!

Посмотрите исполнение этой анимации в замедленном видео:

Если же вы напишете код анимации без метода animate(), то обнаружите похожую, но немного другую ситуацию. Вы увидите по-прежнему неправильную анимацию. Так в чём дело?
```swift
@IBAction func viewAnimate(_ sender: Any) {
        let angle: CGFloat = 45.0 * CGFloat.pi / 180.0
        self.someView.transform = CGAffineTransform(rotationAngle: angle)
        self.someView.transform = CGAffineTransform(translationX: -50.0, y: -50.0)
        self.someView.transform = CGAffineTransform(scaleX: 2.0, y: 2.0)
    }

```

Всё дело в том, что конечным результатом этого кода является масштабированный `UIView`. Это связано с тем, что преобразование (`transform`) всегда переназначается, удаляет значение предыдущей матрицы. И в результате у нас остается последняя матрица, которая масштабирует `UIView`.

Чтобы назначить несколько анимаций для view, необходимо объединить матрицы. CGAffineTransform для этого имеет метод concatenating().

**_Сoncatenating_** в переводе с английского— это связывание. То есть мы связываем несколько анимаций:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/45a002f23391c562eed96385a7bff7ae/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_25_u3_p19.png)

Метод concatenating() принимает параметр t2. Он умножает текущее преобразование (`transform`) на t2 и возвращает результат матрицы произведения.

В конечном результате для нас, наверное, неважно, что тут происходит — сложение, умножение, вычитание матриц. Важно то, что нам позволяет сделать конкретный метод. Но если вы хотите углубиться и понять, почему именно умножение матриц нам дает эффект «‎связывания«» анимаций, то давайте попробуем разобраться. 

**Умножение матриц** — это совсем несложно: нужно всего лишь складывать и умножать числа. С этим мы справимся! Результатом умножения матрицы является матрица произведения.

Дополнительный [источник](http://www.mathprofi.ru/deistviya_s_matricami.html) по действиям с матрицами.

Продолжаем!

Давайте напишем анимацию, которая будет поворачивать someView на 45 градусов вправо и перемещать его вправо на 80 точек.

Для этого мы создадим константы rotationMatrix и translationMatrix и воспользуемся инициализаторами CGAffineTransform:
```swift
       UIView.animate(withDuration: 0.5) {
            // Угол 45 градусов
            let angle: CGFloat = 45.0 * CGFloat.pi / 180.0
            // Создаем матрицу поворота
            let rotationMatrix = CGAffineTransform(rotationAngle: angle)
            // Создаем матрицу перемещения
            let translationMatrix = CGAffineTransform(translationX: 80.0, y: 0.0)
            // Трансформируем someView
            self.someView.transform = rotationMatrix.concatenating(translationMatrix)
        }
```
 

Этот код сначала перемещает someView, а затем вращает его. Вращение рассчитывается на основе центра `UIView`. 

Написав этот небольшой кусочек кода, вы, на самом деле, применили много знаний? «Каких?», — спросите вы. А мы ответим! Вы использовали знания по анимации объектов, по углам, радианам, аффинным преобразованиям, матрицам. Это очень круто! Вы огромные молодцы!

[[Переходы между view, transition]] 