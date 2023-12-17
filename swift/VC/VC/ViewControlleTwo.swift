//
//  ViewControlleTwo.swift
//  VC
//
//  Created by Игорь Крысин on 14.12.2023.
//

import UIKit
import AVFoundation

class ViewControlleTwo: UIViewController {
    
    @IBOutlet weak var sliderBoard: UISlider!
    var player = AVAudioPlayer()
    var slider = UISlider()
    
    //MARK: - Method
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.slider.frame = CGRect(x: 0, y: 0, width: 200, height: 23)
        self.slider.center = self.view.center
        self.slider.minimumValue = 0
        self.slider.maximumValue = 100
        self.view.addSubview(slider)
        //addTarget
        self.slider.addTarget(self, action: #selector(changeSlider), for: .valueChanged)
        
        
        do {
            if let audioPath = Bundle.main.path(forResource: "Another Day", ofType: "mp3") {
                try player = AVAudioPlayer(contentsOf: URL(fileURLWithPath: audioPath))
                self.slider.maximumValue = Float(player.duration)
            }
        } catch {
            print("Error")
        }
        
        
    }
    
    @objc func changeSlider(sender: UISlider) {
        if sender == slider {
            self.player.currentTime = TimeInterval(sender.value)
        }
    }
    
    @IBAction func playButton(_ sender: Any) {
        self.player.play()
    }
    
    @IBAction func pauseButton(_ sender: Any) {
        self.player.pause()
    }
    
    @IBAction func sliderAction(_ sender: Any) {
        self.player.volume = self.sliderBoard.value
    }
    
}
