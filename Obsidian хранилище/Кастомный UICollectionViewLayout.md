#ios #UICollectionViewLayout #swift 

## **Давайте создадим новый проект с именем _CustomLayout_**

Когда создан новый проект, вам необходимо удалить _UIViewController_ из _Storyboard_, а также удалить файл _ViewController_. Они вам не понадобятся. Откройте библиотеку и перетащите в _Storyboard UICollectionViewController_, а также создайте класс с именем _CollectionViewController_ _"Cocoa touch class"_ с сабклассом  _UICollectionViewController_ и подключите этот класс к вашему контроллеру в _Storyboard_. После этого создайте класс для ячейки c именем _CollectionCell_, соедините его с ячейкой. Не забудьте указать идентификатор как _CollectionCell_ для ячейки.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3be60cded45d699b4f08b9183927c199/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p1.png)

Источник: [memesmix.net](http://memesmix.net/media/created/s4xe5j.jpg)

## Ваша «заготовка» готова.

## Скринкаст на тему: «‎Создание заготовки для кастомизации макета»

Приступаем к созданию кастомного макета.

Первое, что нужно сделать, — это создать _SWIFT_-файл с именем _CustomLayout_ (импортируйте _UIKit_), а затем и класс _CustomLayout_, который будет наследоваться от _UICollectionViewFlowLayout._

**_UICollectionViewFlowLayout_** — объект макета, который организует элементы в сетку с дополнительными представлениями верхнего и нижнего колонтитула для каждого раздела.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c7d6887d017a6644ab3365f7956e5a57/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p2.png)

  

Создаем протокол с именем _CustomLayoutDelegate_, он наследуется от _AnyObject_ для того, чтобы методы этого протокола могли реализовывать только классы.

Внутри протокола объявляем  метод, который будет принимать на вход типы `UICollectionView`, `IndexPath` и возвращать `CGSize`:

protocol CustomLayoutDelegate: AnyObject {
  func collectionView( _ collectionView: UICollectionView, heightForImageAtIndexPath indexPath: IndexPath) -> CGSize
}

Теперь давайте создадим переменную в теле класса с именем `delegateLayout` и укажем тип `CustomLayoutDelegate` (создадим делегат):

weak var delegateLayout: CustomLayoutDelegate?

Подготовительная часть закончена, теперь нужно подключить созданные классы и реализовать делегат.

Перейдите в _Storyboard_ и выберите _CollectionView_ → Откройте вкладку _Attributes inspector_ → Нажмите на выпадающую вкладку напротив _Layout_ → В списке выберите _Custom._

Вот что вы увидите:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cacc545baab8101992ef0f4432167664/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p3.png)

  

Появится поле **_Class,_** которое принимает типы UICollectionViewLayout. Впишите в это поле ваш только что созданный класс CustomLayout и нажмите _Enter_.

Это значит, приложение будет ждать от вас действий, которые скажут ему, как нужно отображать ячейки в коллекции. Теперь давайте поместим внутрь ячейки _UIImageView_ и вручную подгоним размер _UIImageView_ под размер ячейки.

Установите все констрейнты в ноль (левый/правый/низ/верх)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6808d22000b4c7a5e7ec4bd5fb92ca27/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p4.png)

  

Теперь свяжите `UIViewController` c классом `CustomCell` по слабой ссылке с именем `image`.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6511aae5278023f03f5a15dcdb89cc93/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p5.png)

  

Связи установили, теперь давайте добавим изображения в папку _Assets,_ так же, как делали ранее, — выделив все и перетащив в _Assets_ (изображения находятся в архиве, который вы скачивали в начале). А также установите _singleScale_ для всех изображений.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bd184b91f4e01d83c40cc09c6ce0455f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p6.png)

  

Переходим в класс `CollectionViewController` и создаем структуру, которая будет выступать в качестве модели для изображений с именем `StructImage`, где есть всего одно поле с именем `image` и типом `UIImage`.

