# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Примечание:
# Алгоритм смотрим тут: https://ru.wikipedia.org/wiki/Негафибоначчи
# Вам понадобится рекурсивный вызов функции или сделайте в виде списка.

def get_fibonacci(n):
    fibonacci_list = []
    a, b = 1, 1
    for i in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fibonacci_list.insert(0, a)
        a, b = b, a - b
    return fibonacci_list


k = 8
fibonacci_list = get_fibonacci(k)
print(f'для k = {k} список будет выглядеть так: {fibonacci_list}')
