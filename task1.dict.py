# Dict comprehensions
# Создайте словарь с помощью генератора
# словарей, так чтобы его ключами были
# числа от 1 до 20, а значениями кубы этих чисел.
z = ((x, x ** 3) for x in range(21))
print(dict(z))
