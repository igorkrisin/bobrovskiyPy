import SwiftUI
import SwiftData




struct ListTimeTodayView: View {
    
    
    
    @State var workName: String
   
    @Environment(\.modelContext) private var contextModel
    @Query private var itemsTime: [MyDataItemTime]
    
    
    
    var body: some View {
        //Text("\(itemsTime[1].timeWork)")
        List {
            ForEach(itemsTime) { item in
                Text("\(workName)")
                Text("\(item.timeWork)")
            } .onDelete(perform: { indexes in
                for index in indexes {
                    deleteItem(item: itemsTime[index])
                }
            })
               
//            List {
//                ForEach(items) { item in
//                    Text("\(item.itemWorkForDataBAse.nameWork)")
//                }
//                .onDelete(perform: { indexes in
//                    for index in indexes {
//                        deleteItem(items[index])
//                    }
//                })
//            }
            
        }
    }
    


    func deleteItem(item: MyDataItemTime) {
        contextModel.delete(item)
    }

}


