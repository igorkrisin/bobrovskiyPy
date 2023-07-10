1
до:////////////////////////////
gameStore = ["к", "н", "б"]
#...код...#
while playerScore != countAttempt and compScore != countAttempt:
#...код...#

после:////////////////////////
#...код...#
gameStore = ["к", "н", "б"]
while playerScore != countAttempt and compScore != countAttempt:
# ...код...#
//массив значений перебираемых в цикле, перенес и инициализировал его непосредственно перед циклом



2
до:////////////////////////////
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

#...код...#
turn = "X"
for i in range(9):
    printBoard(theBoard)
    # ...код...#

после:////////////////////////
#...код...#
turn = "X"
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}
for i in range(9):
    printBoard(theBoard)
    # ...код...#

//словарь ханящий значения клеток крестики-нолики,  перенес и инициализировал его непосредственно перед циклом

3
до://///////////////
#...код...#

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1300, 500))
car = pygame.image.load("car1.png")
car = pygame.transform.scale(car, (180, 132))
car_pink = pygame.image.load("car2.png")
car_pink = pygame.transform.scale(car_pink, (100, 117))
bullet = pygame.image.load("bul.png")
bullet = pygame.transform.scale(bullet,(20,30))
finish = pygame.image.load("finish.png")
finish1 = False
finish2 = False

window = pygame.display.set_mode((1300, 500))
screen = pygame.Surface((1300, 500))
start_game = True
speed = 25
number = 1
bull_speed = 0.1
#...код...#

после://///////////////////

#...код...#

CARS_SPEED = 25
number = 1


bullet = pygame.image.load("bul.png")
bullet = pygame.transform.scale(bullet, (20, 30))

def bul_to_go(y_bull, BULLS_SPEED):
    while y_bull > 0:
        y_bull -= BULLS_SPEED
        screen.blit(bullet, (788, y_bull))


y_car = 340
y_car_pink = 344
y_bull = y_car

text_font = pygame.font.SysFont("comicsansmc", 80)
text_render = text_font.render("Выиграл Игрок 1", 0, (0, 0, 0))
text_render_2 = text_font.render("Выиграл Игрок 2", 0, (0, 0, 0))
text_render_3 = text_font.render(str(number), 0, (0, 0, 0))

finish = pygame.image.load("finish.png")
finish1 = False
finish2 = False
window = pygame.display.set_mode((1300, 500))
screen = pygame.Surface((1300, 500))
start_game = True

while start_game:
 #...код...#

    window.blit(screen, (0, 0))

    bg = pygame.image.load("bg.png")
    bg = pygame.transform.scale(bg, (1300, 500))
    car = pygame.image.load("car1.png")
    car = pygame.transform.scale(car, (180, 132))
    car_pink = pygame.image.load("car2.png")
    car_pink = pygame.transform.scale(car_pink, (100, 117))

    #...код...#

//код в котором все переменные и константы вынесены в начало файла,
//так делать нельзя их нужно инициплизировать непосредственно перед использованием
//перенес все перемные непосредственно к месту их использования, исправил название констанкт
//BULLS_SPEED = 0.1 - никак не используется эта константа - удалил

4
до:////////////////

#...код...#

FRAME_COLOR = (0,255,204)
WHITE = (255,255,255)
BLUE = [204,255,255]
SIZE_BLOCK=20
COUNT_BLOKS = 20
SNAKE_COLOR = [255,6,57]
MARGIN = 1
size = [500,600]

#...код...#

while True:
    # ...код...#
после://///////////////

#...код...#
FRAME_COLOR = (0,255,204)
WHITE = (255,255,255)
BLUE = [204,255,255]
SIZE_BLOCK=20
COUNT_BLOKS = 20
SNAKE_COLOR = [255,6,57]
MARGIN = 1
size = [500,600]

while True:
    # ...код...#

//все константы перенес непосредственно к месту из выполения

