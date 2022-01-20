# Проверить
# корректность работы генератора псевдослучайных чисел языка
# программирования с помощью оценки вероятности выпадения четных чисел на
# выборке не меньше 1000 случайных чисел.

# Вывести процент четных чисел.

from random import randint
i = 0

for _ in range(1000):
    random_num = randint(1, 1000)
    if random_num % 2 == 0:
        i += 1

print(f'Чётные = {i / 10}%')



