"""
Определить, является ли число палиндромом
"""
print('Введите целое положительное число')
a = int(input())
b = a
c = 0
while b > 0:
    c = c * 10 + (b % 10)
    b = b // 10

if c == a:
    print('Палиндром')
else:
    print('Не палиндром')
