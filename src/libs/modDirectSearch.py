from src.libs.timing import *


@speed_test
def modDirectSearch(text, sub) -> int:
    '''
    Усовершенствованный алгоритм КМП и БМХ.
    Сложность:
    * |Σ|=σ - размер алфавита
    * |text|=t — длина текста
    * |pattern|=p — длина паттерна

    Худшее: O(p + t)
    Среднее: O(p + t)
    Препроцессинг: нет
    Дополнительная память: O(1)

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

    char_i = 0
    while char_i < len_text:
        if text[char_i] == sub[0]:
            sum_chars_substr = 1    # сумма совпадающих букв подстроки с подтекстом.

            next_char_i = char_i

            if next_char_i + 1 >= len_text:
                break
            else:
                next_char_i += 1

            for j in range(1, len_sub):
                if text[next_char_i] == sub[j]:
                    sum_chars_substr += 1
                else:
                    break

                if next_char_i + 1 >= len_text:
                    break
                else:
                    next_char_i += 1

            if sum_chars_substr == len_sub:
                return char_i
            else:
                char_i = next_char_i
                # char_i += sum_chars_substr
        else:
            char_i += 1
    return -1
