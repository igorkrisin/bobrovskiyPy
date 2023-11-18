//
//  ContentView.swift
//  TeaCalculator
//
//  Created by Игорь Крысин on 09.11.2023.
//

import SwiftUI



struct ContentView: View {
    
    @State private var amount: String = ""
    
    @State private var selectedPersonNumber = 2
    @State private var percentList = [5, 7, 10, 15, 20]
    @State private var selectedPercent = 0
    
    var summPerPerson: Float {
        return  Float((percentList[selectedPercent] ) * Int((Float(amount) ?? 0)) / 100) / (Float(selectedPersonNumber) + 2)
    }
    //

    var body: some View {
        NavigationView {
            
            Form{
                TextField("Enter amount", text: $amount)
                Picker(selection: $selectedPersonNumber, label: Text("Number of people")) {
                    ForEach(2..<20){ people in
                        Text("\(people)")
                        
                    }
                }
                Section("cколько чаевых вы хотите оставить? "){
                    Picker(selection: $selectedPercent, label: Text("cколько чаевых вы хотите оставить? ")) {
                        ForEach(0..<percentList.count, id: \.self){
                            Text("\(self.percentList[$0])%")
                        }
                    }.pickerStyle(SegmentedPickerStyle())
                }
                Section{
                    Text("\(summPerPerson, specifier: "%.2f")")
                    
                }
            }.navigationBarTitle("Калькулятор чаевых", displayMode: .inline)
        }
    }
}

#Preview {
    ContentView()
}
