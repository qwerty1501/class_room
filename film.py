genre = input("Введите жанр: ")
if genre == 'ужасы' or genre == 'детектив' or genre == 'комедии':
    while True:
        time = int(input("Введите время: "))
        if time >= 21 and time <= 24:
            cost = 500
            print(f"Стоимость билета составляет: {cost} сом.")
            break
        elif time >= 0 and time < 21:
            cost = 300
            print(f"Стоимость билета составляет: {cost} сом.")
            break
        else:
            print(f"Время введено неверно.")
else:
    print("Такого жанра нет.")