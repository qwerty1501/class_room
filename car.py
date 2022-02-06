name1 = 'toyota'
name2 = 'lexus'
passway = 150000
passway1 = 200000
color = 'grey'
color1 = 'white'
wheel = 'left'
owners = 2
price = 10000
price1 = 8000
if name1 == 'toyota' or name2 == 'lexus':
    if passway <= 150000:
        if color == 'grey' or color1 == 'white':
            if wheel == 'left':
                if owners <= 2:
                    if price <= 10000:
                        print("Есть машина за 10к бачей с пробегом меньше 150к")
    elif passway1 <= 200000:
        if color == 'grey' or color1 == 'white':
            if wheel == 'left':
                if owners <= 2:
                    if price1 <= 10000:
                        print("Есть машина за 8к бачей с пробегом меньше 150к")
else:
    print("Такой машины нет в наличии")