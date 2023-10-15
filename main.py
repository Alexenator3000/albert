a = int(input('Введите число 1 '))
c = input('Введите операцию ')
b = int(input('Введите число 2 '))
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '*':
    print(a * b)
if c == '/' and b == 0:
    print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ')
elif c == '/' and b != 0:
    print(a / b)