//
//  AuthService.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 26.10.2023.
//

import Foundation
import Firebase

class AuthService {
    static let shared = AuthService()
    
    private init() { }
    
    private let auth = Auth.auth()
    
    var currentUser: User? {
        return auth.currentUser
    }
    
    func singUp(email: String, 
                password: String,
                completion: @escaping (Result<User, Error>) ->()) {
        auth.createUser(withEmail: email, password: password) { result, error in
            if let result = result {
                let mwUser = MWUser(id: result.user.uid,
                                    name: "",
                                    phone: 0,
                                    adress: "")
                
                DataBaseService.share.setUser(user: mwUser) { resultdb in
                    switch resultdb {
                        
                    case .success(_):
                        completion(.success(result.user))
                    case .failure(let error):
                        completion(.failure(error))
                    }
                }
            } else if let error = error {
                completion(.failure(error))
            }
        }
        
    }
    
    func signIn(email: String,
                password: String,
                completion: @escaping (Result<User, Error>) ->()) {
        
        auth.signIn(withEmail: email, password: password) { result, error in
            if let result = result {
                completion(.success(result.user))
            } else if let error = error {
                completion(.failure(error))
            }
                        
        }
        
    }
}
