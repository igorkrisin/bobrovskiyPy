import Combine
import Foundation


final class WorkModel: ObservableObject {

    @Published var nameWork: String = ""
    
  
    
    func printNameWork() {
        print(nameWork)
    }
}

