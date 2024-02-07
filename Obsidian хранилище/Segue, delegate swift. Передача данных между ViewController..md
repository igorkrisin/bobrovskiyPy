#delegate #swift #segue 

Создадим тестовый проект такого вида

![[Screenshot 2024-01-15 at 12.58.43.png]]

Соединяем контроллеры при помощи segue как показано ан картинке
![[Screenshot 2024-01-15 at 12.26.52.png]]
И в выпадающем меню выбираем <mark style="background: #FFB86CA6;">show</mark>. Связь создана, теперь дадим ID segue - это нужно для того что бы можно было к нему обратиться и попросить что-то сделать при переходе по этому segue.

![[Screenshot 2024-01-15 at 12.29.57.png]]

Добавляем следующие элементы на VC и IBOutlet к ним:


![[Screenshot 2024-01-15 at 12.34.02.png]]

Для того что бы подцепить segue, пишем в IBAction кнопки метод perform, указывая ID установленный в storyboard:

```swift
@IBAction func moveSecondView(_ sender: Any) {
        performSegue(withIdentifier: "toSecondView", sender: self)
    }```

Теперь выведем данные с VС на SVC с кнопки  <mark style="background: #BBFABBA6;">@IBAction func moveSecondView</mark>, создадим переменную во VС для хранения имени, которое будем передавать. Поскольку мне нужно передать информацию в Outlet SVC, мне нужно создать экземпляр класса SVC в классе VC.

- Внутри SVC создаем переменную посредник, что бы она могла проинициализироваться в момент загрузки view и передать свои данные secondLabel. А во ViewDidLoad присваиваем ее значение secondLabel. Это нужно так как в момент вызова в SVC аутлетов VC они еще не проинициализированы.

```swift
var nameLabel = ""
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        secondLabel.text = nameLabel
    }```

- Для начала создадим метод <mark style="background: #FFB86CA6;">prepare(for segue: UIStoryboard ....)</mark> в нем проверим какой идентификатор  сработал и в какой VC мы переходим и кастим его до типа SecondViewController, что бы обратиться к методам SVC. И внутри этого условия обращаемся к объекту SVC и устанавливаем secondLabel из класса SVC в нужное значение.

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        //destination - Это свойство содержит контроллер представления,
        //содержимое которого должно отображаться в конце перехода.
        if segue.identifier == "toSecondView", let vc = segue.destination as? SecondViewController {
            vc.nameLabel = userName
        }
    }```

Теперь попробуем передать информацию "назад" из SVC во VC через textLAbel.

- Создадим метод изменяющий label
```swift
func setTitle(name: String) {
        self.label.text = name
    }```

Теперь что бы этот метод можно было реализовать при передаче значений из другого view - реализуем делегат
- Создаем протокол Delegate во VC c методом 
- Выполняем этот делегат, и выполняет его тот класс <mark style="background: #ABF7F7A6;">который делегирует функции</mark> - создаем extension и вызываем метод делегата
- Создаем делегат в делегируемом классе SVC (переменную с типом делегата)
- Выполняем метод делегата  в этом классе (SVC) при нажатии устанавливаем при помощи delegate через который мы можем обратиться к методам VC присваиваем лэйблу значение textField, a так же закроем контроллер при помощи pop 
- В VC создаем ссылке на delegate через свойство SVC (vc)


**Код Класса <mark style="background: #FFB86CA6;">VC</mark>:**

```swift
import UIKit

protocol delegateView: AnyObject {
    func setlabelText(name: String)
}

class ViewController: UIViewController {

    @IBOutlet weak var label: UILabel!
    
    let userName: String = "Jhon"
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        //destination - Это свойство содержит контроллер представления,
        //содержимое которого должно отображаться в конце перехода.
        if segue.identifier == "toSecondView", let vc = segue.destination as? SecondViewController {
            vc.nameLabel = userName
            vc.myDelegate = self
        }
    }

    @IBAction func moveSecondView(_ sender: Any) {
        performSegue(withIdentifier: "toSecondView", sender: self)
    }
    
    func setTitle(name: String) {
        self.label.text = name
    }
    
}


extension ViewController: delegateView {
    func setlabelText(name: String) {
        self.label.text = name
    }
}
```

**Код Класса <mark style="background: #FFB86CA6;">SVC</mark>:

```swift
import UIKit

class SecondViewController: UIViewController {
    weak var myDelegate: delegateView?
    
    @IBOutlet weak var textField: UITextField!
    
    @IBOutlet weak var secondLabel: UILabel!
    var nameLabel = ""
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        secondLabel.text = nameLabel
        // Do any additional setup after loading the view.
    }
    

    @IBAction func button(_ sender: Any) {
        myDelegate?.setlabelText(name: textField.text ?? "")
        navigationController?.popViewController(animated: true)
    }
}
```










