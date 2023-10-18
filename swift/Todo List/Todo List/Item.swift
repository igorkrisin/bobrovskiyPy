//
//  Item.swift
//  Todo List
//
//  Created by Игорь Крысин on 15.10.2023.
//

import Foundation

struct Item: Identifiable, Codable {
    var id = UUID()
    var descriptionTask: String
}
