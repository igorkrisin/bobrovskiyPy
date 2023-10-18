//
//  ContentView.swift
//  Todo List
//
//  Created by Игорь Крысин on 15.10.2023.
//

import SwiftUI

struct ContentView: View {
    @State private var currentTodo = ""
    @State private var todoList:[Item] = []
    var body: some View {
        NavigationView {
            VStack {
                HStack{
                    TextField("New todo ..", text: $currentTodo).textFieldStyle(PlainTextFieldStyle())
                    
                    Button(action:  {
                        guard !self.currentTodo.isEmpty else {return}
                        self.todoList.append(Item(descriptionTask: self.currentTodo))
                        self.currentTodo = ""
                        save()
                    }) {
                        Image(systemName: "text.badge.plus")
                            .symbolRenderingMode(.multicolor)
                            .foregroundColor(.gray)
                    }
                    .padding(.leading, 5)
                }.padding()
                List {
                    ForEach(todoList) { todoEntry in
                        Text(todoEntry.descriptionTask)
                       
                    }.onDelete(perform: delete)
                }
                .foregroundColor(.gray)
                .bold()
            }
            .navigationBarTitle("Todo List")
        }.onAppear(perform: load)
    }
    private func save(){
        UserDefaults.standard.set(try? PropertyListEncoder().encode(self.todoList), forKey: "myTodoKey")
    }
    private func load() {
        if let todosData = UserDefaults.standard.value(forKey: "myTodoKey") as? Data {
            if let todoLisT = try? PropertyListDecoder().decode(Array<Item>.self, from: todosData) {
                self.todoList = todoLisT
            }
        }
    }
    
    private func delete(at offset: IndexSet) {
        self.todoList.remove(atOffsets: offset)
        save()
    }
        
}

#Preview {
    ContentView()
}
