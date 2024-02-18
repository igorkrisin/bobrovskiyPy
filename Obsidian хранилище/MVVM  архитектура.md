#architect #mvvm #uikit 

## **Что это такое?**

**_MVVM_** — это паттерн проектирования приложений, который впервые был представлен в 2005 году Джоном Госсманом. _MVVM_ должен быть ориентирован на современные платформы разработки (паттерн создавался для приложений _Microsoft_).

Рекомендуем прочесть немного общей информации о [_MVVM_](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

## **Для чего он нужен?**

Паттерн применяется для разделения модели и её представления, тем самым позволяет работать с каждым элементом по отдельности. В качестве примера представьте разработчика, который работает над логикой с данными, что, в свою очередь, не мешает дизайнеру работать с пользовательским интерфейсом.

## **А как же MVC?**

По началу, когда вы новичок, вы повсеместно используете архитектуру _MVC_ в своих проектах (а иногда и в коммерческих), особо не углубляясь, что это такое и не «парясь» за дальнейшую «жизнь» приложения. Но по мере роста ваших скиллов и требований рынка, вам приходится изучать все новые и новые архитектуры, которые впоследствии облегчают вам жизнь.

## **Как расшифровывается MVVM?**

**M**

  
**— Model**

_Model_ — слой, отвечающий за **доступ к данным** для манипуляции над ними. Модель имеет какие-то уникальные данные конкретного объекта.

**V**

  
**— View**

_View_ — слой, отвечающий за **представление** (это все, что начинается на _UI_). Например, когда вы создаете новый проект, в приложении всегда есть _ViewController_, который наследуется от _UIViewController._

**VM**

  
**— ViewModel**

_ViewModel_ — это последний слой, который находится между _View_ и _Model_. Он отвечает за **изменение модели**, реагируя на какие-то действия в представлении. К примеру, пользователь нажимает на кнопку (эта кнопка, естественно, находится на _View_), логика кнопки связана с _ViewModel_ — всегда знает о том, изменилась модель или нет. Если модель изменилась, тогда _ViewModel_ говорит _View_ отрисовать новый контент.

## **Почему MVVM?**

Когда вы используете _MVC_, то вся логика по обработке данных находится в контроллере, и лишь малая её часть — в модели, что очень вредит дальнейшей разработке. Ваш _MVC_ превращается в _Massive View Controller_ (контроллер раздувается до огромных размеров, его становится сложно «обслуживать»).

Что касается _MVVM_, то эта архитектура позволяет скрыть от контроллера (_View_) модель, а все общение идет через _ViewModel_. Тем самым _Controller (View)_ значительно разгружается от ненужной логики, которая не должна быть в нём.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/26264dfb46cfcc14add28a616a003838/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p1.png)

Также если вы будете применять паттерн _MVVM_, то ваш код будет:

- **Распределенный** — это значит, что вы сможете отделить одну логику от другой, тем самым классы станут меньше. Также каждый класс будет соответствовать принципу единственной ответственности.
- **Тестируемый** — паттерн позволяет в принципе писать юнит-тесты, в отличие от паттерна _MVC_, а также написание тестов становится значительно проще, опять же, благодаря принципу единой ответственности.
- **Простой** — кода становится значительно меньше, он более читаемый и понятный.
- **Написан с применением _SOLID_.  
    **Если забыли, что это такое, то освежите воспоминания по _SOLID_ в модуле «[SOLID и внедрение зависимостей](https://lms.skillfactory.ru/courses/course-v1:SkillFactory+iOS-4+14SEP2020/courseware/4248fe4a0e5545d49ddcbfe9fefc51e5/7f575c018aa54400b2f02198fcd9cf7c/1?activate_block_id=block-v1%3ASkillFactory%2BiOS-4%2B14SEP2020%2Btype%40vertical%2Bblock%4022eae91d7a0c4cfcb85f3b4bdc97a893)».

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6d567082226fc923d548c0a0d90ba436/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p2.png)

