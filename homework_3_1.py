print('программа находит произведение пар чисел списка. '
      'Парой считаем первый и последний элемент, второй и предпоследний и т.д.')

while True:
    numbers = input('Введите целые числа через пробел: ').split()
    for number in numbers:
        if not number.isdigit():
            print('Неверно введены числа!')
            break
        continue
    else:
        break

lst = [int(i) for i in numbers]
length = len(lst) // 2 if not len(lst) % 2 else (len(lst) // 2) + 1
new_lst = []
for i in range(length):
    new_lst.append(lst[i] * lst[len(lst)-1-i])
print(new_lst)
