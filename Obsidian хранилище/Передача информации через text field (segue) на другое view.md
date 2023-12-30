#ios #swift #textfield #segue

Для того что бы <mark style="background: #FF5582A6;">подцепить segue</mark> в StoryBoard [[Переход на другие view при помощи segue]] !!! 

[[Создать кодом новое view и перейти на него при помощи кнопки]]

```swift
import UIKit
 
class ViewController: UIViewController {
	 //добавляем outlet полю
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
        guard let destination = segue.destination as? SecondViewController else { return 
																				//destination - пункт назначения - то есть куда отправляем информацию с первого контроллера
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