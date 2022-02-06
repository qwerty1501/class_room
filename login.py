# Login - IU
# Password - IU123
def autorize():
    login = (input("Введите логин: "))
    password = (input("Введите пароль: "))
    LIU = 'IU'
    PIU = 'IU123'
    if login == LIU and password == PIU:
        print(f"Вход выполнен")
    else:
        print("Неверное имя пользователя или пароль:")
        return autorize()
autorize()