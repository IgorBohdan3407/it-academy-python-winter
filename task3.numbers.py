# Даны два списка чисел.
# Посчитайте, сколько различных
# чисел содержится одновременно
# как в первом списке, так и во втором.
a = set(input().split())
b = set(input().split())
c = len((a & b))
print(c)