Источник: [a.d-cd.net](https://a.d-cd.net/f7a3ca5s-480.jpg)

## **В чем отличие между MVP и MVVM?**

Самое главное отличие между _MVP_ и _MVVM_ в том, что _MVP_ — это посредник (_Presenter_), который знает о _View_, а _MVVM_ (_ViewModel_) знает только о _Model_. Далее вы посмотрите в коде, как это реализовывается.

## **«Я слышал про какие-то библиотеки для MVVM…»**

Изначально этот паттерн был создан Майкрософт и применялся для _C#_, но впоследствии перекочевал в _iOS_. Если вы спросите любого программиста, который использует _MVVM_, то он вам скажет, что применяет какой-то реактивный подход.  
Да, это так и есть. Существуют специальные библиотеки, которые позволяют вам писать реактивный код, и его применение в _MVVM_ практически повсеместно обязательно.

Есть такие библиотеки: _ReactiveCocoa, RxSwift_ или _PromiseKit._

**Рекомендуем вам прочесть статьи из списка ниже, чтобы немного узнать об этих подходах:**

- _[ReactiveCocoa](https://habr.com/ru/post/317992/)  
    _
- _[RxSwift](https://habr.com/ru/post/281292/)  
    _
- _[PromiseKit](https://habr.com/ru/post/254435/)  
    _

**Важно!** Если вы хотите использовать _MVVM-_паттерн, то вы будете обязаны узнать одну из этих библиотек, а в последствии выучить её. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/88c43aa48540ed1160c744e9a396424d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p3.png)

Источник: [meme-arsenal.com](https://www.meme-arsenal.com/memes/07127ce6561ba4355e20aee770226aaf.jpg)

**И как же нам быть без реактивного подхода? Сейчас начнем учить какую-то библиотеку?**

Вовсе нет, к счастью можно использовать биндинги.

**Биндинг** — это событие, которое случается когда-то потом. Когда оно случается, то какое-то действие происходит, в противном случае — нет.

В качестве биндинга можно использовать _KVO, Notification, Closures, Delegates._ Единственное неудобство — надо писать их вручную. Также есть уже готовые решения, написанные за вас, их можно брать и применять под свои нужды, одно из таких решений, такие как:

- **_RZDataBinding_** — это платформа, предназначенная для поддержания целостности данных в вашем приложении _iOS_ или _OS X_. Она построена с использованием стандартной структуры _Key-Value Observation_ (_KVO_), но более безопасна и предоставляет дополнительные функции. Как и _KVO_, _RZDataBinding_ помогает избежать бесконечных цепочек делегатов, устанавливая прямые обратные вызовы, когда объект меняет состояние.
- **_SwiftBond_** — построен на основе _ReactiveKit_ и устраняет разрыв между реактивной и императивной парадигмами. Вы можете использовать его как автономную структуру, чтобы упростить изменение состояния с помощью привязок и реактивных источников данных, но вы также можете использовать его с _ReactiveKit,_ чтобы дополнить ваши реактивные потоки данных, реактивными делегатами и реактивными источниками данных.
- Также есть и другие вариации библиотек, которые вы всегда можете найти на _cocoapods_.

**Важно!** Любые библиотеки можно подключать через cocoapods !!!

Если исходить из практического опыта и из того, что требуют работодатели, **то лучше изучить реактивное программирование**, так как оно очень востребовано.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ec2f7e93b13f18156b1563eb74bf2f6b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p4.png)

Источник: [memesmix.net](http://memesmix.net/media/created/f9gpbg.jpg)

_«Я реально должен знать это все для того, чтобы кодить?» —_ спросите вы. Вовсе нет, всего знать невозможно. Вам необходимо понимать, что это такое и знать, где это можно найти в случае чего. Знания приходят с опытом.

## **Как с этим работать в коде?**

Давайте рассмотрим на примере небольшого приложения, как работать с _MVVM_.  
Название приложения — _MVVM_

**В чем идея приложения?**

При нажатии на кнопку на экран выводится конкретное изображение.

**Логика для приложения _MVVM_:**

- Есть две кнопки — _ShowFirstImage_ и _ShowSecondImage._
- При нажатии на _ShowFirstImage_ запускается анимация _Activity Intiacator_, а затем через секунду отображается картинка _Success._ Анимация исчезает.
- При нажатии на _ShowSecondImage_ запускается анимация _Activity Intiacator_, а затем через секунду отображается картинка _Stop._ Анимация исчезает.

**Подготовительная часть:**

1. Создайте новое приложение с именем _LearningPatternMVVM._
2. Создайте три новые папки и назовите их _Model_, _View,_ _ViewModel._
3. Удалите созданный файл _ViewController_ и _UIViewController_ из сториборда (будем создавать все сами).
4. Выберите _Main.Storyboard_ и перетащите в папку _View_ (все, что касается пользовательского интерфейса, всегда должно быть в папке _View)._
5. В папке _Model_ создайте свифт-файл с именем _MvvmModel._
6. В папке _ViewModel_ создайте свифт-файл с именем _MvvmViewModel._
7. В папке _View_ создайте _Cocoa touch class_ с именем _MvvmView._
8. В сториборде создайте новый _UIViewController._
9. Связжите  _MvvmView_ с _UIViewController._
10. Укажите новый контроллер _is initial View Controller._

**Вот как должна выглядеть структура файлов проекта:**

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f4a67647a880f50bfd821d7607481962/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p5.png)

**С созданием проекта разобрались, теперь добавим _UI-_элементы на _UIViewController._**

Вам понадобится: 

- _UIImageView,_ в которое будет подставляться нужное изображение (расположите его по центру экрана).
- Две кнопки — _Show first image_ и _Show second Image_. Они будут располагаться под изображением.
- Последний элемент — это _Activity Indicator_, который также располагается по центру экрана.

Вариант того, как может выглядеть экран с _UI-элементами:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2b9f9946b026aa5065dbc1c1bd1bd999/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p6.png)

## Скринкаст на тему: «Устанавливаем размеры для UI-элементов‎»

Свяжем все _UI-элементы_ с классом `MvvmView`:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7a28bae9955b693c8fedfa2dbcb33d61/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p7.png)

Затем создадим события для кнопок с именами showFirstImageBtnPressed и showSecondImageBtnPressed:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/45319a900b47369532e4a86cb0fa523b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p8.png)

