---
tags:
  - swift
  - uikit
  - "#uiNAvigationController"
  - "#кодом"
  - "#создать"
---
[[создание NavigationControllera кодом]]
[[Жизненный цикл View controller (life cycle)]]

[[Переход на другие view при помощи segue]]] ]
[[Переход на другие view при помощи present() и show()]]
[[Переход на другие view при помощи pushViewController]]


Что бы создать переход через NavigationVC необходимо внутри класса <mark style="background: #FF5582A6;">ScenceDelegate </mark>прописать следующее внутри метода <mark style="background: #FF5582A6;">scene</mark> 


```swift
 guard let windowScene = (scene as? UIWindowScene) else { return }
  // после этой строки в методе scence пишем:


	 let window = UIWindow(windowScene: windowScene)

        let navController = UINavigationController()

        let viewController = ViewController()

        navController.viewControllers = [viewController]

        window.rootViewController = navController

        self.window = window

        window.makeKeyAndVisible()
		self.window?.backgroundColor = UIColor.white // устанавливаем цвет экрана белым
```
```

```

Если вы удалили Main storyboard появится [[Ошибка Could not find a storyboard named 'Main' in bundle NSBundle - не может найти сториборд после его удаления]] по ссылке как ее исправить!

Создаем еще одну сущность <mark style="background: #FF5582A6;">SecondViewController</mark> на который будет переходить главный VC

добавляем кнопку на первый VC  и прописываем для нее параметры и нажаттие определяем переход в addTarget 

```swift
import UIKit

class ViewController: UIViewController {
    var moveButton = UIButton()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Todo"
        
        self.moveButton = UIButton(type: .system)
        self.moveButton.setTitle("SVC", for: .normal)
        self.moveButton.sizeToFit()
        self.moveButton.center = self.view.center
        self.moveButton.addTarget(self, action: #selector(moveToSecondVC), for: .touchUpInside)
        self.view.addSubview(self.moveButton)
    }

//метод перехода на другой VC
    @objc func moveToSecondVC(parametr: Any) {
        let secondVC = SecondViewController()
        self.navigationController?.pushViewController(secondVC, animated: true)
    }
}
```

напишем во SVC удаление самого SVC без нажатия кнопки через 3 секунды:

```swift
import UIKit

class SecondViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        self.title = "SVC"
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(true)
        self.perform(#selector(goBack), with: nil, afterDelay: 3.0)
    }
    
    
    @objc func goBack() {
        //Одним методом убрать контроллер
        //self.navigationController?.popViewController(animated: true)
        
        //Подробно удаление контроллера
        //Получаем текущий массив контроллеров
        var currentControllerArray = self.navigationController?.viewControllers
        
        //Удаляем из массива последний контроллер
        currentControllerArray?.removeLast()
        
        //Присвоить наш результат нашему контролеру
        if let newController = currentControllerArray {
            self.navigationController?.viewControllers = newController
        }
    }
    
    

}
```