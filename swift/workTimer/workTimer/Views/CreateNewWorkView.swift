//
//  createNewWorkView.swift
//  workTimer
//
//  Created by Игорь Крысин on 24.11.2023.
//

import SwiftUI
import SwiftData

struct CreateNewWorkView: View {

    @Environment(\.modelContext)  var contextModel
    
    @Query private var items: [MyDataItemNew]
    
    @ObservedObject var dataWork = WorkModel()
 
    @Binding var list: [ItemWorking]

    var body: some View {
        HStack{
            TextField("enter work's name ", text: $dataWork.nameWork)
            
                .padding()
            
            Button(action:  {
                guard dataWork.nameWork != "" else { return }
                @State var itemWork: ItemWorking = ItemWorking(nameWork: dataWork.nameWork)
                list.append(itemWork)
                addItem(itemWork)

            }) {
                Image(systemName: "text.badge.plus")
                    .symbolRenderingMode(.multicolor)
                    .foregroundColor(.gray)
                    .padding()
            }
          
        }
        List {
            ForEach(items) { item in
                Text("\(item.itemWorkForDataBAse.nameWork)")
            }
            .onDelete(perform: { indexes in
                for index in indexes {
                    deleteItem(items[index])
                }
            })
        }
        
    }
    func addItem(_ item: ItemWorking){
        
        let time = MyDataItemNew(itemWorkForDataBAse: item)
        contextModel.insert(time)
    }
    
    func deleteItem(_ item: MyDataItemNew) {
        contextModel.delete(item)
    }
 
}