**Давайте начнем работать над _MVVM_ с класса MvvmViewModel.**

Для начала вам необходимо задать протокол, который будет обязывать классы реализовать его методы.  
Протокол MvvmViewModelProtocol должен иметь одно замыкание — updateView и два метода — showFirstImage и showSecondImage.  
Замыкание updateView нужно для того, чтобы отслеживать состояние, которое будет меняться в зависимости от того, что сейчас нажато.  
В качестве аргумента принимается модель MvvmModel:

var updateView:((MvvmModel)->())? { get set }

Методы showFirstImage и showSecondImage ничего не принимают и не возвращают:

func showFirstImage()
func showSecondImage()

Их задача — отображать нужное изображение.

Вам необходимо реализовать протокол MvvmViewModelProtocol:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/51289c7df1f73aa50247e3b00923aadf/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p9.png)

**Следующий этап — это создание модели, которая будет иметь четыре состояния и, в зависимости от состояния, будет изменяться.**

Переходим в файл _MvvmModel_. В нем создаём перечисление с именем MvvmModel. Это перечисление будет иметь четыре кейса: initial, loading, success, failure.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e5c39ac7003fc6129fe50f02571b1083/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p10.png)

Далее в перечислении MvvmModel необходимо создать структуру Model, которая будет иметь такие поля, как image с типом String и isHiden с типом Bool.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1578901349ecc3a61b95c357c41eda0f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p11.png)

**Для чего нам нужна эта структура?**

Когда мы будем получать какое-либо из состояний loading, success, failure, то в качестве аргумента будем использовать как раз эту структуру. Если забыли, как её передать, освежите в памяти модуль, в котором вы изучали перечисления.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/493fa7ad23fe08673541f2155645c7af/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p12.png)

Источник: [risovach.ru](https://risovach.ru/upload/2019/01/mem/ya-ne-uspevayu-ponyat-svetlakov-belyakov_197899296_orig_.png)

Вам необходимо передать в качестве аргумента Model непосредственно в кейсы loading(Model), success(Model), failure(Model):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a5360663a97325000dd5c44e13b4efc7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p13.png)

**В initial передавать ничего не нужно!** Так как это состояние является базовым (значением по умолчанию). 

После того, как вы создали все нужные файлы, добавьте все изображения в проект.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0fd6d551c6230ba0e18a2ba4ee002c4e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p14.png)

Когда изображения добавлены, вернитесь в класс MvvmViewModel. В классе есть методы, которые отвечают за показ того или иного изображения (showFirstImage, showSecondImage). И эти методы как-то должны запустить нужное нам действие. Давайте рассмотрим на примере метода showFirstImage.

Как вы помните из пункта №2 логики для приложения _MVVM_: при нажатии на кнопку должен появиться индикатор, после чего отобразится изображение.

Чтобы вам это сделать, необходимо:

