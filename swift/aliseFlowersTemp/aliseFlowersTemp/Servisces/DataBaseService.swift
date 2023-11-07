//
//  DataBaseSetvice.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 27.10.2023.
//

import Foundation
import FirebaseFirestore


class DataBaseService {
    static let share = DataBaseService()
    
    private var db = Firestore.firestore()
    
    private var usersRef: CollectionReference {
        return db.collection("users")
    }
    
    private init() { }
    
    func setUser(user: MWUser, completion: @escaping(Result<MWUser, Error>) -> ()) {
        
        usersRef.document(user.id).setData(user.representation) { error in
            if let error = error {
                completion(.failure(error))
            } else {
                completion(.success(user))
            }
        }
        
    }
}
