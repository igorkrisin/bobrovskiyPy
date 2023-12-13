//
//  ViewController.swift
//  uiKitStart
//
//  Created by Игорь Крысин on 08.12.2023.
//

import UIKit

class ViewController: UIViewController {
    
    var game: Game!
    
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
   
    
    override func loadView() {
        super.loadView()
        print("load View")
        
//        let versionLabel = UILabel(frame: CGRect(x: 20, y: 20, width: 200, height: 20))
//        versionLabel.text = "Version 1.1"
//        self.view.addSubview(versionLabel)
    }
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        print("ViewDidload")
        
        game = Game(startValue: 1, endValue: 50, rounds: 5)
        updateGameWithTheSecretNumber(newText: String(game.currentSecretValue))
       
    }
    // MARK: - взаимодействие  View - Model
    
    
    @IBAction func checkNumber() {
        //подсчитываем очки
        game.calculateScore(with: Int(slider.value))
        //проверяем не закончилась ли игра
        
        if game.isGameEnded {
            showAlert(score: game.score)
            
            game.restartGame()
        } else {
            game.startNewRound()
        }
        //обновляем данные о текущем значении загаданного числа
        
        updateRoundView(round: String(game.currentRound))
        updateViewScores(scores: String(game.score))
        
        updateGameWithTheSecretNumber(newText: String(game.currentSecretValue))
        
        
        
       
        
    }
    
    
    //MARK: обновление View
    func updateGameWithTheSecretNumber(newText: String) {
        label.text = newText
    }
    
    func updateRoundView(round: String) {
        viewRound.text = round
    }
    
    func updateViewScores(scores: String) {
        viewScores.text = scores
    }
    
    func showAlert(score: Int) {
        let alert = UIAlertController(title: "Game over", message: "Your scores:  \(game.score)", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "Начать заново", style: .default, handler: nil ))
        self.present(alert, animated: true, completion: nil)
    }
}

