#swift #uikit #webKit 
## **Что такое WKWebView?**

**_WKWebView_** — это класс, предоставляющий возможность создавать экран, в котором будет отображаться некий контент.

К примеру, в вашем приложении есть ссылка «[https://www.apple.com](https://www.apple.com/)», ведущая на некий внешний ресурс, при клике на неё вы можете открыть этот ресурс в отдельном окне своего приложения, то есть не выходя из приложения.

Сегодня вы научитесь с этим работать, а также напишете свое мини-приложение с использованием _WKWebView_. Давайте посмотрим как добавлять _WKWebView_ и работать с этим классом.

Для этого вам необходимо:

1. Создать новый проект _MyWebView_.
2. Открыть сториборд и выбрать существующий _ViewController_.
3. Открыть библиотеку с UI элементами и начать вводить _web…_

Вы должны увидеть следующую «картину»:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/124fecf1a06de98c89869fbd71e5548e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p1.png)

**Важно!** Непосредственно _WebView_ является **_deprecated_**, это значит, что вы можете использовать данный элемент, а вот в _AppStore_ выложить не сможете.

Конкретно этот элемент мы разбирать не будем, так как он постепенно выходит из использования и в ближайшем будущем его уберут вовсе.

**_WebView_** или **_UI_****_WebView_  — это класс, который отвечает за создание все того же представления, которое встраивает веб-контент в ваше приложение.

_Apple_ решил усовершенствовать и перенести _UIWebView_, создав отдельную библиотеку со своими плюшками.Если у вас есть желание, вы можете ознакомиться с этим классом самостоятельно. Сможете ли вы с этим работать? Да, но в _AppStore_ выложить ничего не получится. _WebKit View_ обладает всеми возможностями, что и _UIWebView_, и даже больше.

Вам необходимо выбрать _WebKit View_ — это тот элемент, с которым вы будете работать в дальнейшем.

### Продолжаем дальше!

Выберите _WebKitView_ и перетащите во _ViewController_, далее растяните его на весь экран (установите констрейнты в 0):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/18e428090b95fd925845849079fa98dd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p2.png)

После этого свяжите слабой ссылкой `WebKitView` с классом `ViewController`. Слабую ссылку назовите `webKitView`.

```swift
 @IBOutlet weak var webKitView: WKWebView!
```


Также для работы с _WKWebView_ необходимо импортировать саму библиотеку _WebKit_ в тот класс, в котором вы работаете, а именно во ViewController.

```swift
import WebKit
```


Отлично, библиотеку подключили, теперь нужно взять чей-то адрес, например, _https://www.apple.com_, и создать для него константу с именем stringUrl.

```swift
let stringUrl = «https://www.apple.com»
```


Следующий шаг — это преобразовать строку в _URL_. Это делается достаточно просто: создаёте константу с именем url и передаёте строковое значение stringUrl в качестве аргумента в метод _URL,_ а метод преобразует строку в _URL_-адрес и возвращает его.

```swift
let url = URL(string: stringUrl)!
```


Когда константа с _URL_ готова, нужно создать запрос при помощи класса URLRequest, в который мы должны передать константу с _URL_ в качестве аргумента.

```swift
let request = URLRequest(url: url)
```


Получившийся запрос необходимо передать в загрузчик, который проделает необходимую работу под «капотом» и выведет изображение на экран девайса.

**Как это делается?**

Берёте ссылку `webKitView` и через точку получаете доступ к методам этого класса (а их там не мало). Давайте на минутку заглянем в класс WKWebView:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/902add3375c2704afe030bd2304facec/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p3.png)

Это малый список того, что там есть. Конкретно сейчас нас интересует метод с именем load, который принимает в качестве аргумента значение URLRequest.

Получите доступ к этому методу и передайте ваш request:

```swift
webKitView.load(request)
```


Вот и все, теперь можно попробовать запустить и протестировать то, что у вас получилось.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e3a270e820f2c2db10f542ecb17a3ba7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p4.png)

Источник: [zakon-auto.ru](https://zakon-auto.ru/i/articles/znaki/znak-kirpich-zapreshchaiushchii-proezd-1.jpg)

К сожалению, это пока не все, при запуске вы увидите вот такую ошибку в консоли:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/82f54b22b6fd788596c9b7513ba08b58/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p5.png)

Здесь приложение говорит, что у вас есть класс WKWebView, но приложение не может получить данные из библиотеки, потому что не может найти библиотеку WebKit.

