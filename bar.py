1.

Прояснение

//Белые - вывод заглавными буквами
//Черные строчные буквы вывод

//белые фигуры выврлятся на печать ЗАГЛАВНЫМИ БУКВАМИ
//черные - строчными буквами

2.

Прояснение

int goToY;//элемент структуры

int goToY;//элемент структуры данных списка

3.
Комментарий TODO


convertBoardToStr (x:xs) = convertLstToStr x++"\n"++convertBoardToStr xs --TODO исправить доску и добавить юникод

convertBoardToStr (x:xs) = convertLstToStr x++"\n"++convertBoardToStr xs --TODO исправить доску и добавить юникод для наглядности
4.
Прояснение

--если встретили открывающую скобку, то кладем ее на стек
checkAmountParenthesses ("(":xs) st  = checkAmountParenthesses xs ("(":st)

--если встретили открывающую скобку, то кладем ее на стек для того что бы опрелелить правильное количество открыващихся
--м закрываюзиъся скобок
checkAmountParenthesses ("(":xs) st  = checkAmountParenthesses xs ("(":st)

5.
Комментарий TODO

-- TODO применить конечный автомат в польский калькулятор

--TODO применить конечный автомат для усоверщенствоания польского калькуллятора

6.
Прояснение

// функция, проверяет что игра закончилась. Если в матрице нет 0, то игра закончена.

// функция, проверяет что игра закончилась. Если в матрице нет 0, то игра закончена.
//пустые клетки на игровом поле закрнчились

7.
Прояснение

def separWordField(word)#разделение полей процессора

def separWordField(word)  # определяем каждое поле в свою переменную,
# что бы взамодействовать с ними по отдельности

8.
Предупреждение о последствиях
case *list:
		// true - нет ошибок
		// false - произошла ошибка

case *list:
    //если вернется false, значит в выражение попало неприемлемое значение/символ
9.
Усиление

memAdress = line.to_s #адрес в памяти куда сложить команду

memAdress = line.to_s #только в данный адрес в необходимо складывать команды

10.
Прояснение

when "01"               #Immediate mode (=)
when "01"               #Immediate mode данный режим активируется добавлением символа (=) к команде
11.
Комментарий TODO

mar = convertTo16Bit(mbr.slice(5,11))#??? TODO правмльно ли записаны индексы? в adress field записаны с 6 по 10

mar = convertTo16Bit(mbr.slice(5,11))#??? #TODO необходимо проверить правмльно ли записаны индексы?
# индексы храняися в поле adress field  с 6 по 10 позицию

12.
Представление намерений

num, remaind = separDivNum(dec1, dec2)
    temp = (num.to_i/dec2.to_i).to_s

num, remaind = separDivNum(dec1, dec2)#отделяем цифры пока первое не станет возможным поделить на второе
    temp = (num.to_i/dec2.to_i).to_s#делим отделимый остаток на второе число