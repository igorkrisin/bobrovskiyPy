//
//  ProductDetailViewModel.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 23.10.2023.
//

import Foundation


class ProductDetailViewModel: ObservableObject {
    enum Size: String {
        case small = "Маленький"
        case arrange = "Средний"
        case big = "Большой"
        
    }
    @Published var count = 0
    @Published var product: Product
    @Published var sizes = [Size.small.rawValue, Size.arrange.rawValue, Size.big.rawValue]
    
    init(product: Product) {
        self.product = product
    }
    
    func getPrice(size: String) -> Int {
        switch size {
        case Size.small.rawValue:
            return product.price / 2
        case Size.arrange.rawValue:
            return product.price
        case Size.big.rawValue:
            return product.price * 2
        default:
            break
        }
        print("Error in getPrixe Product Detail View product Size not found")
        return 0
    }
    
}
