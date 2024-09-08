class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Меня зовут {self.name} мне {self.age}"


class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def info(self):
        return f"{super().info()} и я работаю в {self.job}"


class Manager(Employee):
    def __init__(self, name, age, job, department):
        super().__init__(name, age, job)
        self.department = department

    def info(self):
        return f"{super().info()} в отделе {self.department}"


m1 = Manager("Иван", 30, "Икеа", "Отдел продаж")
print(m1.info())  # Меня зовут Иван мне 30 и я работаю в Менеджер в отделе Отдел продаж