struct StructImage {
  let image: UIImage
}

После создаем массив, который будет принимать объекты типа StructImage:

var arrayImages = [StructImage]()

В методе viewDidLoad вам необходимо создать переменные, которые будут преобразовывать название изображений в изображения:

let i1 = UIImage(named: "i1")!
let i2 = UIImage(named: "i2")!
let i3 = UIImage(named: "i3")!
let i4 = UIImage(named: "i4")!
let i5 = UIImage(named: "i5")!
let i6 = UIImage(named: "i6")!

Константа есть, настало время заполнить массив arrayImages этими изображениями.

Создайте побольше ;)

arrayImages.append(StructImage(image: i1))
arrayImages.append(StructImage(image: i2))
arrayImages.append(StructImage(image: i3))
arrayImages.append(StructImage(image: i4))
arrayImages.append(StructImage(image: i5))
arrayImages.append(StructImage(image: i6))
arrayImages.append(StructImage(image: i2))
arrayImages.append(StructImage(image: i4))
arrayImages.append(StructImage(image: i6))
arrayImages.append(StructImage(image: i1))
arrayImages.append(StructImage(image: i2))
arrayImages.append(StructImage(image: i5))
arrayImages.append(StructImage(image: i1))
arrayImages.append(StructImage(image: i2))
arrayImages.append(StructImage(image: i4))
arrayImages.append(StructImage(image: i3))

Последнее, что нужно добавить в этом методе, — это проверку на существование класса, который будет управлять размерностью макета:

if let layout = collectionView?.collectionViewLayout as? CustomLayout {
       	layout.delegateLayout = self
	}

Ах да, строку с регистрацией ячейки тоже нужно удалить. Вот эту:

self.collectionView!.register(UICollectionViewCell.self, forCellWithReuseIdentifier: reuseIdentifier)

С методом viewDidLoad пока закончили.

Переходим к numberOfSections и устанавливаем единицу:

override func numberOfSections(in collectionView: UICollectionView) -> Int {
    	return 1
	}

В методе numberOfItemsInSection возвращаем общее количество элементов из массива arrayImages:

override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
	return arrayImages.count
  }

Что касается cellForItemAt, то тут все тривиально: делаете проверку на существование ячейки по идентификатору и указываете, какому классу она должна соответствовать, а затем устанавливаете нужное изображение из массива, конечно же, по индексу:

override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
	let cell = collectionView.dequeueReusableCell(withReuseIdentifier: reuseIdentifier, for: indexPath) as! CollectionCell
	cell.image.image = arrayImages[indexPath.row].image
	return cell
  }

Последний штрих в этом файле — нужно **реализовать делегат**.

Создайте расширение класса `CollectionViewController` и реализуйте протокол `CustomLayoutDelegate`.

Все, что вам нужно, — это вернуть размер вашего текущего изображения по индексу. Где его взять? Ну, конечно же, из массива `arrayImages`.

И да, у каждого изображения есть свой (индивидуальный) размер ;)

extension CollectionViewController: CustomLayoutDelegate {
  func collectionView(_ collectionView: UICollectionView, heightForImageAtIndexPath indexPath:IndexPath) -> CGSize {
	return arrayImages[indexPath.item].image.size
  }
}

Теперь нужно протестировать, что все собирается, и ничего не падает.

Сейчас у вас должен быть вот такой вид:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/51fdfec610d744db5dd4e64740e7cb60/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p7.png)

  

Вот и все с этим файлом. Пора переходить к самому вкусному.

Давайте запрограммируем ячейки, чтобы они отображались как здесь:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/30cafc21d927d2e520cbd6d9907388cd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u10_p8.png)

  

код классов

