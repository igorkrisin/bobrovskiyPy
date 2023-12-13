//
//  DataItem.swift
//  workTimer
//
//  Created by Игорь Крысин on 03.12.2023.
//

import Foundation
import SwiftData
//
@Model
class MyDataItemNew: Identifiable {
    var id: String
    var itemWorkForDataBAse: ItemWorking
   
   
  
    
    init(itemWorkForDataBAse: ItemWorking) {
        self.id = UUID().uuidString
        self.itemWorkForDataBAse = itemWorkForDataBAse
       
        
    }
}

@Model
class MyDataItemTime: Identifiable {
    var id: String
    var timeWork: CGFloat
    
    init(timeWork: CGFloat){
        self.id = UUID().uuidString
        self.timeWork = timeWork
    }
}



//
//@Model
//class Category {
//    @Attribute(.unique) var name: String
//    @Relationship( inverse: \Word.category) var words: [Word] = []
//    
//    init(name: String) {
//        self.name = name
//    }
//}
//
//@Model
//class Word {
//    var original: String
//    var translation: String
//    var category: Category?
//    
//    init(original: String, translation: String) {
//        self.original = original
//        self.translation = translation
//    }
//}
