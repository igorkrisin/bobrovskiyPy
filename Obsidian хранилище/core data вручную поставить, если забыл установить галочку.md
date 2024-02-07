### Вручную добавьте поддержку Cord Data.

(1) Сначала создайте файл xcdatamodeld (модель данных) в проекте.


![[2017110110225751760.png]]
(2) Рекомендуется, чтобы имя файла соответствовало имени проекта, например, мое имя здесь: hangge_1841.xcdatamodeld

![[2017110110265339318.png]]

(3) Затем откройте AppDelegate.swift и добавьте методы поддержки, связанные с Core Data (желтая часть).

import UIKit

import CoreData

 

@UIApplicationMain

class AppDelegate: UIResponder, UIApplicationDelegate {

 
```swift
var window: UIWindow?

 

    func application(_ application: UIApplication,

                     didFinishLaunchingWithOptions

        launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

        return true

    }

 

    func applicationWillResignActive(_ application: UIApplication) {

    }

 

    func applicationDidEnterBackground(_ application: UIApplication) {

    }

 

    func applicationWillEnterForeground(_ application: UIApplication) {

    }

 

    func applicationDidBecomeActive(_ application: UIApplication) {

 

    }

 

    func applicationWillTerminate(_ application: UIApplication) {

    }

 

    // MARK: - Core Data stack

    lazy var persistentContainer: NSPersistentContainer = {

        let container = NSPersistentContainer(name: "hangge_1841")

        container.loadPersistentStores(completionHandler: { (storeDescription, error) in

            if let error = error as NSError? {

                fatalError("Unresolved error \(error), \(error.userInfo)")

            }

        })

        return container

    }()

     

    // MARK: - Core Data Saving support

    func saveContext () {

        let context = persistentContainer.viewContext

        if context.hasChanges {

            do {

                try context.save()

            } catch {

                let nserror = error as NSError

                fatalError("Unresolved error \(nserror), \(nserror.userInfo)")

            }

        }

    }

}```
    

  
(4) После указанной выше конфигурации текущий проект может использовать CoreData. Чтобы узнать о конкретном использовании CoreData, обратитесь к этой статье, которую я написал ранее:[Быстрое использование основных данных для постоянного хранения данных](http://www.hangge.com/blog/cache/detail_767.html)  
Исходный текст взят из:[www.hangge.com](http://www.hangge.com/)Сохраните исходную ссылку для перепечатки:[http://www.hangge.com/blog/cache/detail_1841.html](http://www.hangge.com/blog/cache/detail_1841.html)