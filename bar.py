1. summ = (dec%2).to_s + summ - string_decimal = (dec%2).to_s
                             string_summ = string_decimal%2 + string_summ
//арифметическаое действе для последубющей конвертации в бинарный тип,
//вывел в отдельную строчку приведение типов, что бы сделать преобразование типов понятным

2. summ += (bin[n]).to_i * 2 ** n - integer_bin = (bin[n]).to_i
                                    result_convertation += integer_bin * 2 ** n
//обратная операция преобразования бинарного числа в int
//вывел в отдельную строчку приведение типов, что бы сделать преобразование типов понятным

3. dec = dec/2 -    if (decimal/2).is_a? Integer (язык Ruby)
                        decimal = decimal/2
//арифметическаое действе для последубющей конвертации в бинарный тип,
//добавил проверку на целочисленность деления

4. if bin[i+j] == "1" - BINARY_ONE = "1"
                        bin[i+j] == binary_one
//конвератция из бинарного в 16ти разрядное
//убрал магическую строку

5. summ = "" - result_convertation = ""
//конвератция из бинарного в 16ти разрядное
//при конвертации строк название summ вводит читающего в заблуждение -
//сделала более понятным название результирующей переменной

6. if text[0] == "HALT" - mnemonic_command = text[0]
                          if mnemonic_command == "HALT"
//проверка в инеионической команде на остановку вычисления
//добавил доп переменную, которая убирает магическую строку

7. return  "0000000000000000" - BINARY_HALT = "0000000000000000"
                                return BINARY_HALT
//возврат бинарного значения для команды HALT
//заменил магическую строку на константу

8. if(x < 0 || x  > matrWidth || y > matrHight || y < 0) - xOutOfRange = x < 0 || x  > matrWidth
                                                           yOutOfRange = y > matrHight || y < 0
                                                           if(xOutOfRange || yOutOfRange)
//проверка на выход индекса из матрицы
// заменил условия на логические переменные

9. if(board.at(kingDepBl.at(0),kingDepBl.at(1)).name_piece == king && board.at(kingDepBl.at(0),kingDepBl.at(1)).color_piece == colors){
        if(board.at(rookDepBlL.at(0),rookDepBlL.at(1)).name_piece == rook && board.at(rookDepBlL.at(0),rookDepBlL.at(1)).color_piece == colors &&
                board.at(1,0).name_piece == Empty && board.at(2,0).name_piece == Empty && board.at(3,0).name_piece == Empty){

isKingOnCells0_1 = board.at(kingDepBl.at(0),kingDepBl.at(1)).name_piece == king
isBlackKingColor = board.at(kingDepBl.at(0),kingDepBl.at(1)).color_piece == colors
isRookOnCells0_1 = board.at(rookDepBlL.at(0),rookDepBlL.at(1)).name_piece == rook
isBlackRookColor = board.at(rookDepBlL.at(0),rookDepBlL.at(1)).color_piece == colors
isEmptyCell01 = board.at(1,0).name_piece == Empty
isEmptyCell1_0 = board.at(1,0).name_piece == Empty
isEmptyCell1_0 = board.at(2,0).name_piece == Empty
isEmptyCell3_0 = board.at(3,0).name_piece == Empty

if(isKingOnBoard && isBlackKingColor && isRookOnCells0_1 &&
   isBlackRookColor && isEmptyCell1_0 && isEmptyCell1_0 && isEmptyCell3_0){...}}
//проерка условий кастлинга
//заменил вложенность if  и добавил логические переменные

10. if(colors == black && board.enpasBlack[i] == true){...}-  isColorBlack = colors == black
                                                           isEnpassantForBlack = board.enpasBlack[i] == true
                                                           if(isColorBlack && isEnpassantForBlack){...}
//проверка возможности энпассанта
//добавил логические переменные

11.if(checkCheck(board.xKingWhite,board.yKingWhite, board) &&
      filterIlegalMove(listMovesKing(board.xKingWhite,board.yKingWhite, board), board, colors).empty()) {...}

    isCheckKingWhite = checkCheck(board.xKingWhite,board.yKingWhite, board
    isEmptyMoveLstKingWht = filterIlegalMove(listMovesKing(board.xKingWhite,board.yKingWhite, board), board, colors).empty()
    if(isCheckKingWhite && isEmptyMoveLstKingWht){...}
//проверка на наличие шаха у белого кололя и пустоту списка его ходов
//добавил логические переменные

12. float lenght = float volume / float height / float width - double lenght = double volume / double height / double width
//формула подсчета длины из объема
//сменил все чмсла float на число с большей точностью double







