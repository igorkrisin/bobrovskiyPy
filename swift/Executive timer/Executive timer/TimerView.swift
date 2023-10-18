

import SwiftUI
import UIKit
import AVFoundation



var defaultTime: CGFloat = 10

struct ContentView: View {
    var strokeStyle = StrokeStyle(lineWidth: 15, lineCap: .round)
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    @State var player: AVAudioPlayer!
    @State private var currentTime = ""
    @State private var newTime: CGFloat = defaultTime
    @State private var timerRunning: Bool = false
    @State private var countdownTime: CGFloat = defaultTime
    
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
        TabView() {
            ViewA()
                .padding()
                .tabItem {
                    Label("View A", systemImage: "a.square")
                }
                .tag(1)
           
        }
       
        let buttonIcon = timerRunning ? "pause.rectangle.fill" : "play.rectangle.fill"
        let countdownColor: Color = {
            
            switch (countdownTime) {
            case 6...: return Color.green
            case 3...: return Color.yellow
            default: return Color.red
            }
        }()
        HStack{
            TextField("start time  ..", value: $newTime, formatter: NumberFormatter()).textFieldStyle(PlainTextFieldStyle())
                
                .padding()
            Button(action:  {
                //print("Hello")
                
                self.countdownTime = self.newTime
                defaultTime = self.newTime
                self.newTime = 0
                //print(self.$countdownTime)
                
            }) {
                Image(systemName: "text.badge.plus")
                    .symbolRenderingMode(.multicolor)
                    .foregroundColor(.gray)
            }
        }.padding()
        ZStack {
            Circle()
                .stroke(Color.gray.opacity(0.2), style: strokeStyle)
            Circle()
                .trim(from: 0, to: 1 - ((defaultTime - countdownTime)/defaultTime))
                .stroke(countdownColor, style: strokeStyle)
                .rotationEffect(.degrees(-90))
                .animation(.easeInOut(duration: 0.2), value: countdownTime)
            HStack(spacing: 25) {
                Label("", systemImage:  buttonIcon)
                    .foregroundColor(.black)
                    .font(.system(.title3, design: .rounded).bold())
                    .onTapGesture(perform: {
                        timerRunning.toggle()
                            
                    })
                Text("\(Int(countdownTime))")
                    .font(.system(size: 40))
                Label("", systemImage: "gobackward")
                    .foregroundColor(.red)
                    .font(.system(size: 30))
                    .onTapGesture(perform: {
                        timerRunning = false
                        countdownTime = defaultTime
                    })
            }
        }.frame(width: 300, height: 300)
        .padding()
        .onReceive(timer, perform: { _ in
            guard timerRunning else { return }
            if countdownTime > 0 {
                countdownTime -= 1
            } else {
                timerRunning = false
                countdownTime = defaultTime
                playAlarmSound()
            }
        })
        
    }
    
}





#Preview {
    ContentView()
}
