#ios #uikit #segue

Нажмите на кнопку правой кнопкой мыши и перетяните ее на другой экран. Выберите, например, _show_.



![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/983088d648a2e1db8952ea049b9fd992/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p1.png)

У вас создастся _seguе_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5951766a499e62be11ea989a3bb90229/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p2.png)

В демонстрационном проекте также добавлен _NavigationController_. 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1ed0b9fed498addd2ddcc33c2140ca6d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p3.png)

Мы его уже создавали и позже подробно остановимся на нем. 

Напомню, что добавляется он так:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1d9b6f1e4d4fcfc904dda66244ce6696/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p4.png)

import UIKit
 
class ViewController: UIViewController {
 
    override func viewDidLoad() {
        super.viewDidLoad()
    }
}

import UIKit
 
class SecondViewController: UIViewController {
 
     override func viewDidLoad() {
         super.viewDidLoad()
     }
}

[Скачать архив](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5734d839125564f1fc2788d1901390ac/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/21.4.1_segue.zip)

Это начальный архив. То есть выше мы создали _VC_, классы, связали всё это. В этом архиве всё то же самое.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/27d53eadcf589b6a5060e896672f89fd/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p5.png)

Первое, что сейчас нам нужно сделать, — присвоить идентификатор сегвею. Сделать это очень просто:

1. Нажимаем на _segue_.
2. Присваиваем идентификатор. В нашем случае _emodji_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0540e0b58ae2a21f15e1965ffb6bb5b7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p6.png)

Теперь давайте добавим _IBOutlet_ на _SecondViewController_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/7856d460d9a3ddc2d7c25b531e9e8969/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p7.png)

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e9e186f532b52743f478d1bae8870ce7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p8.png)

Далее объявим переменную `emodji`, которая будет хранить в себе какой-то емодзи. Поставьте по умолчанию какой-либо смайлик. В дальнейшем именно в эту переменную мы будем передавать данные из другого _VC_ (_view controller_)

 var emodji = ""

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9af7b61eb7a69d9d1ddd092eee17949d/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p9.png)

В итоге код _SecondViewController’a_ приобрел следующий вид: 

import UIKit
 
class SecondViewController: UIViewController {
 
    @IBOutlet weak var emodjiLabel: UILabel!
    var emodji = ""
 
    override func viewDidLoad() {
         super.viewDidLoad()
     }
}

Идем в _ViewController.swift._ Здесь для того, чтобы наше приложение заработало, нужно написать всего несколько строчек кода :)

<mark style="background: #FFB86CA6;">Схема следующая:</mark>

override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let destination = segue.destination as? yourNextViewControllerClass {
            if segue.identifier == "yourIdentifierInStoryboard" {
                destination.emodji = ""
            }
        }
    }

где <mark style="background: #FF5582A6;">`yourNextViewControllerClass`</mark> — контроллер, на который вы хотите перейти, а <mark style="background: #FF5582A6;">`yourIdentifierInStoryboard`</mark> — идентификатор сегвея, который мы добавляли на сториборде.

В нашем случае код приобретет следующий вид:

override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let destination = segue.destination as? SecondViewController {
            if segue.identifier == "emodji" {
                destination.emodji = ""
            }
        }
    }

Этот код можно написать и по-другому. Например, вот так:

override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard segue.identifier == "emodji" else { return }
        guard let destination = segue.destination as? SecondViewController else { return }
        destination.emodji = ""
  }

Тут мы делаем проверку при помощи оператора `guard`. 

В общем, `prepare()` — это главный метод, с которым вы будете работать, используя `segue`. 

Помните, что **всегда** нужно проверять идентификатор segue (_segue.identifier_) на соответствие названию, которое вы задали ранее. 

Если идентификатор segue соответствует указанному нами идентификатору, то программа идет дальше.

Далее устанавливается `destination` — это _ViewController_, на который вы хотите попасть. Так как мы хотим попасть на _SecondViewController_, то нам необходимо обратиться к свойству сегвея, а именно к свойству destination и скастить его к _SecondViewController’у_. (`segue.destination as? SecondViewController`)

Пополняем словарный запас =) Кастить означает привести к типу.

Теперь, написав destination, вам будут доступны все методы и свойства _SecondViewController’a._ 

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/63b7e12f8f4dada386098f69dd17c7cf/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m21_u4_p10.png)

Давайте еще раз:

1. Указываем `identifier` нашему `segue`.
2. Идем в _ViewController_.
3. Переопределяем метод `prepare(for segue:...)`.
4. Проверяем, соответствует ли `segue.identifier` указанному в сториборде идентификатору.
5. Кастим segue.destination к _SecondViewController_ (`segue.destination as? SecondViewController`), то есть к контроллеру, куда хотим передать данные.
6. Обращаемся к нужному свойству _SecondViewController’_a и указываем его значение.