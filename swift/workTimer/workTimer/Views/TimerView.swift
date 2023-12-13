

import SwiftUI
import UIKit
import AVFoundation
import SwiftData




struct TimerView: View {
    
    @Environment(\.modelContext) private var contextModel2
    
    @Query private var itemsTime: [MyDataItemTime]
    var amountTime: CGFloat = 0
    
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    @State var player: AVAudioPlayer!
    
    @State private var timerRunning: Bool = false
    @State  var countdownTime: CGFloat = 0
    
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
                        print("countDownTIme: ", countdownTime)
                        addItem(countdownTime)
                        countdownTime = 0
                        
                    })
            }
            
            
            .padding()
            .onReceive(timer, perform: { _ in
                // guard timerRunning else { return }
                if(timerRunning && countdownTime >= 0) {
                    countdownTime += 1
                } else {
                    timerRunning = false
                    countdownTime = 0
                    playAlarmSound()
                }
            })
            
        }
        ZStack{
            List {
                ForEach(itemsTime) {item in
                    Text("\(item.timeWork)")
                }
            }
        }
        
        
    }
    func addItem(_ time: CGFloat) {
        let item = MyDataItemTime(timeWork: time)
        contextModel2.insert(item)
    }
    
    
    
}

//TODO: база данных, swift data (работает под ios 17) MVVC и Observed: FrameWork(последняя WWDC)\ lotti для анимаций (как вариант) и встроенный framework для отображения графиков Core Graphics
