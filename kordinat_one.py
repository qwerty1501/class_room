x = int(input("Введите координаты по x: "))
y = int(input("Введите координаты по y: "))
if x > 0 and y > 0:
    print("Точка находится в 1 четверти")
elif x > 0 and y < 0:
    print("Точка находится в 4 четверти")
elif x < 0 and y < 0:
    print("Точка находится в 3 четверти")
elif x < 0 and y > 0:
    print("Точка находится в 2 четверти")
else:
    print("Ошибка")