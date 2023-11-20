import SwiftUI
import UIKit
import AVFoundation

//var defaultTime: CGFloat = 10



struct ItemWorking: Identifiable, Codable {
    var id: UUID = UUID()
    var nameWork: String
    
    
    
}

struct ContentView: View {
    var body: some View {
        TabView {
            // Первая вкладка
            NavigationView {
                Text("Первая вкладка")
                    .navigationBarTitle("Tab 1", displayMode: .inline)
            }
            .tabItem {
                Image(systemName: "1.circle.fill")
                Text("Tab 1")
            }
            
            // Вторая вкладка
            NavigationView {
                NavigationLink(destination: TimerView()) {
                    Text("Вторая вкладка")
                }
                .navigationBarTitle("Tab 2", displayMode: .inline)
            }
            .tabItem {
                Image(systemName: "2.circle.fill")
                Text("Tab 2")
                
            }
        }
    }
}











#Preview {
    ContentView()
}
