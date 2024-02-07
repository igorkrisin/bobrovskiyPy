
#ios #label #кодом

```swift
import UIKit

class ViewController: UIViewController {
    
    let myLabel = UILabel()

    override func viewDidLoad() {
        super.viewDidLoad()
        let labelFrame = CGRect(x: 0, y: 0, width: 100, height: 23)
        myLabel.frame = labelFrame
        //количесво выделенных строк
        myLabel.numberOfLines = 0
        
        //перенос строк
        myLabel.lineBreakMode = .byWordWrapping
        myLabel.text = "Ios 11 end 9 Xcode stop start"
        myLabel.font = UIFont.boldSystemFont(ofSize: 24)
        myLabel.adjustsFontSizeToFitWidth = true
        myLabel.sizeToFit()
        myLabel.textColor  = UIColor.blue
        
        //тень
        myLabel.shadowColor = UIColor.lightGray
        myLabel.shadowOffset = CGSize(width: 2, height: 2)
        
        myLabel.center = self.view.center
        view.addSubview(myLabel)
        
        
    }```