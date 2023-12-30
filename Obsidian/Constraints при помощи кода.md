#constraint #swift #uikit  
## **Добавление Constraints через код**

В коде можно управлять существующими _Constraints_ и добавлять новые. Если мы хотим менять параметры наших ограничений, то достаточно их добавить в код через `@IBOutlet` и дальше мы получим доступ к необходимым значениям. Для этого делаем то же, что и с _view_-элементами: _Выделяем_ → _Зажимаем Ctrl_ → _Нажимаем левой кнопкой мыши_ → _Ведём на ViewController.swift:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/52ef255a74f26fb32b17643f8c564207/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u4_p21.png)

  
  

В результате мы создали аутлет:![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/66140adac6411ec7b6869f037b64e8a3/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u4_p22.png)

  
  

А вот так мы изменили ранее присвоенное значение.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/26cfee97f146fc713ce051e5234a3ce1/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u4_p23.png)




Также на #stackoverflow в одном из [обсуждений](https://stackoverflow.com/questions/26180822/how-to-add-constraints-programmatically-using-swift) представлено несколько подходов создания _Constraints_ через код.ё