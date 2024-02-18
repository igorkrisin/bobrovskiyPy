#ios #view #present #show #переход #pushViewController 
[[Переход на другие view при помощи pushViewController]]
[[UIKit Navigation View Controller создание кодом]]


При отсутствии _navigationController_ переход `navigationController?.pushViewController(destination, animated: true)` не сработает, что логично, ведь тут мы обращаемся к методу _navigationController’a._

Функция `present` используется достаточно часто. Нужна она для того, чтобы сделать переход на другой экран.

```swift

func present(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion: (() -> Void)? = nil)

//В таком случае вы можете использовать следующий код:

destination.modalPresentationStyle = .fullScreen
destination.modalTransitionStyle = .coverVertical
present(destination, animated: true, completion: nil)

//Еще один метод, который поможет осуществить переход на другой экран, — `show`.

func show(_ vc: UIViewController, sender: Any?)

let destination = storyboard?.instantiateViewController(withIdentifier: "SecondViewController") as! SecondViewController
destination.emodji = emodjiTextField.text ?? ""
show(destination, sender: nil)

//Для того, чтобы сделать закрытие модуля, необходимо воспользоваться методом `dismiss`.

dismiss(animated: true, completion: nil)

//Таким образом, для перехода на другой экран вы можете использовать разные методы: `show` и `present`. Если же у вас есть _navigationController_, то необходимо использовать метод `pushViewController`. Опять же, код можно писать по-разному. Давайте посмотрим на другой вариант написания того же функционала. В каждой функции есть два варианта одного и того же кода, написанного чуть иначе.

func presentSecondVC() {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "SecondViewController")
        self.present(controller, animated: true, completion: nil)
 
        // Другой вариант
        if let vc = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "SecondViewController") as? SecondViewController {
            present(vc, animated: true, completion: nil)
        }
    }

 
func pushSecondVC() {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let vc = storyboard.instantiateViewController(withIdentifier: "SecondViewController") as UIViewController
        navigationController?.pushViewController(vc, animated: true)
 
        // Другой вариант
        if let viewController = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "SecondViewController") as? SecondViewController {
            if let navigator = navigationController {
                navigator.pushViewController(viewController, animated: true)
            }
        }
    }

```
Дополнительный [источник](https://learnappmaking.com/pass-data-between-view-controllers-swift-how-to/) для изучения переходов между экранами.