# Запуск программы
```
python ./app.py -t ./texts/Beginners-Luck.txt -s ./texts/Beginners-Luck_sub.txt
python ./app.py -t ./texts/example.txt -s ./texts/example_sub.txt
```

## Формат входных данных
Текст и подстрока, которая ищется в нем сохраняются в 2 файлах .txt, а при запуске указываются после вызова ./app.py следующим образом:
* Для текста -t ./your_path_to_text/example.txt.
* Для подстроки -s ./your_path_to_substring/example_sub.txt.
* -i true/false - флаг, который спрашивает нужно ли сохранять изображения со статистикой после выполнения.

## Формат выходных данных
Создается отдельная папка result, которая состоит из:
* result.txt
    
    **Пример того, что написано в файле:**
    ```
    modDirectSearch: 30, 5.245208740234375e-06
    
    kmp: 30, 6.9141387939453125e-06
    
    bmx: 30, 1.0013580322265625e-05
    
    rabin_karp: 30, 3.719329833984375e-05
    
    aho_find_all: [30], 2.6702880859375e-05
    
    lib_find: 30, 9.5367431640625e-07
    
    ```



