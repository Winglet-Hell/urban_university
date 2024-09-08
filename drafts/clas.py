# Создаем родительский класс
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, speed):
        # Увеличивает скорость на 10 км/ч
        self.speed += 10


class Car(Vehicle):
    def honk(self, name):
        print(f"{name} Сигналит beep-beep!")


class Bicycle(Vehicle):
    def ring_bell(self, name):
        print(f"{name} Сигналит Дзинь-дзинь!")


# Создаем объекты классов
v1 = Car("Audi", 100)
v2 = Bicycle("Stels", 20)
v1_speed = v1.move(1)
print(v1_speed)
v2_speed = v2.move(1)
print(v2_speed)
