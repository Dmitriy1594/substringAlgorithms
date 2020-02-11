# Тесты

Данные, которые генерируются перед началом тестирования.
```python
def _get_data(self, mod=None):
    text = ""
    sub = ""
    methods = [modDirectSearch, kmp, bmx, rabin_karp, aho_find_all]
    if mod == 1:
        fake = Faker()
        text = fake.text()
        sub = choice(text.split(' ')).split('\n')[0].split('.')[0]
    elif mod == 2:
        c = 3
        text = "".join(choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(c))
        sub = "".join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(c))
        while lib_find(text, sub) != -1:
            sub = "".join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(c))
    elif mod == 3:
        return (text, sub, methods)

    return (text, sub, methods)
```

## Тест test_base
```python
def test_base(self):
    text, sub, methods = self._get_data(mod=1)
    for method in methods:
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(text[tk:tk + len(sub)], sub)
```
Базовый тест для проверки функций на правильный результат.

## Тест test_out
```python
def test_out(self):
    text, sub, methods = self._get_data(mod=2)

    for method in methods:
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)
```
Тест, который проверяет устойчивость алгоритмов к рандомным данным.

## Тест test_stress
```python
def test_stress(self):
    ans = []
    for i in range(100):
        text, sub, methods = self._get_data(mod=1)

        for method in methods:
            tk = method(text, sub)
            if type(tk) == list:
                if len(tk) != 0:
                    tk = tk[0]
                else:
                    tk = -1
            ans.append(text[tk:tk + len(sub)] == sub)

    self.assertTrue(all(ans))
```
Стресс тест, который проверяет на правильный результат. При большом количестве итераций проверяются разные варианты устойчивости данного алгоритма. Для сбора стастистики был объявлен массив ans, в который записваются булевое значение. В этом массиве ожидается наличие только True.

## Тест test_null
```python
def test_bad_data(self):
    text, sub, methods = self._get_data(mod=3)
    for method in methods:
        tk1 = method("", "s")
        tk2 = method("asd", "")
        tk3 = method("", "")
        tk4 = method("s", "ss")
        if type(tk1) == list or type(tk2) == list or type(tk3) == list or type(tk4) == list:
            if len(tk1) != 0 or len(tk2) != 0 or len(tk3) != 0 or len(tk4) != 0:
                tk1 = tk1[0]
                tk2 = tk2[0]
                tk3 = tk3[0]
                tk4 = tk4[0]
            else:
                tk1 = -1
                tk2 = -1
                tk3 = -1
                tk4 = -1

        self.assertEqual(tk1, -1)
        self.assertEqual(tk2, -1)
        self.assertEqual(tk3, -1)
        self.assertEqual(tk4, -1)
```
Тест проверяет результат функций на ввод некорректных данных.

## Тесты, учитывающие конкретные реализации алгоритмов поиска подстроки в строке.
### Тест для алгоритма rabin_karp
```python
def test_collision(self):
    c = 3
    t = randint(c, 7)
    s = c
    
    # генерирование данных 
    text = "".join(
        choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in
        range(t))
    sub = "".join(
        choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in
        range(s))
    while lib_find(text, sub) == -1 and text == sub:
        sub = "".join(
            choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in
            range(s))

    len_text = len(text)
    len_sub = len(sub)
    
    # вычисление хеша
    htext = Hash(text, len_sub)
    hsub = Hash(sub, len_sub)
    hsub.update()

    # входим в цикл, если хеши не совпали и генерируем данные, до тех пор, пока не совпадут
    while hsub.digest() != htext.digest():
        text = "".join(
            choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in
            range(t))
        sub = "".join(
            choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in
            range(s))
        while lib_find(text, sub) == -1 and text == sub:
            sub = "".join(
                choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i
                in range(s))

        len_text = len(text)
        len_sub = len(sub)

        htext = Hash(text, len_sub)
        hsub = Hash(sub, len_sub)
        hsub.update()

    # проверка на то, что происходит коллизия и она обрабатывается алгоритмом
    self.assertTrue(hsub.digest() == htext.digest())
    self.assertEqual(rabin_karp(text, sub), -1)
```
Данный тест проверяет корректность работы алгоритма, если результат хеширвания текста и строки совпадут при этом текст и строка отличные друг от друга.

### Тест для алгоритмов modDirectSearch, kmp и bmx
```python
def test_mods(self):
    text, sub, methods = self._get_data(mod=3)
    for method in methods[:3]:
        # 1 Проверка в конце строки
        text = 'aaa'
        sub = 'aab'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 2 Инвертированая строка
        text = 'baa'
        sub = 'aab'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 3 Последние 2 символа
        text = 'bab'
        sub = 'ab'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, 1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 4 Проверка на полидром
        text = 'baab'
        sub = 'ab'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, 2)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 5 Проверка на правильное изменение итератора
        text = 'baac' * 2
        sub = 'aabac'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 6 Множественное повторение
        text = 'aabcaabcaabaabcaabac'
        sub = 'abcaa'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, 1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)

        # 7 Проверка stuff
        text = 'aabcaa'
        sub = 'abcaa'
        tk = method(text, sub)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, 1)
        tk = method(sub, text)
        if type(tk) == list:
            if len(tk) != 0:
                tk = tk[0]
            else:
                tk = -1
        self.assertEqual(tk, -1)
```
Данный тест для 3 алгоритмов включает тестирование, учитывающие конкретные реализации алгоритмов поиска подстроки в строке. Благодаря 1, 2, 3 и 4 тестам были выявлены ошибки во всех 3 алгоритмах и особенности генератора чисел range() в Python и был заменен на while в коде modDirectSearch и kmp.
#### Особенность:
range() возвращает объект, по которому можно итерироваться, но нельзя в цикле поменять значение (прибавить, умножить или удалить), даже если мы поменяем значение итератора, то на следующем шаге оно будет таким как в возвращаемом объекте. Все изменения итератора в цикле игнорируются.

### Тест для алгоритма aho_find_all
```python
def test_aho(self):
    # 1
    text = 'Gollum did not like Frodo. But Gandalf did.'
    sub = 'Frodo'
    tk = aho_find_all(text, sub)[0]
    self.assertEqual(tk, 20)

    # 2
    text = 'Gollum did not like Frodo. But Gandalf did.'
    sub = 'Gandalf'
    tk = aho_find_all(text, sub)[0]
    self.assertEqual(tk, 31)

    # 3
    sub = 'Dawn Higgins'
    text = ''
    with open('textblob.txt') as keyword_file:
        text = keyword_file.read()
    tk = aho_find_all(text, sub)[0]
    self.assertEqual(tk, 34153)
```
Данный тест проверяет устойчивость алгоритма.
