from src.libs.timing import *


# @speed_test
class Hash:
    '''
    hash class to simplify code function rabin_karp.

    '''
    def __init__(self, string, size):
        self.str  = string
        self.hash = 0

        for i in range(0, size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end  = size

    def update(self):
        if (self.end <= len(self.str) - 1):
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end  += 1

    def digest(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]

@speed_test
def rabin_karp(text, sub):
    '''
    Алгоритм:
    1. Вычисляем хеш-функции от каждой строки S
    2. Перебираем в цикле все подстроки T длины L
    3. Для каждой такой подстроки вычиляем хеш-функцию
    4. Сравниваем значение хеш-функции с значением хеш-функций всех строк S
    5. Только если есть совпадение хеш-функций, то тогда сравниваем эту подстроку T с той строкой S, для которой было совпадение

    Сложность:
    * |Σ|=σ - размер алфавита
    * |text|=t — длина текста
    * |pattern|=p — длина паттерна

    Худшее: O(p * t)
    Среднее: O(p + t)
    Препроцессинг: O(p)
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

    htext = Hash(text, len_sub)
    hsub = Hash(sub, len_sub)
    hsub.update()

    for i in range(len_text - len_sub + 1):
        if htext.digest() == hsub.digest():
            if htext.text() == sub:
                return i
        htext.update()

    return -1