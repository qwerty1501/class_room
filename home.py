raion = input("Введите район: ")
cost = int(input("Введите стоимость: "))
material = input("Введите материал: ")
size = int(input("Введите размер участка: "))
if raion == 'чон арык' or raion == 'байтик' or raion == 'ортосай':
    if material == 'кирпич' and cost <= 50000 and size <= 4:
        print("Есть такой дом")
    elif material == 'пескоблок' and cost <= 45000 and size <= 5:
        print("Есть такой дом")
else:
    print("Нет такого дома")