class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.speed} км/ч')
        else:
            print(f'{self.speed} км/ч - Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'{self.speed} км/ч')
        else:
            print(f'{self.speed} км/ч - Превышение скорости!')


class PoliceCar(Car):
    pass


a = WorkCar(55, 'White', 'Volvo', False)
a.show_speed()
a.go()
a.turn('направо')
a.stop()

b = TownCar(43, 'Red', name='Toyota', is_police=False)
print(b.speed)
b.go()
b.turn('налево')
b.stop()

c = PoliceCar(speed=100, name='Lada', color='Blue', is_police=True)
print(c.is_police)
c.go()
c.turn('налево')
c.stop()
