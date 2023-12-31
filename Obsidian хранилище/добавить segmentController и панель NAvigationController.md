#ios #swift #barButtonItem #segmentController

Как кодом добавить NavViewController смотрим [[Добавляем barButtonItem и картинку в шапку NavigationController]]


```swift
import UIKit

class ViewController: UIViewController {

   
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "View Controller"
        
        let items = ["up", "down"]
        //создаем segment 
        let segmentController = UISegmentedControl(items: items)
        //isMomentary - показывает какая вкладка выбрана и показывать ее как выбранную (если значение false)
        segmentController.isMomentary = true
        segmentController.addTarget(self, action: #selector(segmentTapped(param:)), for: .valueChanged)
        //присваиваем в navigationController на место правой кнопки
        self.navigationItem.rightBarButtonItem = UIBarButtonItem(customView: segmentController)
    
        
    }
    
    @objc func segmentTapped(param: UISegmentedControl) {
        switch param.selectedSegmentIndex {
        case 0:
            print("up")
        case 1:
            print("down")
        default:
            break
        }
    }```