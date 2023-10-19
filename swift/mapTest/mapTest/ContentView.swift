//
//  ContentView.swift
//  mapTest
//
//  Created by Игорь Крысин on 19.10.2023.
//


import SwiftUI
import MapKit

class GameScore: ObservableObject {
    @Published var numericalScore = 0
    @Published var piecesCaptured = 0
}

struct ContentView: View {
    @StateObject var score = GameScore()
    var body: some View {
        VStack {
            Text("Score is \(score.numericalScore), \(score.piecesCaptured) pieces captured.")
            ScoreView(score: score)
        }
    }
}
struct ScoreView: View {
    @ObservedObject var score: GameScore
    var body: some View {
        Button("Bigger score!") {
            score.numericalScore += 1
        }
        Button("More pieces!") {
            score.piecesCaptured += 1
        }
    }
}
     

#Preview {
    ContentView()
}
