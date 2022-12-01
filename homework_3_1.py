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

length = (
    len(numbers) // 2 if not len(numbers) % 2
    else (len(numbers) // 2) + 1
)
new_lst = []
for i in range(length):
    new_lst.append(int(numbers[i]) * int(numbers[len(numbers)-1-i]))
print(new_lst)
