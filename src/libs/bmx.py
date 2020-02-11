from src.libs.timing import *


@speed_test
def bmx(text, sub):
    '''
    Эффективность алгоритма БМХ обусловлена тем, что удается пропускать те части текста, которые заведомо не участвуют в успешном сопоставлении.
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

    d = {}
    for char_i in range(len_sub):
        if (char_i + 1 != len_sub):
            d[sub[char_i]] = len_sub - char_i - 1
        elif (sub[char_i] not in d and char_i + 1 == len_sub):
            d[sub[char_i]] = len_sub

    for char_i in range(len_sub - 1, len_text):
        if text[char_i] == sub[-1]:
            sum = 1
            char_tx = char_i - 1
            for j in range(len_sub - 1)[::-1]:
                if text[char_tx] == sub[j]:
                    sum += 1
                    char_tx -= 1
                else:
                    if text[char_tx] in d:
                        char_i += d[text[char_tx]]
                    else:
                        char_i += len_sub
                    break

            if sum == len_sub:
                return char_i - len_sub + 1
        else:
            if text[char_i] in d:
                char_i += d[text[char_i]]
            else:
                char_i += len_sub

    return -1