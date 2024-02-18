#indexPAth #swift #uikit #tableViewController #TableView 

```swift
//создаем экземпляр IndexPath
let indexPatxNewRow = IndexPath(row: allTime.count - 1, section: 0)
//пример применения
tableViewController.tableView.insertRows(at: [indexPatxNewRow], with: .automatic)
```
