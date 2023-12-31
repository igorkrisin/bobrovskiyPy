#barButtonItem #ios #uiNAvigationController 

[[UIKit Navigation View Controller]]


Для создания UINavigationViewControllera через код пишем в классе ScenceDelegate  в методе scene:

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {

		//создаем экземпляр класса VC
        let vc = ViewController()
        
	    //создаем NavVC и делаем корневым предcтавлением созданный выше vc
        let navViewController = UINavigationController(rootViewController: vc)
        guard let _ = (scene as? UIWindowScene) else { return }
        
        self.window?.rootViewController = navViewController
        self.window?.backgroundColor = .white
        self.window?.makeKeyAndVisible()
    }```
Далее переходим в класс ViewController

```swift

import UIKit

class ViewController: UIViewController {

   
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //устанавливаем заголовок для  VC
        //title = "View Controller"
        createImageTitleView()
    }
    
    //пишем метод и вызываем его во ViewDidLoad
    fileprivate func createImageTitleView() {
        //создаем элемент imageView что бы можно было его отобразить на navigationItem впоследствии
        
        let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 100, height: 40))
        
        //даем ему свойство AspectFit что бы view не пастягивало по краям
        imageView.contentMode = .scaleAspectFit
        
        //загружаем картинку в Assets и присваиваем в переменную
        let image = UIImage(named: "apple")
        
        //кладем картинку во View
        imageView.image = image
        
        //присваиваем NavController view
        self.navigationItem.titleView = imageView
    }

}
}```

так же можно [[Добавить правую или левую кнопку в NavigationViewController]]
или [[добавить в панель NAvigationViewController switch (переключатель)]] вместо правой или левой кнопки

Или же [[добавить segmentController и панель NAvigationController]]

