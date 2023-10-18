//
//  ViewA.swift
//  Executive timer
//
//  Created by Игорь Крысин on 18.10.2023.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            TimerView()
                .padding()
                .tabItem {
                    Image(systemName: "timer")
                    Text("Timer")
                }
                .tag("Timer")
            TimerSettingView()
                .padding()
                .tabItem {
                    Image(systemName: "gear")
                    Text("Settings")
                }
                .tag("Settings")
        }
    }
}

#Preview {
    ContentView()
}
