

import SwiftUI
import UIKit
import AVFoundation



var defaultTime: CGFloat = 0

struct TimerView: View {
    var strokeStyle = StrokeStyle(lineWidth: 15, lineCap: .round)
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    @State var player: AVAudioPlayer!
    @State private var currentTime = ""
    @State private var newWork = ""
    @State private var timerRunning: Bool = false
    @State private var countdownTime: CGFloat = defaultTime
    @State var currentWork = ""
    
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
                TextField("enter new work  ...", value: $newWork, formatter: NumberFormatter()).textFieldStyle(PlainTextFieldStyle())
                
                    .padding()
                
                Button(action:  {
                    //print("Hello")
                    
                    currentWork = self.newWork
                    print(currentWork)
                    
                    
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
                countdownTime = defaultTime
                playAlarmSound()
            }
            
        })
        }.padding()
        
    }
    
}





#Preview {
    TimerView()
}
