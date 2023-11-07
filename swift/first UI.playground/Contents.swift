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


//var name: String = "Pavel"
//var secondName: String = "Ivanov"
//
//func renameUser(_ name: inout String, _ secondName: inout String){
//    name = "Fedor"
//    secondName = "Jarugin"
//    print("My new data : \(name) \(secondName)")
//}
//
//renameUser(&name, &secondName)
//
//func cofeeMashion(_ coffee: String, _ waterAmount: Double, _ name: String) -> String {
//    return "please mr \(name), this your cofee \(coffee) \(waterAmount) ml"
//}
//
//print(cofeeMashion("mocachino", 100, "Faruh"))
//
//func printer(str: inout String,_ closure: (inout String)->()){
//    str = str + " jopa"
//    closure(&str)
//}
//var name2 = "piska"
//printer(str: &name2, {str -> Void in
//    str = str + " sosiska"
//    print(str)
//})
//
//
//printer(str: &name, {str -> Void in
//    print(str)
//    
//})
//
//func cigaretteVendingMachine(age: Int, checkAge: (Int) -> Bool){
//    if checkAge(age) {
//        print("Thank you for purchasing our products, do not forget that smoking is harmful to your health! Have a nice day.")
//    } else {
//        print("I apologize! But cigarettes are not sold to people under 18!")
//    }
//}
//
////func checkPersonAge(age: Int)-> Bool {
////    return age > 18
////}
//
//cigaretteVendingMachine(age: 33, checkAge:{ $0 > 18 })
//
//func salaryEmployee(_ name: String, _ age: Int, _ staff: String, _ salary: Int,_ ammountSalary: (Int)->Int){
//    print("Employee \(name), \(age), works as a \(staff) with a salary of $ \(ammountSalary(salary)) a month.")
//}
//
//salaryEmployee("ikolay", 39, "developer", 300, { Int(Double($0) * 3.14) })
//
//
//func joinText(_ hi: String) -> (String) -> String{
//    return { return hi + $0 }
//}
//
//let clouser = joinText("Hello")
//
//print(clouser(" World"))
//
//var nameUser: String = ""
//var secondNameUser: String = ""
//var ageUser: String = ""
//var readLicenceAcepts: Bool = true
//
//func storeName(_ name: inout String) -> String{
//    nameUser = name
//    return nameUser
//}
//
//func isNameEmpty(_ name: String) -> Bool {
//    return !name.isEmpty
//}
//
//func storeSecondName(_ secondNAme: inout String) -> String{
//    secondNameUser = secondName
//    return secondNameUser
//}
//
//func isSecondNameEmpty(_ secondName:  String) -> Bool{
//    return !secondName.isEmpty
//}
//
//func isSecondNameEmpty(_ age:  inout String) -> Int{
//    ageUser = age
//    return Int(ageUser)!
//}
//
//func isAgeMoreZero(_ age:  Int) -> Bool {
//    if(Int(age) > 0) {
//        return true
//    }
//    return false
//}
//
//func registratAcept(_ accept: inout Bool) -> Bool {
//    readLicenceAcepts = accept
//    return readLicenceAcepts
//}
//
//func isFiledRegisrationEmpty(_ filedReg:  Bool) -> Bool{
//    
//    return filedReg
//}
//
//func registerUser() -> Bool{
//    return isNameEmpty("Igor") && isSecondNameEmpty("Krysin") && isAgeMoreZero(15) && isFiledRegisrationEmpty(true)
//}
//
//print(registerUser())
//
//
//
//
//
//
//
//
//
//
//
////
////struct ContentViev: View {
////    var body: some View {
////        HStack{
////            Text("i'm button: ")
////            Image(systemName: "text.badge.plus")
////                .symbolRenderingMode(.multicolor)
////                .foregroundColor(.gray)
////                .padding()
////        }.padding()
////    }
////}
////
////PlaygroundPage.current.setLiveView(ContentViev())
////
////
//
//struct ChessPlayer {
//    var name: String
//    var nickName: String = "fuck"
//    var age: Int = 12
//    var victory: Int?
//    var defeat: Int?
//    
////    init(name: String, nickName: String, age: Int, victory: Int, defeat: Int) {
////        self.name = name
////        self.nickName = nickName
////        self.age = age
////        self.victory = victory
////        self.defeat = defeat
////    }
//    
//    init() {
//        self.name = "name"
//    }
//    
//    func printName() {
//        print(self.name)
//    }
//    
//}
//
////var kostjaChess: ChessPlayer = ChessPlayer(name: "kostja", nickName: "Shark", age: 18, victory: 2, defeat: 22)
////
////kostjaChess.printName()
////print(kostjaChess.name)
//
//var fedja: ChessPlayer = ChessPlayer()
//fedja.name = "fefo"
//fedja.age = 18
//fedja.nickName = "Fefo"
//fedja.victory = 4
//fedja.defeat = 1
//fedja.printName()

class Car {
    var gas: Int
    init(gas: Int) {
        self.gas = gas
    }
    
    func driveForward() {
        print("Car drive to forward")
    }
}
    

var car = Car(gas: 45)
car.driveForward()

