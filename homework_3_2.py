# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
from random import randrange, uniform

lst = [round(uniform(1, 10), 2) for _ in range(randrange(2, 10))]
print(lst)


def find_diff(list_):
    list_ = [round(i % 1, 2) for i in lst]
    min_item = list_[0]
    max_item = list_[0]
    for i in range(len(list_)):
        if max_item < list_[i]:
            max_item = list_[i]
        elif min_item > list_[i]:
            min_item = list_[i]

    return f'{max_item} - {min_item} = {round(max_item - min_item, 2)}'


print('Разница между max и min значением дробной части элементов:', find_diff(lst))
