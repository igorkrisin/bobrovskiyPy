#stackView/constraint #ios #swift #stackViewAndConstraint 

То, что мы сейчас рассмотрели, — простой пример использования _StackView_. Но у _StackView_ есть и свои заморочки. Например, у нас есть три _view_-элемента с разными параметрами, мы их выделили, получили _StackView_. Но эти параметры пропали, а элементы получили _Intrinsic Content Size_ и уравнялись.

Что делать? На первый взгляд кажется, что так оно и может происходить, что ведёт нас к безысходности. Но даже если мы сформировали _StackView_, мы можем изменять параметры элементов уже внутри _StackView_. Неважно, какую ось мы выбрали — _x_ или _y_, мы сможем изменить ширину и высоту наших элементов внутри _StackView_. Тут нам на помощь приходят _Constraints_. У нас есть четыре кнопки, каждая 100x100 пикселей, в обычном виде:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/97d2b8a0ffe7a8940b46a85cf1df2a9e/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p14.png)                                           ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c0a624ed527258c57c9b1c31a6bb66cb/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p15.png)

  
  

Соберём их в _StackView_. Мы уже знаем, что мы сейчас получим:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1af02cbb5d59b98812d9826dff53a7e2/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p16.png)               ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/19bf700cb05e7afff939e60ac3ff6c18/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p17.png)               ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/72684ed38b0a1c9a4b1453e2a81fa305/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p18.png)

  
  

Кастомные размеры покинули чат. Окей. Сейчас _Constraints_ спасут положение. Для начала посмотрим на одном из элементов. Выберем третью по счёту кнопку:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/3ee8675b2dd44087cf4121f06e850c63/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p19.png)                 ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/6996a22601509b155982e8871961fbf0/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p20.png)

  
  

Спустимся в правый нижний угол сториборда и найдём кнопку. Нажмём на неё. Нас интересуют два параметра — _width_ и _height_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/9dc025adee7806b1dcbad8bd058d58df/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p21.png)

  

Окей, система выставила нам параметры исходя из _Intrinsic_ _Content_ _Size_. Мы же поставим на оба параметра 100 и нажмём _Add 2 Constraints:_

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/bfbf0653023f500a85c582a21dc17bb8/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p22.png)

  

И происходит интересная ситуация: у каждого элемента _StackView_ изменилась высота, но ширина изменилась только у третьей кнопки. Окей, дальше — проще. Выбираем оставшиеся три кнопки:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/5c0eaea84ef525eb601bb3cb9d7c5cce/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p23.png)

  

Снова идём в окно _Add New Constraints_, ставим галочку на _width_ и прописываем туда 100:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/59def076bb801b0e3c35ca3ffa093e8f/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p24.png)

  

Нажимаем _Add 3 Constraints_ и получаем элементы равных размеров — 100x100 пикс. каждый:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/1115ea358bf2515b889f2d6ab8faf235/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p25.png)

  

Единственное только, наш _StackView_ выехал за пределы экрана. Чтобы этого избежать, мы можем уменьшить размеры элементов. Пусть это будет 85x85. Изменим значения через редактирование _Constraints_. Для этого развернём нашу иерархию и найдём _Constraints_:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/a96182f89e943f2f6adbc9b57cb26333/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p26.png)

  

Сначала стоит поменять значение у _height_, чтобы у всех элементов появилась равная высота. Выбираем _height_ и на экране справа в _Size_ _Inspector_ изменяем её значение со 100 на 85:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/c4eac318cd5f692987291373c955c102/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p27.png)               ![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/8f47b71abddb0305671347649a9ce595/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p28.png)

  
  

Теперь пройдёмся по оставшимся _Constraints_ и каждую поменяем со 100 до 85. Наш _StackView_ будет таять на глазах и в результате станет тем, что нам нужно:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/73fceffa8682d6a340b119b429618002/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p29.png)

  

Теперь мы получили «‎однородный»‎ _view_, который мы сможем размещать так, как нам вздумается. Стоит помнить, что на _StackView_ распространяется такое же правило, как и на обычные view-элементы — если нет _Constraints_, то можно забыть о «‎нормальном»‎ расположении. Спустим наш _StackView_ ближе к низу экрана и добавим _Constraints_ так, чтобы наш _StackView_ мог отображаться на всех экранах одинаково хорошо:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2f565928b617fcbf8057573fb160cb52/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p30.png)

  

Запустим на симуляторе наш _StackView_ и увидим, что наш план удался:

![img](https://lms-cdn.skillfactory.ru/assets/courseware/v1/ea5cffc64d745f70cee49f765eb18800/asset-v1:SkillFactory+iOS-2.0+2021+type@asset+block/ios_m20_u6_p31.png)