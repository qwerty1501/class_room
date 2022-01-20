class Mcompany():
    cpu = None
    ram = None
    video_card = None
    hdd = 0
    motherboard = None
    screen_size = 0

    def __init__(self, name):
        self.name = name


com = Mcompany('macbook')
com.cpu = 'intel core i7'
com.ram = '32 гб'
com.video_card = 'gtx 1950'
com.hdd = 512
com.motherboard = 'asus rog gt 350i'
com.screen_size = 15.3

print(com)





# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана