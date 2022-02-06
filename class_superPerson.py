class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}")

class Student(Person):
    def __init__(self, name, age, major):
        Person.__init__(self, name, age)
        self.major = major

    def displayStudent(self):
        print(f"Имя студента: {self.name}\nВозраст студента: {self.age}\nСпециальность: {self.major}")


P = Person("Tomas Shelbi", 37)
P.display()
print('-------------------------------')
S = Student("Albert", 23, "Mathematics")
S.displayStudent()