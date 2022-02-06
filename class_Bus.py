# Создайте класс Bus, унаследованный от класса Vehicle. Задайте аргументу 
# capacity

# Bus.seating_capacity() значение по умолчанию 50

# Используйте следующий код для родительского класса Vehicle.
# Вам нужно использовать переопределение метода. 



class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):
    def seating_capacity(capacity = 50):
        return f"The seating capacity is {capacity} passengers"


print(Bus.seating_capacity(50))