#swift #ios #viper #architect 

Архитектура _VIPER_ **не** самая главная/крутая/правильная в линейке архитектур, про которые мы вам рассказали. Это просто еще одна архитектура, которая применяется в зависимости от требований проекта.

_У каждого свой VIPER ©_

## **Что это такое?**

**_VIPER_** — это еще один архитектурный подход, позволяющий вести разработку под _iOS,_ основанный на идеях «Дядюшки Боба» ([Роберт Мартин](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D1%82%D0%B8%D0%BD,_%D0%A0%D0%BE%D0%B1%D0%B5%D1%80%D1%82_(%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80))) [чистая архитектура](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8e7e09dd47cc7504375a92e990502a1e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p1.png)

## **Какие слои есть в VIPER?**

В этой архитектуре присутствует аж **пять** слоев. В отличие от _MVC, MVP_ и _MVVM_ он выбивается из линейки _MV(x)_. У _VIPER_ каждая буква — это и есть отдельный слой:

**V**

  
— это **_View_** или _**ViewController**,_ он отвечает за **отображение данных для пользователя**, оповещая о каких-либо изменениях непосредственно _P (Presenter)_, **_View_ данные не запрашивает**, он получает данные от _Presenter_.

**I**

  
— это **_Interactor,_** который **содержит абсолютно всю бизнес-логику**. Интерактор во многих случаях работает с сервисами (_Service_ — это какие-то ресурсы, предоставляющие те или иные данные).

**P**

  
— это _**Presentor**_, он получает сигналы о действиях пользователя (от _View_) и отправляет запросы в _Interactor_ и _router_, а также получает данные от _Interactor_.

**E**

  
— это _**Entity**_, **объекты**, которые содержат какие-то данные, **аналог модели**.

**R**

  
— это _**Router**_, он отвечает за навигацию в приложении.

- Еще есть **_Assambly_**, которая выполняет сборку и проставляет зависимости (знает про то, какие данные должны передаться во _View_ при инициализации того или иного экрана).
- Также часто для получения каких-то данных используют _**Services**_ (не всегда, но часто).  
    Например, сервис погоды, который предоставляет вам данные о погоде, а дальше вы что-то с ними делаете.

Вот как выглядит схема архитектуры с сервисами:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e48846aa653375d1dcee5f0ac97ae1d4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p2.png)

А вот как **без** них:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ae8a395993d2abff9ddf183093baa140/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p3.png)

Теперь давайте посмотрим как, кто и с кем взаимодействует в этой архитектуре на примере взаимодействия с сервисами:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/19e508eaae3ee8c6e9a067dff2b1fba6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p4.png)

**Как понять, что на этой схеме?**

- Есть _Assambly,_ который отвечает за сборку всего модуля и проставления зависимостей.
- Стрелками проставлены зависимости, их направление указывает на ссылки конкретных объектов (например, стрелка от _Entity_ идет в _Service._ Это значит, что сервис знает о сущности _Entity_ и умеет взаимодействовать с ней, но _Entity_ ничего не знает ни про какой сервис).
- Пунктирная стрелка означает, что зависимость необязательна (но может быть проставлена в случае необходимости).


## Скринкаст на тему: «Разбираем схему VIPER‎»

## **Что помогает решать VIPER?**

- Обширное покрытие юнит-тестами такого слоя, как _Presenter_.
- Разбитие крупных классов на более мелкие, с четкими границами ответственности.

Также нужно иметь в виду, что _VIPER_ — это не «жесткие правила», а скорее «рекомендации» по тому, как нужно строить архитектуру. Эта архитектура является сложной для понимания и без «подготовки» лучше не начинать проект. Сначала нужно изучить три предыдущие архитектуры, и только потом постепенно погружаться в _VIPER._

**Плюсы _VIPER:_**

