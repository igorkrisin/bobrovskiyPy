#DataSource #delegate #отдельныеФайлы 

например мы делаем почтовый клиент и используем UITable для отображения входящих писем пользователя в <mark style="background: #FFB86CA6;">InboxViewController</mark>

```swift 
extension InboxViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView,
                   numberOfRowsInSection section: Int) -> Int {
        return messages.count
    }

    func tableView(_ tableView: UITableView,
                   cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let message = messages[indexPath.row]
        let cell = tableView.dequeueReusableCell(
            withIdentifier: "message",
            for: indexPath
        )

        cell.textLabel?.text = message.title
        cell.detailTextLabel?.text = message.preview

        return cell
    }
}```

Этот подход хорош для простых view controller'ов не содержащих большого количества логики. Но все станет более запутанным, если наш контроллер будет выполнять множество других задач или мы хотим переиспользовать логику dataSource в других частях нашего приложения.

Например нам понадобится отображать  сообщения в разных частях приложения, например в отправленных, архивированных, в черновиках или папках писем. В такой ситуации переиспользование DataSource кода может быть реально полезной, поскольку это позволяет очень быстро создавать пользовательские интерфейсы основанные на той же модели данных.

Один из способов сделать это - просто переместить всю логику data source из нашего контроллера в отдельные классы и что бы их классы соответствовали  <mark style="background: #BBFABBA6;">UITableViewDataSource</mark>

```swift
class MessageListDataSource: NSObject, UITableViewDataSource {
    //мы создаем это публичным, что бы data source мог измнятся
    //по мере поступления новых данных
    var messages: [Message]

    init(messages: [Message]) {
        self.messages = messages
    }

    func tableView(_ tableView: UITableView,
                   numberOfRowsInSection section: Int) -> Int {
        return messages.count
    }

    func tableView(_ tableView: UITableView,
                   cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let message = messages[indexPath.row]
        let cell = tableView.dequeueReusableCell(
            withIdentifier: "message",
            for: indexPath
        )

        cell.textLabel?.text = message.title
        cell.detailTextLabel?.text = message.preview

        return cell
    }
}
```


Преимущество такого метода в том, что мы можем легко и быстро создавать новые UI (user interface) и функции из строительных блоков. Так же как и с дочерними View Controller элементы  становятся проще понимать и дорабатывать, если они разбиты на отдельные части, что бы они могли работать в большей изоляции.

Разбиение классов на части поможет избежать их массивности, но ингода это может привести к дублированию кода, хотя дублирование не обязательно плохо, иногла небольшое дублирование лучше, чем создание небольших абстракций, которые сложно настроить.

Когда дело доходит до таблиц или коллекций мы хотим что бы точно такие же задачи были для всех похожих моделей. Мы хотим показывать одну и ту же  клетку для каждого экземпляра модели. И нам всегда нужно выполнять одно и то же dequeueing для каждого типа данных.

Вместо реализации, специально привязанной к отрисовке модели сообщенний , создадим универсалный класс который может отрисовывать любые модели, учитывая идентификатор повторного использования ячейки и замыкание которое настраивает ячейку табличного представления для данной модели.

```swift

class TableViewDataSource<Model>: NSObject, UITableViewDataSource {
    typealias CellConfigurator = (Model, UITableViewCell) -> Void

    var models: [Model]

    private let reuseIdentifier: String
    private let cellConfigurator: CellConfigurator

    init(models: [Model],
         reuseIdentifier: String,
         cellConfigurator: @escaping CellConfigurator) {
        self.models = models
        self.reuseIdentifier = reuseIdentifier
        self.cellConfigurator = cellConfigurator
    }
}
```
Теперь мы можем реализовывать UITableVievDataSource без каких либо знаний о деталях реализации модели, просто используя массив модели и настраивающего ячейку замыкания, которое было введено в инициализатор нашего DataSource (источника данных):

```swift
func tableView(_ tableView: UITableView,
               numberOfRowsInSection section: Int) -> Int {
    return models.count
}

func tableView(_ tableView: UITableView,
               cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let model = models[indexPath.row]
    let cell = tableView.dequeueReusableCell(
        withIdentifier: reuseIdentifier,
        for: indexPath
    )

    cellConfigurator(model, cell)

    return cell
}
```

