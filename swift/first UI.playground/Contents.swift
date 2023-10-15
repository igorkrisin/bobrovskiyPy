import SwiftUI
import PlaygroundSupport
import Foundation


//struct CountDrink: View{
//    @State private var countCoffee: Int = 0
//    @State private var countCoctail: Int = 0
//    @State private var countTea: Int = 0
//    
//    //let picture = String(UnicodeScalar(0x1F34E))
//    var body: some View {
//        
//        VStack {
//            Button(action: { countCoffee += 1 }, label: {
//                Text(" \u{2615} Cofee: \(countCoffee)")
//                    .padding()
//            })
//            Button(action: { countCoctail += 1 }, label: {
//                Text("\u{1F378} Coctail: \(countCoctail)")
//                    .padding()
//            })
//            Button("\u{1F375} Tea: \(countTea)") { countTea += 1 }
//                    .padding()
//            
//        }
//        
//    }
//}
//
//PlaygroundPage.current.setLiveView(CountDrink())

//struct ConvertInchesToCentimeters: View {
//    @State var inshes: Double = 0.0
//    var body: some View{
//        
//        VStack{
//            Slider(value: $inshes, in: 0...100, step: 0.1)
//                .accentColor(Color.red)
//                .border(Color.red, width: 1)
//                .frame(width: 300)
//            Text("\(inshes, specifier: "%.2f") inches is \(inshes*2.54, specifier: "%.2f") inshes")
//                .italic()
//                .bold()
//                .font(.system(size: 12))
//        }
//    }
//}
//
//PlaygroundPage.current.setLiveView(ConvertInchesToCentimeters())
struct ColorTest: View {
    var body: some View {
        Text("Big red Text")
            .font(.headline)
            .foregroundColor(.red)
            .background(Color.green)
            .padding()
            .background(Color.brown)
    }
}

PlaygroundPage.current.setLiveView(ColorTest())