1. Тестируемость слоя _Presenter_.
2. Независимость слоев друг от друга дает возможность поддерживать, разрабатывать и переиспользовать написанный код.
3. Добавление в проект новой функциональности стало ещё проще.

**Минусы _VIPER:_**

1. Огромное количество классов в приложении (создавая новый модуль, вы плодите много классов), даже создавая простой экран.  
      
    К примеру, вы хотите создать один экран. Один экран — это один модуль, но не всегда, часто бывает так, что на одном экране может быть несколько модулей. Это называется _сложный экран_, и чтобы его спроектировать, нужно съесть не одну собаку.
    
    
    Если этот экран состоит из одного модуля, то вам нужно создать **пять** классов, **пять** протоколов (и это абсолютный минимум), а еще есть сервисы, если они вам понадобятся. Что в свою очередь увеличивает время разработки в начале проекта.
    
2. Не всегда получается подружить _UIKit_ с этим паттерном, приходится изобретать велосипеды.
3. Очень мало информации по этой архитектуре, то, как делать «правильно» и «**не** правильно»

## **Когда нужно/можно использовать архитектуру VIPER?**

Когда нужно обеспечить покрытие проекта _unit_-тестами (так, как вы будете использовать протоколы, а значит завязываться на абстракцию). Если у вас в команде есть больше одного человека, то вы можете работать параллельно, не мешая друг другу.

Из-за того, что эта архитектура предполагает использование большого количество протоколов (абстракций), то при необходимости вы можете достаточно легко/просто изменять/добавлять новую функциональность или изменять/добавлять новые модули.

## **Как это работает в коде?**

Чтобы понять, как работать с _VIPER_, необходимо очень много кодить.

Давайте напишем мини приложение на примере схемы **без сервисов** _(Viper without services)_, тем самым приблизимся к пониманию того, что же такое _VIPER._

### ТЗ приложения

- У вас есть три экрана (прямо, как в сказке про царя и троих сыновей ☺).
- Первый экран отвечает за логин в приложении. При нажатии на кнопку _Login_ осуществляется переход на второй экран, на котором расположены две кнопки _Log out_ и _Show photo._
- Кликая на _Log out,_ вы возвращаетесь на первый экран.
- Кликая на _Show photo_, вас перемещает на третий экран, в котором отображается некое фото и есть кнопка _Done,_ при нажатии на которую вас перебрасывает на второй экран.


Звучит просто, не правда ли? Учитывая тот факт, что это задание можно выполнить вообще не прибегая к написанию кода, чисто используя _UI-_элементы.

Но мы с вами разбираемся, как работать с _VIPER_. Так что приготовьтесь: мозг и нервная система могут не выдерживать нагрузки от _VIPER_ :)


**Приступаем.**

1. Создайте новый проект и назовите его _Viper._
2. В проекте создайте папку _Modules._ Именно в этой папке будут храниться наши модули: _Login,_ _Home,_ _Photo_ (создайте эти папки).
3. Следом создайте папку _AppScene-Delegates_ и переместите туда два файла: _AppDelegate_ и _SceneDelegate._
4. Также создайте папку Storyboards и переместите туда _Main.storyboard_ и _LaunchScreen.storyboard._

Все это вы проделали для того, чтобы уменьшить нагрузку на глаза, и поэтому распределили файлы по папкам !!!

Ах да, у вас есть файл _ViewController,_ который сгенерирован самим _Xcode,_ поэтому можете его удалить, он нам не понадобится. В итоге вот, что у вас должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ab22e8749a238cd6a001f44eedbe0a75/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p11.png)

**Теперь давайте поработаем с _Main.storyboard._**

Вам необходимо создать еще два _ViewController’a_ и разместить их в линию. Почему два, спросите вы? Да потому, что один у вас уже есть, воспользуемся им тоже. Тут дело вкусовщины, разместите, как хотите.

Далее.

На первом экране:

- Разместите кнопку по центру с размерами W — 130, H — 80, текст кнопки удалите.

