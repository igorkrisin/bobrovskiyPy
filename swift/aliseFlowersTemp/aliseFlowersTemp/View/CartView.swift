//
//  CartView.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct CartView: View {
    
    @StateObject var viewModel: CartViewModel
    
    var body: some View {
        VStack{
            List(viewModel.positions){ position in
                PositionCell(position: position)
                    .swipeActions {
                        Button {
                            viewModel.positions.removeAll { pos in
                                pos.id == position.id
                            }
                            
                        } label: {
                            Text("Удалить")
                        }.tint(.red)
                    }
                        
            }
            .listStyle(.plain)
            .navigationTitle("Корзина")
            
            HStack {
                Text("Итого: ")
                    .fontWeight(.bold)
                Spacer()
                Text("\(self.viewModel.cost) ₽")
                    .fontWeight(.bold)
            }.padding()
                .padding(.horizontal, 10)
            
            HStack ( spacing: 37 ) {
                
                Button("Отменить") {
                    print("Отменить")
                }
                .frame(width: 100, height: 40)
                .font(.body)
                .fontWeight(.bold)
                .foregroundColor(.black)
                .background(Color(.white))
                .cornerRadius(8)
                .opacity(0.5)
                
                Button("Заказать") {
                    print("Заказать")
                }
                .font(.body)
                .fontWeight(.bold)
                .foregroundColor(.black)
                .frame(maxWidth:.infinity, minHeight: 45)
                .background(Color(.mygray))
                .cornerRadius(24)
                
                
                
            }.padding(.horizontal)
                .padding(.bottom, 45)
        }
    }
}

#Preview {
    CartView(viewModel: CartViewModel.shared)
}
