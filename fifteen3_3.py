import time
import numpy as np

maximum = 0
array_field = []
change = 0
search_list = {}
intermediate_array = []


def init():
    global maximum
    global array_field
    global intermediate_array

    unknown_x = 0
    unknown_y = 0
    step = 0

    global search_list
    search_list[0] = np.array([[1, 2, 3],
                               [4, 8, '_'],
                               [6, 5, 7]])

    parents = dict()
    flag_change = True
    list_of_numbers_for_paste = []
    maximum = 3
    last_step = 10
    # draw()
    while True:
        try:
            intermediate_array = search_list[step]
        except KeyError:
            step += 1
            continue
        step += 1
        draw()
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
            saving_array = intermediate_array.copy()
            saving_array[1][0], saving_array[0][0] = saving_array[0][0], saving_array[1][0]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[0][1], saving_array[0][0] = saving_array[0][0], saving_array[0][1]
            search_list[last_step + 2] = np.array(saving_array.copy())
            last_step += 2

        elif unknown_y == 0 and unknown_x == 1:
            # Left
            saving_array = intermediate_array.copy()
            saving_array[0][0], saving_array[0][1] = saving_array[0][1], saving_array[0][0]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Down
            saving_array = intermediate_array.copy()
            saving_array[1][1], saving_array[0][1] = saving_array[0][1], saving_array[1][1]
            search_list[last_step + 2] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[0][2], saving_array[0][1] = saving_array[0][1], saving_array[0][2]
            search_list[last_step + 3] = np.array(saving_array.copy())
            last_step += 3

        elif unknown_y == 0 and unknown_x == 2:
            # Left
            saving_array = intermediate_array.copy()
            saving_array[0][1], saving_array[0][2] = saving_array[0][2], saving_array[0][1]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Down
            saving_array = intermediate_array.copy()
            saving_array[2][0], saving_array[0][2] = saving_array[0][2], saving_array[2][0]
            search_list[last_step + 2] = np.array(saving_array.copy())
            last_step += 2

        # Second line
        elif unknown_y == 1 and unknown_x == 0:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[0][0], saving_array[1][0] = saving_array[1][0], saving_array[0][0]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Down
            saving_array = intermediate_array.copy()
            saving_array[2][0], saving_array[1][0] = saving_array[1][0], saving_array[2][0]
            search_list[last_step + 2] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[1][1], saving_array[1][0] = saving_array[1][0], saving_array[1][1]
            search_list[last_step + 3] = np.array(saving_array.copy())
            last_step += 3

        elif unknown_y == 1 and unknown_x == 1:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[0][1], saving_array[1][1] = saving_array[1][1], saving_array[0][1]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Left
            saving_array = intermediate_array.copy()
            saving_array[1][0], saving_array[1][1] = saving_array[1][1], saving_array[1][0]
            search_list[last_step + 2] = np.array(saving_array.copy())

            # Down
            saving_array = intermediate_array.copy()
            saving_array[2][1], saving_array[1][1] = saving_array[1][1], saving_array[2][1]
            search_list[last_step + 3] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[1][2], saving_array[1][1] = saving_array[1][1], saving_array[1][2]
            search_list[last_step + 4] = np.array(saving_array.copy())
            last_step += 4

        elif unknown_y == 1 and unknown_x == 2:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[0][2], saving_array[1][2] = saving_array[1][2], saving_array[0][2]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Left
            saving_array = intermediate_array.copy()
            saving_array[1][1], saving_array[1][2] = saving_array[1][2], saving_array[1][1]
            search_list[last_step + 2] = np.array(saving_array.copy())

            # Down
            saving_array = intermediate_array.copy()
            saving_array[2][2], saving_array[1][2] = saving_array[1][2], saving_array[2][2]
            search_list[last_step + 3] = np.array(saving_array.copy())
            last_step += 3

        # Third line
        elif unknown_y == 2 and unknown_x == 0:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[1][0], saving_array[2][0] = saving_array[2][0], saving_array[1][0]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[2][1], saving_array[2][0] = saving_array[2][0], saving_array[2][1]
            search_list[last_step + 2] = np.array(saving_array.copy())
            last_step += 2

        elif unknown_y == 2 and unknown_x == 1:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[1][1], saving_array[2][1] = saving_array[2][1], saving_array[1][1]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Left
            saving_array = intermediate_array.copy()
            saving_array[2][0], saving_array[2][1] = saving_array[2][1], saving_array[2][0]
            search_list[last_step + 2] = np.array(saving_array.copy())

            # Right
            saving_array = intermediate_array.copy()
            saving_array[2][2], saving_array[2][1] = saving_array[2][1], saving_array[2][2]
            search_list[last_step + 3] = np.array(saving_array.copy())
            last_step += 3

        elif unknown_y == 2 and unknown_x == 2:
            # Up
            saving_array = intermediate_array.copy()
            saving_array[1][2], saving_array[2][2] = saving_array[2][2], saving_array[1][2]
            search_list[last_step + 1] = np.array(saving_array.copy())

            # Left
            saving_array = intermediate_array.copy()
            saving_array[2][1], saving_array[2][2] = saving_array[2][2], saving_array[2][1]
            search_list[last_step + 2] = np.array(saving_array.copy())
            last_step += 2
        print(step)






def draw():
    for y in range(maximum):
        for x in range(maximum):
            print(str(intermediate_array[y][x]), end=' ')
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
            if intermediate_array[y][x] == '_':
                intermediate_array[y][x] = 9
                y_space = y
                x_space = x
    # Сравнение предыдущего и нынешнего значения
    for y in range(maximum):
        for x in range(maximum):
            # Если предыдущее больше чем нынешнее - ты не выиграл
            if y > 0 and x == 0 and intermediate_array[y - 1][maximum - 1] > intermediate_array[y][x]:
                flag_won = False
            elif intermediate_array[y][x - 1] > intermediate_array[y][x] and x > 0:
                flag_won = False
    intermediate_array[y_space][x_space] = '_'
    if flag_won:
        return True
    else:
        return False


if __name__ == '__main__':
    init()