На втором экране:

- Разместите две кнопки одну под другой, обе по центру:
    
    - Сверху кнопка с размерами W — 130, H—80, отступ от центра — -100.
    - Снизу кнопка с размерами W — 200, H — 80, отступ от центра — 100.
    
- Текст кнопки удалите.

На третьем экране:

- Разместите кнопку с текстом Done (размер текста 27), цвет белый.
- Размер W — 63, H — 45, отступ слева и сверху 20
- А также _UIimageView_, которое необходимо растянуть по всему экрану.

В нашем примере мы будем работать с переходами по «**Сеге**» (идентификатор перехода с первого на второй экран _"LoginToHome"_, со второго на третий _"HomeToPhoto"_). Пробросив все переходы, вот что должно получиться (как пробрасывать переходы, посмотрите видео ниже):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/661e6edbc2b6bd0a1ecd6c2111187000/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p12.png)

Почему мы не установили все нужные изображения?  
Потому что установкой всех изображений займемся в коде далее.

## Скринкаст на тему: «Устанавливаем UI для экранов‎»

С экранами пока закончили.

**Переходим непосредственно к созданию модулей. И начнем с модуля _Login_.**

**Важно!** Все файлы, которые будут располагаться в конкретном модуле, должны иметь префикс этого модуля, затем все остальное. К примеру, если мы работаем над модулем _Login_, то файлы должны иметь такой вид: _LoginView_, _Logininteractor_ и так далее.

Создайте пять файлов по _VIPER_ для модуля _Login_ (файл _LoginView_ — это `_cocoa touch class_` с сабклассом `_UIViewController_`), также не забудьте создать `_LoginAssambly,_` который будет отвечать за сборку модуля.

Вот, что должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f093764c4e47a28dffade7283fb091df/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p13.png)

Проделайте то же самое и для _Home_ (файл _HomeView_ — это _cocoa touch class_ с сабклассом _UIViewController)_ и _Photo (PhotoView_ — это _cocoa touch class_ с сабклассом _UIViewController):_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4860f240adf110c78d7efffc6a21646e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p14.png)

Со структурой файлов разобрались и создали все необходимые для работы этого приложения.

Следующим шагом необходимо связать все (три) контроллера с классами: первый контроллер с классом _LoginView,_ второй — с _HomeView,_ третий — с _PhotoView._

Также перетащите все изображения (предоставленные вам) в папку _Assets:_ 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0ee8e2482a51d5e0331fa56929af4de9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p16.png)

Вот теперь подготовка закончена, можно приступать к самому «вкусному» — к «кодингу».

Возможно, вы забыли, но для каждого слоя нужно создать как класс, так и протокол, который будет «закрывать» этот класс. Это значит, что вся работа будет вестись через протоколы (привет, _SOLID_!)

Создайте для каждого файла свой протокол и свой класс соответственно:

- Модуль _Login:_  
      
    
    Class LoginView — protocol LoginViewProtocol: class
    Class LogInInteractor — protocol LoginInteractorProtocol: class
    Class LoginPresenter — protocol LoginPresenterProtocol: class
    Struct LoginEntity — protocol LoginEntityProtocol (так как LoginEntity — это структура, то после протокола не нужно ставить class)
    Class LoginRouter — protocol LoginRouterProtocol: class
    Class LoginAssambly — protocol LoginAssamblyProtocol: class
    
- Модуль _Home:_  
      
    
    Class HomeView — protocol HomeViewProtocol: class
    Class HomeInteractor — protocol HomeInteractorProtocol: class
    Class HomePresenter — protocol HomePresenterProtocol: class
    Struct HomeEntity — protocol HomeEntityProtocol (так как LoginEntity — это структура, то после протокола не нужно ставить class)
    Class HomeRouter — protocol HomeRouterProtocol: class
    Class HomeAssambly — protocol HomeAssamblyProtocol: class
    

