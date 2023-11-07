//
//  ProductDetailView.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct ProductDetailView: View {
    
    var viewModel: ProductDetailViewModel
    @State var size = "Средний"
    @State var count = 1
    
    @Environment(\.presentationMode) var presentationMode
    
    var body: some View {
        VStack {
            Image("rozyPh")
                .resizable()
                .cornerRadius(18)
                .aspectRatio(contentMode: .fit)
                .frame(maxWidth: screen.width * 0.8, minHeight: screen.width * 0.45, maxHeight: screen.width * 1)
                
            HStack {
                Text("\(viewModel.product.title)")
                    .font(.title2.bold())
                Spacer()
                    
                Text("\(viewModel.getPrice(size: self.size)) ₽")
                    .font(.title2)
            }.padding(.horizontal, 39)
            Text("\(viewModel.product.descript)")
                .frame(maxWidth: .infinity, alignment: .center)
                .padding(.horizontal, 45)
                .padding(.vertical, 12)
            HStack{
                Stepper("Количество", value: $count, in: 1...10)
                
                Text("\(self.count)")
                    .padding(.leading, 24)
            }.padding(.horizontal, 26)
            
            Spacer()
            
            Picker("Размер букета", selection: $size) {
                ForEach(viewModel.sizes, id: \.self) { item in
                    Text(item)
                }
            }.pickerStyle(.segmented)
                .padding(20)
            
            
            Button("Добавить в корзину") {
                var position = Position(id: UUID().uuidString,
                                        product: viewModel.product,
                                        count: self.count)
                
                position.product.price = viewModel.getPrice(size: size)
                
                CartViewModel.shared.addPosition(position)
                presentationMode.wrappedValue.dismiss()
            }.padding()
                .frame(maxWidth: .infinity)
                .background(Color("Mygray"))
                .cornerRadius(12)
                .padding(8)
                .padding(.horizontal, 12)
                .font(.title3.bold())
                .foregroundColor(.white)
             
           Spacer(minLength: 100 )
        }
        
        
    }
}

#Preview {
    ProductDetailView(viewModel: ProductDetailViewModel(product: Product(id: "1",
                                                                  title: "Букет роз",
                                                                  imageUrl: "Not found",
                                                                  price: 5990,
                                                                  descript: " Большой букет роз ")
                                  ))
}