Дело в том, что для библиотек (не всех) мало прописать строку import WebKit , нужно еще добавить эту библиотеку в вашем **таргете** (таргет — это когда вы нажимаете на самую верхнюю вкладку в иерархии папок в меню справа):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/28424f0b5ae5dacf0cccdd9be37579d4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p7.png)

Когда нажали на «+», вы увидите выпадающее окно, введите название библиотеки _Webkit_, выберите и жмите _Add_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f2a06d9f9ff4d808232411cf8f8a9cd3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p8.png)

Все, библиотека добавлена. Можно снова запустить приложение на симуляторе.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/68704cf4311a2891d07e596b72a4cea4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p9.png)

## Скринкаст на тему: «Как добавлять библиотеку WebKit‎»

Теперь вы знаете, как можно выводить в приложении некий контент, используя _URL_-адрес. Как вы понимаете, это не полный список возможностей, которые дает использование _WKWebView_.


Давайте немного попрактикуемся и напишем небольшое приложение. А чтобы было интереснее писать, мы сымитируем работу некоего мессенджера. 

Суть приложения такова: ваш друг увидел, что фирма _Apple_ выпустила новый _MacBook Air_, и не смог сдержаться, чтобы не поделиться этой новостью с вами в некоем _FakeMessanger’e_. Друг скинул вам ссылку с очень интересным контентом. Вам необходимо перейти по этой ссылке и ознакомиться с контентом (ощутите себя разработчиком, который «пилит» новую «фичу» для _FakeMessanger’а_)


Вот как будет выглядеть _FakeMessanger_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2dd200437805faf2a1bc5e3d37bb2e81/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p12.png)

А вот как будет выглядеть экран с открытой ссылкой:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/43bd2438c0fe5dad5dddd69c09f78542/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p13.png)

Ну как, уже чешутся лапки покодить? Тогда погнали!

Первым делом создайте новый проект назовите его _FakeMessanger._

Из только что созданного проекта удалять ничего не нужно, будем использовать то, что есть, и дописывать новое. Перетащите все предложенные вам изображения в папку _Assets_, установив их как _Single Scale._

Следующим шагом необходимо определить элементы _UI_, которые будут присутствовать на экранах (напомним, всего их два).

  
Первый экран:

Сначала посмотрим, какие контейнеры нужно установить (под контейнерами подразумеваются элементы, на которые вы будете накладывать другие элементы), в нашем случае это будет _View_.

Всего их будет три штуки на экране:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2c374f3a1749f7a36bba559dc04dfbdb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p15.png)

С _View_ разобрались, теперь то, что будет в них.

- В верхней _View_:
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/f5c44a782ed784b36690767d5ffde253/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p16.png)
    
- В средней _View_:
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1dc5c3756cdf9acf99f530fc7b8eeb3e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p17.png)
    
- В нижней _View_:
    
    ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/126005b6ff8538f1e78e12b657473827/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p18.png)
    

  
Теперь давайте посмотрим на второй экран, начнем так же с контейнеров.

Здесь картина немного отличная от первого экрана:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ea6d59e7de215e89e07b8b5fed96f42c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p19.png)

Далее давайте рассмотрим каждый «контейнер» по порядку, начнем с верхнего:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ade85c94cec0cc1ae09524e11815f2b7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p20.png)

У вас будет два элемента: первый — это кнопка, а второй — лейбл, который будет появляться, когда идет подгрузка страницы.

Средний контейнер, на котором будет размещаться только один элемент, — это _Activity Indicator View._ Данный элемент служит для того, чтобы дать понять пользователю, что контент загружается. Вот как он выглядит:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/955ed2bd4e65299dc20cbaca96a02573/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p21.png)

Далее мы с ним поработаем.

И третий элемент _ToolBar_ — это элемент _UI_, на котором будут размещаться три кнопки (вы научитесь добавлять его непосредственно в _ToolBar_). _Bar Button Item_ в данном случае — это эквивалент _UIButton_ за одним исключением: эти элементы добавляются в _ToolBar_ или _NavigationBar_. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/255f5d49e92c2b1d33db357e919e5496/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p22.png)

Теперь вы знаете, какие элементы будут на двух экранах.

Давайте сделаем их вместе!


После того как вы создали два экрана, необходимо связать все элементы, которые будут выполнять действия.

## **Что нужно добавить с первого экрана?**