Что касается модуля _Photo_, то это будет уже ваше практическое задание…


А вы думали, что останетесь без практики? Ну уж нет! :)  
Но не об этом сейчас.

**Обратите внимание!** Естественно, каждый класс должен реализовывать свой протокол.

Что касается `_LoginView,_` то вам нужно связать один элемент — кнопку. Создадим `_Outlet_` этой кнопки с именем `_loginBtn_` в классе `_LoginView,_` а также создадим событие при нажатии на эту кнопку.

@IBOutlet weak var loginBtn: UIButton!
@IBAction func loginBtnPressed(_ sender: Any)

Также не забудьте создать константу `segueIdentifier`, которая будет хранить имя идентификатора для «сеги», с помощью которого мы будем осуществлять переход.

let segueIdentifier = "LoginToHome"

## Скринкаст на тему: «Создаем протоколы для модуля Login‎»

Вам необходимо проделать ту же самую работу и для модели _Home_ (создать классы и протоколы), а также установите ссылки на кнопки:

Outlets — logOutBtn и showPhotoBtn
Actions — logOutBtnPressed и showPhotoBtnPressed

@IBOutlet weak var logOutBtn: UIButton!
@IBOutlet weak var showPhotoBtn: UIButton!

@IBAction func logOutBtnPressed(_ sender: Any)
@IBAction func showPhotoBtnPressed(_ sender: Any)

**Возвращаемся к модулю _Login_ и классу _LoginView._**

Первое, что вы сделаете, — это создадите связь между `_Presenter_` и `_View,_` создав переменную типа LoginPresenterProtocol. Это нужно для того, чтобы сообщить _Presenter_ о том, что произошло какое-то изменение на экране.

var presenter: LoginPresenterProtocol!

Чтобы все связи были проброшены по файлам, конечно же, необходимо объявить экземпляр класса assambly:

var assambly: LoginAssamblyProtocol = LoginAssambly()

Он нужен для того, чтобы вы могли сделать сборку модуля.

Теперь давайте разберемся с протоколом LoginViewProtocol, для чего он нужен и что с ним делать. Этот протокол будет иметь один метод, который будет устанавливать изображение для нашей кнопки. Помните? Мы не устанавливали изображение в контроллере. И называется этот метод setLoginbuttonImage, на вход принимает изображение.

Так как мы унаследованы от этого протокола, то класс LoginView должен его реализовать:

extension LoginView: LoginViewProtocol {
  func setLoginbuttonImage(image: UIImage) {
    loginBtn.setBackgroundImage(image, for: .normal)
  }
}

В этом методе мы устанавливаем изображение нашей кнопки. Вы, наверное, подумали: «Что за ерунда? Этот класс сам же и реализовывает метод, а откуда он берет это изображение?».  
Резонный вопрос! Но не забывайте, что у нас есть `_Presenter,_` который как раз нужен для этих вещей.

Переходим в `_LoginPresenter Protocol_` и создаем метод, который и будет отвечать за установку всего нужного контента (изображений):

func configureView()

Соответственно вам придется реализовать этот метод в классе `LoginPresenter`.

Вспоминайте схему: `View` имеет ссылку на `Presenter`, мы уже ее создали в классе `LoginView`, НО также `Presenter` имеет ссылку на `View`.

Так давайте ее и создадим в классе `LoginPresenter`:

weak var view: LoginViewProtocol?

Она нам нужна для того, чтобы получить доступ к тому самому методу `setLoginbuttonImage`, который отдает некое изображение для `Outlet`.

func configureView() {
    view?.setLoginbuttonImage(image: ????????)
  }

Вы получили доступ к этому методу, через ссылку view, теперь нужно откуда-то получить это самое изображение (это там, где сейчас проставлены вопросики).

Как вы помните из схемы, за всю бизнес логику отвечает `Interactor`, а он в свою очередь знает об `Entity`.

