#ios #swift #uikit #UITableViewController

для создания кодом таблицы через UITableViewController пишем код прямо в классе контроллера:


```swift
class ViewController: UIViewController {
    
    let tableViewController = UITableViewController(style: .plain)
    
    var array = ["Jons", "Smit", "Ashly"]
    var myIdentifier = "Cell"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        createTableView()
        addChild(tableViewController)
        view.addSubview(tableViewController.tableView)
        //это для того что бы таблица не вылазила за view
        tableViewController.didMove(toParent: self)
    }

    func createTableView() {
        tableViewController.tableView = UITableView(frame: view.bounds, style: .plain)
        tableViewController.tableView.register(UITableViewCell.self, forCellReuseIdentifier: myIdentifier)
        
        tableViewController.tableView.delegate = self
        tableViewController.tableView.dataSource = self
        
        
    }
}

//delegate и datasorce убираем в extensions 

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return array.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: myIdentifier, for: indexPath)
        
        let item = array[indexPath.row]
        
        cell.textLabel?.text = item
        
        return cell
    }
    
    
}
```

[[Создание indexPath вне методов таблицы]] 

