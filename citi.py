city = 'none'
s = 0
while s == 0:
    i = int(input('''
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            Выберете действие: '''))
    if i == 1:
        new = str(input("Введите название города: "))
        if new == city:
            print("Такой город уже есть - ", new)
        elif new != city:
            city = new
            print("Город добавлен!")
        else:
            print("Ошибка 1")
    elif i == 2:
        print(city)
    elif i == 3:
        if city == 'none':
            print("Текущий город отсутствует.")
        else:
            print("Текущий город:", city)
        change = input("Текущий город: ")
        if change == city:
            print("Такой город уже есть!", change)
        else:
            city = change
            print("Город заменен")
    elif i == 4:
        delete = input("Введите название города: ")
        if city == 'none':
            print("Текущий город отсутствует.")
        elif city == delete:
            print("Город удален")
            city = 'none'
        else:
            print("Ошибка.")
    elif i == 5:
        s = 1
    else:
        print("Ошибка.")
