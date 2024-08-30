# класс который будет принимать имя и возраст и здороваться с этим человеком
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.greet()

    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old.")


# создаем объект класса Person
person = Person("Alice", 25)
