maximum = 0
array_field = []
change = 0


def init():
    global maximum
    global array_field

    unknown_x = 0
    unknown_y = 0
    step = 1

    search_list = dict()
    search_list['0'] = [[1, 2, 3],
                        [4, 8, '_'],
                        [6, 5, 7]]

    parents = dict()
    flag_change = True
    list_of_numbers_for_paste = []
    maximum = 3
    draw()
    while True:
        intermediate_array = search_list[step]
        step += 1
        if won():
            break
        for y in range(maximum):
            for x in range(maximum):
                if intermediate_array[y][x] == '_':
                    unknown_x = x
                    unknown_y = y

        # First line
        if unknown_y == 0 and unknown_x == 0:
            # Down
            saving_array = intermediate_array
            saving_array[1][0], saving_array[0][0] = saving_array[0][0], saving_array[1][0]
            search_list[step * 4 + 3] = saving_array

            # Right
            saving_array = intermediate_array
            saving_array[0][1], saving_array[0][0] = saving_array[0][0], saving_array[0][1]
            search_list[step * 4 + 4] = saving_array

        elif unknown_y == 0 and unknown_x == 1:
            # Left
            saving_array = intermediate_array
            saving_array[0][0], saving_array[0][1] = saving_array[0][1], saving_array[0][0]
            search_list[step * 4 + 2] = saving_array

            # Down
            saving_array = intermediate_array
            saving_array[1][1], saving_array[0][1] = saving_array[0][1], saving_array[1][1]
            search_list[step * 4 + 3] = saving_array

            # Right
            saving_array = intermediate_array
            saving_array[0][2], saving_array[0][1] = saving_array[0][1], saving_array[0][2]
            search_list[step * 4 + 4] = saving_array

        elif unknown_y == 0 and unknown_x == 2:
            # Left
            saving_array = intermediate_array
            saving_array[0][1], saving_array[0][2] = saving_array[0][2], saving_array[0][1]
            search_list[step * 4 + 2] = saving_array

            # Down
            saving_array = intermediate_array
            saving_array[2][0], saving_array[0][2] = saving_array[0][2], saving_array[2][0]
            search_list[step * 4 + 2] = saving_array

        # Second line
        elif unknown_y == 1 and unknown_x == 0:
            # Up
            saving_array = intermediate_array
            saving_array[0][0], saving_array[1][0] = saving_array[1][0], saving_array[0][0]
            search_list[step * 4 + 1] = saving_array

            # Down
            saving_array = intermediate_array
            saving_array[2][0], saving_array[1][0] = saving_array[1][0], saving_array[2][0]
            search_list[step * 4 + 3] = saving_array

            # Right
            saving_array = intermediate_array
            saving_array[1][1], saving_array[1][0] = saving_array[1][0], saving_array[1][1]
            search_list[step * 4 + 4] = saving_array

        elif unknown_y == 1 and unknown_x == 1:
            # Up
            saving_array = intermediate_array
            saving_array[0][1], saving_array[1][1] = saving_array[1][1], saving_array[0][1]
            search_list[step * 4 + 1] = saving_array

            # Left
            saving_array = intermediate_array
            saving_array[1][0], saving_array[1][1] = saving_array[1][1], saving_array[1][0]
            search_list[step * 4 + 2] = saving_array

            # Down
            saving_array = intermediate_array
            saving_array[2][1], saving_array[1][1] = saving_array[1][1], saving_array[2][1]
            search_list[step * 4 + 3] = saving_array

            # Right
            saving_array = intermediate_array
            saving_array[1][2], saving_array[1][1] = saving_array[1][1], saving_array[1][2]
            search_list[step * 4 + 4] = saving_array

        elif unknown_y == 1 and unknown_x == 2:
            # Up
            saving_array = intermediate_array
            saving_array[0][2], saving_array[1][2] = saving_array[1][2], saving_array[0][2]
            search_list[step * 4 + 1] = saving_array

            # Left
            saving_array = intermediate_array
            saving_array[1][1], saving_array[1][2] = saving_array[1][2], saving_array[1][1]
            search_list[step * 4 + 2] = saving_array

            # Down
            saving_array = intermediate_array
            saving_array[2][2], saving_array[1][2] = saving_array[1][2], saving_array[2][2]
            search_list[step * 4 + 3] = saving_array

        # Third line
        elif unknown_y == 2 and unknown_x == 0:
            # Up
            saving_array = intermediate_array
            saving_array[1][0], saving_array[2][0] = saving_array[2][0], saving_array[1][0]
            search_list[step * 4 + 1] = saving_array

            # Right
            saving_array = intermediate_array
            saving_array[2][1], saving_array[2][0] = saving_array[2][0], saving_array[1][0]




def draw():
    for y in range(maximum):
        for x in range(maximum):
            print(str(array_field[y][x]), end=' ')
        print()


# def move():
#     global change
#     y_number = None
#     x_number = None
#     y_space = None
#     x_space = None
#     changing_number = int(input('Укажите номер на плитке, которую вы хотите переместить: '))
#     for y in range(maximum):
#         for x in range(maximum):
#             if array_field[y][x] == changing_number:
#                 y_number = y
#                 x_number = x
#             elif array_field[y][x] == '_':
#                 y_space = y
#                 x_space = x
#     # Если номер выше чем пустая ячейка
#     if y_number == y_space - 1 and x_number == x_space:
#         array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
#                                                                          array_field[y_number][x_number]
#         draw()
#     # Если номер правее чем пустая ячейка
#     elif y_number == y_space and x_number == x_space + 1:
#         array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
#                                                                          array_field[y_number][x_number]
#         draw()
#     # Если номер ниже чем пустая ячейка
#     elif y_number == y_space + 1 and x_number == x_space:
#         array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
#                                                                          array_field[y_number][x_number]
#         draw()
#     # Если номер левее чем пустая ячейка
#     elif y_number == y_space and x_number == x_space - 1:
#         array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
#                                                                          array_field[y_number][x_number]
#         draw()
#     else:
#         print('Вы ввели неверное значение, повторите вновь.')
#         move()


def won():
    # Определение переменных для дальнейшего использования
    flag_won = True
    y_space = None
    x_space = None
    # Замена пустой ячейки на ячейку которая должна быть на её месте
    for y in range(maximum):
        for x in range(maximum):
            if array_field[y][x] == '_':
                array_field[y][x] = 9
                y_space = y
                x_space = x
    # Сравнение предыдущего и нынешнего значения
    for y in range(maximum):
        for x in range(maximum):
            # Если предыдущее больше чем нынешнее - ты не выиграл
            if y > 0 and x == 0 and array_field[y - 1][maximum - 1] > array_field[y][x]:
                flag_won = False
            elif array_field[y][x - 1] > array_field[y][x] and x > 0:
                flag_won = False
    array_field[y_space][x_space] = '_'
    if flag_won:
        return True
    else:
        return False