1. Установить состояние _Loading_. Это значит, что вам необходимо использовать замыкание updateView, в котором нужно выбрать то состояние, которое нужно (в данном случае это `.loading`), а затем передать в структуру `Model` нужные значения (инициализировать структуру параметрами) — изображение с именем `Loading` и булевое значение `false`.
    
    updateView?(.loading(MvvmModel.Model(image: "Loading", isHiden: false)))
    
2. После того, как состояние установилось как .loading, индикатор появился на экране. Вам необходимо через секунду поменять состояние на _Success_, отобразить другое изображение и поменять `isHiden` на `true` (тем самым скрыв индикатор). Проще всего сымитировать такую задержку, то есть воспользоваться функцией, которая работает с многопоточностью (асинхронной).
    
3. ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/aa1dae52776542ae3f8abbaf8d21d9a6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p15.png)
    
    В качестве `deadline` установите `.now() + 1` — это означает, что нужно запустить какое-то действие через секунду от текущего времени.  
      
    Что касается `execute`, то это замыкание, которое будет выполнено после той самой задержки в одну секунду. Уже в самом замыкании поменяйте состояние на `.success` и передайте в качестве изображения файл с именем `Success` и `false` для `isHiden`:
    
    func showFirstImage() {
        updateView?(.loading(MvvmModel.Model(image: "Loading", isHiden: false)))
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
          self.updateView?(.success(MvvmModel.Model(image: "Success", isHiden: true)))
        }
      }
    

### Задание 25.2.1

Опираясь на предыдущий пример, самостоятельно добавьте логику для showSecondImage.

Ответ для самопроверки

## Скринкаст на тему: «Создаем логику для MvvmViewModel»

### **Настало время связать всю логику.**

Переходите в класс MvvmView. Тут у вас только IBOutlets и IBActions, а вам необходимо получить доступ к MvvmViewModel. Чтобы это сделать, создайте переменную viewModel, но не с типом MvvmViewModel, а с типом MvvmViewModelProtocol (привет вам из _SOLID_ — не привязывайтесь к классам, используйте абстракции).

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/259ee7a88544d2e65de8b66ddbe17df7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p16.png)

Источник: [memesmix.net](http://memesmix.net/media/created/1jb8kk.jpg)

var viewModel: MvvmViewModelProtocol!

У вас есть ссылка, теперь нужно инициализировать класс. Для этого переменной viewModel присвойте значение MvvmViewModel():

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4fb5650480b313a50b7f5cb235db92e8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p17.png)

Теперь в событиях showFirstImageBtnPressed и в showSecondImageBtnPressed нужно вызвать соответствующие методы, а где их взять? Конечно же, использовав viewModel! Так вы сможете достучаться до нужных методов.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7b9bb3aca14050e3c98e8d13bbb36cea/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p18.png)

Запустив приложение сейчас, вы увидите:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/849c11aa97e2345a58058b7d229b6c0e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p19.png)

У вас есть кнопки, готовые к «бою», но, увы... того, что есть сейчас, — недостаточно.

Код в них, верный, но из-за того, что изменение экрана происходит когда-то потом (отрисовка экрана происходит позже, чем изначальное отображение), _view_ не знает, что произошли какие-то изменения. Вот сейчас нам и предстоит научить _View_ отрисовывать новый контент в зависимости от того, что поменялось.

Первым делом создайте приватный метод update, который будет принимать тип Model, либо nil.

private func update(state: MvvmModel.Model?)

Этот метод получает на вход данные, а именно — название изображения и булевую переменную, нужную для отображения индикатора. После чего присваивает значения непосредственно в IBOutlets: imageView и activityIndicator.

private func update(state: MvvmModel.Model?) {
     guard let state = state else { return }
     imageView.image = UIImage(named: state.image)
     activityIndicator.isHidden = state.isHiden
   }

Итак, у нас есть универсальный метод, который будет раздавать нужные параметры в зависимости от того, какое состояние будет выбрано. **Помните, у нас всего четыре состояния.**

Чтобы использовать состояния, создайте еще один приватный метод с именем getState(). Именно этот метод будет знать обо всех состояниях, которые будут у вас в приложении.

И чтобы первым делом установить состояние индикатора как скрытый, добавьте в этот метод вот этот код:

private func getState() {
    self.activityIndicator.isHidden = true
  }

Теперь при вызове метода getState() индикатор будет всегда скрываться.

Идем далее.

