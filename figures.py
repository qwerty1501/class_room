while True:
    try:        
        a = int(input('Напишите любую сумму: '))
        b = int(input('Напишите любую сумму: '))
        c = (input('Выберите операцию: 0 . + . - . * . /  '))

        if c == '+':
            print(a + b)

        if c == '-':
            print(a - b)

        if c == '*':
            print(a * b)

        if c == '/':
            print(a / b)

    except  ZeroDivisionError:
        print("На ноль делить нельзя!")

        if c == '0':
            break
