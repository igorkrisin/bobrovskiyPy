//
//  MainTabBarViewModel.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 26.10.2023.
//

import Foundation
import FirebaseAuth

class MainTabBarViewModel: ObservableObject {
    
    @Published var user: User
    
    init(user: User) {
        self.user = user
    }
}
