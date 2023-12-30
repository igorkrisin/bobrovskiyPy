#ios #viewController #lifeCycle 

При загрузке любого view происходит вызов следующих методов:

![[Screenshot 2023-12-26 at 07.15.34.png]]


1. <mark style="background: #FF5582A6;">loadView</mark> (загружается один раз, при первой загрузке view) - view загружается и все ui элементы создаются связи которые настроены через IBOutlet и IBAction и <mark style="background: #FFB86CA6;">после того </mark>как все будет загружено вызовется следующий метод.
2. <mark style="background: #FF5582A6;">viewDidLoad</mark> (загружается один раз, при первой загрузке view. <mark style="background: #FFB86CA6;">Сразу после</mark> загрузки `view` вызывается метод `viewDidLoad()`. Во viewDidLoad() можно выполнить, например, сетевой запрос, который нужен нам при запуске экрана (или любое другое действие, которое нам нужно только один раз, при запуске). Или, например, установить какой-то цвет фона.
3. <mark style="background: #FF5582A6;">viewWillAppear</mark> - вызывается каждый раз<mark style="background: #FFB86CA6;"> перед </mark>добавлением view в иерархию, на этом этапе view пока не видна на экране, размеры view еще не понятны. Данный метод можно использовать для более детальной настройки subview - например заполнить данными таблицу перед показом пользователю
4. <mark style="background: #FF5582A6;">viewVillLaioutSubviews</mark> - на <mark style="background: #FFB86CA6;">этом этапе </mark>устанавливаются размеры экрана Если вы не используете _constraints_ или _Auto Layout_, вы, вероятно, захотите обновить здесь размеры или положение subviews.
5. <mark style="background: #FF5582A6;">vivDidLayoutSubViews</mark> - в этом месье все subview ViewController'a были настроены. Если нужно внести правки в subviews после того как они были установлены - это подходящее место.
6. <mark style="background: #FF5582A6;">viewDidAppear</mark> - данный метод вызывается сразу <mark style="background: #FFB86CA6;">после</mark> появления view на экране - отличное место что бы сохранить данные в базу данных или начать анимацию воспроизведения видео или звука или получение данных из сети
7. <mark style="background: #FF5582A6;">viewWillDisappear</mark>  - вызывается <mark style="background: #FFB86CA6;">до того </mark>как subview будет удалено из view hierarchy. Внутри можно добавить код скрытия клавы. отмену сетевых запросов или операцию по сохранению чего-либо
8. <mark style="background: #FF5582A6;">viewDidDisappear</mark> - уведомляет контролер, что view будет удалена из иерархии представлений вызывается<mark style="background: #FFB86CA6;"> сразу после</mark> того как содержимое ViewController'a из иерархии представлений (view hierarchy). Лучше всего подходит для удаления данных которые используют память, которые можно пересоздать позже


![[Screenshot 2023-12-26 at 09.25.22.png]]