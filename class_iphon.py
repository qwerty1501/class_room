# а) Создайте класс Phone, который содержит атрибуты number, model и weight.
# б) Создайте три экземпляра этого класса. 
# в) Выведите на консоль значения их атрибутов. 
# г) Добавить конструктор в класс Phone, который принимает на вход три параметра для инициализации переменных класса - number, model и weight. 
# д) Создать метод sendMessage. Данный метод принимает

class Iphone:

    def __init__(self, model, number, weight):
        self.model = model
        self.number = number
        self.weight = weight
        print("Мой телефон !!!")
    
    def phone(self):
        return self.model, self.number, self.weight


my_phone = Iphone('iphon 12', '+996554764499', '112g')
print(my_phone.phone())

iphon_13 = Iphone('iphon 13', '+996504764499', '113g')
print(iphon_13.phone())

nokia6700 = Iphone('nokia_6700', '+0996222764499', '90g')
print(nokia6700.phone())
