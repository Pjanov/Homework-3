# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
sum_elements = 0

print(my_list, '-> на нечётных позициях элементы', end=' ')

for index in range(len(my_list)):
    if index % 2 == 1:
        print(my_list[index], end='  ')
        sum_elements += my_list[index]
print('ответ:', sum_elements)
