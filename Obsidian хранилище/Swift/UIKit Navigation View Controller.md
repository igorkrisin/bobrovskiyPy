---
tags:
  - swift
  - uikit
---

Что бы создать переход через NVC необходимо внутри класса <mark style="background: #FF5582A6;">ScenceDelegate </mark>прописать следующее

```Swift
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
