//
//  ContentView.swift
//  swiftUINovember
//
//  Created by Игорь Крысин on 01.11.2023.
//

import SwiftUI
import Foundation

//struct ContentView: View {//slider
//
//    @State private var meter: Double = 0
//    @State private var isOn = false
//    
//    var body: some View {
//        VStack {
//            Slider(value: $meter, in: 0...1000, step: 0.1)
//            Text("km: \(round(meter * 10) / 10), mile: \(meter/1.6)")
//        }.padding()
//      
//    }
//}
//
//#Preview {
//    ContentView()
//}


//struct ContentView: View {//picker
//    var сolors = ["black", "white", "yellow", "green", "red"]
//   @State private var selectedColor = 0
//    
//    var body: some View {
//        VStack {
//            
//            Picker(selection: $selectedColor,  label: Text("color choose")) {
//                ForEach(0..<сolors.count) { index in
//                    Text(self.сolors[index])
//                    
//                }
//            }
//            Text("my choose: \(сolors[selectedColor])")
//        }
//      
//    }
//}
//
//
//#Preview {
//    ContentView()
//}


//
//struct ContentView: View {//stepper
//
//   @State private var age = 0
//    
//    var body: some View {
//        VStack {
//           Stepper("choose age", onIncrement: {
//               age += 1
//               print("age addition 1")
//           }, onDecrement: {
//               age -= 1
//               print("age subtr   1")
//           })
//            Text("age = \(age)")
//           
//        }.padding()
//      
//    }
//}
//
//
//#Preview {
//    ContentView()
//}

//
//struct ContentView: View {//picker
//  
//   @State private var age = 0
//    
//    var body: some View {
//        VStack {
//           Stepper("choose age", onIncrement: {
//               age += 1
//               print("age addition 1")
//           }, onDecrement: {
//               if age > 0 {
//                   age -= 1
//                   print("age subtr   1")
//               }
//           })
//            Text("age = \(age)")
//           
//        }.padding()
//      
//    }
//}
//
//
//#Preview {
//    ContentView()
//}



//struct ContentView: View {//нажатия
//  
//   @State private var age = 0
//    
//    var body: some View {
//        VStack {
//           Text("Tap me")
//                .onTapGesture {
//                    print("Tapped")
//                }
//           
//        }.padding()
//      
//    }
//}
//
//
//#Preview {
//    ContentView()
//}
//
//struct ContentView: View {//жесты
//  
//   @State private var age = 0
//    
//    var body: some View {
//        VStack {
//            Text("Hello")
//                .gesture(
//                    DragGesture(minimumDistance: 50)
//                        .onEnded{ _ in
//                            print("dragged")
//                        }
//                    )
//        }
//        Image("flowers")
//            .resizable()
//            .aspectRatio(contentMode: .fit)
//    }
//}
//
//
//#Preview {
//    ContentView()
//}
//

//список Статический
//struct MusicRow:View {//как выглядит одна строка списка (каждый ряд списка)
//    var name: String
//    var body: some View {
//        Text("This music is \(name)")// передаем в строку свойство
//    }
//}
//
//struct ContentView: View {// создаем экземпляры одной строки MusicRow и заполняем список
//    var body: some View {
//        List {
//            MusicRow(name: "Rap")
//            MusicRow(name: "Classic")
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}


//список Динамический

//1 создаем структуру подписаную на Identifiable, что бы каждая строка могла иметь свой ID
//struct Pharmacy: Identifiable {
//   var id = UUID()
//    var name: String
//}
//
////2 Создаем структуру каждого ряда
//struct PharmacyRaw: View {
//    var pharmacy: Pharmacy
//    var body: some View {
//        Text("buy medical in \(pharmacy.name)")// передаем свойство name Pharmacy экземпляра.
//    }
//}
//
////3 Далее выводим на экран строки из массива
//struct ContentView: View {
//    var body: some View {
//        var gorZdrav = Pharmacy(name: "Gor Zdrav") //создаем экземпляры Pharmacy
//        var FirstHelp = Pharmacy(name: "First Help")
//        var pharmacies = [gorZdrav, FirstHelp] //помещаем их в массив
//        return List(pharmacies) { pharmacy in //возврашаем при помощи замыкания элемены массива динамически
//            PharmacyRaw(pharmacy: pharmacy)
//            
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}


//List с секциями

