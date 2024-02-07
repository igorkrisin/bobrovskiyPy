#UICollectionView #swift #UICollectionView_Item_or_Cell

Как и в табличном представлении, в коллекциях вы тоже можете создавать ячейки, в которых будут отображаться ваши данные. Как вы уже успели заметить, коллекции внешне не похожи на табличное представление, но если посмотреть шире, то у них действительно много общего. К примеру, они вызывают _Datasource_ для управления данными и _Delegate_ для управления действиями. Как и в табличные ячейки, в коллекции вы сможете добавить любые элементы _UI_.

Есть действительно важное отличие _Item_ из коллекции — они могут скроллиться как по вертикали, так и по горизонтали. Опять же, яркий пример: откройте _AppStore_ и попробуйте проскочить элементы вправо и влево.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/dae0353f8ced7c2b9ab3921213d6ab96/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p1.png)

  

Выглядит действительно стильно.

Настала пора узнать, как создавать ячейки. Далее мы будем называть их **_Item_**, чтобы исключить путаницу в ваших головах и не проводить параллели между табличным представлением.

Итак... 

## **_Item_. Что это вообще такое?**

Это контейнер, который принимает различные элементы _UI_ и структурировано выводит для пользователя.

Количество _Item_ неограниченно, вы можете создать их столько, сколько необходимо

## **Как с этим работать?**

Помните, вы в самом начале модуля создавали _UICollectionViewController_ («коробочное» решение)? Так вот, на нем уже есть один _Item_, который мы и заполним вместе.

Откройте _Storyboard_ и выберите _MyCollectionViewController_.

Не забудьте включить галочку **_Is initial view controller_**, когда выберите _MyCollectionViewController!_

Видите квадрат, обозначенный тонкой серой линией в левом верхнем углу?

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2cb17252d906ac83b596f924170080e2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p2.png)

  

Это и есть **_Item_** (который и нужно кастомизировать).

Выберите этот квадрат. Вы можете увеличить его или уменьшить, потянув за край (его местоположение будет меняться в зависимости от размеров). Выделите его и потяните за правый нижний угол.

Увеличим его и сделаем 200 х 220. Как вы видите, не так-то просто «поймать» нужный размер. Перейдите во вкладку _Show the size inspector_, как раз здесь вы можете установить нужный размер.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/02bb646061d06389d9d0bf1ada7ec161/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p3.png)

  

Супер, где найти размеры и как их установить, разобрались.

Давайте поместим в этот контейнер _UIImageView_ и _UILabel_.

Откройте _Library_ и перетащите в _Item_ _UIImageView_, установите констрейнты:  
лево = 0,  
право = 0,  
вверх = 0,  
высота = 200

А также перетащите из библиотеки _UILabel_ и установите констрейнты для него:  
лево = 0,  
право = 0,  
низ = 0,  
высота = 20

## Отличная работа!

Вот, что у вас должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/575937fe6599db170f2d13a929f1735f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p4.png)

  

Теперь нужно связать эти элементы _UI_ c кодом, но прежде чем вы это сможете сделать, вы должны создать класс, который будет отвечать за _Item_ (создайте _Cocoa touch class_ с именем _ItemCell_ c сабклассом _UICollectionViewCell_), после необходимо установить этот класс в качестве класса _Item_. И установить идентификатор для этой ячейки.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bab0e6546d5715ed10a3ee09a5b1fd6f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p5.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/22fe838a600c746d4808209330713d50/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p6.png)

  

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/435bcd56f9a007aaffb089a4f5a66272/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p7.png)

  

Теперь вы готовы связать элементы, которые содержатся в _Item_ с кодом (с классом _ItemCell_). Для этого пройдите в _Storyboard_, откройте ассистент (чтобы видеть код и _Storyboard_ на одном экране), затем выберите любой из двух элементов (_UILabel_ или _UIImageView_). У вас должен открыться нужный класс (_ItemCell_), если этого не произошло, тогда в верхнем углу экрана выберите нужный класс вручную и перейдите в него.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5533f1fde7828b717d46297d89f3406f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p8.png)

  

Теперь у вас перед глазами есть _Storyboard_ и класс _ItemCell_.

Выберите _UIImageView_ и создайте ссылку на этот элемент в коде, перетащив _UIImageView_ в класс _ItemCell_ с именем _ImageView_. Также поступим и с _UILabel_ — выделим и перетащим в класс с именем _labelText_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c990350f3116221af723dddff75fe3da/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p9.png)

  

Итак, ячейка с нужными элементами готова, связи есть, что дальше? Теперь необходимо объяснить классу _MyCollectionVC_, как работать с этим _Item_.

Откройте  класс ViewController (либо в другом классе соосвествующему протоколам UIViewController, UICollectionViewDelegate, UICollectionViewDataSource), видите там строку?
```swift
private let reuseIdentifier = "Cell"
```


Замените её на эту (ранее вы указали идентификатор ячейки, как _ItemCell_):
```swift
private let reuseIdentifier = "ItemCell"
```


В методе _ViewDidLoad_ необходимо удалить следующую строку (если такая имеется):

