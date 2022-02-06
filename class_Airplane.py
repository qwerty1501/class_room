class Airplane():
    def __init__(self, make, model, year, max_speed, odometer, is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying
        
    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self, range):
        self.odometer += range

    def info(self):
        print(self.is_flying, self.odometer)
        
m = Airplane('Mitsubishi', 'A6M просто «Зеро»', 1940, 500, 0)
m.info()
m.take_off()
m.info()
m.fly(1000)
m.info()
m.land()
m.info()