//struct Task:  View{
//    var body: some View {
//        Text("Some Task")
//    }
//}
//
//
////3 Далее выводим на экран строки из массива
//struct ContentView: View {
//    var body: some View {
//        List{
//            Section(header: Text("important task")){
//                Task()
//                Task()
//                Task()
//            }
//            Section(header: Text("Other task")){
//                Task()
//                Task()
//                Task()
//            }
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}



//// NavigationView
//struct ContentView: View {
//    var body: some View {
//        
//        NavigationView {
//            Text("SwiftUI")
//                .navigationBarTitle("Information", // создаем Заголовок навигации
//                                    displayMode: .inline)//распологаем его в нужном месте
//                .navigationBarItems(trailing: //создаем элементы навигации
//                                        HStack {
//                    Button("Help") {
//                        print("Help tapped")
//                    }
//                    Button("Menu") {
//                        print("Menu tapped")
//                    }
//                }
//                )
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}

// NavigationView удаление и перемещение элементов в List

////УДАЛЕНИЕ из LIST
//struct ContentView: View {
//    
//    @State private var users = ["Maria", "Igor", "Ivan"]
//    
//    var body: some View {
//        
//        NavigationView {
//            List {
//                ForEach(users, id: \.self) { user in //перебираем все элементы и вывожи на экран
//                    Text(user)
//                } .onDelete(perform: { indexSet in
//                    users.remove(atOffsets: indexSet) // удаление элементов List
//                })
//            }
//           
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}

//ПЕРЕМЕЩЕНИЕ в LIST
//struct ContentView: View {
//    
//    @State private var users = ["Maria", "Igor", "Ivan"]
//    
//    var body: some View {
//        
//        NavigationView {
//            List {
//                ForEach(users, id: \.self) { user in //перебираем все элементы и выводим на экран
//                    Text(user)
//                } .onMove(perform: move ) // передаем в модификатор функцию move из 320 строки
//            }
//            .navigationBarItems(trailing: EditButton()) //кнопка Edit для входа в режим перемещения элементов
//        }
//    }
//    func move(from source: IndexSet, to destination: Int) //функция перемещения принимает что куда перемещать
//    {
//        users.move(fromOffsets: source, toOffset: destination) // перемещает элементы
//    }
//}
//
//
//#Preview {
//    ContentView()
//}


//Tab View переход между страницами
//struct ContentView: View {
//
//    @State private var selected = 1
//    
//
//    var body: some View {
//        
//        TabView (selection: $selected){
//            Text("First page") // отображается на странице
//                .tabItem { // элемент управления перехода между страницами (мождификатор)
//                    Image(systemName: "1.circle") //то как будет выглядеть элемент
//                    Text("first") //то как будет подписан элемент
//                } .tag(1) // теги что бы отслеживать какое окно из Item активно
//            Text("Second page")
//                .tabItem {
//                    if selected == 2 {
//                        Image(systemName: "2.circle")
//                    } else {
//                        Text("second")
//                    }
//                } .tag(2)
//
//        }
//
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}

//
//struct ContentView: View {
//
//    @State private var colors = ["red", "green", "blue"]
//    @State private var selectColor = 0
//    @State private var additionalSettings = false
//    
//    
//    var body: some View {
//        NavigationView {
//            Form {
//                Picker(selection: $selectColor, label: Text("Select a color")) {
//                    ForEach(0..<colors.count, id: \.self){selectColor in
//                        Text(self.colors[selectColor])
//                    }
//                }.pickerStyle(SegmentedPickerStyle())
//                
//                Toggle(isOn: $additionalSettings) {
//                    Text("Additional Setting")
//                }
//                Button(action: {
//                    //
//                }) {
//                    Text("Save changes")
//                }.disabled(additionalSettings)//отключение кнопки при помозщи модификатора
//            }.navigationBarTitle("Settings")
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}

////ALERT!
//
//struct ContentView: View {
//
//    @State private var showingAlert1 = false
//    @State private var showingAlert2 = false
//
//    var body: some View {
//        
//        HStack {
//            Button("Show1") {
//                self.showingAlert1 = true
//            } .alert(isPresented: $showingAlert1) {
//                Alert(title: Text("One"), message: nil,
//                      dismissButton: .cancel())
//            }
//            Button("Show2") {
//                self.showingAlert2 = true
//            } .alert(isPresented: $showingAlert2) {
//                Alert(title: Text("Two"), message: nil,
//                      dismissButton: .cancel())
//            }
//        }
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}

