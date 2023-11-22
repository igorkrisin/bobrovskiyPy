import SwiftUI
import UIKit
import AVFoundation

//var defaultTime: CGFloat = 10



struct ItemWorking: Identifiable, Codable {
    var id: UUID = UUID()
    var nameWork: String
}

struct WorkRow: View {
    var itemWork: ItemWorking
    var body: some View {
        Text(itemWork.nameWork)
    }
}

struct ContentView: View {
    @State var tabSelection = 0
    
    @State private var navigateToAnotherView = false

    
    @State var currentWork = ""
    
    @State var listWorks : [ItemWorking] = []
   
    
    
    var body: some View {
        
        TabView {
            
            NavigationView {
                List(listWorks) { item in
                    NavigationLink(destination: TimerView(currWork: $currentWork, navi: $navigateToAnotherView, list: $listWorks)) {
                        WorkRow(itemWork: item)
                    }
                }
                Text("text: \(currentWork)")
                    .navigationBarTitle("Tab 1", displayMode: .inline)
               
            }.navigationDestination(isPresented: $navigateToAnotherView, destination: {
                ContentView()
            })
            .tabItem {
                Image(systemName: "list.bullet")
                Text("List work")
            }.tag(0)
            
            // Вторая вкладка
            TimerView(currWork: $currentWork, navi: $navigateToAnotherView, list: $listWorks)
            .tabItem {
                Image(systemName: "clock.fill")
                Text("Setting")
                
            }.tag(1)
        }
    }
    
   
}











#Preview {
    ContentView()
}
