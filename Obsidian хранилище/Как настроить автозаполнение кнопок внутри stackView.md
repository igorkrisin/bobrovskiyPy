#stackView #swift #button #calculator #калькулятор

подробно о stackView [[StackView + Constraints]] а так же [[Расположение элементов внутри stackView]]

Для того что бы кнопки заполнили все пространство нужно, вложить кнопки в stack view горизонтальные и затем вложить их все в родительский VIEW, затем родительскому view  указать constraintes и в attributes inspector в distribution установить Fill Equaly

тогда дочерние stack с вложенными в них кнопками  поровну займут все пространство

так я делал в проекте калькулятор https://github.com/igorkrisin/swift_course/tree/igorkrisin.github.io/swift/SkillFactory/home%20works через storyboard






![[Screenshot 2023-12-20 at 22.35.32.png]]

Для главного экрана такие констрейнты

![[Screenshot 2024-01-02 at 20.31.18.png]]

так же нужно расставить основному стеку 

![[Screenshot 2024-01-03 at 22.50.45.png]]

вложенным стекам

![[Screenshot 2024-01-03 at 22.51.12.png]]

ноль выполнен отдельно во вложенном стеке

![[Screenshot 2024-01-03 at 22.35.30.png]]

. и = в отдельном стеке внутри последнего стека

настройки последнего стека

![[Screenshot 2024-01-03 at 22.53.28.png]]