//ALERT! с действием
//
//struct ContentView: View {
//
//    @State private var showingAlert = false
//  
//    var body: some View {
//        
//        HStack {
//            Button(action: {
//                self.showingAlert = true
//            }
//                   , label: {
//                Text("Show alert")
//            }
//            ).alert(isPresented: $showingAlert) {
//                Alert(title: Text("Are you sure you want to delete this"), message: Text("There is now way back"), primaryButton:
//                        .destructive(Text("Delete")) {
//                            print("deleting ... ") // выполняем действие по кнопке Delete
//                        }, secondaryButton: .cancel())
//            }
//        }
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}


//модификаторы с условием!
//
//struct ContentView: View {
//
//    @State private var useGreen = false // cоздаем bool и исполльзуем его в тернарнике
//
//    var body: some View {
//        Button("Hello"){
//            self.useGreen.toggle()
//        } .foregroundColor(useGreen ? .green : . red) // при нажатии меняется цвет кнопки
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}
//

//рефакторинг модификаторов за счет выноса в отдельную структуру


//struct CustomModofier: View {
//    var name: String // создаем cвойство которое будем модифицировать
//    var body: some View {
//        Text(name)// во вью текст передаем свойство name и пишем к нему модификаторы
//            .font(.largeTitle)
//            .padding()
//            .foregroundColor(.red)
//            .background(Color.green)
//    }
//}
//
//struct ContentView: View {
//
//    @State private var useGreen = false
//  
//    var body: some View {
//        CustomModofier(name: "Text1") //передаем сразу объекты CustomModidier и в свойсво name переваем строку
//        CustomModofier(name: "Text2")
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}

//Создание собственного модификатора и добавление модификаторов в extension

//struct CustomModifier: ViewModifier { //собственный модификатор
//    func body(content: Content) -> some View {
//        content
//            .font(.largeTitle)
//            .foregroundColor(.red)
//            .padding()
//            .background(Color.green)
//    }
//}
//
//
//
//struct ContentView: View {
//    var body: some View {
//       Text("hello")
//            .modifier(CustomModifier())
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}


// расширяем View при помощи extension



//struct CustomModifier: ViewModifier { //собственный модификатор
//    func body(content: Content) -> some View {
//        content
//            .font(.largeTitle)
//            .foregroundColor(.red)
//            .padding()
//            .background(Color.green)
//    }
//}
//
//// добавляем extension
//extension View {
//    func customM() -> some View {
//        self.modifier(CustomModifier())
//    }
//}
//
//struct ContentView: View {
//    var body: some View {
//       Text("hello")
//            .customM() // добавляем свой метод в качестве модификатора
//    }
//    
//}
//
//
//#Preview {
//    ContentView()
//}


//ObservableObject, Piblished, ObservedObject

//@ObservableObject - на этот протокол подписывается class, который будет делиться изменяемым свойством,
//внутри этого протокола изменяемое св-во оборачивается property Wrapper @Published
//внутри другого вью создаем объект изменяемого класса с изменяемым св-ом
//и оборачиваем property wrapper @ObservedObject
// "@EnvironmentObject - wrapper property, применяется для того что бы данное свойтво могли изменять все структуры

//class Count: ObservableObject { // создаем класс и подписываем на ObservableObject
//    @Published var count: Int = 0 // свойство оборачиваем @Published
//}
//
//struct ContentView: View {
//    @ObservedObject var count = Count() // оборачиваем объект класса Count в @ObservedObject
//    @State var strCount: String = "0"
//    var body: some View {
//        VStack{
//            Button("count++ \n \(count.count)") {
//                count.count += 1 // свойство из класса меняется в структуре ContentView
//            }
//            TextField("enter count: ", text:  $strCount)
//                .padding()
//            
//            Text("your number \(strCount)")
//        }
//    }
//    
//   
//}
//
//
//#Preview {
//    ContentView()
//}

// переход между view при помощи Navigation link

//1 делаем вьторой экран
//
//struct DetailView: View {
//    var body: some View {
//        Text("Some detail")
//    }
//}
//
//struct ContentView: View {
//
//    var body: some View {
//        NavigationView { //создаем view перехода
//            VStack {
//                NavigationLink(destination: DetailView()) { //ссылка указывает на какаое view переходим
//                    Text("show detail") // как выглядит переход (кнопка, картинка, текст)
//                } .navigationTitle("Hello detail") // заголовок страницы навигации
//                
//            }
//        }
//    }
//}
//
//
//#Preview {
//    ContentView()
//}
//

// переход между view при помощи Navigation link и списка в нем

//1 идентефицируем каждый ряд в списке

