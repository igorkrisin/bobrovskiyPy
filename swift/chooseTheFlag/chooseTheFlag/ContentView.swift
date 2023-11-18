//
//  ContentView.swift
//  chooseTheFlag
//
//  Created by Игорь Крысин on 11.11.2023.
//

import SwiftUI


struct ContentView: View {
    
    @State private var countries: [String] = ["USA", "UK", "argentina", "bangladesh", "germany", "brazil", "canada", "greece", "russia", "sweden"].shuffled()
    @State private var corectAnswer: Int = Int.random(in: 0...2)
    @State private var score: Int = 0
    @State private var showingAlert: Bool = false
    @State private var answerForUser: String = ""
    
    
    
    var body: some View {
        ZStack {
            VStack {
                VStack {
                    Text("Choose correct flag: " )
                    Text(countries[corectAnswer].uppercased())
                        .bold()
                }
                .padding()
                ForEach(0..<3) { member in
                    Button(action: {
                        isCorrectFlag(member)
                    }) {
                        Image(self.countries[member])
                            .resizable()
                            .frame(width: 250, height: 150)
                            .clipShape(Capsule())
                            .shadow(radius: 10)
                        
                    }
                    
                    .padding(10)
                    
                    
                }
                Text("Обший счет: \(score)")
                    .font(.title)
                
                Spacer()
            }
            
        }.alert(isPresented: $showingAlert) {
            Alert(title: Text("\(answerForUser) \n\nOбщий счет: \(score)"), message: nil,
                  dismissButton: .default(Text("Продолжить")))
        }
        
    }
    func isCorrectFlag( _ member: Int) {
        if member == corectAnswer{
            score += 1
            self.showingAlert = true
            answerForUser = "Правильный ответ!"
            countries.shuffle()
        } else {
            score -= 1
            self.showingAlert = true
            answerForUser = "Не правильно! Это флаг \(countries[corectAnswer].uppercased())!"
            countries.shuffle()
        }
    }
}










#Preview {
    ContentView()
}
