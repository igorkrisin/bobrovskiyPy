

7.1
    el1 - isEqualValueEl
    //Проверяем равенство двух элементов

    possCastLeftWhite - isPossCastLeftWhite
    //Проверка возможности кастлинга для белых слева

    enpasWhite - isEmpassantWht
    //произошел ли эмпассант

    flag - isGameAgain
    //повторить  игру или выйти

    castlingFlag - isAddMoveInList
    //можно ли добавить ход кастлинга в список общий списрк ходов


7.2
    finishSearchMove - found
    //поиск хода в списку ходов

   checkCheck - foundCheck
   //в списку ходов найден шах

    wrongMove - error
    //выбран не не правильный ход на доске

7.3
    for(int X = x+dirX... - for(int xCurrentCoord = xCoord + xStep...
    //расчетная координата Х с учетом шага хода фигуры (X - передаеюся в функцию аргументом)

7.4
    int xDeparture - xStartCoord
    int xArrivle - xFinishCoord
    //координата откуда ходит фигура и куда ходит фигура

    startStr - headString
    finishString - tailString
    //начало и конец строки

7.5
    arrTempX - arrAddNewCoordX
    //массив в крирвый добавляются координаты Х

    tempList - ListForReverse
    //список хранящий перевернутый список

    tempStr - strForTokenize
    //строка хранящая результат токенизации

    tempDict - dictionaryForCopy
    //словарь для копирования основного словаря


    //нашел, что в первом доп задании по АСД я добавил лишние списки, временные списки не нужны были, можно обойтись без них