Это значит, что вам нужно создать ссылку на `Interactor` в `Presentor` для того, чтобы получить доступ к методам и свойствам `Interactor`.

var interactor: LoginInteractorProtocol!

Ссылка есть, теперь нужно создать свойство, которое мы будем вызывать для того, чтобы получить ту самую картинку.

Переходим в `LoginInteractorProtocol` и создаем свойство, которое знает, где брать нужное изображение: 

var login: UIImage { get }

Реализуем это свойство в классе `LoginInteractor`, оно должно получать изображение непосредственно от `LoginEntity`. Эта сущность знает о том, где лежит эта картинка.

Значит вам нужно создать экземпляр на эту сущность, чтобы получить доступ к ее полям:

let loginEntity: LoginEntityProtocol = LoginEntity()

Для самой сущность нужно установить поле, которое будет знать о картинке _"Login":_

protocol LoginEntityProtocol {
  var logInImageForButton: UIImage { get }
}
 
struct LoginEntity: LoginEntityProtocol {
  var logInImageForButton: UIImage { get { return  imageLiteral(resourceName: "Login")}}
}

Теперь, когда вы знаете, где брать картинку, присвойте эту картинку свойству `login` из класса `LoginInteractor` через геттер:

Для этого получите доступ к сущности и просто возьмите эту картинку.

var login: UIImage {
    get { return loginEntity.logInImageForButton }
  }

Все готово, чтобы презентер смог установить эту самую картинку в своем методе `configureView` вместо вопросов. Теперь получаем доступ через ссылку `Interactor` к полю `login`:

func configureView() {
    view?.setLoginbuttonImage(image: interactor.login)
  }

Метод `configureView` готов, теперь его можно вызвать в `viewDidLoad` класса `ViewLogin`

## Скринкаст на тему: «Путь установки изображения "_Login"_‎»

Теперь давайте перейдем с файл `LoginAssambly`, там у нас есть класс `LoginAssambly` и протокол `LoginAssamblyProtocol`. 

Так как класс `LoginAssambly` отвечает за сборку всего модуля, нам нужно иметь все компоненты, но пока у нас их нет. Давайте создадим в этом классе и в протоколе соответственно метод configure, принимающий текущий контроллер, который мы передадим. 

func configure(view: LoginView)

Мы вернемся к нему позже. А пока вызовем этот метод в viewDidLoad и передадим self  в качестве контроллера (то есть сам текущий контроллер) 

assambly.configure(view: self)

С классом `LoginAssambly` пока закончим, вернемся в класс LoginView. У нас есть кнопка, по нажатию на которую должен осуществляться переход на другой экран. В этом нам, опять же, поможет презентер.

Вы помните, что презентер также должен иметь ссылку и на Router, а Router – это тот класс, который отвечает за навигацию.

Давайте выполним работу по этапам: 

1. В протоколе LoginPresenterProtocol создайте метод loginPressed/
2. Реализуйте этот метод в классе LoginPresenter.
3. Вызовите этот метод в событии loginBtnPressed

@IBAction func loginBtnPressed(_ sender: Any) {
    presenter.loginPressed()
  }

Вот, как должен выглядеть весь ваш класс LoginView:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2edbdbd9d30a1c79a577d2e9f16a698b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p18.png)

Теперь переходим в класс LoginPresenter и реализуем логику для метода loginPressed()

Для этого нам нужно получить доступ к самому LoginRouterProtocol. Чтобы это сделать, создайте ссылку  router c типом  LoginRouterProtocol. Когда у вас есть ссылка, перейдите в протокол LoginRouterProtocol для того, чтобы создать нужный нам метод openHomePage, отвечающий за навигацию.

func openHomePage()

Реализуем этот метод в классе LoginRouter.

func openHomePage() {
   }

Теперь, когда наш presenter знает, что можно работать с навигацией, соответственно, он может вызвать метод «openHomePage», отвечающий за навигацию

