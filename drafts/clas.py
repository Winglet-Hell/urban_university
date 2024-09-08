# Регистрация пользователей с использованием классов


class User:
    """
    Создайте класс User, у которого есть: конструктор __init__,
    который принимает имя и пароль.
    """

    def __init__(self, name, password, password_confirmation):
        self.name = name
        if password == password_confirmation:
            self.password = password
        else:
            raise ValueError("Passwords do not match")


class UserDB:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None


User1 = User("John", "123", "123")
Db = UserDB()
Db.add_user(User1)
CurrentUser = Db.get_user("John")
print(CurrentUser.password)
