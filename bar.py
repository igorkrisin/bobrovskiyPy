
1 x - START_GAME_COORD_X
//координаты с которых стратует змейка по оси Х - сделал название константы понятным,
//написал заглавными буквами с подчеркиванием

//далее по коду я менял эту константу - показывая направление движения змейки, что неверно
//и затрудняет чтение кода, нужно было присвоить значение константы в переменной и изменять ее

2 одну такую строку x += x_napravl -
заменить на 2 таких current_coord_x = START_GAME_COORD_X
                    current_coord_x += direction_move


3 vh - VIEW_HIGHT_PXL
// высота экрана pygame в пикселях, правильно и понятно записал константу добавил постфикс с еденицами измерения

4 pygame.time.delay(100) - TIME_DELAY_MS = 100
                         pygame.time.delay(TIME_DELAY_MS)
//время задержки при обновлении экрана в миллисекундах. 100 - магическое число непонятное значение в коде,
//я решил выделить ее в отдельную константу

5 speed - SNAKE_SPEED_FPS
//скорость движения змейки, она же обновеления экрана. Символы заменил на заглавные добавил осмымсленное название
//и префикс с единицами измерения

6 y_car - START_COORD_RED_CAR_TO_Y
//начальная координата машины по оси y, указал что это координаты начала движения авто


7 creen.blit(text_render, (200, 200)) - TEXT_HIGHT_PXL = 200
                                      TEXT_WIDTH_PXL = 200
                                      creen.blit(text_render, (TEXT_HIGHT_PXL, TEXT_WIDTH_PXL))
//размер поля для текста, данная величина используется по коду в нескольких местах, в одном и том же смысле.
// Я сложил ее в константу, в случае изменения величины поля для текста, не нужно будет менять несколько мест
//плюс это магические величины непонятно что означают

8 const num - const FACTOR_NUMS
//множитель чисел, изменил на правильное написание добавмл понятное название

9 TITLE - SIZE_TITLE_TEXT_PXL
//размер текста титула в пикселях, добавил осмысленное назвние

10 DIRECTS - DIRECTS_MOVE_FOR_TANK
//направление движения для танка. Добавил осмысленное название.

11 if jump_counter >= -30 - MAX_JUMP_SIZE = -30
                            if jump_counter >= MAX_JUMP_SIZE
//Максималтная величина вылета персонажа по оси Y, добавил название числу
//значение которого без описания малопонятно(или не понятно)

12 number = 1 -
//количество строк которые выведутся на экран, думаю данную констарту можно убрать -
// в коде применяется в одном месте в стандартной функции и имеет значение 1.


