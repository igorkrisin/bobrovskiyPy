#ios #swift #UIViewCollectionController

## **Что это такое?** 

_UICollectionViewController_, как и _UITableViewController_, — это более простое коробочное решение для тех случаев, когда вы не хотите заморачиваться, создавая элементы вручную. Он уже содержит в себе подключенные _delegate_ и _datasource_. Данный элемент _UI_ прекрасно подходит для создания нового проекта, закладывая в него базовый функционал.

Давайте попробуем создать _UICollectionViewController_.

Для этого мы **не** будем удалять _UIViewController_ и его связанный файл _ViewController_, они нам еще пригодятся, когда будем изучать _CollectionView_. Единственное, что вы должны сделать, — это сказать приложению, чтобы оно перестало стартовать с базового (созданного _Xcode_) _UIViewController’а._

Для этого перейдите в _main.storyboard_ → Выберите _UIViewController_ → Перейдите во вкладку _Show attribute inspector_ → Отключите галочку _Is initial view controller_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/290523920a17b2b4784a5a4d14f1c5c6/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p1.png)


  

Теперь давайте создадим _UICollectionViewController_ в файле _main.storyboard._

Для этого откройте _Library_ → В строке поиска введите _Collection View Controller_ → Перетаскивайте этот экран на пустое место в _Storyboard_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/fe12f10bf3456b36fa8ce3ee564d3f4f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p4.png)

  

Последний штрих — необходимо сказать приложению, чтобы оно стартовало с созданного только что _UICollectionViewController_. Для этого:

Выделите контроллер → Перейдите во вкладку _S__how attribute inspector_ → Включите галочку _Is initial view controller:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2b1efae5233a54463dfcf15e25ba5377/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p5.png)

  

Сам контроллер готов, но для работы этого недостаточно. Вам необходимо создать _Cocoa Touch Class_, который впоследствии вы свяжете с  _UICollectionViewController_.

Чтобы узнать, как создать класс и проассоциировать его с вашим контроллером, посмотрите скринкаст :)

## **Что есть в _UICollectionViewController_?**

Вот, что есть в структуре файлов _View Controller Scene_ (если выбрать сам контроллер):

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/cadf3460b01a02c78fcbe055b9845922/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p10.png)

  

1. Непосредственно _ViewController_, где расположена первая (базовая) _View_, которая и будет в дальнейшем содержать все элементы _UI._
2. _Safe Area_ — область, в которой размещаются такие элементы, как иконка батарейки, сети, оператора.
3. Непосредственно сам _Collection View_, в котором есть ячейка.
4. А также _View_, которая лежит внутри ячейки и выступает в качестве контейнера, где можно размещать разные элементы _UI._
5. И, конечно же, _Collection View Flow Layout_ — элемент для создания макета (то, как ячейки будут расположены). Об этом мы поговорим позже.

Теперь вы знаете, что в себе содержит контроллер из «коробки».

Давайте переместимся в файл _MyCollectionVC_ и посмотрим, что вам доступно при создании класса _UICollectionViewController._

## **Краткая информация: что доступно в классе, который наследуется от _UICollectionViewController_?**

1. У вас сразу есть идентификатор.
2. Класс _MyCollectionVC_ наследуется от _UICollectionViewController_ (его мы рассмотрим далее).
3. Регистрация ячейки.
4. Вы имеете реализованные обязательные методы из протокола _UICollectionViewDataSource_
5. А также закомментированный код из протокола _UICollectionViewDelegate,_ который в дальнейшем вы можете использовать для своих нужд.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3c38147df15e636808c729cd43807832/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p11.png)

  

Наверняка у вас возник вопрос, а откуда взялись методы из протоколов, мы же их не подключали? 

Да, вы их действительно сами не подключали, но вы создали класс _MyCollectionVC_, который наследуется от _UICollectionViewController_, а уже этот класс содержит в себе все необходимые связи для работы с _CollectionView_, а именно — протокол _UICollectionViewDelegate_ и _UICollectionViewDataSource_. Поэтому у вас уже есть обязательные компоненты для работы, а также те, что могут понадобиться.

## **Краткая информация: что содержит _UICollectionViewController_?**

Давайте заглянем внутрь _UICollectionViewController_:

Наведите на класс мышку → Зажмите _Command_ + ЛКМ (левая клавиша мыши) → Выберите _Jump to Definition:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/65bf11cbf9894a4daa4c482a551c6ddb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p12.png)

  

Внутри класса вы увидите:

- Подключенные протоколы _UICollectionViewDelegate_ и _UICollectionViewDataSource_ (вот откуда взялись методы) в вашем классе _MyCollectionVC_
- Ряд инициализаторов.

Обратите внимание на свойство _open var collectionView: UICollectionView!_ — это ссылка, которая связывает _UICollectionView_ из _Storyboard_ и класс _MyCollectionVC:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/64f7cad51794f0307a07e71dd84cc06c/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m23_u3_p13.png)

  

Узнать больше о _UICollectionViewController_ вы можете из официального [источника](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller).

Итак, вы рассмотрели все основные элементы по созданию _UICollectionViewController_, а чтобы вдохновиться на новые свершения и более глубокое понимание «коробочного» решения **обязательно** прочтите [эту статью](https://habr.com/ru/post/311064/) (в ней говорится о том, как важно уметь применять эти коробочные решения, и как они помогают облегчить жизнь).

К сожалению, к «коробочному» решению прибегают крайне редко, в основном стараются использовать _UI_-элементы по отдельности, это значит, что в подавляющем большинстве у вас будет какой-то [[ViewController,  на который необходимо разместить  CollectionView]]_.


