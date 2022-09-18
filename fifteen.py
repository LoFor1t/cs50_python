import random

maximum = 0
array_field = []
change = 0


def init():
    global maximum
    global array_field
    global change
    flag_change = True
    list_of_numbers_for_paste = []
    # Определение размеров поля
    while type(maximum) == str or maximum <= 0:
        maximum = input('Введите размер поля одной цифрой (при вводе 4 - поле = 4x4) - ')
        try:
            maximum = int(maximum)
        except ValueError:
            continue
    # Создание массива для последующего вставления в него ячеек
    array_field = [[-1] * maximum for i in range(maximum)]
    # Заполнения поля ячейками
    for number in range(maximum * maximum):
        list_of_numbers_for_paste.append(number + 1)
    for y in range(maximum):
        for x in range(maximum):
            array_field[y][x] = random.choice(list_of_numbers_for_paste)
            list_of_numbers_for_paste.remove(array_field[y][x])
    # Замена одной из ячеек на пустую
    while flag_change:
        draw()
        change = int(input('Из выведенного поля выше, введите число которое присвоено этой ячейке, которую, вы хотели '
                           'бы "вытащить": '))
        for y in range(maximum):
            for x in range(maximum):
                if array_field[y][x] == change:
                    array_field[y][x], change = '_', array_field[y][x]
                    flag_change = False
        if flag_change:
            print('Такого числа нет в вашей игре, повторите операцию снова.')
    draw()


def draw():
    for y in range(maximum):
        for x in range(maximum):
            print(str(array_field[y][x]), end=' ')
        print()


def move():
    global change
    y_number = None
    x_number = None
    y_space = None
    x_space = None
    changing_number = int(input('Укажите номер на плитке, которую вы хотите переместить: '))
    for y in range(maximum):
        for x in range(maximum):
            if array_field[y][x] == changing_number:
                y_number = y
                x_number = x
            elif array_field[y][x] == '_':
                y_space = y
                x_space = x
    # Если номер выше чем пустая ячейка
    if y_number == y_space - 1 and x_number == x_space:
        array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
                                                                         array_field[y_number][x_number]
        draw()
    # Если номер правее чем пустая ячейка
    elif y_number == y_space and x_number == x_space + 1:
        array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
                                                                         array_field[y_number][x_number]
        draw()
    # Если номер ниже чем пустая ячейка
    elif y_number == y_space + 1 and x_number == x_space:
        array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
                                                                         array_field[y_number][x_number]
        draw()
    # Если номер левее чем пустая ячейка
    elif y_number == y_space and x_number == x_space - 1:
        array_field[y_number][x_number], array_field[y_space][x_space] = array_field[y_space][x_space], \
                                                                         array_field[y_number][x_number]
        draw()
    else:
        print('Вы ввели неверное значение, повторите вновь.')
        move()


def won():
    # Определение переменных для дальнейшего использования
    flag_won = True
    y_space = None
    x_space = None
    # Замена пустой ячейки на ячейку которая должна быть на её месте
    for y in range(maximum):
        for x in range(maximum):
            if array_field[y][x] == '_':
                array_field[y][x] = change
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


if __name__ == '__main__':
    init()
    while True:
        move()
        if won():
            print('Ты выиграл!🥳')
            break
