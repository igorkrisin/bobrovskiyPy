//
//  mainTabBar.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct MainTabBar: View {
    
    var viewModel: MainTabBarViewModel
    
    
    
    @State private var isTabViewShow = false
    var body: some View {
        TabView {
            NavigationView {
                CatalogView()
            }
                .tabItem {
                    VStack {
                        Image(systemName: "bag.fill.badge.plus")
                        Text("Каталог")
                    }
                }
            CartView(viewModel: CartViewModel.shared)
                .tabItem {
                    VStack {
                        Image(systemName: "basket.fill")
                        Text("Корзина")
                    }
                }
            ProfileView()
                .tabItem {
                    VStack {
                        Image(systemName: "person.circle")
                        Text("Профиль")
                    }
                }
        }
    }
}

