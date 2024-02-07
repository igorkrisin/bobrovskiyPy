---
tags:
  - swift
  - uikit
  - "#uiNAvigationController"
---
[[создание NavigationControllera кодом]]
[[Жизненный цикл View controller (life cycle)]]

[[Переход на другие view при помощи segue]]] ]
[[Переход на другие view при помощи present() и show()]]
[[Переход на другие view при помощи pushViewController]]


Что бы создать переход через NavigationVC необходимо внутри класса <mark style="background: #FF5582A6;">ScenceDelegate </mark>прописать следующее


```swift
 guard let windowScene = (scene as? UIWindowScene) else { return }
  // после этой строки в методе scence пишем:


	 let window = UIWindow(windowScene: windowScene)

        let navController = UINavigationController()

        let viewController = ViewController()

        navController.viewControllers = [viewController]

        window.rootViewController = navController

        self.window = window

        window.makeKeyAndVisible()


```
```

```

Создаем еще одну сущность <mark style="background: #FF5582A6;">SecondViewController</mark> на который будет переходить главный VC
Изменить цвет корт

