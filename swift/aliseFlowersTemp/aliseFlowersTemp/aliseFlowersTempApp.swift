//
//  aliseFlowersTempApp.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 21.10.2023.
//

import SwiftUI
import Firebase



let screen = UIScreen.main.bounds

@main
struct aliseFlowersTempApp: App {
    
    @UIApplicationDelegateAdaptor private var appDelegate: AppDelegate
    
    var body: some Scene {
        WindowGroup {
            AuthView()
        }
    }
    
    class AppDelegate: NSObject, UIApplicationDelegate {
        func application(_ application: UIApplication,
                         didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
            
            FirebaseApp.configure()
            
            print("OK")
            
            return true
        }
    }
    
}