Теперь, когда нам нужен DataSource для отображения массива моделей мы можем просто создать экземпляр TableViewDataSource, например что бы заменить наш вышеописаный MessageListDataSource:

```swift
func messagesDidLoad(_ messages: [Message]) {
    let dataSource = TableViewDataSource(
        models: messages,
        reuseIdentifier: "message"
    ) { message, cell in
        cell.textLabel?.text = message.title
        cell.detailTextLabel?.text = message.preview
    }

    // Нам также необходимо сохранять строгую ссылку на источник данных, 
    // поскольку UITableView использует для него только слабую ссылку.
    self.dataSource = dataSource
    tableView.dataSource = dataSource
}

```

И самое интересное, что теперь мы можем использовать тот же класс для рендеринга любых других моделей, которые у нас скорее всего есть - черновики, контакты и тд и мв можем добавить статические удобные методы, что бы упростить создание Data source для наших моделей.

```swift 
extension TableViewDataSource where Model == Message {
    static func make(for messages: [Message],
                     reuseIdentifier: String = "message") -> TableViewDataSource {
        return TableViewDataSource(
            models: messages,
            reuseIdentifier: reuseIdentifier
        ) { (message, cell) in
            cell.textLabel?.text = message.title
            cell.detailTextLabel?.text = message.preview
        }
    }
}
```

Добавление таких удобных методов не только еще больше уменьшает необходимость дублировать код, но и позволяет создавать нам data source с использованием точечного синтаксиса:

```swift

func messagesDidLoad(_ messages: [Message]) {
    dataSource = .make(for: messages)
    tableView.dataSource = dataSource
}
```

Изменения, подобные приведенным выше, на первый взгляд могут показаться чисто косметическими, но на самом деле они могут оказать большое положительное влияние на производительность разработчиков, особенно когда мы работаем над приложением, требующим быстрых итераций и экспериментов, поскольку создание большинства источников данных больше не является большой проблемой.

Если мы захотим реализовать несколько источников, каждый со своим типом данных, например в нашем почтовом приложении реализуем <mark style="background: #FFF3A3A6;">HomeViewController</mark>, который показывает пользователю список последних контактов, а также самые популярные сообщения из почтового ящика пользователя.

Хотя это можно сделать с помощью нового выделенного объекта, который принимает все данные для главного экрана и предоставляет их через специальную реализацию <mark style="background: #BBFABBA6;">UITableViewDataSource</mark>, давайте попробуем использовать композицию для объединения нескольких небольших Data source вместе, чтобы сформировать тот, который нам нужен.


Для этого давайте реализуем <mark style="background: #BBFABBA6;">DivisionedTableViewDataSource</mark>, который просто принимает массив других data source и использует каждый из них для формирования раздела в табличном представлении, которому он предоставляет данные. Мы начнем так:

```swift
class SectionedTableViewDataSource: NSObject {
    private let dataSources: [UITableViewDataSource]

    init(dataSources: [UITableViewDataSource]) {
        self.dataSources = dataSources
    }
}
```


Затем мы согласуем UITableViewDataSource, перенаправив большинство вызовов к базовому источнику данных, соответствующему индексу раздела текущего пути индекса:

```swift
extension SectionedTableViewDataSource: UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return dataSources.count
    }

    func tableView(_ tableView: UITableView,
                   numberOfRowsInSection section: Int) -> Int {
        let dataSource = dataSources[section]
        return dataSource.tableView(tableView, numberOfRowsInSection: 0)
    }

    func tableView(_ tableView: UITableView,
                   cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let dataSource = dataSources[indexPath.section]
        let indexPath = IndexPath(row: indexPath.row, section: 0)
        return dataSource.tableView(tableView, cellForRowAt: indexPath)
    }
}```

Имея вышеизложенное, мы теперь можем легко создавать секционированные источники данных практически без дублирования кода, а в сочетании с нашими удобными API-интерфейсами для создания источников данных для конкретной модели, которые мы использовали раньше, мы можем начать составлять источники данных, состоящие из нескольких наборов моделей с помощью простота:

```swift
let dataSource = SectionedTableViewDataSource(dataSources: [
    TableViewDataSource.make(for: recentContacts),
    TableViewDataSource.make(for: topMessages)
])
```

В этом и заключается сила композиции в целом: нам не всегда нужно начинать с нового типа, а вместо этого часто можно составить функциональность из существующих.