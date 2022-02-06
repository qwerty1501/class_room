# Ввести логин и пароль и сравнить. Вывести результат авторизации: True или False

login = input('Ведите логин: ')
password = input('Ведите пароль: ')

login_a = 'qwerty'
password_a = 'qwerty'

if login == login_a and password ==password_a:
    print(True)
    
else:
    print(False)