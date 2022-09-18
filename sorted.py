# selection sort


def selection_sort():
    # Принимаем не отсортированный список чисел
    list_of_numbers = input('Введите список чисел который желаете отсортировать: ')
    list_of_numbers = list_of_numbers.split()  # Переносим в массив, разделяя через пробел
    length_list_of_numbers = len(list_of_numbers)
    for i in range(0, length_list_of_numbers):
        min_number = i  # Принимаем за минимальное значение первое число в неотсортированном списке
        for m in range(i+1, length_list_of_numbers):
            if int(list_of_numbers[min_number]) > int(list_of_numbers[m]):
                min_number = m  # Если какое-то из чисел меньше чем предыдущее минимальное - оно новое минимальное
        # Меняем местами первое и минимальное значение из неотсортированного списка
        list_of_numbers[i], list_of_numbers[min_number] = list_of_numbers[min_number], list_of_numbers[i]
    return list_of_numbers

# bubble sort


def bubble_sort():
    # Принимаем неотсортированный список чисел
    list_of_numbers = input('Введите список который желаете отсортировать: ')
    list_of_numbers = list_of_numbers.split()  # Переносим в массив, разделяя через пробел
    length_list_of_numbers = len(list_of_numbers)
    flag_swapped = True  # Флаг, обозначающий были ли перестановки в списке, или нет
    while flag_swapped:
        flag_swapped = False
        for i in range(length_list_of_numbers - 1):
            # Замена неправильно стоящих данных между собой
            if int(list_of_numbers[i]) > int(list_of_numbers[i+1]):
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
                flag_swapped = True
    return list_of_numbers

# insertion sort


def insertion_sort():
    # Принимаем неотсортированный список чисел
    list_of_numbers = input('Введите список который желаете отсортировать: ')
    list_of_numbers = list_of_numbers.split()  # Переносим в массив, разделяя через пробел
    length_list_of_numbers = len(list_of_numbers)
    for i in range(0, length_list_of_numbers):
        element = list_of_numbers[i]  # Первый элемент неотсортированного списка
        j = i  # Индикатор элемента, который будет сдвигаться
        # Пока индикатор сдвига больше нуля, и предыдущий элемент больше первого: переносим все большие элементы на одну
        # позицию вправо
        while j > 0 and int(list_of_numbers[j - 1]) > int(element):
            list_of_numbers[j] = list_of_numbers[j - 1]
            j -= 1
        list_of_numbers[j] = element  # Ставим наш элемент на его место в отсортированном списке
    return list_of_numbers

# heap sort


# def heapify(nums, heap_size, root_index):
#     # Индекс наибольшего элемента считаем за корневой индекс
#     largest = root_index
#     left_child = (root_index * 2) + 1
#     right_child = (root_index * 2) + 2
#
#     # Если новый потомок имеет допустимый индекс, а элемент больше чем наибольший, меняем их местами
#     if left_child < heap_size and nums[left_child] > nums[largest]:
#         largest = left_child
#
#     # То же самое и для правого потомка
#     elif right_child < heap_size and nums[right_child] > nums[largest]:
#         largest = right_child
#
#     # Если наибольший больше чем корневой, то они меняются
#     if largest != root_index:
#         nums[root_index], nums[largest] = nums[largest], nums[root_index]
#         # Проход ещё раз для проверки
#         heapify(nums, heap_size, largest)


# def heap_sort(nums):
#     n = len(nums)
#
#     # Создаем Max Heap из списка
#     # Второй аргумент означает остановку перед -1, т.е. на первом элементе списка
#     # Третий аргумент означает обратный проход по списку, уменьшая i на 1
#     for i in range(n, -1, -1):
#         heapify(nums, n, i)
#
#     # Перемещаем корень Max Heep в конец списка
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)
#     return nums

# Merge sort

def merge(array, left_index, right_index, middle):
    # Создаём копии массивов, которые хотим отсортировать

    # Второй параметр не включается, поэтому мы должны добавить 1
    left_copy = array[left_index:middle+1]
    right_copy = array[middle+1:right_index+1]

    # Инициализируем переменные, которые мы будем использовать для слежки в каком мы месте в каждом массиве
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Идём вдоль каждой из копий, пока одна из них не закончится
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        # Проверяем, если в левом массиве элемент меньше, то ставим его в начало нашего отсортированного массива и
        # добавляем один к индексу левого массива
        if left_copy[left_copy_index] < right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        # Если иначе
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        # Идём вперёд по отсортированному списку
        sorted_index += 1

        # Мы пробежались по right_copy и left_copy и если что-то осталось в каком-то из массивов, то просто добавляем
        # его в конец отсортированного списка

        while left_copy_index < len(left_copy):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
            sorted_index += 1

        while right_copy_index < len(right_copy):
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
            sorted_index += 1


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


# Binary Search

def binary_search_recursive(array, element, start, end):
    # Выход из рекурсивной функции, если элемент не был найден
    if start > end:
        return -1

    middle = (start + end) // 2
    if array[middle] == element:
        return middle
    elif array[middle] > element:
        return binary_search_recursive(array, element, start, middle - 1)
    else:
        return binary_search_recursive(array, element, middle + 1, end)


if __name__ == '__main__':
    # print(selection_sort())
    print(bubble_sort())
    # print(insertion_sort())
    # random_list = [35, 12, 43, 8, 51]
    # print(heap_sort(random_list))
    # merge_sort(random_list, 0, len(random_list) - 1)
    # print(random_list)
    # array1 = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
    # print(binary_search_recursive(array1, 16, 0, len(array1) - 1))
