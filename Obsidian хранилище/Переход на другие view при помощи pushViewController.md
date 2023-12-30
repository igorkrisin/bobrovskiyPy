#pushViewController #ios #swift #uiNAvigationController 

[[Переход на другое view кодом через  NavVC]]
[[Tab Bar Controller создание через Story board]]

Ранее в этом модуле мы уже добавляли _NavigationController_ к нашему _ViewController_.

Напомню, что сделать это можно на сториборде:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fb4bdefda257b856ea638027e9b15c22/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p3.png)

Добавьте кнопку на основной _ViewController_. Создайте второй _ViewController_, не забудьте присвоить ему _storyboard ID._ 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/df4264eb2b7a41cb8e8abcfdc7470950/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p4.png)

Итак, для начала создадим _IBAction_. Добавим код для перехода на _SecondViewController_. Ранее было рассмотрено, как это сделать. Напомню, что для этого мы должны использовать метод _pushViewController_. И не забудьте указать на сториборде _storyboard ID_. В общем, тут ничего нового. Всё это мы проделывали ранее.

 ```swift
import UIKit
 
class ViewController: UIViewController {


    override func viewDidLoad() {
        super.viewDidLoad()
    }
 
    @IBAction func openSecondModule(_ sender: Any) {
    
        guard let viewController = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "SecondViewController") as? SecondViewController else { return }
        guard let navigator = navigationController else { return }
        navigator.pushViewController(viewController, animated: true)
    }
}
```

