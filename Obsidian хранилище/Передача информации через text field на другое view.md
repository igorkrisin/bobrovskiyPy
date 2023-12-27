#ios #swift #textfield

[[Создать кодом новое view и перейти на него при помощи кнопки]]

```swift
import UIKit
 
class ViewController: UIViewController {
	 //добавляем экшн полю
    @IBOutlet weak var emodjiTextField: UITextField!
 
    override func viewDidLoad() {
        super.viewDidLoad()
        //прописываем сворачивание клавы при нажати на любую кнопку экрана
        let tap = UITapGestureRecognizer(target: self, action: #selector(self.dismissKeyboard))
        view.addGestureRecognizer(tap)
    }
	 //`prepare()` — это главный метод, с которым вы будете работать, используя `segue`.
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard segue.identifier == "emodji" else { return }
        guard let destination = segue.destination as? SecondViewController else { return }
        destination.emodji = emodjiTextField.text ?? ""
    }
 
    // При нажатии на любое место экрана клавиатура скроется
    @objc func dismissKeyboard() {
      view.endEditing(true)
    }
}
 // второе view в нем код вывода emodji после загрузки view
import UIKit
 
class SecondViewController: UIViewController {
 
    @IBOutlet weak var emodjiLabel: UILabel!
    var emodji = ""
 
    override func viewDidLoad() {
        super.viewDidLoad()
        emodjiLabel.text = emodji
    }
}
```