//struct Dog:Identifiable {
//    var id = UUID()
//    var name: String
// }
//
////2 Определяем  структуру одного ряда в строчке
//
//struct DogRow: View {
//    var dog: Dog //создаем объкт одного ряда
//    var body: some View {
//        Text(dog.name) //отрисовываем свойствo name
//    }
//}
////3 Определяем структуру ContentView
//
//struct ContentView: View {
//
//    var body: some View {
//        let first = Dog(name: "Sobaka")//создаем один элемент для хранения в списке
//        let second = Dog(name: "Palkan")
//        let dogs = [first, second] // кладем его в массив
//        return NavigationView { // возвращаем из body NavigationView
//
//            List(dogs) { dog in //складываем в список массив и перебираем в замыкании элементы массива
//// 5 добавялем cозданную в 4 пункте DogView в NavigationLink
//                NavigationLink(destination: DogView(dog: dog)) {
//                    DogRow(dog: dog) // и каждый объкт выводим в виде одной строки свойства dog объкта DogRow
//                }
//            }
//        }
//    }
//}
//
////4 Создаем структуру DogView (то, что отрисуется после перехода на DogRow)
//
//struct DogView: View {
//    var dog: Dog
//    var body: some View {
//        Text("Come and choose a \(dog.name)")
//    }
//}
//
//
//
//#Preview {
//    ContentView()
//}
//

// переход между view при помощи Sheet - shhet закрывается оттягиванием вниз
//
//struct DetailView: View {
//    var body: some View {
//        Text("Detail")
//    }
//}
//
//
//struct ContentView: View {
//    
//    @State private var showingDetail = false
//    
//    var body: some View {
//        VStack {
//            Button(action: { // кнопка переключает showingDetail
//                self.showingDetail.toggle()
//            }) {
//                Text("Show detail")
//            } .sheet(isPresented:  $showingDetail, content: { //когда showingDetail true показываес sheet
//                DetailView()//отрисовываем DeatailView на страничке Sheet
//            })
//        }
//    }
//}
//
////4 Создаем структуру DogView (то, что отрисуется после перехода на DogRow)
//
//
//
//
//#Preview {
//    ContentView()
//}
//


// переход между view при помощи Sheet - sheet закрывается оттягиванием вниз и по кнопке

struct DetailView: View {
    
    @Environment (\.presentationMode) var presentanionMode//добавляем перемнную с propertyWrap Environmment
    
    var body: some View {
        VStack {
            Text("Detail")
            Button("Back") {
                self.presentanionMode.wrappedValue.dismiss()//добавляем кнопку скрытия обращаемся к переменной и освобождаем модальное окно 
            }
        }
        
       
    }
}


//struct ContentView: View {
//    
//    @State private var showingDetail = false
//    
//    var body: some View {
//        VStack {
//            Button(action: {
//                self.showingDetail.toggle()
//            }) {
//                Text("Show detail")
//            } .sheet(isPresented:  $showingDetail, content: {
//                DetailView()
//            })
//        }
//    }
//}
//
////4 Создаем структуру DogView (то, что отрисуется после перехода на DogRow)
//
//
//
//
//#Preview {
//    ContentView()
//}


//Хранение двнных UserDefaults после перезапуска приложения данные не обнуляются

//struct ContentView: View {
//    //достаем данные из сохраненных в UserDefaults
//    @State private var tapCount = UserDefaults.standard.integer(forKey: "Tap")
//    
//    var body: some View {
//        VStack {
//            Button("tap count: \(tapCount)") {
//                tapCount += 1
//            //добаволяем данные в UserDefaults
//                UserDefaults.standard.set(self.tapCount, forKey: "Tap")
//            }
//        }
//    }
//}
//
//
//
//
//
//#Preview {
//    ContentView()
//}

//Архивирование данных при помощи протокола Codable и кодировнание при помоши JsonEncoder
//Хранение данных UserDefaults после кодировки в Json
//Работа с более сложными типами данных

struct User: Codable { // подписываем двнные на Codable, что бы заархивировать их
    var firstName: String
    var secondName: String
}

struct ContentView: View {
    //создаем объект User и делаем его наблюдаемым
    @State private var user = User(firstName: "Ivan", secondName: "Petrov")
    
    var body: some View {
        VStack {
            Button("save user") {
                let encoder = JSONEncoder()
                
                if let data = try? encoder.encode(self.user) {
                    UserDefaults.standard.setValue(data, forKey: "UserData")
                }
            }
        }
    }
}





#Preview {
    ContentView()
}
