#swift #передачаДанных #uikit #вперед

Так же:
[[Переходы между ViewController]]
[[Передача данных в обратную сторону или назад]] 

![[Screenshot 2024-02-05 at 18.54.25.png]]



- Что бы передавать данные можно использовать метод prepare for segue

![[Screenshot 2024-02-05 at 18.48.25.png]]



- В отличие от show у present есть completion замыкание в методе, в котором мы можем передавать информацию.
вызываем в замыкании экземпляр класса и передаем туда сообщение, можно передавать сразу в label:

![[Screenshot 2024-02-05 at 18.10.48.png]]


- Передача  через свойства - берем в action кнопки обращаемся к свойству и присваиваем ему данные
![[Screenshot 2024-02-05 at 18.57.53.png]]


