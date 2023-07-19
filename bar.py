3.1

1.
int yEnpasWhite = 3;
int yEnpasBlack = 4;
//следует добавить комментарий, что шахматных  правилах enpassant для белых может
//случится только по линии 3, а для черных только по линии 4 и добавить  комментарий о правиле empassant
//данное описание будет служить напомнанием части правил именно самой игры
// и поможет разобраться новому разрабу или напомнит, а что такое enpassant мне
// например: en passant — (на проходе) в шахматах означает специальный ход пешки,
//при котором она берёт пешку противника, перемещённую с начальной позиции сразу на два поля,
//Первая пешка завершает взятие именно на этом, пересечённом поле, как если бы пешка противника
//переместилась лишь на одно поле.
//именно поэтому координаты при которых enpassant имеет место быть для белых линия 3 для черных 4.

2.

vector<variant<Move, castling>> & Castling(Matrix<Pieces> & board, color colors) {
    //координаты castling для белых
    array <int, 2> kingDepW = {4, 7};

//Castling(Рокировка) — двойной ход, который выполняют король и ладья, ни разу не ходившие.
//Сначала король делает ход на две клетки в сторону ладьи.
//Затем ладья переносится через короля и ставится на следующее за ним поле.
//Координаты для кастлинга соотвествуют начальному расположению фигур,
//что соотвестует условиям выполения castling

3.
bool checkMate(Matrix<Pieces> &board, color colors) {
    if(colors == white) {
        if(checkCheck(board.xKingWhite,board.yKingWhite, board) && filterIlegalMove(listMovesKing(board.xKingWhite,board.yKingWhite, board), board, colors).empty()) {
            return true;
        }

//можно добавить условие мата например так:
//когда король белых находится под ударом и его список ходов пуст - белым мат,
//игра заканчивается победой черных

4.
//Шах - это попадание короля под угрозу "вражеской" фигуры (когда в списке ходов фигуры есть король)
//функция проверки короля на наличие шаха от "вражеской фигуры"
bool checkForCheck(int x, int y, Matrix<Pieces> &board, color colors)


5.
//проверка на шах королю от вражеской фигуры Пешка
bool checkToPawn(int x, int y, Matrix<Pieces> &board)


6.

// для того что бы сделать рокировку(Castling), в качесиве хода принимаем 0-0 и О-О
//конкретные команды для рокировки:
//0-0 - Castling rightBlack
//0-0-0 - Castling leftBlack
//O-O - Castling rightWhite
//O-O-O - Castling leftWhite

if(coord == "0-0" && checkMoveInEverList(everyMove, convertZeroToVariant(coord, colors))){
    return moveForBoard(board, colors==white?rightWhite:rightBlack);
}
else if(coord == "0-0-0" && checkMoveInEverList(everyMove, convertZeroToVariant(coord, colors))) {

7.

iff(getYArr(move) == 0 && board.at(getXDep(move), getYDep(move)) == P(pawn, white)){
//при достижении пешки противоположного края доски, она превращается в королеву
    board.at(getXArr(move), getYArr(move)) = P(queen, white);
    board.at(getXDep(move), getYDep(move)) = Empty;
}




3.2

1.
// координаты castling для белых
array <int, 2> kingDepW = {4, 7};
array <int, 2> rookhDepWL = {0, 7};
array <int, 2> rookDepWR = {7, 7};
// координаты castling для черных
array <int, 2> kingDepBl = {4, 0};
array <int, 2> rookDepBlL = {0, 0};
array <int, 2> rookDepBlR = {7, 0};
vector <variant<Move, castling>> *listMoves = new vector <variant<Move, castling>>;
//можно сделать код более наглядным за счет имен переменных м убрать комментарии.
//например: kingDepW - startCastlingCoordWhtKing

2.
// проверяем есть ли слева у белых кастлинг
if (board.at(kingDepW.at(0), kingDepW.at(1)).name_piece == king && board.at(kingDepW.at(0),
                                                                             kingDepW.at(1)).color_piece == colors){
//можно заменить длинные выражения на лонические переменные и сделать код понятным без комментариев
//например: (board.at(kingDepW.at(0), kingDepW.at(1)).name_piece == king && board.at(kingDepW.at(0)
//заменить на isKingForCastling && isColorWhiteForCastling

3.
if(board.at(arrX.at(i), arrY.at(i)).name_piece == knight &&
                                    board.at(x, y).color_piece == board.at(arrX.at(i), arrY.at(i)).color_piece) {//проверить есть ли конь в пятне короля?
    continue;
}

//при помощи логических переменных сделать код условий более понятным, например:
//isKnightInLstMoveKing = board.at(arrX.at(i), arrY.at(i)).name_piece == knight
//isColorKnightSameKing = board.at(x, y).color_piece == board.at(arrX.at(i), arrY.at(i)).color_piece)

4.

return false;//нет угрозы от фигуры - поэтому я false
//можно сложить булевое значение в переменную, что бы сделать код понятнее
//тогда комментарий будет не нужен
//например: isDangerFromEnemyPiece = true
            return !isDangerFromEnemyPiece

5.
def addQuantityZero(bin, quan):#эта функция добавляет НУЖНОЕ количество нулей
//можно прописать в названии функции более явный смысл и убрать комментарий
//например: def addRequiredQuantZero(bin, quan):