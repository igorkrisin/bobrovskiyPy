#CollectionView #ios #swift  #UICollectionViewDelegate #UICollectionViewDataSource #протоколы

Как Реализовать протоколы делегат и датасорс:

для начала перетаскиваем из сториборда элемент collection view и добавляем протоколы к VC - <mark style="background: #ADCCFFA6;">UICollectionViewDelegate</mark> и <mark style="background: #ADCCFFA6;">UICollectionViewDataSource</mark>, фиксим ошибки
и появляются 2 метода 

```swift
//1 количество эдементов в секциии
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
//сюда проставляем одну сецию (или сколько необходимо)
       return 1
    }
    //2 и ячейки по индексу (их количество)
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    //здесь ставим заглушку (создаем ячейку и возвращаем ее). Берем наше CollectionView и его метод dequeueReusableCell в идентификаторе указываем пока "Cell" в индексе indexPath - он передается в аргументах 
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
        // возвращаем ячейку
        return cell
    }
```

Затем во viewDidload активируем delegate от <mark style="background: #ADCCFFA6;">UICollectionViewDelegate</mark> и <mark style="background: #ADCCFFA6;">UICollectionViewDataSource</mark> что бы мы могли пользоваться методами  этих делегатов


```swift

override func viewDidLoad() {
        super.viewDidLoad()
        collectionView.delegate = self
        collectionView.dataSource = self
    }
    
```

А так же добавляем идентификатор ячейке в соотвествии с названием идентификатора в коде после<mark style="background: #FFB86CA6;"> withReuseIdentifier:</mark> 