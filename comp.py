ram = int(input("Введите объем оперативной памяти: "))
ssd = int(input("Введите объем ССД диска: "))
hdd = int(input("Введите объем жесткого диска: "))
cost = int(input("Введите стоимость: "))
if ram >= 4 and ram <=8:
    if ssd >= 256 and hdd >= 1000 and cost <= 1000:
        print("Есть такой ноутбук")
else:
    print("Нету такого ноутбука")