//
//  ContentView.swift
//  MySwiftData
//
//  Created by Игорь Крысин on 03.12.2023.
//

import SwiftUI

import SwiftData

struct ContentView: View {
    
    @Environment(\.modelContext) private var context
    
    @Query private var items: [DataItem]
    
    var body: some View {
        VStack {
           
            Text("Tap on this button to add data")
            Button("Add an item") {
                addItem()
            }
            
            List {
                ForEach(items) { item in
                    HStack {
                        Text(item.name)
                        Spacer()
                        Button {
                            updateItem(item)
                        } label: {
                            Image(systemName: "pencil")
                        }
                        
                    }
                   
                }
               
                .onDelete { indexes in
                    for index in indexes {
                        deleteItem(items[index])                    }
                }
            }
            
        }
        .padding()
    }
    func addItem() {
        //create the item
        let item = DataItem(name: "Test Item")
        //add the item to data context
        context.insert(item)
    }
    
    func deleteItem(_ item: DataItem) {
        context.delete(item)
    }
    func updateItem(_ item: DataItem) {
        // Edit the item data
        item.name = "New name"
        //Save the context
        try? context.save()
    }
}

#Preview {
    ContentView()
}
