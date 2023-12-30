#ios #uiNAvigationController #pushViewController 

[[Добавление barButtonItem програмно]]
[[Удаление VC через код из стэка контроллеров с таймером 3 сек]]

```swift
class ViewController: UIViewController {
 
    override func viewDidLoad() {
        super.viewDidLoad()
    }
 //создаем экшн в первом VC 
    @IBAction func openSecondModule(_ sender: Any) {
    //обращаемся к сториборду и инициализируем через него VC указывая то нужен переход на SVC через название Storyboard ID
        guard let viewController = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "SecondViewController") as? SecondViewController else { return }
        // cоздаем NavVC и пушим в него view
        guard let navigator = navigationController else { return }
        navigator.pushViewController(viewController, animated: true)
    }
}
```

Созадаем SVC прописываем в у него Storyboard ID, а так же создаем класс  SVC и указываем его в поле class - identify inspector'a