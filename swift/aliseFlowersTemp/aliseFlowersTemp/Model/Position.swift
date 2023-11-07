//
//  Position.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 25.10.2023.
//

import Foundation

struct Position: Identifiable {
    var id: String
    var product: Product
    var count: Int

    var cost: Int {
        return product.price * self.count
    }
}
