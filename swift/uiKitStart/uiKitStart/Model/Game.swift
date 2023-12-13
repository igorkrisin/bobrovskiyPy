//
//  Game.swift
//  uiKitStart
//
//  Created by Игорь Крысин on 13.12.2023.
//

import Foundation


protocol GameProtocol {
    //общий счет в игре
    var score: Int { get }
    //действующее загаданное число
    var currentSecretValue: Int { get }
    //флаг о состоянии игры
    var isGameEnded: Bool { get }
    
   
    
    
    // метод перезапуска  игры
    func restartGame()
    //метод начала нового раунда
    func startNewRound()
    //метод подсчета очков и равнения загаданного и пользовательского числа
    func calculateScore(b value: Int)
    
}


class Game: GameProtocol {
    
    private var minSecretValue: Int
    private var maxSecretValue: Int
    
    var score: Int = 0
    
    var currentSecretValue: Int = 0
    
    var lastRound: Int
    var currentRound: Int = 1
    
    var isGameEnded: Bool {
        return currentSecretValue >= lastRound
    }
    
    init?(startValue: Int, endValue: Int, rounds: Int) {
        //стартовое значение для выбора случайного числа не может быть больше конечного
        
        guard startValue <= endValue else {
            return nil
        }
        minSecretValue = startValue
        maxSecretValue = endValue
        lastRound = rounds
        currentSecretValue = self.getNewSecretValue()
    }
    
    func restartGame() {
        self.score = 0
        self.lastRound = 0
        startNewRound()
    }
    
    func startNewRound() {
        currentSecretValue = self.getNewSecretValue()
        currentRound += 1
    }
    
    func calculateScore(b value: Int) {
        if value > currentSecretValue {
            score += 50 - value + currentSecretValue
        } else if value < currentSecretValue {
            score += 50 - currentSecretValue + value
        } else {
            score += 50
        }
    }
    
    private func getNewSecretValue() -> Int {
        (minSecretValue...maxSecretValue).randomElement()!
    }
    
    
}
