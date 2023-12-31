#stackView #swift #button #calculator #калькулятор

подробно о stackView [[StackView + Constraints]] а так же [[Расположение элементов внутри stackView]]

Для того что бы кнопки заполнили все пространство нужно, вложить кнопки в stack view горизонтальные и затем вложить их все в родительский VIEW, затем родительскому view  указать constraintes и в attributes inspector в distribution установить Fill Equaly

тогда дочерние stack с вложенными в них кнопками  поровну займут все пространство

так я делал в проекте калькулятор https://github.com/igorkrisin/swift_course/tree/igorkrisin.github.io/swift/SkillFactory/home%20works через storyboard






![[Screenshot 2023-12-20 at 22.35.32.png]]