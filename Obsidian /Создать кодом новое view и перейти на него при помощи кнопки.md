#ios #storyboard #view #prepare

Для того, чтобы передать данные на другой экран программно, не используя segue, можно воспользоваться следующим кодом. Но для начала создайте кнопку на _ViewController_ и добавьте ее _IBAction_.

[[Переход на другие view при помощи present() и show()]]

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0170e25b11e44c85acc8298bdbea780c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p13.png)



```swift 

@IBAction func pushSecondVC(_ sender: Any) {
        let destination = storyboard?.instantiateViewController(withIdentifier: "SecondViewController") as! SecondViewController
        destination.emodji = ""
        navigationController?.pushViewController(destination, animated: true)
    }
    
    ```

`instantiateViewController(withIdentifier:)` создает _view controlle_r со специальным идентификатором и инициализирует его данными из сториборда.

Теперь, обращаясь к константе `destination`, нам становятся доступны свойства и методы _SecondViewController’a._

Теперь нам нужно сделать переход на другой экран. Важно учитывать то, что у нас есть _navigationController_, а значит, необходимо использовать следующий метод:

`navigationController?.pushViewController(destination, animated: true)`

Теперь, если вы запустите приложение, оно упадет. Причина этому очень проста: в коде вы указали идентификатор сториборда (`withIdentifier: "SecondViewController"`), а на самом сториборде нет.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2ebd92406116a3483606910567cbc773/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p14.png)

После того, как вы укажете _storyboard ID,_ вы можете запустить приложение и увидеть, что оно работает =)

 
import UIKit
 
class ViewController: UIViewController {
 ```swift 
    @IBOutlet weak var emodjiTextField: UITextField!
 
    override func viewDidLoad() {
        super.viewDidLoad()
        let tap = UITapGestureRecognizer(target: self, action: #selector(self.dismissKeyboard))
        view.addGestureRecognizer(tap)
    }
 
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard segue.identifier == "emodji" else { return }
        guard let destination = segue.destination as? SecondViewController else { return }
        destination.emodji = emodjiTextField.text ?? ""
    }
 
    // При нажатии на любое место экрана клавиатура скроется
    @objc func dismissKeyboard() {
      view.endEditing(true)
    }
 
    @IBAction func performToSecondVC(_ sender: Any) {
        let destination = storyboard?.instantiateViewController(withIdentifier: "SecondViewController") as! SecondViewController
        destination.emodji = ""
        navigationController?.pushViewController(destination, animated: true)
    }
}
```