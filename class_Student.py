class Student:
    def __init__(self, name, lastname, departament, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.departament = departament
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f"{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.departament}")

a = Student('Вася', 'Иванов', 'Программирование', 2017)
a.get_student_info()