from src.libs.timing import *


@speed_test
def lib_find(text, sub):
    '''
    Библиотечная функция поиска подстроки.

    :param text: текст
    :param sub: подстрока
    :return: индекс
    '''
    if text == "" or sub == "":
        return -1

    if len(text) < len(sub):
        return -1

    return text.find(sub)
