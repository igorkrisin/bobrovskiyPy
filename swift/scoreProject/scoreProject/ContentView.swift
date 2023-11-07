//
//  ContentView.swift
//  scoreProject
//
//  Created by Игорь Крысин on 21.10.2023.
//

import SwiftUI


class GameScore: ObservableObject {
    @Published var scores = 0
    @Published var pieces = 0
}

struct ContentView: View {
    @StateObject var gameScore = GameScore()
    var body: some View {
        NavigationView {
            VStack {
                Button ("Add score") {
                    gameScore.scores += 1
                    print(gameScore.scores)
                }.padding()
                Button ("Add pieces") {
                    gameScore.pieces += 1
                    print(gameScore.pieces)
                }.padding()
                NavigationLink(destination: ScoreView()) {
                    Text("view scores")
                        .padding()
                }
                AsyncImage(url: URL(string: "https://cataas.com/cat?type=square")) {
                    image in
                    image.resizable()
                } placeholder: {
                    ProgressView()
                }
            }
            .padding()
        } .environmentObject(gameScore)
    }
}

#Preview {
    ContentView()
}
