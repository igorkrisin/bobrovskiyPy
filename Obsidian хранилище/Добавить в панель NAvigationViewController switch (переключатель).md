#ios #button #uiNAvigationController #barButtonItem 


Как кодом добавить NavViewController смотрим [[Добавляем barButtonItem и картинку в шапку NavigationController]]

Сначала создаем switch а потом присваиваем его одной из кнопок в панели навигации.

```swift
import UIKit

class ViewController: UIViewController {

   
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //создание switch 
        
      let simpleSwitch = UISwitch()
        simpleSwitch.isOn = true
        simpleSwitch.addTarget(self, action: #selector(switchIsChamge(param:)), for: .valueChanged)


		//присваиваем switch кнопке
        self.navigationItem.leftBarButtonItem = UIBarButtonItem(customView: simpleSwitch)
        
    }
    
    @objc func switchIsChamge(param: UISwitch) {
        if param.isOn {
            print("switch is On")
        } else {
            print("switch is Off")
        }
    }
    
}
```