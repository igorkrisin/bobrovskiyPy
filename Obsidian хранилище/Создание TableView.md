#swift #TableView #удалениеЯчеек #изменениеЯчеек

Для того что бы контроллер узнал о взаимодействии пользователя с view придумали протокол <mark style="background: #FFB86CA6;">UITableViewDelegate</mark> .

 <mark style="background: #FFB86CA6;">UITableViewDataSourse</mark>  нужен для хранения данных, которые будут переданы  в таблицу

```swift
class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    
    
    //создаем элемент TAbleView
    var myTableView = UITableView()
    let identifire =  "MyCell"
    var array = ["1","2", "3","4", "5", "6", "7", "8", "9"]
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //инициализируем его  чз функцию
        createTable()
       
    }
    
    func createTable() {
        self.myTableView = UITableView(frame: view.bounds, style: .plain)
        //подключаем делегат
        self.myTableView.delegate = self
        self.myTableView.dataSource = self
        
        myTableView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        
        //регестрируем ячейку
        myTableView.register(UITableViewCell.self, forCellReuseIdentifier: identifire)
        
        view.addSubview(myTableView)
    }
    
    //MARK: - UITableViewDataSource
   
    
    //сколько ячеек в каждой секции
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return array.count
    }
    //какие ячейки
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: identifire, for: indexPath)
        
        let number = array[indexPath.row]
        
        cell.textLabel?.text = number
        //добавим на кнопку  значок информации
        cell.accessoryType = .detailButton
        //разукрасим секции
        
        
        return cell
    }

    
    //MARK: - UITableViewDaelegate
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 50
    }
    
    //добавим действия к accesoty
    func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath) {
        print("Accessory path =", indexPath)
        
        let ounerCell = tableView.cellForRow(at: indexPath)
        print("cell title: ", ounerCell?.textLabel?.text ?? "nil")
    }
}

```

так же можно организовать удаление и изменение места ячеек, для этого добавляем NavigationViewController и размещаем на нем item:

[[UIKit Navigation View Controller создание кодом]]

затем добавляем кнопку:

[[Добавить правую или левую кнопку в NavigationViewController]]

в action этой кнопки прописываем:

```swift
@objc func editBtnTapped(_ sender: Any) {
//переводим из режима режактирования в обычный режим и наоборот
        myTableView.isEditing = !myTableView.isEditing
    }
```

**Редактирование** tableView - перемещение ячеек - воспользуемся методом <mark style="background: #FFB86CA6;">canMoveRowAt</mark> и <mark style="background: #FFB86CA6;">moveRowAt</mark>

```swift 
func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
//разрешаем редактирование
        return true
    }
    
    func tableView(_ tableView: UITableView, moveRowAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath) {
    //создаем элементы для редакирования и назначем всем исходные места
        let item = array[sourceIndexPath.row]
        //удаляем элемент со старого места
        array.remove(at: sourceIndexPath.row)
        //устанавливаем на новый
        array.insert(item, at: destinationIndexPath.row)
    }
```


 **Удаление** tableView ячеек воспользуемся методом <mark style="background: #FFB86CA6;">editingStyleForRowAt</mark> и <mark style="background: #FFB86CA6;">commit editingStyle</mark>:

```swift
 func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle {
 //разрешаем удаление
        return .delete
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
    //если стиль удаление
        if editingStyle == .delete {
        //удали из массива
            array.remove(at: indexPath.row)
        //удали из таблицы
            tableView.deleteRows(at: [indexPath], with: .left)
        }
    }
```

