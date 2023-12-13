//
//  ViewController.swift
//  uiKitStart
//
//  Created by Игорь Крысин on 08.12.2023.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var slider: UISlider!
    @IBOutlet var label: UILabel!
    @IBOutlet var viewRound: UILabel!
    @IBOutlet var viewScores: UILabel!
    
//    @IBAction func showNextScreen() {
//        let storyboard = UIStoryboard(name: "Main", bundle: nil)
//        let vc = storyboard.instantiateViewController(identifier: "SecondViewController")
//        self.present(vc, animated: true, completion: nil)
//    }
    // код перехода на следующий view  при помощи present
    var number: Int = 0
    var round: Int = 1
    var scores: Int = 0
    
    
    
    override func loadView() {
        super.loadView()
        print("load View")
        
//        let versionLabel = UILabel(frame: CGRect(x: 20, y: 20, width: 200, height: 20))
//        versionLabel.text = "Version 1.1"
//        self.view.addSubview(versionLabel)
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        print("viewWillDisappear")
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        print("viewDidDisappear")
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        print("viewDidAppear")
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("viewWillAtppear")
    }
    
    override func viewDidLoad() {
       
        self.number = Int.random(in: 1...50)
        self.label.text = String(self.number)
        
        super.viewDidLoad()
        print("ViewDidload")
        // Do any additional setup after loading the view.
    }
    
    @IBAction func checkNumber() {
        self.round += 1
        
        if(Int(slider.value.rounded()) > self.number) {
            self.scores += 50 - Int(slider.value.rounded()) + self.number
            
            print("slider.value >: ",slider.value.rounded(), "self.number: ", self.number)
        }
        else if (Int(slider.value.rounded()) < self.number) {
            self.scores += 50 -  self.number + Int(slider.value.rounded())
            print("slider.value <: ",slider.value.rounded(), "self.number: ", self.number)
        }
        else {
            self.scores += 50
        }
        self.viewScores.text = String(self.scores)
        self.viewRound.text = String(self.round)
        
        
        if self.round == 5 {
            let alert = UIAlertController(title: "Game over", message: "Your scores:  \(self.scores)", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "Начать заново", style: .default, handler: nil ))
            self.present(alert, animated: true, completion: nil)
            self.round = 0
            self.scores = 0
        }
        
        
        self.number = Int.random(in: 1...50)
        self.label.text = String(self.number)
        
    }
    
}

