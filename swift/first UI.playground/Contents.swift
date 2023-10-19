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
//struct ColorTest: View {
//    var body: some View {
//        Text("Big red Text")
//            .font(.headline)
//            .foregroundColor(.red)
//            .background(Color.green)
//            .padding()
//            .background(Color.brown)
//    }
//}
//
//PlaygroundPage.current.setLiveView(ColorTest())
//struct Shape: View {
//    var body: some View {
//        Rectangle()
//            .stroke(Color.green, style: StrokeStyle(lineWidth: 4, lineCap: .round))
//            .frame(width: 300.0, height: 300)
//            .padding()
//    }
//}

//PlaygroundPage.current.setLiveView(Shape())

//struct Triangle: Shape {
//    func path(in rect: CGRect) -> Path {
//        var path = Path()
//
//        path.move(to: CGPoint(x: rect.midX, y: rect.minY))
//        path.addLine(to: CGPoint(x: rect.minX, y: rect.maxY))
//        path.addLine(to: CGPoint(x: rect.maxX, y: rect.maxY))
//        path.addLine(to: CGPoint(x: rect.midX, y: rect.minY))
//
//        return path
//    }
//}
//
//Triangle()
//    .stroke(.red, style: StrokeStyle(lineWidth: 10, lineCap: .round, lineJoin: .round))
//    .frame(width: 300, height: 300)
//PlaygroundPage.current.setLiveView(Triangle())

//struct zStack: View {
//    var body: some View {
//        ZStack {
//            HStack{
//                Text("Hello world")
//                VStack{
//                    
//                    Text("i'm big text")
//                        .italic()
//                        .bold()
//                        .font(.system(size: 18))
//                    Circle()
//                }
//            }
//        }.padding()
//    }
//}
//
//
//PlaygroundPage.current.setLiveView(zStack())


var name: String = "Pavel"
var secondName: String = "Ivanov"

func renameUser(_ name: inout String, _ secondName: inout String){
    name = "Fedor"
    secondName = "Jarugin"
    print("My new data : \(name) \(secondName)")
}

renameUser(&name, &secondName)

func cofeeMashion(_ coffee: String, _ waterAmount: Double, _ name: String) -> String {
    return "please mr \(name), this your cofee \(coffee) \(waterAmount) ml"
}

print(cofeeMashion("mocachino", 100, "Faruh"))

func printer(str: inout String,_ closure: (inout String)->()){
    str = str + " jopa"
    closure(&str)
}
var name2 = "piska"
printer(str: &name2, {str -> Void in
    str = str + " sosiska"
    print(str)
})


printer(str: &name, {str -> Void in
    print(str)
    
})

func cigaretteVendingMachine(age: Int, checkAge: (Int) -> Bool){
    if checkAge(age) {
        print("Thank you for purchasing our products, do not forget that smoking is harmful to your health! Have a nice day.")
    } else {
        print("I apologize! But cigarettes are not sold to people under 18!")
    }
}

//func checkPersonAge(age: Int)-> Bool {
//    return age > 18
//}

cigaretteVendingMachine(age: 33, checkAge:{ $0 > 18 })

func salaryEmployee(_ name: String, _ age: Int, _ staff: String, _ salary: Int,_ ammountSalary: (Int)->Int){
    print("Employee \(name), \(age), works as a \(staff) with a salary of $ \(ammountSalary(salary)) a month.")
}

salaryEmployee("ikolay", 39, "developer", 300, { Int(Double($0) * 3.14) })


func joinText(_ hi: String) -> (String) -> String{
    return { return hi + $0 }
}

let clouser = joinText("Hello")

print(clouser(" World"))


var nameUser: String = ""
var secondNameUser: String = ""
var ageUser: String = ""
var readLicenceAcepts: Bool = true

func storeName(_ name: inout String) -> String{
    nameUser = name
    return nameUser
}

func isNameEmpty(_ name: String) -> Bool {
    return !name.isEmpty
   
}


func storeSecondName(_ secondNAme: inout String) -> String{
    secondNameUser = secondName
    return secondNameUser
}

func isSecondNameEmpty(_ secondName:  String) -> Bool{
    return !secondName.isEmpty
}

func isSecondNameEmpty(_ age:  inout String) -> Int{
    ageUser = age
    return Int(ageUser)!
}


func isAgeMoreZero(_ age:  Int) -> Bool {
    if(Int(age) > 0) {
        return true
    }
    return false
}

//////Осталась последняя функция и проверка

func registratAcept(_ accept: inout Bool) -> Bool {
    readLicenceAcepts = accept
    return readLicenceAcepts
}

func isFiledRegisrationEmpty(_ filedReg:  Bool) -> Bool{
    
    return filedReg
}

func registerUser() -> Bool{
    return isNameEmpty("Igor") && isSecondNameEmpty("Krysin") && isAgeMoreZero(15) && isFiledRegisrationEmpty(true)
   
}

print(registerUser())












struct ContentViev: View {
    var body: some View {
        HStack{
            Text("i'm button: ")
            Image(systemName: "text.badge.plus")
                .symbolRenderingMode(.multicolor)
                .foregroundColor(.gray)
                .padding()
        }.padding()
    }
}

PlaygroundPage.current.setLiveView(ContentViev())
