//
//  SecondViewController.swift
//  uiKitStart
//
//  Created by Игорь Крысин on 12.12.2023.
//

import UIKit

class SecondViewController: UIViewController {
    
//    @IBAction func hideCurrentScene() {
//        self.dismiss(animated: true, completion: nil)
//        print("DISMISS")
//    }
//    код для удадения информации с view и возврат на предыдузую страницу
    
    
    override func loadView() {
        super.loadView()
        print("loadView SVC")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        print("viewDidLoad SVC")
        // Do any additional setup after loading the view.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("viewWillAppear SVC")
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        print("viewDidAppear SVC")
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        print("viewWillDisappear SVC")
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        print("viewDidDisappear SVC")
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