Переходим в LoginPresenter и в методе loginPressed вызываем метод навигации.

func loginPressed() {
    router.openHomePage()
  }

**Важно!** Presenter абсолютно не знает про то, что делает router, он знает лишь о его методах или полях.

Перейдите в файл LoginRouter. У вас уже есть нужный метод, который будет выполнять навигацию, но у вас еще нет самой логики.

Опять вспоминайте схему VIPER – router имеет ссылку на View!

А значит, вам нужно создать эту ссылку по примеру, как в Presenter

weak var viewController: LoginView?

Теперь в методе openHomePage можно «запилить» нужную нам логику перемещения на другой экран при помощи performSegue. В качестве идентификатора мы будем использовать тот, что создали в самом начале segueIdentifier

func openHomePage() {
    viewController?.performSegue(withIdentifier: viewController!.segueIdentifier, sender: nil)
  } 

Мы практически закончили с login модулем.

Осталось самое главное – доделать метод configure класса LoginAssambly.

Переходим в него.

Теперь давайте немного поразмышляем… Так как метод configure отвечает за сборку и проброску связей, значит нам нужно устанавливать те самые связи между классами (вспоминайте стрелочки из схемы VIPER), следовательно, в эти классы (LoginPresenter, LoginInteractor, LoginRouter) нужно передавать эти самые ссылки. Для этого необходимо использовать инициализаторы.

Не стоит пугаться, давайте создадим все инициализаторы. Всего потребуется три инициализатора для Presenter, Interactor, Router (все их создаем в протоколах!)

LoginPresenter - init(_ view: LoginViewProtocol) 
LoginInteractor - init(_ presenter: LoginPresenterProtocol)
LoginRouter - init (_ viewController: LoginView)
 

И естественно реализуем их, присваивая ссылкам данные из инициализаторов: 

 required init(_ view: LoginViewProtocol) {
    self.view = view
  }

LoginInteractor:

Создайте ссылку на Presenter (из схемы VIPER та самая пунктирная стрелочка, в нашем приложении эта ссылка не участвует в коде, но знать, как ее создавать, вы должны)

weak var presenter: LoginPresenterProtocol?

Сам инициализатор для LoginInteractor

required init(_ presenter: LoginPresenterProtocol) {
    self.presenter = presenter
  }

LoginRouter:

required init(_ viewController: LoginView) {
    self.viewController = viewController
  }

Все инициализаторы есть, а значит, мы все сможем увязать в методе configure.

Переходим именно туда.

Здесь нужно создать экземпляры всех классов, у которых есть инициализаторы, а это Presenter, Interactor, Router, и передать в качестве входных параметров следующее:

для Presenter – это view

let presenter = LoginPresenter(view)

для Interactor – это  только что созданный presenter

let interactor = LoginInteractor(presenter)

А для router – это тоже view

let router = LoginRouter(view)

Далее нужно передать в Strong-ссылки наши данные 

У самой view есть ссылка presenter

view.presenter = presenter

Затем у presenter есть сильные ссылки на роутер и интерактор:

presenter.interactor = interactor
presenter.router = router

Вот теперь модуль Login закончен.


Следующим к реализации у нас будет модуль Home. Реализация этого модуля похожа на реализацию модуля Login. У вас уже есть все классы и протоколы, а также есть Actions и Outlents. Давайте начнем наш «путь», также с HomeView.

### Задание 25.3.1

Самостоятельно напишите протокол с методами setLogOutImage и setShowPhoto для этого класса и реализуйте его.

Ответ для самопроверки

### Задание 25.3.2

Самостоятельно, используя знания из предыдущего «Login» модуля, сконфигурируйте HomePresenter. Единственное отличие заключается в том, что вам необходимо отобразить две кнопки, а не одну, соответственно, нужно установить логику для двух кнопок.

Что касается названия методов роутера, то это closeCurrentController и showSecondController.

А имена HomeEntity – loginImage и showPhotoImage

