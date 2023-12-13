//
//  DataItem.swift
//  MySwiftData
//
//  Created by Игорь Крысин on 03.12.2023.
//

import Foundation
import SwiftData

@Model
class DataItem: Identifiable {
    var id: String
    var name: String
    
    init(name: String) {
        self.id = UUID().uuidString
        self.name = name
    }
}
