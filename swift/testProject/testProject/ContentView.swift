// ContentView.swift

import SwiftUI

struct ContentView: View {
    
    @State var tabSelection = 0
    
    var body: some View {
        TabView (selection: $tabSelection) {
            // Первая вкладка
            NavigationView {
                Text("Первая вкладка")
                    .navigationBarTitle("Первая вкладка", displayMode: .inline)
            }
            .tabItem {
                Image(systemName: "1.circle.fill")
                Text("Tab 1")
            }.tag(0)
            
            // Вторая вкладка
            NavigationView {
                NavigationLink(destination: SecondView()) {
                    Text("Вторая вкладка")
                }
                .navigationBarTitle("Вторая вкладка", displayMode: .inline)
            }
            .tabItem {
                Image(systemName: "2.circle.fill")
                Text("Tab 2")
            }.tag(1)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
