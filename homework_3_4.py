print('Программа принимает на вход целое число, '
      'а выводит список чисел Фибоначчи, '
      'в том числе для отрицательных индексов.')
while True:
    number = input('Введите целое число: ')
    if number.isdigit():
        number = int(number)
        break
    print('Неверно введено число!')


def fib(n, sum_=1, previous_sum=0):
    if n == 0:
        return previous_sum
    else:
        return fib(n-1, sum_+previous_sum, sum_)


print(
    [
        fib(i) if i >= 0
        else round((-1)**(i+1)*fib(-i))
        for i in range(-number, number+1)
    ]
)
