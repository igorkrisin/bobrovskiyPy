#smile #temperature #CollectionView #application

Давайте напишем приложение, которое  будет иметь следующий функционал:

- Должны быть изображения (иконки) температуры и смайлы.
- Используя UIViewController необходимо разместить две коллекции: в одной будут отображаться иконки с температурой, а во второй — иконки-смайлы (обе коллекции с горизонтальной прокруткой).
- При нажатии на любую иконку будет открываться окно, где будет выводиться изображение той иконки, на которую вы нажали.
- 1. Создайте проект с именем _CollectionView_ (базовый _UIViewController_, как и файл _ViewController.swift_ удалять не нужно, как и класс _ViewController)_.
- сложить все картинки в assets и поставить всем св-во single scale в inspector

Начнем:


1. В _Storyboard_ добавьте _CollectionView_ на _ViewController_, разместив коллекцию в стеке, а стек расположив по центру экрана (центр по вертикали и горизонтали). Стек должен иметь отступы: слева и справа по 20. Высота одной коллекции должна быть 130.
2. В саму ячейку поместите _UIImageView_ и установите все стороны в ноль, а также ширину и высоту по 130.


	![[Screenshot 2024-01-12 at 12.11.16.png]]





3. Создайте класс Cell для работы с ячейкой, свяжите класс с ячейкой, не забыв добавить идентификатор для первой коллекции cellOne.
4. В классе Cell установите слабую ссылку с именем _temperatureImage: UIImageView_.  
	  Для установки изображения в _temperatureImage_, создайте отдельный метод `setTemperatureImage`, который будет принимать строку (имя изображения), конвертировать в _UIImage_ и присваивать значение temperatureImage.

```swift


class ViewCell: UICollectionViewCell {
    
    
    @IBOutlet weak var temperatureImage: UIImageView!
    
    func setTemperatureImage(name: String) {
        self.temperatureImage.image = UIImage(named: name)
    }
    
    
```

5. 1. Создайте еще один _ViewController_ в _Storybard_, который будет отвечать за показ изображения.  
      
    По центру контроллера разместите _UIImageView_ с высотой 260 и отступом слева и справа по 20.
    
    ![[Screenshot 2024-01-12 at 12.09.54.png]]

6. Создайте класс _ShowImageVC_ и свяжите его с только что созданным контроллером.
7. В _Storybard_ выберите контроллер _ShowImageVC_.  
      
    Перейдите во кладку _Show Identity Inspector_ и установите в поле _Storyboard ID_ идентификатор _ShowImageVC_. Он нужен для того, чтобы вы могли обратиться к классу по этому идентификатору и получить доступ к управлению, в нашем случае требуется переход из одного контроллера в другой.
8. В классе ShowImageVC:
    
    - Создайте ссылку на `UIImageView` с именем `currentImage.`
    - Создайте переменную с именем `imageName` типа _String_.
    - Создайте метод `setImageName`, который будет принимать строковое значение, затем в теле метода присвойте  аргумент к `imageName`.
    - В методе `viewDidLoad` присвойте слабой ссылке `currentImage` значение `imageName`.
    
```swift

class SmileViewController: UIViewController {

    @IBOutlet weak var currentImage: UIImageView!
    
    var imageName: String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        currentImage.image = UIImage(named: imageName)
    }
    
    func setImageName(name: String) {
        self.imageName = name
    }
}
```

9. 1. В классе `ViewController` создайте слабую ссылку на коллекцию с именем collectionViewOne и реализуйте делегат и датасорс.
	 Создайте массив arrayTemperature, в котором будут храниться имена всех изображений температуры.
	 В методе numberOfItemsInSection количество элементов равно arrayTemperature.
	 Что касается метода cellForItemAt, то вы получаете доступ к классу по идентификатору и при помощи метода setTemperatureImage устанавливаете все изображения.
	Чтобы реализовать нажатие на ячейку, вам необходимо использовать метод делегата.  
	      
	    
```swift
func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath)
```


Данный метод выступает в качестве обработчика нажатия на ячейку по индексу. Именно он будет обрабатывать логику нажатия и открывать тот _ViewController_, который нам нужен.

Для этого нужно создать экземпляр класса, к которому мы хотим получить доступ, используя идентификатор по _Storybard_ — _"Storyboard ID"_ (вы указали его ранее, как ShowImageVC). А делается это так:

```swift
guard let vc = storyboard?.instantiateViewController(withIdentifier: "ShowImageVC") as? ShowImageVC else { return }

```


Создайте переменную, которая будет хранить название изображения с именем currentSelectedImage, присвойте этой переменной значение из массива по индексу. Так как у вас есть экземпляр класса ShowImageVC, вы можете получить доступ к его методам.

В метод setImageName передайте название изображения. И последнее, что нужно сделать, — это совершить сам переход (отобразить вверху вашего экрана новый экран). Для этого используется стандартный метод:

```swift
present(vc, animated: true, completion: nil)
```


В качестве его аргументов передается контроллер, нулевое значение анимации и замыкание, но оно может быть nil.

Код всего класса OneViewvController
```swift

class OneViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {
    
    var arrayImageName: [String] = ["temp.blackGreen", "temp.darkYellow", "temp.green", "temp.lightYellow", "temp.orange", "temp.red"]
    
    @IBOutlet weak var collectionViewOne: UICollectionView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //подключаем делегаты
        collectionViewOne.dataSource = self
        collectionViewOne.delegate = self
    }

    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return arrayImageName.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        if let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath) as? ViewCell {
            cell.setTemperatureImage(name: arrayImageName[indexPath.row])
            return cell
        }
        
        return UICollectionViewCell()
       
    }
    
    //это метод делегата, который отвечает за нажатие на конкретную ячейку в хранилище по индексу он обработает логику и откроет нам VC который нам нужен
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
    //для этого нужно создать экземпляр класса к кторому мы хотим получить доступ используя идетификатор сториборда srotyboard
        guard let vc = storyboard?.instantiateViewController(withIdentifier: "ShowImageVC") as? SmileViewController else { return }
        //переменная которая хранит имя изображения
        var currentSelectedImage = arrayImageName[indexPath.row]
        //поскольку теперь есть доступ к методам SmileVC, при помощи метода присваиваем имя картинки в поле currentImage в классе SmileVC 
        vc.setImageName(name: currentSelecredImage)
        // выводим изображение на экран при помози метода present
        present(vc, animated: true, completion: nil)
    }
}
```

Для упрощения кода в контроллерах можно [[ вынести работу с DataSource и Delegate в отдельные файлы и разгрузить наш ViewController]]
