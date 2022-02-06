# Построить
# класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.). 

# Класс
# должен содержать:

# Данные:

# длина и ширина прямоугольника 

# Методы для операций с данными: 

# Нахождения периметра, площади, изменения размеров, печати результата.

# Написать
# программу, демонстрирующую работу с этим классом. Программа должна содержать
# меню, позволяющее осуществить проверку всех методов класса.


class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimetr(self):
        return f"Периметр прямоугольника: {(self.length + self.width) * 2}"

    def square(self):
        return f"Площадь прямоугольника: {self.length * self.width}"

def main():
    a, b = map(int, input("Введите длину и ширину через пробел: ").split())
    rectangle = Rectangle(a, b)
    while True:
        choose = int(input("1. Найти периметр прямоугольника.\n2. Найти площадь прямоугольника.\n3. Выход.\n  >>>"))
        if choose == 1:
            print(rectangle.perimetr())
        elif choose == 2:
            print(rectangle.square())
        elif choose == 3:
            break
        else:
            print("Ошибка")
            break

main()