Как понять, что у нас произошло какое-то изменение в приложении? Как раз для этого вы и создавали замыкание updateView, которое вернет новые данные, когда произойдет какое-то событие. Именно это замыкание «отслеживает» изменения.

private func getState() {
      self.activityIndicator.isHidden = true
 
      viewModel.updateView = { [weak self] data in
 
      }
    }

Именно data будет хранить в себе то состояние, которое было установлено. Если проще, то data содержит нужный контент.

А чтобы разобрать, что пришло в это замыкание в качестве data, воспользуйтесь switch и переберите все данные (это будут: initial, loading, success, failure), которые уже будут содержать нужный контент типа MvvmModel .

viewModel.updateView = { [weak self] data in
        guard let self = self else { return }
        switch data {
        case .initial:
        case .loading(let loading):
        case .success(let success): 
        case .failure(let failure):
        }
      }

Теперь у вас есть столь нужные состояния и, что более важно, — у вас есть нужный контент в зависимости от состояния, его нужно лишь передать в «правильный» метод, которым выступает update.

Вызовите метод update в каждом состоянии и передайте в него нужный контент:

 private func getState() {
    self.activityIndicator.isHidden = true
 
    viewModel.updateView = { [weak self] data in
      guard let self = self else { return }
      switch data {
      case .initial:
        self.update(state: nil)
 
      case .loading(let loading):
        self.update(state: loading)
 
      case .success(let success):
        self.update(state: success)
 
      case .failure(let failure):
        self.update(state: failure)
      }
    }
  }

Остался последний штрих — объяснить приложению, когда оно должно запускать индикатор, а когда останавливать.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c241d44a851eb68225a4fd19bab43197/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p20.png)

Источник: [risovach.ru](https://risovach.ru/upload/2016/10/mem/pff_126632688_orig_.jpg)

В нашем случае индикатор должен запускаться только при состоянии «загрузка», при всех других он должен останавливаться.

private func getState() {
    self.activityIndicator.isHidden = true
 
    viewModel.updateView = { [weak self] data in
      guard let self = self else { return }
      switch data {
      case .initial:
        self.update(state: nil)
 
      case .loading(let loading):
        self.update(state: loading)
        self.activityIndicator.startAnimating()
      case .success(let success):
        self.update(state: success)
        self.activityIndicator.stopAnimating()
      case .failure(let failure):
        self.update(state: failure)
        self.activityIndicator.stopAnimating()
      }
    }
  }

И да, этот метод getState() является самым **главным** (без него «магии» не произойдет). Не забудьте его вызвать во viewDidLoad():

override func viewDidLoad() {
    super.viewDidLoad()
 
    viewModel = MvvmViewModel()
    getState()
  }

## Скринкаст на тему: «Разбираем написанный код кода в MvvmView»

Теперь вы знаете, как работать с архитектурой _MVVM_. Настало время выполнить небольшое практическое задание.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d2b28adf07eabf86a3ad871a2fe6d450/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p21.png)

Источник: [memesmix.net](http://memesmix.net/media/created/j8uo00.jpg)

### Задание 28.2.2

Как вы можете помнить, у нас не было задействовано состояние initial, потому настал ваш час.

**Задача такая:** при запуске приложения должно подставляться дефолтное значение в imageView, при этом вы должны использовать состояние initial.  
P.S. Работа аналогична той, что мы делали вместе с вами.

Ответ для самопроверки

1. Добавьте изображение с именем _Default_ в папку асет.
2. В MvvmModel измените initial() на initial(Model).
3. В MvvmViewModelProtocol добавьте метод showDefauliImage.
4. Реализуйте в классе MvvmViewModel метод `showDefauliImage`.
5. В методе `showDefaultImage` реализуйте логику изменения состояния на 
    
    updateView?(.initial(MvvmModel.Model(image: "Default", isHiden: true)))
    
6. В методе getState() класса MvvmView в состоянии initial вызовите метод update и отключите анимацию индикатора:
    
     case .initial(let initial):
     self.update(state: initial )
     self.activityIndicator.stopAnimating()
    
7. Вызовите метод `showDefauliImage` в методе viewDidLoad():
    
    override func viewDidLoad() {
        super.viewDidLoad()
     
        viewModel = MvvmViewModel()
        getState()
        viewModel.showDefauliImage()
      }
    

**А это то, что у вас должно получиться:**

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5c70ee33880eb06b150501a73e2d6cc0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u2_p22.png)