class Laptop:

    r = 0

    def __init__(self, name, cpu, ram, graph_card, hdd, screensize):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.graph_card = graph_card
        self.hdd = hdd
        self.screensize = screensize

    def get_dict(self):
        dict1 = {
            'Название ноутбука':self.name,
            'Процессор':self.cpu,
            'Оперативная память':f'{self.ram} гб',
            'Видеокарта':self.graph_card,
            'Размер диска':self.hdd,
            'Диагональ экрана':self.screensize,
        }
        return dict1
    
    def output(self):
        some_dict = Laptop.get_dict(self).items()
        for k, v in some_dict:
            print(k , ':', v, self.r)


aser = Laptop('Acer Aspire 7', 'Intel Core i7', 16, 'nvidia geforce gtx 1650', 512, 15.6)
aser.r = 5
dell = Laptop('Dell Inspiron', 'i7 ', 32, '1660 Ti', 2000, 15.6)
aser.output()
dell.output()