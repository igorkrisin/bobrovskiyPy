

import SwiftUI
import UIKit
import AVFoundation




struct TimerView: View {
    var strokeStyle = StrokeStyle(lineWidth: 15, lineCap: .round)
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    @State var player: AVAudioPlayer!
    @State var newWork = ""
    @State private var timerRunning: Bool = false
    @State private var countdownTime: CGFloat = 0
    @Binding var currWork: String
    @Binding var navi: Bool
    @Binding var list: [ItemWorking]
    var itemWork: ItemWorking = ItemWorking(nameWork: "")
    
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
            HStack{
                TextField("enter work's name ", text: $newWork)
                
                    .padding()
                
                Button(action:  {
                    guard newWork != "" else { return }
                    
                    self.currWork = self.newWork
                    self.newWork = ""
                    print("currWork: \(currWork)")
                    timerRunning = true
                    navi = true
                    
                }) {
                    Image(systemName: "text.badge.plus")
                        .symbolRenderingMode(.multicolor)
                        .foregroundColor(.gray)
                        .padding()
                }
            }
        
        ZStack {
            
            HStack(spacing: 25) {
                Label("", systemImage:  buttonIcon)
                    .foregroundColor(.black)
                    .font(.system(.title3, design: .rounded).bold())
                    .onTapGesture(perform: {
                        timerRunning.toggle()
                            
                    })
                Text("\(Int(countdownTime))")
                    .font(.system(size: 40))
                Label("", systemImage: "stop")
                    .foregroundColor(.black)
                    .font(.system(size: 30))
                    .onTapGesture(perform: {
                        timerRunning = false
                        countdownTime = 0
                        
                    })
            }
        }.frame(width: 300, height: 300)
        .padding()
        .onReceive(timer, perform: { _ in
            guard timerRunning else { return }
            if countdownTime >= 0 {
                countdownTime += 1
            } else {
                timerRunning = false
                countdownTime = 0
                playAlarmSound()
            }
            
        })
        }.padding()
        
    }
    
}

