import SwiftUI
import SwiftData


struct ItemWorking: Identifiable, Codable {
    var id: UUID = UUID()
    var nameWork: String
}



struct WorkView: View {
    @State var itemWork: ItemWorking

    var body: some View {
        VStack {
            Text(itemWork.nameWork)
            TimerView()
        }
       
    }
}
