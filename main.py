a = input('Введите число 1 ')
if a.isnumeric() != True:
    print('nononononono')
    exit('error')
a = int(a)
c = input('Введите операцию ')
if c != '+' and c != '-' and c != '/' and c != '*':
    print('nononononono')
    exit('error')
b = input('Введите число 2 ')
if b.isnumeric() != True:
    print('nononononono')
    exit('error')
b = int(b)
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '*':
    print(a * b)
if c == '/' and b == 0:
    print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ')
    exit('error')
elif c == '/' and b != 0:
    print(a / b)