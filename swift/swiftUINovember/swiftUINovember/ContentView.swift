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
//    func move(from source: IndexSet, to destination: Int) //функция перемещения принимает что куда перемещвать
//    {
//        users.move(fromOffsets: source, toOffset: destination) // перемещает элементы
//    }
//}
//
//
//#Preview {
//    ContentView()
//}


//Tab View
struct ContentView: View {

    @State private var selected = 1
    

    var body: some View {
        
        TabView (selection: $selected){
            Text("First page") // отображается на странице
                .tabItem { // элемент управления перехода между страницами (мождификатор)
                    Image(systemName: "1.circle") //то как будет выглядеть элемент
                    Text("first") //то как будет подписан элемент
                } .tag(1) // теги что бы отслеживать какое окно из Item активно
            Text("Second page")
                .tabItem {
                    if selected == 2 {
                        Image(systemName: "2.circle")
                    } else {
                        Text("second")
                    }
                } .tag(2)

        }

    }
    
}


#Preview {
    ContentView()
}