С первого экрана нужно добавить непосредственно только одну кнопку, которая имитирует нажатие по ссылке.

Откройте сториборд и ассистент, перейдите на _ViewController_ и создайте событие для кнопки с именем `showWebView`:

```swift
@IBAction func showWebView(_ sender: Any) {
```


При нажатии на кнопку должен осуществиться переход на другой экран. Это можно осуществить, к примеру, если у вас есть идентификатор класса StorybordID.

Чтобы установить идентификатор:  
Перейдите в сториборд → Выберите _ViewController_ второго экрана → Перейдите во вкладку _identity Inspector_ и в строке _StorybordID_ установите идентификатор _ShowWebView_.

Теперь можно написать логику по переходу на другой экран.

Создаете защищенную константу showVC, которая получает доступ к нужному контроллеру по идентификатору ShowWebView. После этого происходит переход на нужный экран при помощи стандартного метода present:
str
```swift
guard let showVC = storyboard?.instantiateViewController(identifier: "ShowWebView") else { return }
 
present(showVC, animated: true, completion: nil)
```


Перед началом тестирования вам необходимо создать класс, который вы свяжете с контроллером второго экрана. Создайте класс с именем ShowWebView и свяжите со вторым экраном.

После этого запустите приложение и протестируйте кнопку перехода:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6067c53b743088ffbe47e0a51bbaf242/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p23.png)

Приложение запустилось и переход был протестирован удачно.

**Сейчас при нажатии на кнопку открывается экран, который вы можете свернуть, свайпнув его вниз.** Нам этот эффект **не нужен**, поэтому сделайте следующее: в сториборде выберите контроллер вашего второго экрана и во вкладке _Attributes inspector_ нажмите на выпадающее поле _Presentation_, там выберите _Full Screen:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/00bd84083fc2515e4212eb41b94bbaf1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p24.png)

Протестируйте снова. Вы должны увидеть, что теперь свайпом свернуть это окно не получится:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/32873143478ad698aa700ca4907e3e54/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p25.png)

**Изменим еще пару моментов.** Мы не задали цвет для вью: как для первого экрана, так и для второго. Задайте для них такой же цвет, как и для _ToolBar (F8F7F8)._

Выглядит круто, не так ли? :)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5816e50aa735bbce6d466fd02302f24d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p26.png)     ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bd49354d12f26bbcd8cc3a44b9569f09/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p27.png)

Можем двигаться дальше.

С первым экраном и его логикой разобрались. Переходим ко второму, именно в нем будет вся основная работа, так как нам необходимо изучить новый элемент — _WebView_.

Давайте начнем с того, что свяжем все элементы _UI_ с кодом. И начнем мы с самого верхнего _View_, в котором есть кнопка и лэйбл. 

Ваши действия: создайте _Action_ на кнопку с именем `doneBtnPressed`, при нажатии на которую будет происходить закрытие этого экрана и возврат на предыдущий при помощи метода `dismiss`.

```swift
 @IBAction func doneBtnPressed(_ sender: Any) {
    dismiss(animated: true, completion: nil)
  }
```


Что касается _UILabel_, то для него нужна слабая ссылка с именем `textLabel`. В дальнейшем будем работать с этим лэйблом.

```swift
@IBOutlet weak var textLabel: UILabel!
```


Переходим к среднему элементу. Здесь у вас есть _WebView_ и _Activity Indicator_, также создайте две слабые ссылки с именами: для первого — `webView`, для второго — `indicator`.

Не забудьте импортировать _WebKit_!

Переходим к третьему и последнему блоку.

Нужно создать _Actions_ для трех _Items_ с именами (слева направо) backBtnPressed, forwardBtnPressed, refreshBtnPressed.

А также создайте слабые ссылки для этих кнопок с именами (слева направо) backBtn, forwardBtn, refreshBtn.

Вот, что должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/23a2abd5d118c47883d2eecc18eca736/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p29.png)

Заготовка под кодирование готова.

Давайте немного подумаем над логикой того, как должно работать приложение.

Пользователь нажимает на ссылку и переходит на экран с _WebView_. Происходит загрузка контента и наш индикатор начинает вращаться посредине экрана, а также в верхней части экрана мы должны увидеть текст _"Loading…"_. После того, как контент загружен, мы должны уметь перемещаться по страницам как вперед, так и назад, при помощи _Items_ (кнопки вперед и назад), а также должны уметь перезагружать ту страницу, на которой находимся (это тоже _item_).