```swift
self.collectionView!.register(UICollectionViewCell.self, forCellWithReuseIdentifier: reuseIdentifier)
```


Она нам не нужна, так как мы явно создали класс и установили все связи для _Item._

В методе `func numberOfSections(in collectionView: UICollectionView) -> Int` установите количество секций — единица.

А сейчас в методе `func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int` надо указать количество элементов, но как его посчитать?

## Давайте немного порассуждаем.

Вы только что создали _Item_, в котором два элемента _UI_ — это _UILabel_ и _UIImageView_ (любой _Item_ всегда считается за один элемент, неважно, сколько вы вложили в него _UI_). Чтобы вам указать верное значение в методе `numberOfItemsInSection`, нужно создать абстрактный контейнер для этих элементов.

Давайте сделаем это при помощи _структуры_.

Создайте структуру с именем _StructItem_, в которой будет два свойства: изображение и текст для нашей ячейки.

## **Для чего мы создаем этот контейнер?**

Так как мы не знаем, сколько у нас должно быть элементов в коллекции (а в реальной разработке в 99% случаев бывает именно так), мы создаем этот абстрактный контейнер для того, чтобы переиспользовать его столько раз, сколько потребуется.

Вот как он выглядит:

```swift
struct  StructItem {
  let image: String
  let text: String
}
```


Считайте эту структуру за один элемент _Item._ Также создайте массив, который будет хранить элементы с типом _StructItem_:

```swift
var arrayItems = [StructItem]()
```


Отлично, теперь мы можем воспользоваться методом:
```swift
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int
```


И вернуть в качестве значения количество элементов в массиве `arrayItems`.

```swift
return arrayItems.count
```


Сейчас в нем нет элементов, а значит, вам необходимо добавить их. Это можно сделать в следующем методе:

```swift
override func viewDidLoad()
```


Добавьте в массив три элемента, в каждом элементе по два параметра (название изображения и описание изображения):

```swift
arrayItems.append(StructItem(image: "temp.darkYellow", text: "Dark yellow color"))
arrayItems.append(StructItem(image: "temp.orange", text: "Orange color"))
arrayItems.append(StructItem(image: "temp.red", text: "Red color"))
```


После этих манипуляций в вашем массиве arrayItems будут храниться три значения.

С массивом и данными разобрались.

## **Откуда взялись названия изображений?**

Эти изображения будут доступны для вас, всего их шесть. Данные изображения необходимо поместить в папку под названием _Assets.xcassets_.

Выделите все изображения и перетащите в папку _Assets._


Далее вы должны использовать метод:

```swift
collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell
```


**Чтобы сказать приложению:**

1. Какой класс взять за основу в качестве _Item._
2. Откуда взять данные для _Item._
3. Какие данные _Item_ должен отобразить

Для этого создайте в теле метода «безопасную» константу, которая будет искать класс в приложении, соответствующий индексу:

```swift
if let cell = collectionView.dequeueReusableCell(withReuseIdentifier: reuseIdentifier, for: indexPath) as? ItemCell {}
```


Эта константа будет существовать, если идентификатор класса будет соответствовать классу _ItemCell_, в противном случае вернется `nil`, и вам нужно будет вернуть пустую ячейку.

Если константа не nil, тогда получите доступ к свойствам этого класса и присвойте им значения, соответствующие типам из массива arrayItems. Вот как это делается:

```swift
override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
	if let cell = collectionView.dequeueReusableCell(withReuseIdentifier: reuseIdentifier, for: indexPath) as? ItemCell {
  	cell.imageVIew.image = UIImage(named: arrayItems[indexPath.row].image)
  	cell.labelText.text = arrayItems[indexPath.row].text
  	return cell
	}
	return UICollectionViewCell()
  }

```

Чтобы наглядно разобраться, как это все было реализовано, посмотрите обучающее видео по процессу создания _Item_:


Можно запустить приложение. Вот что вы увидите:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2bba085be1de324f24bfdc8fe51d228c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u7_p11.png)

  

Данное изображение не соответствует тому, что мы с вами планировали увидеть, когда растягивали _Item_ 200/220. Дело в том, что добавленные 2 элемента «лежат» на View, которую нельзя настраивать.

Чтобы размеры, задуманные нами, отображались правильно, необходимо добавить кастомные вью из библиотеки, где впоследствии и необходимо расположить UI элементы.

## Скринкаст на тему: «‎Исправление отображения ячеек»

Давайте резюмируем:

1. Добавляем новое _View_ во _ContentView_.
2. Устанавливаем _Constraint View_ в (0, 0, 0, 0) а также высоту 240 и ширину 200.
3. Переносим _UIImageView_ и _UILabel_ внутрь _View._
4. Устанавливаем _Constraint_ для _UIImageView_ (лево — 0, право — 0, верх — 0) высота — 200.
5. Устанавливаем _Constraint_ для _UILabel_ (лево — 0, право — 0, низ — 0) высота — 40.

На этом создание ячейки закончено.

Следующим этапом будет [[создание кастомной ячейки (item) UICollectionView]] 