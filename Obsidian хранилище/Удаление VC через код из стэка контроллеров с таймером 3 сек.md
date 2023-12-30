#ios #pop #viewController 

В классе удаляемого контроллера вызывем viewDidAppear  и метод perform

```swift 
import UIKit

class SecondViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        self.perform(#selector(goBack), with: nil, afterDelay: 3.0)// таймер 3 сек
    }
    
    @objc func goBack() {
        //self.navigationController?.popViewController(animated: true)//это не для новичков
        // для новичков подробно
        // получаем массив контроллеров
        var currentControllerArray = self.navigationController?.viewControllers
        
        //удаляем послелний контроллер
        currentControllerArray?.removeLast()
        
        //присвоим
        if let newCintroller = currentControllerArray {
            self.navigationController?.viewControllers = newCintroller
        }
    }
    ```
для [[создания NavigationControllera кодом ]] переходим в sceneDelegate