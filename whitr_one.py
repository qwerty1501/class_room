password_list = ['password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '234567']

while True:
    a = input('Ведите пароль: ')
    if a in password_list:
        print('Добро пожаловать!')
        break
    else: 
        pass