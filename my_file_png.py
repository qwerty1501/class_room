i = input("Введите имя файла: ")
check = i.count('.')
if check == 0 or check >1:
    print("Расширение не найдено.")
else:
    spl = i.split('.')
    type = spl[1]
    print("Расширение файла - ", type)