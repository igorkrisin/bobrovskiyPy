//
//  ProductCell.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct ProductCell: View {
    
    var product: Product
    
    var body: some View {
        VStack(spacing: 1) {
            Image("rozyPh")
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(maxWidth: screen.width * 0.8, minHeight: screen.width * 0.45, maxHeight: screen.width * 0.45)
                .clipped()
                //.cornerRadius(16)
            HStack {
                Text(product.title)
                    .font(.custom("AvenirNext-regular", size: 14))
                Spacer()
                Text("\(product.price) ₽")
                    .font(.custom("AvenirNext-bold", size: 14))
            }.padding(.bottom, 20)
                .padding(4)
            Spacer()
                //.padding(.bottom, 1)
            
            
        }.frame(width: screen.width * 0.4 , height: screen.width * 0.45)
            .background(.white)
            .cornerRadius(16)
            .shadow(radius: 4)
    }
}

#Preview {
    ProductCell(product: Product(id: "1",
                                 title: "Букет fgfdgffgd",
                                 imageUrl: "Not found",
                                 price: 5990,
                                 descript: " Большой букет роз "))
}
