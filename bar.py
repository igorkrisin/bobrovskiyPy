1.

Не используйте комментарии там, где можно использовать функцию или переменную
Короткие

// функция, проверяет что игра закончилась. Если в матрице нет 0, то игра закончена.
(данный комментарий можно удалить и назвать функцию понятнее)
def isGameOver

2.
Закомментированный код

func main() {

	/*submit := exec.Command("ls")
	result, codError := submit.Output()
	fmt.Println(string(result))
	fmt.Println(codError)
	//fmt.Printf("You pressed: %q\r\n", char)*/
    (убираем закомментированный неиспользуемый код)

func main() {

3.
Бормотание

return stack.data, true //некий костыль
(комментарий не говорящий ни о чем)

return stack.data, true //возырат пары значений, true - выражение верно

4.

Закомментированный код

var tempList *list = nil
	//exp = exp.nextdata
	for exp != nil {

var tempList *list = nil
	for exp != nil {

5.
Не используйте комментарии там, где можно использовать функцию или переменную

case *list:
// true - нет ошибок
// false - произошла ошибка


isValueRight = true
isValueWithError = false
case *list

6.
Позиционные маркеры

case string:
			////////////////////////////////////////////////////////////////////////
(можно просто убрать особого профита в коде нет от этой конструкции)

case string


7.
Закомментированный код

fmt.Print("exp: ")
					printList(exp)
					fmt.Println("")
					//evalList(exp,dict)

fmt.Print("exp: ")
					printList(exp)
					fmt.Println("")

8.
Избыточные комментарии

if err == io.EOF { // если конец файла
		break // выходим из цикла
	}
(вполне очевидное поведение, комментарии издишни)

if err == io.EOF {
		break
	}

9.
Позиционные маркеры
//////////////////////////////////////////////////////////////////////////////////////// class end///////////////////////////////////////////////////////

void push_back_list(vector<variant<Move, castling>> &listMove, vector<variant<Move, castling>> &everyMoveList);//прототип!!!//////////////////////////////////////////////////////////
(без данных маркеров очевидно окончание классв=ов и начало прототипов функций)

void push_back_list(vector<variant<Move, castling>> &listMove, vector<variant<Move, castling>> &everyMoveList);


10.
Не используйте комментарии там, где можно использовать функцию или переменную
// координаты castling для белых
array < int, 2 > kingDepW = {4, 7};

array < int, 2 > kingStartCoordWhtCast= {4, 7};

11.
Не используйте комментарии там, где можно использовать функцию или переменную

return false;    //этот false возвращается, когда наткнулись на фигуру другого цвета не на rook  и не на queen

bool notRookAndNotQeen = false
return notRookAndNotQeen

12.
Шум

traceRegister(ir, xr, mar, mbr, pc, ac,index)         #TRACER
(данный комментарий дублирует очевидную информацию)

traceRegister(ir, xr, mar, mbr, pc, ac,index)

13.
Не используйте комментарии там, где можно использовать функцию или переменную
memAdress = line.to_s #адрес в памяти куда сложить команду

memAdressForCommand = line.to_s

14.
Закомментированный код

end
# traceBitMemory(options[:trace], memArr)
mainLoop()

end
mainLoop()

15.
Избыточные комментарии
Закомментированный код

def divDec(dec1, dec2)
    num, remaind = separDivNum(dec1, dec2)#отделяем цифры пока первое не станет возможным поделить на второе
    temp = (num.to_i/dec2.to_i).to_s#делим отделимый остаток на второе число
    rem2 = num.to_i%dec2.to_i#остаток от деления после отделения цифры и выполенния первого шага деления
    while remaind != ""

        rem2 = (rem2.to_s + remaind[0]).to_i#прибавляем к этому остатку следующее число из делителя для следующей итерации деления
        remaind = remaind.slice(1, remaind.size - 1)# остаток от делителя режем на 1 знак спереди (его забрали на сл цикл строкой выше)
       #rem2, remaind = separDivNum((rem2.to_s + remaind), dec2)
        print "rem2: #{rem2}\n"
        temp = temp + (rem2.to_i/dec2.to_i).to_s
        rem2 = (rem2.to_i%dec2.to_i).to_s
    end

def divDec(dec1, dec2)
    number, remaindOfNumOne = separDivNum(dec1, dec2)
    summRemindOfNumOne = (number.to_i/dec2.to_i).to_s
    remaindOfNumTwo = number.to_i%dec2.to_i
    while remaindOfNumOne != ""
        remaindOfNumTwo = (remaindOfNumTwo.to_s + remaindOfNumOne[0]).to_i
        remaindOfNumOne = remaindOfNumOne.slice(1, remaindOfNumOne.size - 1)
        summRemindOfNumOne = summRemindOfNumOne + (remaindOfNumTwo.to_i/dec2.to_i).to_s
        remaindOfNumTwo = (remaindOfNumTwo.to_i%dec2.to_i).to_s
    end