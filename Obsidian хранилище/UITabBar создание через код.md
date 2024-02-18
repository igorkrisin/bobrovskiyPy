#ios #TabBarController #swift 

Создаем в SceneDelegate tabBar, window и [[UIKit Navigation View Controller создание кодом]]


```swift

import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?


    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
       
        if let windowScene = scene as? UIWindowScene {
            let window = UIWindow(windowScene: windowScene)
            let firstVC = ViewController()
            let secondVC = SecondViewController()
            
            //добавим навигацию
            let firstNAvController = UINavigationController(rootViewController: firstVC)
            let secondNAvController = UINavigationController(rootViewController: secondVC)
            
            let tabBarVC = UITabBarController()
            tabBarVC.setViewControllers([firstNAvController, secondNAvController], animated: true)
            
            window.rootViewController = tabBarVC
            window.backgroundColor = .white
            
            secondVC.loadViewIfNeeded()
            
            self.window = window
            window.makeKeyAndVisible()
        }
        
    }
    ```
Во вью контроллерах обращаемся к элементу UITabBarItem и меняем его

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //добавим кнопки-картинки в NC
        self.navigationItem.title = ""
        
        
        title = "First VC"
        
        //что бы изменить кнопки на таб баре создаем экземпляр класса UITabBarItem и работем с ним
        
        var tabBarItem = UITabBarItem()
        tabBarItem = UITabBarItem(tabBarSystemItem: .contacts, tag: 0)
        
        self.tabBarItem = tabBarItem

        self.view.backgroundColor = UIColor.white
    }
}

```