//
//  ConsumptionView.swift
//  instaFeed
//
//  Created by Игорь Крысин on 18.11.2023.
//

import SwiftUI




struct ConsumptionView: View {
    
    @Environment (\.presentationMode) var presentationMode
    
    @ObservedObject var expensec: ArrayConsunptions
    
    @State private var name = ""
    @State private var type = "Personal"
    @State private var amount = ""
    
    let types = ["Busines", "Personal"]
    
    var body: some View {
        NavigationStack {
            Form {
                TextField("name", text: $name)
                Picker("type", selection: $type) {
                    ForEach(self.types, id: \.self) {
                        Text($0)
                    }
                }
                TextField("amount", text: $amount)
                    .keyboardType(.numberPad)
            }
            .navigationTitle("Add")
            .navigationBarItems(trailing:
                                    Button(action: {
                if let amountSumm = Int(self.amount){
                    let item = MyConsumptionItems(name: self.name, type: self.type, amount: amountSumm)
                    self.expensec.itemConsumption.append(item)
                    self.presentationMode.wrappedValue.dismiss()
                }
                
            }) {
                Image(systemName: "plus")
            }).disabled(false)
            
        }
    }
}

#Preview {
    ConsumptionView(expensec: ArrayConsunptions())
}
