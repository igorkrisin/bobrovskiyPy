import SwiftUI
import UIKit
import AVFoundation
import SwiftData

struct ContentView: View {
   
    
    @Query private var items: [MyDataItemNew]
    
    @ObservedObject var workTime = WorkModel()
    @State var listWorks : [ItemWorking] = []
 
    var body: some View {
        
        TabView {
            NavigationView {

                List(items) { item in
                    NavigationLink(destination: ListTimeTodayView(workName: item.itemWorkForDataBAse.nameWork)) {
                        WorkView(itemWork: item.itemWorkForDataBAse)
                    }
                }
                    
//                List(listWorks) { item in
//                    NavigationLink(destination: ListTimeTodayView(workName: item.nameWork)) {
//                        WorkView(itemWork: item)
//                    }
//                }
//                .navigationTitle("Work list")
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
