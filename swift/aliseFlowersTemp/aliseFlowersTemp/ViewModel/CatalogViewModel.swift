//
//  CatalogViewModel.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import Foundation

class CatalogViewModel: ObservableObject {
    static let shared = CatalogViewModel()
    
    var popularProducts: [Product] = [ 
        Product(id: "1",
                             title: "Букет роз",
                             imageUrl: "Not found",
                             price: 5990,
                             descript: " Большой букет роз "),
        Product(id: "2",
                             title: "Букет ромашек",
                             imageUrl: "Not found",
                             price: 7500,
                             descript: " Большой букет роз "),
        Product(id: "3",
                             title: "Букет лилий",
                             imageUrl: "Not found",
                             price: 3500,
                             descript: " Большой букет роз "),
        Product(id: "4",
                             title: "Букет гвоздики",
                             imageUrl: "Not found",
                             price: 4500,
                             descript: " Большой букет роз "),
        Product(id: "5",
                             title: "Букет альстромерии",
                             imageUrl: "Not found",
                             price: 2000,
                             descript: " Большой букет роз "),
        Product(id: "6",
                             title: "Букет лизиантуса",
                             imageUrl: "Not found",
                             price: 3900,
                             descript: " Большой букет роз "),
                                
    ]
    
    var flowersToday: [Product] = [
        Product(id: "1",
                             title: "Букет роз",
                             imageUrl: "Not found",
                             price: 5990,
                             descript: " Большой букет роз "),
        Product(id: "2",
                             title: "Букет ромашек",
                             imageUrl: "Not found",
                             price: 7500,
                             descript: " Большой букет роз "),
        Product(id: "3",
                             title: "Букет лилий",
                             imageUrl: "Not found",
                             price: 3500,
                             descript: " Большой букет роз "),
        Product(id: "4",
                             title: "Букет гвоздики",
                             imageUrl: "Not found",
                             price: 4500,
                             descript: " Большой букет роз "),
        Product(id: "5",
                             title: "Букет альстромерии",
                             imageUrl: "Not found",
                             price: 2000,
                             descript: " Большой букет роз "),
        Product(id: "6",
                             title: "Букет лизиантуса",
                             imageUrl: "Not found",
                             price: 3900,
                             descript: " Большой букет роз "),
                                
    ]
}