5
до://///////////////
int whiteBl = white;
 	  while(1) {
		list* lst = NULL;
        # ...код...#

после://////////////////
int whiteBl = white;
 	  while(1) {
        # ...код...#

//главный цикл программы, в нем нашел неиспользуемую переменную - удалил

6.
до://////////////////
int findBoardinLst(boards* lstBoard, piece board[64]){
    while(lstBoard != NULL) {
	if(comparisonBoards(lstBoard->board, board)){
	    return 1;
	}
	lstBoard = lstBoard->next;
    }
    # ...код...#
после://////////////////

int findBoardinLst(boards* lstBoard, piece board[64]){
    while(lstBoard != NULL) {
	if(comparisonBoards(lstBoard->board, board)){
	    return 1;
	}
	lstBoard = lstBoard->next;
    }
    lstBoard = NULL;

// в функции поиска досок, после использования переменной присвоил ей null

7.
до://////////////////////
piece * newBoard2 = copyBoard(board);
# ...код...#
if (checkEnPassantBlackRight(newBoard2)){
newBoard2[y * 8+x] = empty;
newBoard2[(y-1) * 8+x] = pawn;
newBoard2[(y-2) * 8+x-1] = empty;
}
# ...код...#
после://////////////////////
piece * newBoard2 = copyBoard(board);
# ...код...#
if (checkEnPassantBlackRight(newBoard2)){
newBoard2[y * 8+x] = empty;
newBoard2[(y-1) * 8+x] = pawn;
newBoard2[(y-2) * 8+x-1] = empty;
}
piece* newBoard2 = NULL;
# ...код...#

//присвоил временному списку для хранения досок NULL после использования

8.

до://///////////////////////
list* returnEl(list* lst, int numbEl) {
    int count = 0;
    while(count != numbEl) {
		count++;
		lst = lst -> next;
    }
# ...код...#
после:///////////////////////
list* returnEl(list* lst, int numbEl) {
    int count = 0;
    while(count != numbEl) {
		count++;
		lst = lst -> next;
    }
    count = 0
# ...код...#
//В функции возврата элемента по его номеру обнулил счетчик после его использования

9.
    до:///////////////////////
    bin1 = convertTo16Bit(bin1)
    bin2 = convertTo16Bit(bin2)
    # ...код...#
    summ = additionBin(bin1, temp)
    if(summ.size() > bin1.size())
        summ[0] = ""
    end
    # ...код...#
    после:////////////////////////
    bin1 = convertTo16Bit(bin1)
    bin2 = convertTo16Bit(bin2)
    # ...код...#
    summ = additionBin(bin1, temp)
    if(summ.size() > bin1.size())
        summ[0] = ""
    bin1 = "Error шт functionn SubBinNEw"
    bin2 = "Error шт functionn SubBinNEw"
    end

//записал во временную строку сообщение об ошибке указав название функции откуда сообние вызывано

10.
до:////////////////////////////
def dataInstruc()
    # ...код...#
    for i in 0...tempArr.size
        if tempArr[i][0] == "#"
            next
        elsif  tempArr[i] == ""
            next
        elsif tempArr[i].match(/ORG\s+([0-9]+)/)
            temp = tempArr[i].match(/ORG (.*)/)
            objectFile += addition0Param(10, convertDecToBin(temp[1].to_i).to_s)+"\n"
            # ...код...#

после:///////////////////////////
def dataInstruc()
    # ...код...#
    for i in 0...tempArr.size
        if tempArr[i][0] == "#"
            next
        elsif  tempArr[i] == ""
            next
        elsif tempArr[i].match(/ORG\s+([0-9]+)/)
            puts "tempARR: #{(tempArr[i])}"
            temp = tempArr[i].match(/ORG (.*)/)
            objectFile += addition0Param(10, convertDecToBin(temp[1].to_i).to_s)+"\n"
            puts "objectFile: \n#{objectFile}"
            # ...код...#

//добавил в функцию обработки инструкций отладочную печать занчений временного массива объекта файла

11.
до:////////////////////////
# ...код...#
when "1010"                                        #MULT
    if adressModeField != '01'
        mbr = memory[convertBinToInt(mar)]
    end
    ac = multBin(ac, mbr)
    pc = binIncrement(pc)
# ...код...#
после:////////////////////////
# ...код...#
when "1010"                                        #MULT
    if adressModeField != '01'
        mbr = memory[convertBinToInt(mar)]
        p "mbr: #{mbr}"
    end
    p "ac1: #{ac}"
    ac = multBin(ac, mbr)
    p "ac2: #{ac}"
    pc = binIncrement(pc)
# ...код...#

//Добавил отладчную печать регистров в главный цикл процессора, теперь буду явно видет значения регистров

12.
до:////////////////////////
# ...код...#
case operatField
    when "0000" 			                        #HALT
    traceRegister(ir, xr, mar, mbr, pc, ac,index)         #TRACER
    break
# ...код...#
после://///////////////////
# ...код...#
case operatField
    when "0000" 			                        #HALT
    p "operatField: #{operatField}"
    traceRegister(ir, xr, mar, mbr, pc, ac,index)         #TRACER
    break
# ...код...#

// добавил отладочную печать в главный цикл программы при отладке сиогу уонтролировать значения полей

13.
до://////////////////////////
# ...код...#
    if temp == nil
        raise "line number: #{i}"
    end
    arr = temp[0].split(" ")
    puts arr[1]
    if arr[0] == "ORG"
        valueLable = arr[1].to_i - 1
    # ...код...#

после://////////////////////////
# ...код...#
    if temp == nil
        print "mnemonic text with lable is wrong: ";p temp;
        raise "line number: #{i}"
    end
    arr = temp[0].split(" ")
    puts arr[1]
    if arr[0] == "ORG"
        valueLable = arr[1].to_i - 1
        puts "valueLable: #{valueLable}"
    # ...код...#

//Добавлена для парсинга значений отдалочная печать что бы модно было контролировать
//что парсинг выдает

14.

до://////////////////////////////
def multBin(bin1, bin2)
    summSubTotal = []
    summ = ""
    bin1 = bin1.reverse
    bin2 = bin2.reverse
    # ...код...#
    summ = additionBin(summSubTotal[0], summSubTotal[1])
    # ...код...#
после://////////////////////////////
def multBin(bin1, bin2)
    summSubTotal = []
    bin1 = bin1.reverse
    bin2 = bin2.reverse
    # ...код...#
    summ = additionBin(summSubTotal[0], summSubTotal[1])
    # ...код...#

// в функции слишкрм рано объявлено значение пересенной summ - убрал инициализацию пустой строкой
//оставил код где она иницивлизируется в нужном месте значением

15.

до://////////////////////////
def multBin(bin1, bin2)
    summSubTotal = []
    bin1 = bin1.reverse
    bin2 = bin2.reverse
    for i in 0...bin1.size
        temp = ""
        for y in 0...bin2.size
            temp = ((bin1[i].to_i) * (bin2[y].to_i)).to_s + temp
            puts temp
        end
        # ...код...#
def multBin(bin1, bin2)
    summSubTotal = []
    bin1 = bin1.reverse
    bin2 = bin2.reverse
    puts "bin1 #{bin1}"
    puts "bin2 #{bin2}"
    for i in 0...bin1.size
        puts "i: #{i} "
        temp = ""
        for y in 0...bin2.size
            puts "y: #{y} "
            temp = ((bin1[i].to_i) * (bin2[y].to_i)).to_s + temp
            puts temp
        end
        # ...код...#
//Добавил отладочную печать что ms видеть явно правильное ли значение принимают числа
//на какой итерации цикла какие действия происходят распечатал счетчики
//и значение промежуточного массива