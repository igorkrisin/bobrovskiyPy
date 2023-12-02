import SwiftUI

struct ListTimeTodayView: View {
    
//    @ObservedObject var dataWork = WorkModel()
    @State var timer: TimerView = TimerView()
    @State var workName: String
    var amountTime: CGFloat = 0
  
    
    var body: some View {
        Text("\(workName)")
        Text("\(timer.amountTimeForWork)")
        
    }
    
    
   
}


