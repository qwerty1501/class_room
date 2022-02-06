class Car:
    def __init__(self, make, model, year, max_speed, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.fuel = fuel

    def __add_distance(self, range):
        self.odometer += range
        print(self.odometer)

    def __subtract_fuel(self, range):
        self.fuel -= range/10

    def drive(self, range):
        if self.fuel >= range/10:
            self.__add_distance(range)
            self.__subtract_fuel(range)
            print("Let's drive!")
        elif self.fuel < range/10:
            print("Need more fuel, please, fill more!")

a = Car('Mercedes_AMG', 'GT-63amg', 2021, 400)
a.drive(600)
a.drive(100)
a.drive(1)