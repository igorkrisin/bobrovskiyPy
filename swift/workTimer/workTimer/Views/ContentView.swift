import SwiftUI
import UIKit
import AVFoundation

struct ContentView: View {
    
    @ObservedObject var workNAme = WorkModel()
    
    @State var listWorks : [ItemWorking] = []
 
    var body: some View {
        
        TabView {
            
            NavigationView {
                List(listWorks) { item in
                    NavigationLink(destination: ListTimeTodayView(workName: item.nameWork)) {
                        WorkView(itemWork: item)
                    }
                }
                .navigationTitle("Work list")
            }
            .tabItem {
                Image(systemName: "list.bullet")
                Text("List work")
            }.tag(0)
            CreateNewWorkView(list: $listWorks)
            .tabItem {
                Image(systemName: "clock.fill")
                Text("Create Work")
                
            }.tag(1)
        }
    }
}



#Preview {
    ContentView()
}
