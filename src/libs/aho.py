from src.libs.timing import *


class AhoNode:
    '''
    Класс для составления дерева ключевых слов(бора).

    '''
    def __init__(self):
        '''
        Стандартный конструктор.
        '''
        self.goto = {}
        self.out = []
        self.fail = None

# @speed_test
def aho_create_forest(patterns):
    '''
    Создать бор - дерево паттернов.

    :param patterns: подстрока, паттерн
    :return: корень дерева
    '''
    root = AhoNode()

    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root

# @speed_test
def aho_create_statemachine(patterns):
    '''
    Создает бор и инициализирует fail-функции всех узлов, обходя дерево в ширину.
    Бор - это эффективный способ хранить словарь и искать в нем слова.

    :param patterns: подстрока, паттерн
    :return: корень дерева
    '''
    # Создаем бор, инициализируем
    # непосредственных потомков корневого узла
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    # Инициализируем остальные узлы:
    # 1. Берем очередной узел (важно, что проход в ширину)
    # 2. Находим самую длинную суффиксную ссылку для этой вершины - это и будет fail-функция
    # 3. Если таковой не нашлось - устанавливаем fail-функцию в корневой узел
    while len(queue) > 0:
        rnode = queue.pop(0)

        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out

    return root

@speed_test
def aho_find_all(text, sub):
    '''
    Находит все возможные подстроки из набора паттернов в строке.

    Сложность:
    * |Σ|=σ - размер алфавита
    * |text|=t — длина текста
    * |pattern|=p — длина паттерна
    * a — размер ответа(кол-во пар)
    * m — суммарная длина всех паттернов

    Худшее: O(m * σ + t + a)
    Среднее: O(m * σ + t + a)
    Препроцессинг: O(m)
    Дополнительная память: O(mσ)

    :param text: текст
    :param sub: подстрока
    :return: индекс
    '''
    if text == "" or sub == "":
        return []

    if len(text) < len(sub):
        return []

    root = aho_create_statemachine([sub])
    node = root
    pos = []

    for i in range(len(text)):
        while node is not None and text[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[text[i]]

        for pattern in node.out:
            pos.append(i - len(pattern) + 1)
    return pos