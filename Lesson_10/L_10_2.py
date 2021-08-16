class Car:
    def __init__(self, model, speed, ):
        self.model = model
        self.speed = speed
        self.odometr = 0

    def move(self):
        return f'Машина {self.model} едет со скоростью {self.speed}'

    def read_odometr(self):
        return self.odometr

    def update_odometr(self, km):
        self.odometr += km


class ElectricCar(Car):
    def __init__(self, model, speed, zapas):
        super().__init__(model, speed)
        self.zapas = zapas

    def check(self):
        temp = self.read_odometr() % self.zapas
        return temp


if __name__ == "__main__":
    bmw = Car('BMW', 90)
    for i in range(10):
        bmw.update_odometr(i)

    print(getattr(bmw, 'odometr'))
    print(hasattr(bmw, 'odometr'))
    setattr(bmw, 'speed', 123)
    print(bmw.speed)
    # delattr(bmw, 'speed')
    print(bmw.read_odometr())
    x = 7
    print(bmw.__dict__)
    for attr in bmw.__dict__:
        print(attr, bmw.__dict__[attr])
