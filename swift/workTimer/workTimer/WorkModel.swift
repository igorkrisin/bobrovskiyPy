import Combine


final class WorkModel: ObservableObject {
    
    
    
    @Published var nameWork: String = ""
    
    @Published var timeForWork: Int = 100
    
    func printNameWork() {
        print(nameWork)
    }
}

