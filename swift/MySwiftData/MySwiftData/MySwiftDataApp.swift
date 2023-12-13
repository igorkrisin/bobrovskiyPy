//
//  MySwiftDataApp.swift
//  MySwiftData
//
//  Created by Игорь Крысин on 03.12.2023.
//

import SwiftUI
import SwiftData

@main
struct MySwiftDataApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: DataItem.self)
    }
}
