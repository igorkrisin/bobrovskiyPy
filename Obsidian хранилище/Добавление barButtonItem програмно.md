#barButtonItem #ios #uiNAvigationController 

[[Добавляем обычный Button  програмно через код]]

На _SecondViewController’e_ предлагаю программно добавить **_barButtonItem_** — это кнопка, которая находится в _navigationBar’e:_ слева или справа. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9e7e217005c29310dcd3c7133cc524e8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p5.png)

  ```swift

import UIKit
 
class SecondViewController: UIViewController {

    override func viewDidLoad() {
    super.viewDidLoad()
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .edit,

            target: self,
            action: #selector(edit))

    }
 
    @objc func edit() {
        print("Edit is done")
    }
    ```
    Начнём с barButtonSystemItem — здесь мы можем выбрать разные системные варианты.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a89808d09a6f6caa716c7e6e3da17bfb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p6.png)

_**target**_ — объект, получающий сообщение о действии. Указываем в качестве объекта «себя», то есть _self_.

**_action_** — @objc метод. При нажатии на элемент будет срабатывать метод, который вы укажете. Нужно указать только его название.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/876e9a123bd0e1ff300f0c3e95cdbca3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p7.png)

Далее пишем:

@objc func nameFunc() {
 
/// Код метода
 
}

Также _barButtonItem_ можно добавить на сториборде.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/96e7f8998ae8196119c6bae1a668178c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p8.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/35c469eb15d8bd4e4c4f627a94405a17/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p9.png)

И ему также можно выставить различные параметры — свойства _UIBarButtonItem_, к которым мы можем обратиться.

 ```swift

@IBOutlet weak var rightBarButtonItem: UIBarButtonItem!
 
    override func viewDidLoad() {
        super.viewDidLoad()
        rightBarButtonItem.title = "Settings"
    }
    ```

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e9585be27765a295fc0fedb6b2ec1aeb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p10.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/b427966c5e959ca8cb195016e42ebee2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p11.png)

Если нужно добавить какой-то _action_, который будет срабатывать при нажатии, не забудьте перед этим указать _target_, как _self_.
```swift

    override func viewDidLoad() {
        super.viewDidLoad()
        rightBarButtonItem.title = "Settings"
        rightBarButtonItem.target = self
        rightBarButtonItem.action = #selector(edit)
    }
 
    @objc func edit() {
        print("Settings is open")
    }
 ```

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7587b6733e3b1a1ce9f4565ba57210ef/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p12.png)

А еще мы можем указать стиль нашего _barButtonItem’a_. Давайте укажем `.done`. Как видите, в таком случае текст будет жирным =)
```swift

rightBarButtonItem.style = .done
```

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/88db0cccaed9e3fbb660b19bf05daaab/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p13.png)

Также мы можем указывать _title_ у нашего _navigationItem_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6028ab589ba4a72097cd5c5b66ebfd62/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p14.png)

**_Navigation item_** — это выделенная синим область.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d1b809a55dc58b3291b1afced0f0b5a4/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p15.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/026d754e0018ac48628fbf4f950232d2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u5_p16.png)