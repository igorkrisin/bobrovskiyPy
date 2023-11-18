import SwiftUI


struct MyConsumptionItems: Identifiable, Codable {
    var id: UUID = UUID()
    var name: String
    var type: String
    var amount: Int
}

class ArrayConsunptions: ObservableObject {
    @Published var itemConsumption = [MyConsumptionItems]() {
        didSet {
            let encoder = JSONEncoder()
            if let encoded = try? encoder.encode(itemConsumption) {
                UserDefaults.standard.set(encoded, forKey: "item")
            }
        }
    }
    init() {
        if let items = UserDefaults.standard.data(forKey: "item") {
            let decoder = JSONDecoder()
            if let decoded = try? decoder.decode([MyConsumptionItems].self, from: items) {
                self.itemConsumption = decoded
                return 
            }
        }
    }
}


struct ContentView: View {
    
    @State private var showingAddExpense = false
    @ObservedObject var consumption = ArrayConsunptions()
    
    var body: some View {
        NavigationView {
            List {
                ForEach(consumption.itemConsumption) { item in
                    HStack{
                        VStack(alignment: .leading) {
                            Text(item.name)
                                .font(.title)
                            Text(item.type)
                            
                        }
                        Spacer()
                        Text("₽\(item.amount)")
                        
                    }
                    
                }.onDelete(perform: { indexSet in
                    consumption.itemConsumption.remove(atOffsets: indexSet)
                })
            }
            .navigationTitle("Мои расходы")
            .navigationBarItems(trailing:
                                    Button(action: {
                self.showingAddExpense = true
            }) {
                Image(systemName: "plus")
            }
            )
            .sheet(isPresented: $showingAddExpense) {
                ConsumptionView(expensec: self.consumption)
            }
            
        }
    }
}

#Preview {
    ContentView()
}