```swift

import UIKit
 
class CollectionCell: UICollectionViewCell {
 
  @IBOutlet weak var image: UIImageView!
}
 
Класс CollectionView:
import UIKit
 
private let reuseIdentifier = "CollectionCell"
 
struct StructImage {
  let image: UIImage
}
 
class CollectionViewController: UICollectionViewController {
 
  var arrayImages = [StructImage]()
 
  override func viewDidLoad() {
	super.viewDidLoad()
 
	let i1 = UIImage(named: "i1")!
	let i2 = UIImage(named: "i2")!
	let i3 = UIImage(named: "i3")!
	let i4 = UIImage(named: "i4")!
	let i5 = UIImage(named: "i5")!
	let i6 = UIImage(named: "i6")!
 
	arrayImages.append(StructImage(image: i1))
	arrayImages.append(StructImage(image: i2))
	arrayImages.append(StructImage(image: i3))
	arrayImages.append(StructImage(image: i4))
	arrayImages.append(StructImage(image: i5))
	arrayImages.append(StructImage(image: i6))
	arrayImages.append(StructImage(image: i2))
	arrayImages.append(StructImage(image: i4))
	arrayImages.append(StructImage(image: i6))
	arrayImages.append(StructImage(image: i1))
	arrayImages.append(StructImage(image: i2))
	arrayImages.append(StructImage(image: i5))
	arrayImages.append(StructImage(image: i1))
	arrayImages.append(StructImage(image: i2))
	arrayImages.append(StructImage(image: i4))
	arrayImages.append(StructImage(image: i3))
 
	if let layout = collectionView?.collectionViewLayout as? CustomLayout {
  	layout.delegateLayout = self
	}
  }
 
 override func numberOfSections(in collectionView: UICollectionView) -> Int {
	return 1
  }
 
  override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
	return arrayImages.count
  }
 
  override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
	let cell = collectionView.dequeueReusableCell(withReuseIdentifier: reuseIdentifier, for: indexPath) as! CollectionCell
	cell.image.image = arrayImages[indexPath.row].image
	return cell
  }
}
 
extension CollectionViewController: CustomLayoutDelegate {
  func collectionView(_ collectionView: UICollectionView, heightForImageAtIndexPath indexPath:IndexPath) -> CGSize {
	return arrayImages[indexPath.item].image.size
  }
}
```

