//
//  CartViewModel.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 25.10.2023.
//

import Foundation

class CartViewModel: ObservableObject {
    
    static let shared = CartViewModel()
    
    private init() {
        
    }
    
    @Published var positions = [Position]()
    
    
    var cost: Int {
        var sum = 0
        for pos in positions {
            sum += pos.cost
        }
        return sum
    }
    
    func addPosition(_ position: Position) {
        self.positions.append(position)
    }
}
