//
//  workTimerApp.swift
//  workTimer
//
//  Created by Игорь Крысин on 18.11.2023.
//

import SwiftUI
import SwiftData

@main
struct workTimerApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [MyDataItemNew.self, MyDataItemTime.self])
    }
}
