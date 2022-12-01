print('Программа принимает на вход десятичное число, '
      'а выводит его двоичное представление.')
while True:
    number = input('Введите десятичное число: ')
    if number.isdigit():
        number = int(number)
        break
    print('Неверно введено число!')

string = ''
while number > 0:
    string += str(number % 2)
    number = number // 2
print(''.join(reversed(string)))
