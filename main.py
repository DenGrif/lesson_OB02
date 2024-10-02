class User:

    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа для обычных пользователей

    # Создание ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Создание имени пользователя
    def get_name(self):
        return self.__name

    # Создание нового имени пользователя
    def set_name(self, new_name):
        self.__name = new_name

    # Получение уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):

    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администратора

    @staticmethod
    def add_user(users, user):
        if isinstance(user, User):
            users.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему")
        else:
            print("Ошибка: Объект не является экземпляром класса User.")

    @staticmethod
    def remove_user(users, user_id):
        for user in users:
            if user.get_user_id() == user_id:
                users.remove(user)
                print(f"Пользователь {user.get_name()} удалён из системы.")
                return
        print(f"Пользователь с указанным ID не найден.")


# Список для хранения пользователей
user_list = []

# Создаем админа
admin = Admin(1, "Admin Den")

# Создаем обычных пользователей
user1 = User(234, "Женя")
user2 = User(235, "Женя5")
user3 = User(236, "Женя6")

# Админ добавляет пользователя в систему
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)

# Админ удаляет пользователя из системы
admin.remove_user(user_list, 236)

