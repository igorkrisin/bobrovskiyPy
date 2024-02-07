#swift #ios #UICollectionView 

## **Что это такое?**

Это элемент _UI_, который нужно размещать на каком-то контроллере. Как и _TableView_, для _CollectionView_ необходимо подключать _Delegate_ и _Datasource_, а после реализовывать обязательные методы этих протоколов.

## **Зачем он нужен?**

Данный элемент _UI_ используют в тех случаях, когда нужен «кастомный» _ViewController?_ и нет возможности использовать _UICollectionViewController_ (_UICollectionViewController_ используют крайне редко).

## **Как создать CollectionView и связать с ViewController?**

В самом начале мы не стали удалять созданный _Xcode_-файл _ViewController_ и _UIViewController_ из _Storyboard_ как раз для этих целей.

Первое, что вам необходимо сделать, — это сказать приложению, что теперь нужно запускаться с экрана _UIViewController_, а не с _UICollectionViewController!_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a5cbed606dc1aa85025884a51c18be24/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u4_p2.png)

  

Так как у вас уже есть _UIViewController_ в _Storyboard_, вам необходимо:

1. Выделить _UIViewController_.
2. Нажать на кнопку Library (это плюсик в правом верхнем углу экрана).
3. В поисковой строке ввести _Collection View_.
4. Перетащить _CollectionView_ на _UIViewController_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/e89d103d6086d2d3f4ea99c2bf115d14/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u4_p3.png)

  

Отлично, теперь на _ViewController_ есть _CollectionView_. Вам необходимо растянуть его на весь экран (установить все констрейнты в ноль), чтобы получилось вот так:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2d2cad2483c09b565c425488ad73ca9b/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u4_p4.png)

  

Ваш первый экран с _CollectionView_ почти готов, осталось связать _CollectionView_ и класс _ViewController_.

## Давайте сделаем это:

У вас есть файл _ViewController_, который связан с этим _UIViewController_. Вам необходимо его и использовать в качестве расширяемого файла. Это значит, вам нужно связать элемент _CollectionView_ с классом _ViewController_, попробуйте сделать это сами.

[[Как связать CollectionView с классом ViewController]]

Вот, что у вас должно получиться:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/57d614567d2e9b366408d814824bd7d0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u4_p5.png)

  

Данная процедура идентична по подключению _TableView_ из прошлого модуля. Что касается создания ячеек —  мы займемся этим немного позже.

Вот и все, главное отличие от «коробочного» решения — это **необходимость подключать все вручную**. Помните, что есть больша-а-а-а-а-я вероятность того, что вы что-то упустите и получите крэш при запуске приложения. Все будет зависеть только от времени на понимание «что пошло не так» и «как это исправить». Но не стоит вешать нос! Немного практики и все пойдет как по маслу.

Итак, вы разобрались с нюансами по созданию контроллеров. Чтобы двигаться дальше и приступить к созданию приложения, вам необходимо рассмотреть некоторые методы протоколов, которые используются наиболее часто в совокупности с ячейками, о которых мы также поговорим.

Начнем с [[UICollectionViewDataSource]].