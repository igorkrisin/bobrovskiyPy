//
//  ScoreView.swift
//  scoreProject
//
//  Created by Игорь Крысин on 21.10.2023.
//

import SwiftUI

struct ScoreView: View {
    @EnvironmentObject var gameScore: GameScore
    var body: some View {
        VStack {
            Text("The score is !\(gameScore.scores)")
            Text("The piece count is \(gameScore.pieces)")
            Spacer()
        }
        
    }
}

#Preview {
    ScoreView()
}
