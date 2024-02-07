#делегат #delegate #ios 

1. Сoздаем протокол <mark style="background: #ABF7F7A6;">делегата</mark>

```swift
// 1 указывае в нем функционал делегата
protocol Delegate: AnyObject {
    func moveData(data: String)
}

```

2. Объявляем <mark style="background: #ABF7F7A6;">делегат</mark> в том классе из которого будем брать инфу для делегирования. То есть в том классе откуда надо забрать данные (например) или получить для передачи другую инфу
3. Вызываем метод делегата

```swift

class SecondViewController: UIViewController {

    //2 Объявляем как optional поскольку инициализировать пока его нечем
    weak var delegate: Delegate?
    
    var mainVC = MainViewController()
    
    @IBOutlet weak var seconLabel: UILabel!
    @IBOutlet weak var secondTextfield: UITextField!
    
    var userName = "1"
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        seconLabel.text = userName
    }
    
    
    
    
    @IBAction func saveTecxtfieldData(_ sender: Any) {
        guard let secViewContrText = secondTextfield.text else { return }
        guard !secViewContrText.isEmpty else { return }
        // 3 Вызывем метод делегата передав ему информацию необходимого типа
        delegate?.moveData(data: secViewContrText)
        //закрывем контроллер после надатия на кнопку save
        navigationController?.popViewController(animated: true)
        
    }
    
    ```
4.  Пишем метод делегата (реализация в классе где применяем делегат - там где передаем информацию)
5. Присваиваем полю делегата ссылку на класс в котором его выполняем, по сути делегируем тут ему это действие

```swift


class MainViewController: UIViewController {
    
    var svc: SecondViewController?
    
    @IBOutlet weak var labelMainVC: UILabel!
    
    var nameUser: String = "Jhon"
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toSecVC",
            let vc = segue.destination as? SecondViewController {
            print("prepare")
            vc.userName = nameUser
            //5 передаем ему делегирование ссылку на тот класс который его использует - self ссылка на самого себя
            vc.delegate = self
            
        }
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func toSecondVCButton(_ sender: Any) {
        performSegue(withIdentifier: "toSecVC", sender: self)
    }
    

}

//4 пишем реализацию метода делегата
extension MainViewController: Delegate {
    func moveData(data: String) {
        print("extension")
        labelMainVC.text = data
    }
    
    
}


```