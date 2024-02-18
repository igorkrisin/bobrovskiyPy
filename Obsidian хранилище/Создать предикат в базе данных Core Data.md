#coreData #predicate




```swift
  //сначала создаем запрос
  let fetchRequest: NSFetchRequest<Todo> = Todo.fetchRequest()
  //создаем предикат указываем по какому признаку (полю) отбираем информацию
  fetchRequest.predicate = NSPredicate(format: "isActive == %@", NSNumber(value: true))
  //пробуем ее вывести на 'thfy'
  do {
	let user = try SettingsViewController.manager.persistentContainer.viewContext.fetch(fetchRequest)
    cell.nameToDo.text  = user.first?.name
    user.first?.isActive = false
  } catch {
    print(error)
  }
  ```

