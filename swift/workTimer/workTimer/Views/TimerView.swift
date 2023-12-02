

import SwiftUI
import UIKit
import AVFoundation




struct TimerView: View {
    
    
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    @State var player: AVAudioPlayer!
    
    @State private var timerRunning: Bool = false
    @State  var countdownTime: CGFloat = 0
    @State var amountTimeForWork: Int =  0
    
    func playAlarmSound() {
        if let soundURL = Bundle.main.url(forResource: "alarm", withExtension: "mp3") {
            do {
                player = try AVAudioPlayer(contentsOf: soundURL)
                player.play()
            } catch {
                print("Ошибка воспроизведения звука: \(error)")
            }
        }
    }
    
    var body: some View {

        let buttonIcon = timerRunning ? "pause.rectangle.fill" : "play.rectangle.fill"
        
        VStack{
            ZStack {
                
                HStack(spacing: 25) {
                    Label("", systemImage:  buttonIcon)
                        .foregroundColor(.black)
                        .font(.system(.title3, design: .rounded).bold())
                        .onTapGesture(perform: {
                            timerRunning.toggle()
                            
                        })
                    Text("\(Int(countdownTime))")
                        .font(.system(size: 20))
                    Label("", systemImage: "stop")
                        .foregroundColor(.black)
                        .font(.system(size: 15))
                        .onTapGesture(perform: {
                            timerRunning = false
                            countdownTime = 0
                            
                        })
                }
            }
            .padding()
            .onReceive(timer, perform: { _ in
               // guard timerRunning else { return }
                if(timerRunning && countdownTime >= 0) {
                    countdownTime += 1
                } else if (!timerRunning && countdownTime != 0) {
                    amountTimeForWork = Int(countdownTime)
                    print("amountFOR WORK: ", amountTimeForWork)
                } else {
                    timerRunning = false
                    
                    countdownTime = 0
                    playAlarmSound()
                }
                
            })
        }
        
    }
    
    func amountTime() -> CGFloat {
        return self.countdownTime
    }
    
}

