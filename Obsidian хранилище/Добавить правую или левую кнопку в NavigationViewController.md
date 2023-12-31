#ios #swift #uiNAvigationController #right #left #button #target #action 

Как кодом добавить NavViewController смотрим [[Добавляем barButtonItem и картинку в шапку NavigationController]]


При создании экземпляра есть 3 свойства 
- <mark style="background: #BBFABBA6;">barButtonSystemItem</mark>: - это как будет выглядеть элемент
- <mark style="background: #BBFABBA6;">target</mark> - объект который получает сообщение о действии при нажатии кнопки
- <mark style="background: #BBFABBA6;">action</mark> - действие которое произойдет после нажатия кнопки (описывается в методе ниже передается с пометкой #selection)


```swift
 override func viewDidLoad() {
        super.viewDidLoad()
        //добавляем правую кнопку в панель NavVC - 
        self.navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .camera,
            target: self,
		    action: #selector(performAdd(parametr:)))
    }
    
    @objc func performAdd(parametr: Any) {
        print("Add tapped")
    }
    ```

так же можно [[ добавить в панель NAvigationViewController switch (переключатель)]]
