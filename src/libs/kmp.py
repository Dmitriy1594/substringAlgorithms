from src.libs.timing import *


@speed_test
def kmp(text, sub):
    '''
    Метод КМП использует предобработку искомой строки, а именно: на ее основе создается префикс-функция.
    * |Σ|=σ - размер алфавита
    * |text|=t — длина текста
    * |pattern|=p — длина паттерна

    Худшее: O(p + t)
    Среднее: O(p + t)
    Препроцессинг: O(p)
    Дополнительная память: O(p) - создается массив длины p

    :param text: текст
    :param sub: подстрока
    :return: индекс
    '''
    if text == "" or sub == "":
        return -1

    len_text = len(text)
    len_sub = len(sub)

    if len_text < len_sub:
        return -1

    help_list = [0] * len_sub
    help_list[0] = 0
    char_j = 0

    # O(n)
    char_i = 1
    while char_i < len_sub:
        if (sub[char_i] == sub[char_j]):
            help_list[char_i] = char_j + 1
            char_i += 1
            char_j += 1
        elif (char_j == 0):
            help_list[char_i] = 0
            char_i += 1
        else:
            char_j = help_list[char_j - 1]

    # O(m)
    char_l = 0
    char_k = 0
    while char_k < len_text:
        if text[char_k] == sub[char_l]:
            char_k += 1
            char_l += 1
            if char_l == len_sub:
                return char_k - len_sub
        else:
            if (char_l == 0):
                char_k += 1
                if char_k == len_text:
                    return -1
            else:
                char_l = help_list[char_l - 1]

    return -1
