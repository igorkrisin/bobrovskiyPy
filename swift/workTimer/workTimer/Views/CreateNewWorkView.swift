//
//  createNewWorkView.swift
//  workTimer
//
//  Created by Игорь Крысин on 24.11.2023.
//

import SwiftUI

struct CreateNewWorkView: View {

    
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

            }) {
                Image(systemName: "text.badge.plus")
                    .symbolRenderingMode(.multicolor)
                    .foregroundColor(.gray)
                    .padding()
            }
        }
    }
}


