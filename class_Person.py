# a) поля fullName, age, place(address)
# б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод 

# move()  будет менять его адрес
# в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
# г) Настроить  метод __str__  (Сделать отображение всех полей объекта)



class Person:
    def __init__(self, fullName, place, age = 18):
        self.fullName = fullName
        self.age = age
        self.place = place #(address)
        
    def __str__(self):
        return f"{self.fullName}, {self.age}, {self.place}"
   
    def talk(self):
        return f"Такой-то  {self.fullName} говорит"
    
    def move(self, adres):
        self.place = adres
        
     
        
a = Person('bolot','bishkek', 22)
print(a)
print(a.talk())
a.move('osh')
print(a)

