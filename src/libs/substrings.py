import csv
from faker import Faker
from random import choice

from src.libs.timing import *
from src.libs.modDirectSearch import *
from src.libs.kmp import *
from src.libs.bmx import *
from src.libs.rabin_karp import *
from src.libs.aho import *
from src.libs.lib_find import *


def get_csv_table(filename, n=1000, faker=True):
    '''
    Записывает необходимые значения в таблицу для последующего анализа в Jupiter Notebook.

    :param filename: название файла
    :param n: количество записей в csvfile
    :param faker: включение генератора псевдореальных данных
    :return: None
    '''
    headers = "modDirectSearch,kmp,bmx,rabin_karp,aho_find_all,lib_find,textLen,subLen,index"
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers.split(','))
        writer.writeheader()

        for i in range(n):
            text = ""
            sub = ""

            if faker is True:
                fake = Faker()
                text = fake.text()
                sub = choice(text.split(' ')).split('\n')[0].split('.')[0]
            else:
                text = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(11))
                sub = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(3))
                while lib_find(text, sub) == -1:
                    sub = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(3))

            tk = modDirectSearch(text, sub)
            tk = kmp(text, sub)
            tk = bmx(text, sub)
            tk = rabin_karp(text, sub)
            tk = aho_find_all(text, sub)
            tk = lib_find(text, sub)

            global timedict
            timedict["textLen"] = len(text)
            timedict["subLen"] = len(sub)
            timedict['index'] = tk
            # print(timedict)
            writer.writerow(timedict)
    return

def simple_test():
    text = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(11))
    sub = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(3))
    while lib_find(text, sub) == -1:
        sub = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(3))

    # text = 'aaa'
    # sub = 'aab'

    print(text)
    print(sub)

    tk = modDirectSearch(text, sub)
    print("modDirectSearch: " + text[tk:tk + len(sub)])

    tk = kmp(text, sub)
    print("kmp: " + text[tk:tk + len(sub)])

    tk = bmx(text, sub)
    print("bmx: " + text[tk:tk + len(sub)])

    tk = rabin_karp(text, sub)
    print("rabin_karp: " + text[tk:tk + len(sub)])

    tk = aho_find_all(text, sub)
    for i in tk:
        print("Aho: " + text[i:i + len(sub)])


if __name__ == '__main__':
    # простой тест работоспособности алгоритмов
    simple_test()

    # функция для генерирования данных
    # get_csv_table('substr.csv', n=1000, faker=False)