//
//class CashbackCalculator { // 1. Объявили класс
//    var startValue = 0 // 2. Сделали рабочее поле
// 
//// 3. Объявляем методы для экземпляра (не static)
//    func increaseWithConstant() { // функция увеличивает startValue на фикс. значение (1)
//        startValue += 1
//    }
//    func increase(by value: Int) { // функция увеличивает startValue на фикс. значение (value)
//        startValue += value
//    }
//    func zerofy() { // функция обнуляет startValue
//        startValue = 0
//    }
//}
//
//
//var myWallet: CashbackCalculator = CashbackCalculator()
//
//myWallet.increase(by: 100)
//myWallet.increaseWithConstant()
//myWallet.zerofy()
//
//
//
//struct TimesTable {
//    let multiplier: Int
//    subscript(index: Int) -> Int {
//        return multiplier * index // видите? Сабскрипт не будет работать без этого поля
//    }
//}
//
//let firstNumber = 3
//let secondNumber = 6
//let threeTimesTable = TimesTable(multiplier: firstNumber) // а вот и наша зависимость на практике
//print("\(firstNumber) умножить на \(secondNumber) будет \(threeTimesTable[6])")
//print(threeTimesTable[4])
//
//
//struct AdditionTables {
//    let additionNum: Int
//    subscript(num: Int) -> Int {
//        return additionNum + num
//    }
//}
//
//let five : Int = 5
//let additionFive = AdditionTables(additionNum: five)
//print(additionFive[6])
//
//
//

// Создаём переменные для данных о пользователе
var name: String = ""
var surname: String?
var age: Int = 0
var agree: Bool = false
 
// Создаём функции, которые будут принимать данные о пользователе и сохранять в переменные
func enterName(text: String) {
    name = text
}
 
func enterSurname(text: String) {
    surname = text
}
 
func enterAge(number: Int) {
    age = number
}
 
func enterAgreement(value: Bool) {
    agree = value
}
 
// Валидируем введённые данные через отдельные функции
func validateName() -> Bool {
    name.isEmpty == false
}
 
func validateSurname() -> Bool {
    true
}
 
func validateAge() -> Bool {
    age > 0
}
 
func validateAgreement() -> Bool {
    agree
}
// Проверяем данные пользователя и возвращаем флаг Bool, который говорит об успешной регистрации
func registerUser() -> Bool {
    if !validateName() {
        print("Проверьте введенное имя")
        return false
    }
    if !validateSurname() {
        print("Проверьте введенную фамилию")
        return false
    }
    if !validateAge() {
        print("Возраст должен быть больше 0")
        return false
    }
    if !validateAgreement() {
        print("Вы должны согласиться с лицензионным соглашением")
        return false
    }
    return true
}
 
 
// Вводим данные пользователя и проверяем, что регистрация проходит успешно
enterName(text: "")
enterSurname(text: "Ivanov")
enterAge(number: 15)
enterAgreement(value: true)
if registerUser() {
    print("Вы успешно зарегистрированы!")
}


struct Student {
    var name: String
    var secondName: String
    var univerity: String
    var facultet: String
    var arrangeNote: Int
}

var student1: Student = Student(name: "Igor", secondName: "Krysin", univerity: "KGSHA", facultet: "MSH", arrangeNote: 3)
var student2: Student = Student(name: "Lena", secondName: "Smirniv", univerity: "KGSHA", facultet: "MSH", arrangeNote: 3)

print(student1)
print(student2)

class Spotsman {
    var name: String
    var age: Int
    var place: Int
    
    func printName() {
        print(self.name)
    }
    
    init(name: String, age: Int, place: Int) {
        self.name = name
        self.age = age
        self.place = place
    }
}

class Runner: Spotsman {
    var amountTournirce: Int
    var arrangePlace: Int {
        return amountTournirce / place
    }
    
    override func printName() {
        print("myname: ", self.name)
    }
    init(name: String, age: Int, place: Int, amountTournirce: Int) {
        self.amountTournirce = amountTournirce
        super.init(name: name, age: age, place: place)
       
    }
    
    func printPlace() {
        print(self.amountTournirce)
    }
    
    
}

var run = Runner(name: "Igor", age: 24, place: 2, amountTournirce: 4)
run.printName()


class Calculator {
    var numb1: Int
    var numb2: Int
    
    init(numb1: Int, numb2: Int) {
        self.numb1 = numb1
        self.numb2 = numb2
    }
    
    func wordCalculator(numb1: Int, numb2: Int, toDo: String) {
        switch toDo{
        case "add":
            addition(numb1: numb1, numb2: numb2)
        case "sub":
            substraction(numb1: numb1, numb2: numb2)
        case "div":
            division(numb1: numb1, numb2: numb2)
        case "mul":
            multiplication(numb1: numb1, numb2: numb2)
        default:
            print("command not found")
            break
        }
    }
    
    private func addition(numb1: Int, numb2: Int) -> Int {
        return numb1 + numb2
    }
    
    private func substraction(numb1: Int, numb2: Int) -> Int {
        return numb1 - numb2
    }
    
    private func division(numb1: Int, numb2: Int) -> Int {
        return numb1 / numb2
    }
    
    private func multiplication(numb1: Int, numb2: Int) -> Int {
        return numb1 * numb2
    }
}


var value: Calculator = Calculator(numb1: 2, numb2: 3)

value.wordCalculator(numb1: 2, numb2: 3, toDo: "sub")


struct PuzzleStruct {
    let babyYears: Int
    
    
}

enum Puzzle {
    case baby(numberOfPieces: Int)
    case toddler(numberOfPieces: Int)
    case preschooler(numberOfPieces: Int)
    case gradeschooler(numberOfPieces: Int)
    case teenager(numberOfPieces: Int)
}

let player: Puzzle = .baby(numberOfPieces: 3)

//let player2: PuzzleStruct = PuzzleStruct(numberOfPieces: 3)

func iconName(for fileExtension: String) -> String {
    switch fileExtension {
    case "jpg": return "assetIconJpeg"
    case "bmp": return "assetIconBitmap"
    case "gif": return "assetIconGif"
    default: return "assetIconUnknown"
    }
}
iconName(for: "jpg")






























