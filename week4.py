def sigma(n):
    # Если число меньше единицы, то завершаем рекурсивную функцию
    if n <= 1:
        return 1

    # Возвращаем нынешнее значение и туже функцию со значением на единицу меньше
    return n + sigma(n - 1)


def search(n, array, start, end):
    # Если начало поиска больше чем конец - значит завершаем рекурсивную функцию
    if start > end:
        return False

    # Середина списка - отправная точка
    middle = (start + end) // 2
    # Если середина == искомому - завершаем функцию выводя True
    if array[middle] == n:
        return True
    # Если середина меньше искомого - запускаем функцию с началом - середина+1(чтобы уменьшить количество итераций,
    # так как мы уже знаем, что искомое не равно середине) и уже известным концом
    elif array[middle] < n:
        return search(n, array, middle + 1, end)
    # Если середина больше искомого - запускаем функцию с известным уже началом и с концом - серединой-1
    # (чтобы уменьшить количество итераций, так как мы уже знаем, что искомое не равно середине)
    elif array[middle] > n:
        return search(n, array, start, middle - 1)


def whodunit():
    with open('pset4/bmp/clue.bmp', 'rb') as f:
        res = []  # Массив, в который будет вставляться конечный результат
        header = f.read(54)  # Переменная с заголовками
        val = bytearray(f.read())  # Переменная с данными о цветах пикселей
        # Цикл с шагом в 3, для того, чтобы переходить от одного пикселя к другому
        for increment in range(2, len(val), 3):
            # Если пиксель красного цвета - приравниваем его к предыдущему
            if val[increment] == 255 and val[increment - 1] == 0 and val[increment - 2] == 0:
                val[increment], val[increment - 1], val[increment - 2] = val[increment - 3], val[increment - 4], val[
                    increment - 5]
            # Если красного меньше 240 - следовательно он не белый, тогда мы приравниваем значение всех остальных цветов
            # этого пикселя, чтобы получить оттенок серого цвета
            if val[increment] < 240:
                val[increment - 2] = val[increment - 1] = val[increment]
            # Добавление информации о пикселе в массив с кончеными данными
            res.append(val[increment - 2])
            res.append(val[increment - 1])
            res.append(val[increment])
        with open('whodunit.bmp', 'wb') as w:
            # Запись в конечный файл заголовков и данных о цветах пикселей
            w.write(header)
            w.write(bytes(res))


def resize():
    with open('pset4/bmp/clue.bmp', 'rb') as input_file:
        # step = int(input('Количество раз во сколько вы хотите увеличить изображение: '))
        res = []
        header = bytearray(input_file.read(54))
        print(header)


if __name__ == '__main__':
    # print(sigma(2))
    # array = [1, 2, 3, 4, 5]
    # print(search(1, array, 0, len(array)-1))
    whodunit()
