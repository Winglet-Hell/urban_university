class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Переменная с манглингом имён

    def __private_method(self):
        print("This is a private method")


# print(obj.__private_variable)  # Ошибка: AttributeError
# obj.__private_method()         # Ошибка: AttributeError

# Правильный доступ через манглинг имён:
obj = MyClass()
print(obj._MyClass__private_variable)  # Доступен через манглинг имён
obj._MyClass__private_method()  # Доступен через манглинг имён
