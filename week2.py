def get_first_upper_case():
    out_name = ''  # Переменная для обозначения вывода
    start_name = input(
        "Введи своё имя пожалуйста: ")  # Переменная обозначающая имя над которым будут проводиться операции
    # Разделение полученной строки при помощи пробела, и дальнейший вывод первой буквы в каждом слове в верхнем регистре
    name = start_name.split()
    for name in name:
        out_name += name[0].upper()
    return out_name


# print(get_first_upper_case())


def caesar():
    k = ''  # Переменная использующаяся как шаг для шифрования
    x = ''  # Строка, которая будет принимать уже зашифрованные буквы
    while type(k) == str or int(k) < 0:
        k = input('Введите шаг шифрования - ')
        try:
            k = int(k)
        except ValueError:
            continue
    # Если шаг шифрования, больше чем букв в английском алфавите - отнимаем кол-во букв в алфавите, пока шаг не станет
    # меньше кол-ва букв в алфавите
    while k > 26:
        k -= 26
    string = input("Введите строку, которую хотите зашифровать: ")  # Получаем строку, которую требуется зашифровать
    for i in string:
        if i.isalpha():
            old = ord(i)  # Получение номера в таблице ASCII
            new = (old + k)  # Добавляем шаг
            i = chr(new)  # Переводим из ASCII в букву
        x += i
    return x


def vigenere():
    old_string = input('Введите фразу которую хотите зашифровать: ')  # Строка которую мы хотим зашифровать
    encryption_phrase = ' '  # Слово при помощи которого будет происходить шифрование
    flag_word = False  # Флаг помогающий в определении слово это или нет
    new_string = ''  # Зашифрованная фраз
    n = int(0)  # Номер символа в слове при помощи которого шифруется строка
    # Введение слова при помощи которого будет шифроваться строка, и проверка его на отсутствие пробелов
    # и других символов кроме букв
    while True:
        for i in encryption_phrase:
            if i == ' ' or i.isalpha() is not True:
                flag_word = True
        if flag_word:
            encryption_phrase = input('Введите слово, при помощи которого хотите зашифровать фразу: ')
            flag_word = False
        else:
            break
    length_of_encryption_phrase = len(encryption_phrase)  # Длина кодирующего слова
    for letter_string in old_string:
        if n == length_of_encryption_phrase:  # Если количество проходов достигло кодирующего слова - слово начинается
            n = 0                             # заново
        if letter_string.isalpha():
            old_letter_ascii = ord(letter_string)  # Номер буквы из кодирующейся строки в таблицы ASCII
            phrase_letter_ascii = ord(encryption_phrase[n])  # Номер буквы из кодирующего слова в таблице ASCII
            if letter_string.isupper():
                new_letter_ascii = 65 + ((old_letter_ascii - 65 + phrase_letter_ascii - 97) % 26)
            else:
                new_letter_ascii = 97 + ((old_letter_ascii - 97 + phrase_letter_ascii - 97) % 26)
            letter_string = chr(new_letter_ascii)  # Преобразования номера в букву
            n += 1  # Проход + 1
        new_string += letter_string # Добавление зашифрованной буквы в зашифрованную строку
    return new_string


if __name__ == '__main__':
    # print(get_first_upper_case())
    # print(caesar())
    print(vigenere())
