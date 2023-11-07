//
//  Catalog.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct CatalogView: View {
    let layout = [GridItem(.adaptive(minimum: screen.width / 2.2))]
    @State private var padd: CGFloat = 6
    var body: some View {
        ScrollView(.vertical, showsIndicators: false) {
            Section("Акции") {
                ScrollView(.horizontal, showsIndicators: false) {
                    LazyHGrid(rows: layout, spacing: 15) {
                        ForEach(CatalogViewModel.shared.popularProducts, id: \.id) { item in
                            NavigationLink {
                                let viewModel = ProductDetailViewModel(product: item)
                                ProductDetailView(viewModel:  viewModel)
                            } label: {
                                ProductCell(product: item)
                                    .foregroundColor(.black)
                            }
                        }
                    }.padding(padd)
                }
            }
            Section("Популярные") {
                ScrollView(.horizontal, showsIndicators: false) {
                    LazyHGrid(rows: layout, spacing: 15) {
                        ForEach(CatalogViewModel.shared.popularProducts, id: \.id) { item in
                            NavigationLink {
                                let viewModel = ProductDetailViewModel(product: item)
                                ProductDetailView(viewModel:  viewModel)
                            } label: {
                                ProductCell(product: item)
                                    .foregroundColor(.black)
                            }
                            
                        }
                    }.padding(padd)
                }
            }
            Section("Добавить к заказу") {
                ScrollView(.horizontal, showsIndicators: false) {
                    LazyHGrid(rows: layout, spacing: 15) {
                        ForEach(CatalogViewModel.shared.popularProducts, id: \.id) { item in
                            NavigationLink {
                                let viewModel = ProductDetailViewModel(product: item)
                                ProductDetailView(viewModel:  viewModel)
                            } label: {
                                ProductCell(product: item)
                                    .foregroundColor(.black)
                            }
                            
                        }
                    }.padding(padd)
                    
                }
            }
        }.padding(.leading, 8)
            .navigationBarHidden(true)
    }
}

#Preview {
    CatalogView()
}
