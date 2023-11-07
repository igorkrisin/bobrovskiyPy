//
//  PositionCell.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 25.10.2023.
//

import SwiftUI

struct PositionCell: View {
    
    let position: Position
    
    var body: some View {
        HStack {
            Text(position.product.title)
                .fontWeight(.bold)
            Spacer()
            Text("\(position.count) шт")
            Text("\(position.cost) ₽")
                .frame(width: 95, alignment: .trailing)
        }.padding(.horizontal)
    }
}

#Preview {
    PositionCell(position: Position(id: UUID().uuidString, product: Product(id:  UUID().uuidString, 
                                                                            title: "Букет белых роз",
                                                                            imageUrl: "pozyPh",
                                                                            price: 1590,
                                                                            descript: "fgdgfdg"),
                                                        count: 3))
}