```swift

import UIKit
 
// Делегат, который будет реализован в нужном классе.
protocol CustomLayoutDelegate: AnyObject {
  func collectionView( _ collectionView: UICollectionView, heightForImageAtIndexPath indexPath: IndexPath) -> CGSize
}
 
// Класс, отвечающий за кастомное отображение коллекций.
class CustomLayout: UICollectionViewFlowLayout {
 
  // Подключаем делегат обязательно со слабой ссылкой.
  weak var delegateLayout: CustomLayoutDelegate?
 
  // Устанавливаем количество изображений (в колонку).
  private let numberOfColumns = 2
 
  // Устанавливаем отступ изображений по горизонтали.
  private let cellPadding: CGFloat = 2
 
  // Создаем хранилище макетов, в котором будут храниться данные объекта с размерами.
  private var cache: [UICollectionViewLayoutAttributes] = []
 
  // Создаем переменную, отвечающую за высоту контента с дефолтным значением 0.
  private var contentHeight: CGFloat = 0
 
  // Ширина изображения (вычисляется в процессе)
  private var contentWidth: CGFloat {
	guard let collectionView = collectionView else { return 0 }
	return collectionView.bounds.width
  }
 
  // Метод, возвращающий размер контента
  override var collectionViewContentSize: CGSize {
	return CGSize(width: contentWidth, height: contentHeight)
  }
 
  // Метод, отвечающий за расстановку контента по ячейкам
  override func prepare() {
 
	// Проверяем хранилище на nil
	guard cache.isEmpty, let collectionView = collectionView else { return }
 
	// Устанавливаем ширину колонки под изображения
	let columnWidth = contentWidth / CGFloat(numberOfColumns)
 
	// Создаем контейнер, который будет хранить значения смещения по оси Х
	var xOffset: [CGFloat] = []
 
	// Перебираем количество колонок в цикле и заполняем хранилище в соответствии с осью, на которой находится колонка.
	for column in 0..<numberOfColumns {
  	xOffset.append(CGFloat(column) * columnWidth)
	}
 
	// Создаем переменную, отвечающую за количество колонок по дефолту 0.
	var column = 0
 
	// Создаем контейнер, который будет хранить данные смещения по оси Y и инициализируем его, устанавливая центр по Y как 0.0 для каждой колонки.
	var yOffset: [CGFloat] = .init(repeating: 0, count: numberOfColumns)
 
	// В цикле перебираем каждый Item
	for item in 0..<collectionView.numberOfItems(inSection: 0) {
  	// Берем индекс каждого Item в конкретной секции, у нас это 0
  	let indexPath = IndexPath(item: item, section: 0)
 
  	// Создаем константу, которая будет хранить данные каждого загруженного изображения.
  	let imageSize = delegateLayout?.collectionView(collectionView, heightForImageAtIndexPath: indexPath)
 
  	// Создаем константу с шириной ячейки и присваиваем ширину колонки, в которой будет располагаться ячейка (то есть за основу берем ширину колонки).
  	let cellWidth = columnWidth
 
  	// Создаем переменную, отвечающую за высоту ячейки, и присваиваем ей вычисляемое значение, как:
  	var cellHeight = imageSize!.height * cellWidth/imageSize!.width
 
  	// Дополняем полученное ранее значение (сделано, чтобы не загромождать код выше математическими вычислениями).
  	cellHeight = cellPadding * 2 + cellHeight
 
  	// Создаем константу, которая будет хранить все вычисленные значения.
  	let frame = CGRect(x: xOffset[column],
                     	y: yOffset[column],
                     	width: cellWidth,
                     	height: cellHeight)
  	// Создаем константу, которая будет хранить отступы по оси X и Y (отступы между самими ячейками)
  	let insetFrame = frame.insetBy(dx: cellPadding, dy: cellPadding)
 
  	// Создаем константу, которая будет собирать все данные на каждую ячейку по индексу и работать с ними.
  	let attributes = UICollectionViewLayoutAttributes(forCellWith: indexPath)
 
  	// Добавляем во фрейм дополнительные отступы между ячейками.
  	attributes.frame = insetFrame
 
  	// Собираем полученные при помощи вычислений данные в хранилище.
  	cache.append(attributes)
 
  	// Сравнение величин между собой, устанавливается наибольшее из двух (если contentHeight будет больше frame.maxY, то значение будет взято из высоты контента, в противном случае из фрейма)
  	contentHeight = max(contentHeight, frame.maxY)
 
  	// Выравниваем все изображения по колонкам, учитывая их размеры и отступы
  	yOffset[column] = yOffset[column] + cellHeight
 
  	// Распределяем контент по колонкам, что в первую, что во вторую.
  	column = column < (numberOfColumns - 1) ? (column + 1) : 0
	}
  }
 
  //Переопределяем метод. Представление коллекции вызывает его после prepare (), чтобы отобразить те элементы, которые будут выводиться в конкретной ячейке.
  override func layoutAttributesForElements(in rect: CGRect) -> [UICollectionViewLayoutAttributes]? {
	var visibleLayoutAttributes = [UICollectionViewLayoutAttributes]()
 
	//	Здесь перебираем атрибуты в кэше и проверяем, пересекаются ли их фреймы с прямоугольником, предоставляемым представлением коллекции.
	for attributes in cache {
  	if attributes.frame.intersects(rect) {
 
    	//	Вы добавляете атрибуты с фреймами, которые пересекаются с этим прямоугольником, в visibleLayoutAttributes, который будет возвращаться в представление коллекции.
    	visibleLayoutAttributes.append(attributes)
  	}
	}
	return visibleLayoutAttributes
  }
 
//  Здесь извлекаем и возвращаем из кэша атрибуты макета, которые соответствуют запрошенному indexPath.
  override func layoutAttributesForItem(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes? {
	return cache[indexPath.item]
  }
}
```