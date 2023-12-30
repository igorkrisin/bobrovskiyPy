#ios #button #код
с переходом на другое view !


```swift
import UIKit

class ViewController: UIViewController {


    @IBOutlet weak var ButtonOpenSVC: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        openSecondVCButton()
    }
    
    func openSecondVCButton() {
        print("i'm here")
        let button = UIButton(frame: CGRect(x: 100, y: 200, width: 150, height: 50))
        //добаляем кнопку на view
        view.addSubview(button)
        //устанавливаем надпись
        button.setTitle("Open Second VC", for: .normal)
        //меняем внешний вид
        button.backgroundColor = .white
        button.setTitleColor(.blue, for: .normal)
        //располагаем по центру
        button.center = view.center
        
        //добавляем какое-то событие по нажаьтю
        button.addTarget(self, action: #selector(openSVC(sender:)), for: .touchUpInside)
    }
    
    @objc func openSVC(sender: Any) {
        let secondVC = SecondViewController()
        
        
        self.navigationController?.pushViewController(secondVC, animated: true)
    }

}```