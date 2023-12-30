#stackView #ios #swift 

Так же можно почитать про [[Constraints при помощи кода]]

_**Axis**_ — определяет ориентацию, горизонтальное расположение или вертикальное. То есть по сути в этой настройке мы выбираем ось — _x_ или _y_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/51d997fc3f27b08eceded81b14bf4cd7/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p2.gif)



_**Alignment**_ — определяет, как будут расположены элементы:

- в горизонтальном виде _StackView_ — вверху, по середине или внизу,
- в вертикальном — слева, по центру или справа.

При горизонтальном _StackView (axis = horizontal)_ основные варианты выравнивания элементов выглядят так:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3ae71ac01c7e7b57fda186f1634f9641/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p3.png)


А так выглядят основные варианты выравнивания элементов при работе с вертикальным _StackView (vertical axis):_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0503e0674d96aa34c66e9ae5bafc0764/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p4.png)  


_**Distribution**_ — определяет режим расположения элементов в выбранной ориентации. У _Distribution_ есть несколько вариантов настройки, которые стоит рассмотреть внимательнее.

**_Fill_** — один элемент заполняет бОльшую часть свободного пространства в _StackView_, в то время как другие элементы не меняют своих размеров.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1cdf01cbdbbd9b1963f8c23d80cc3859/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p5.png)  


**_Fill Equally_** — элементы используют равное количество свободного места и встают в _StackView_ с одинаковым размером.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/202781b8052451f01c004898d93c26de/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p6.gif)  


**_Fill Proportionally_** — элементы изменяют свой размер и расстояние между собой пропорционально, в зависимости от содержимого.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/883113107dadb63ffab8ff8aa2861a03/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p7.gif)  

**_Equal Spacing_** — устанавливает равное расстояние между элементами _StackView_, при этом не меняя их размеры.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/4a59179ad3c1c897640832d00a73bfd5/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p8.png)  


**_Equal Centering_** — пытается уточнить, всё ли нормально с центрами элементов: соответствует ли расстояние между центрами равно удалённых объектов, и неважно насколько далеко они друг от друга расположены.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ba89743f9890c7a15797d03fbb7400e9/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p9.png)  


**_Spacing_** — дословно это пространство между элементами _StackView_.

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8e692f54aec99b471f9857ca70c2eec0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p10.png)  


Более того, если у нас не заладилось с _Constraints_, то _StackView_ снимает с нас обязательство применять их к каждому элементу. Ведь всё дело в компоновке схожих элементов

более продвинутый вариант [[StackView + Constraints]]