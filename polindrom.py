words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил', 'language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку']
for i in words:
    i_l = i.lower()
    if i_l == i_l[::-1]:
        print(f"Слово '{i}' является палиндромом.")
    else:
        print(f"Слово '{i}'' НЕ палиндром.")