Ответ для самопроверки

У вас теперь есть Presenter с методами и связями во все стороны - Interactor, Router, View.


View и Presenter уже реализованы, давайте реализуем Interactor.

Вы уже знаете, что у Interactor есть свойства loginImage и showPhotoImage, которые получают изображения. А значит, у Interactor есть сущность, которая отдает ему эти изображения.

Перейдите в Interactor и создайте экземпляр структуры, по которой вы будете получать изображения:

let homeEntity: HomeEntityProtocol = HomeEntity()

Соответственно, в сущности homeEntity уже должны быть эти изображения: logout и showImage.

Протокол и класс сущности похожи на LoginEntity: 

protocol HomeEntityProtocol {
  var logoutImage: UIImage { get }
  var showPhotoImage: UIImage { get }
}
 
struct HomeEntity: HomeEntityProtocol {
  var logoutImage: UIImage { get { return  imageLiteral(resourceName: "logout")}}
  var showPhotoImage: UIImage { get { return  imageLiteral(resourceName: "showImage")}}
}
 

Также необходимо реализовать инициализатор из протокола HomeInteractorProtocol для того, чтобы потом извне передать Presenter.

required init(_ presenter: HomePresenter) {
    self.presenter = presenter
  }

А раз есть Presenter, значит должна быть и слабая ссылка на него.

weak var presenter: HomePresenterProtocol?

Вот как должен выглядеть файл HomeInteractor:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f2a475bc47de98111ff5bb1f35473c26/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p23.png)

Осталось реализовать Router и Assambly

Давайте перейдем к Router.

Протокол роутера должен иметь два метода: closeCurrentController и showSecondController, а также инициализатор

protocol HomeRouterProtocol {
  init(_ viewController: HomeView)
  func closeCurrentController()
  func showSecondController()
}

Соответственно, вы должны реализовать этот протокол в классе HomeRouter.

Что касается метода closeCurrentController, то он должен сворачивать текущий экран и возвращаться на предыдущий.

Для этого можно использовать метод Dismiss

func closeCurrentController() {
    viewController?.dismiss(animated: true, completion: nil)
  }

А метод showSecondController наоборот должен перекинуть вас на новый экран PhotoView, для этого нужно использовать сегу и ее идентификатор.

func showSecondController() {
    viewController?.performSegue(withIdentifier: viewController!.segueIdentifire, sender: nil)
  }

Вот, как должен выглядеть класс HomeRouter:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/32f56cea7dbe48815c254bd469e810ef/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p24.png)

Остался касс Assambly.

В нем нет ничего нового, вы все также создаете три экземпляра класса (HomePresenter, HomeInteractor, HomeRouter),  в которые передаете нужные параметры, а затем присваиваете сильным ссылкам данные.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5f64b29ea793e41234cc26caa69920b6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m28_u3_p25.png)

## Скринкаст на тему: «Рассматриваем HomeView»

## Скринкаст на тему: «Рассматриваем HomePresenter»

## Скринкаст на тему: «Рассматриваем HomeInteractor и HomeEntity»

## Скринкаст на тему: «Рассматриваем HomeRouter и HomeAssambly»

### Задание 25.3.3

В качестве вашего практического задания вам необходимо реализовать третий модуль Photo. Для этого вы должны использовать полученные знания из предыдущих модулей Home и Login.

Нейминг всех методов остается за вами.

В скринкасте ниже посмотрите, как должно работать приложение, третий экран.

## Скринкаст на тему: «Презентация приложения, третий экран‎»

Ответ для самопроверки

Как вы уже поняли, _VIPER —_ достаточно сложная архитектура, желательно к ней подходить со знанием предыдущих трех.

А еще сложность заключается в том, что _VIPER_ у каждого свой (мы писали об этом в самом начале изучения этого архитектурного паттерна). Это значит, что каждый проект может реализовывать эту архитектуру так, как захочет.