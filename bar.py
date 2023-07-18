1.
shcitalka = ["на ", "злотом ", "крыльце ", "сидели ", "царь ", "царевич ", "король ",
             "корлевич ", "сапожник ", "портной ", "кто ты будешь такой ", "выбирай поскорей",
             "не задерживай", "добрых и честных", "людей"]
your_сhoiсe = input("приступиступим к считалке? введите 'да' с клавиатуры\n для отмены введите нет\n")
if your_сhoiсe == "да":
for y in range(len(shcitalka)):
    time.sleep(1)
    count = random.randint(0, playerCounts - 1)
    print(shcitalka[y], " ", playerName[count][0])

// здесь вместо цикла по массиву можно воспользоваться односвязным списком(например) или стеком,
// и итерироваться по нему последовательно

2.
int bestScore(vector<int> evaluatMove) {
int bScore = evaluatMove[0];
for(int i = 0; i < evaluatMove.size();i++) {
    if(evaluatMove.at(i) > bScore) {
	    bScore = evaluatMove.at(i);
    }
}
    return bScore;
}
//в данной функции (поиск лучшей оценки) можно было вместо массива(вектора) использовать односвязный список
//здесь итерация идет последовательная по элементам, ничего не мешает сменить структуру данных

3.

int indexMaxEl(vector < int > allEvaluat)
{
int bScore = allEvaluat[0];
int index = 0;
for (int i = 0;i < allEvaluat.size(); i++) {
    if (allEvaluat.at(i) > bScore){
        bScore = allEvaluat.at(i);
        index = i;
    }
}
cout << "index max: " << index << endl;

return index;
}

//в данной функции(определение индекса максимального элемента) можно было
//вместо массива(вектора) использовать односвязный список или очередь
//номер элемента можно без проблем определить и в списке и в очереди

4.
bool isInt(int num) {
int arr[9];
    for (int i = 1; i < 10; i++){
            arr[i] = i;
    }
    for (int i = 0; i < 9; i++){
        if (arr[i] == num){
            return true;
        }
    }
    return false;

}

// в данной функции(определяет число или нет является ее аргументом) можно было сравнивать
//сам итератор с арнументом без создания массива

5.
vector<variant<Move, castling>> &listMovesKing(int x, int y, Matrix<Pieces> &board) {
    vector<variant<Move, castling>> *listMove = new vector<variant<Move, castling>>;
    variant<Move, castling> doMove;

    array <int, 8> arrY = {y+1, y+1, y+1, y, y-1, y-1, y-1, y};
    array <int, 8> arrX = {x+1, x, x-1, x-1, x-1, x, x+1, x+1};

     for (int i = 0; i <(int)(sizeof(arrX)/sizeof(arrX.at(0))); i++) {
         if(!checkOutOfRange(arrX.at(i), arrY.at(i), board)){
             addMovesInList(x, y, arrX.at(i), arrY.at(i), doMove, *listMove, board);
         }
         else {
             continue;
         }
     }

    return *listMove;
}

//вместо массива можно сложить логистику ходов сложить в массив или стек и итерироваться по нему последовательно
