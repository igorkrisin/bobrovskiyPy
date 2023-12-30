#uiNAvigationController #delegate #ios 

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
	//создаем окно
    var window: UIWindow?
    
    //создаем навигационный контроллер
    var navController = UINavigationController()

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
     //создаем viewController 
        let viewController = ViewController()
        //делаем корневым контроллером VC
        self.navController = UINavigationController(rootViewController: viewController)
      
        
        if let windowScene = scene as? UIWindowScene {
                   let window = UIWindow(windowScene: windowScene)
                   
                   let viewController = ViewController()
                   let navController = UINavigationController(rootViewController: viewController)

                   window.rootViewController = navController

                   self.window = window
                   window.backgroundColor = UIColor.white
                   window.makeKeyAndVisible()
               }
    }```