Для начала давайте скроем тот _UI_, который нам сейчас не нужен, а именно — _Activity Indicator_ в методе ViewDidLoad:
```swift
indicator.isHidden = true
```


Следующим шагом будет подключение делегата, который будет отвечать за навигацию (у этого протокола есть методы, отслеживающие, когда контент начал загружаться и когда закончил). Подключение его всегда **обязательно**, иначе ваш код работать не будет.

```swift
webView.navigationDelegate = self
```


А также вам потребуется реализовать протокол, который нужен для работы с делегатом выше. 

```swift
class ShowWebView: UIViewController, WKNavigationDelegate
```


Далее вам необходимо создать запрос для того, чтобы отобразить страницу по ссылке и передать его в метод, отвечающий за загрузку страницы (вы делали это ранее в этом модуле).

```swift
let urlSrintg = "https://www.apple.com/ru/macbook-air/"
guard let url = URL(string: urlSrintg) else { return }
let request = URLRequest(url: url)
webView.load(request)
```


Теперь, когда у вас есть страница, нужно реализовать переходы: назад, вперед, а также обновление страницы.

Чтобы понять, можно ли двигаться вперед, используем проверку:
```swift
if webView.canGoBack {
      webView.goBack()
    }
```


Чтобы понять, можно ли двигаться назад, используем проверку:

```swift
if webView.canGoForward {
      webView.goForward()
    }
```


Что касается перезагрузки текущей страницы, используйте метод:
```swift
webView.reload()
```


С первой частью логики, отвечающей за навигацию по страницам, закончили. Теперь нужно «запилить» логику, которая будет делать наши кнопки (вперед/назад) активными, если пользователь совершал переходы.

А также необходимо добавить логику по отображению индикаторов.

Сначала давайте напишем метод enableBtnIfCanGoBack, который будет отвечать за отображение кнопки назад. Здесь как раз пригодятся слабые ссылки:
```swift
private func enableBtnIfCanGoBack(){
    if webView.canGoBack {
      backBtn.isEnabled = true
    }else{
      backBtn.isEnabled = false
    }
  }  
```


Второй метод enableBtnIfCanGoForward будет отвечать за отображение кнопки вперед:
```swift
private func enableBtnIfCanGoForward() {
    if webView.canGoForward {
      forwardBtn.isEnabled = true
    }else{
      forwardBtn.isEnabled = false
    }
  }
```


И последний метод workIndicator будет отвечать за отображение индикаторов _Action indicator & UIlabel_, которые будут появляться/скрываться, если контент загружается:
```swift
private func workIndicator(isAnimated: Bool) {
     if isAnimated {
       self.indicator.isHidden = false
       self.indicator.startAnimating()
       textLabel.text = "Loading..."
     }else{
       self.indicator.isHidden = true
       self.indicator.stopAnimating()
       textLabel.text = ""
     }
   }
```


Теперь у вас есть методы, которые нужно где-то вызывать, чтобы задуманная логика начала работать.


Для этого вам и пригодится делегат протокола WKNavigationDelegate! Перейдите внутрь протокола WKNavigationDelegate:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/97915f0063c26b192a042fc2ae089b8c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p31.png)

Эти два метода вам нужны, чтобы запустить код в том порядке, в котором требуется согласно логике.

Используйте метод webView didFinish, чтобы вызвать в нем три метода, написанных ранее. Этот метод вызовет все методы по порядку и скроет ненужные данные.

```swift
func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
    workIndicator(isAnimated: false)
    enableBtnIfCanGoBack()
    enableBtnIfCanGoForward()
  }
```


Чтобы отобразить индикаторы при старте загрузки контента, воспользуйтесь методом webView didStartProvisionalNavigation:

```swift
func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
    workIndicator(isAnimated: true)
  }
```


![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/feb5f7629f2b0759f8a8eeac14687c23/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_26_u3_p32.png)

После добавления логики запустите приложение и «пройдитесь» по всему функционалу, который вы добавили. Всё прекрасно работает.


С _WKWebView_ закончили. Теперь вы обладаете базовыми знаниями, которые помогут вам создавать свои экраны для того, чтобы пользователь подольше оставался в приложении.

Но функциональность _WKWebView_ не ограничивается этим, как вы видели, в этой библиотеке содержится очень много классов, с которыми вы, возможно, столкнётесь в реальной разработке.