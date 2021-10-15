"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
# # Импортируем библиотеку, соответствующую типу нашей базы данных
# import sqlite3
#
# # Создаем соединение с нашей базой данных
# # В нашем примере у нас это просто файл базы
# conn = sqlite3.connect('Users.sqlite')
#
# # Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()
# user = 0
# query_get_user = """
# SELECT user_name FROM users WHERE user_name = ?
# """
# try:
#     cursor.execute(query_get_user, ("wasea",))
# except sqlite3.OperationalError as e:
#     print(e.with_traceback)
# else:
#     user = cursor.fetchone()
# print(user)
#
# # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# # КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО
#
# # Не забываем закрыть соединение с базой данных
# conn.close()
from hashlib import sha256
import sqlite3


class Users:
    def __init__(self, login, password=None):
        self.db = sqlite3.connect('Users.sqlite')
        self.login = login
        self.password = password

    def user_exist(self):
        query_get_user = """
        SELECT user_name FROM users WHERE user_name = ?
        """
        cursor = self.db.cursor()
        try:
            cursor.execute(query_get_user, (self.login,))
        except sqlite3.OperationalError as err:
            if str(err).find("table") < 0:
                query_create_table = """
                    CREATE TABLE IF NOT EXISTS users(
                        user_name VARCHAR(100) PRIMARY KEY,
                        password VARCHAR(256)
                        )
                """
                try:
                    cursor.execute(query_create_table)
                except sqlite3.OperationalError as e:
                    print(e)
                else:
                    self.db.commit()
                    return False
        else:
            user = cursor.fetchone()
            if user is None:
                return False
        return True

    def create_user(self):
        attempt = 1
        while attempt < 5:
            password = input("Придумайте пароль: ")
            if len(user_name) < 3:
                print("Пароль слишком короткий")
                attempt += 1
            else:
                solt = self.login
                password_solted = password + solt
                password_hesh = sha256(bytes(password_solted.encode("utf-8"))).hexdigest()
                print(f"В базе данных хранится строка: {password_hesh}")
                re_password = input("Введите пароль еще раз для проверки: ")
                if len(re_password) >= 3:
                    password_solted = re_password + solt
                    if password_hesh == sha256(bytes(password_solted.encode("utf-8"))).hexdigest():
                        return self.__add_user(password_hesh)
                print(f"Пароль не совпал с ранее введёным.")
                attempt += 1
        print("Произошла ошибка! Попробуйте позже")
        return False

    def __add_user(self, password):
        print(f"Вы ввели правильный пароль")
        insert_users_query = """
            INSERT INTO users (user_name, password)
            VALUES
                (?, ?)
            """
        try:
            self.db.cursor().execute(insert_users_query, (self.login, password))
        except sqlite3.OperationalError as e:
            return e
        self.db.commit()
        return True

    def user_login(self):
        attempt = 1
        while attempt < 4:
            password = input("Введите пароль: ")
            if len(password) >= 3:
                solt = self.login
                password_solted = password + solt
                password_hesh = sha256(bytes(password_solted.encode("utf-8"))).hexdigest()
                query_get_user = """
                SELECT password FROM users WHERE user_name = ?
                """
                cursor = self.db.cursor()
                cursor.execute(query_get_user, (self.login,))
                user_data = cursor.fetchone()
                if user_data[0] == password_hesh:
                    return True
            print(f"Неверный пароль. Осталось {3 - attempt} попытки/а")
            attempt += 1
        return False


if __name__ == "__main__":
    user_name = input("Введите логин: ")
    if len(user_name) < 3:
        print("Логин слишком короткий")
        exit(0)
    users_class = Users(user_name)
    exists = users_class.user_exist()
    if exists:
        if users_class.user_login():
            print("Вы успешно авторизировались")
        else:
            print("Вы исчерпали попытки введения паролей.")
    else:
        print(f"Пользователя с логин {user_name} нет")
        print(users_class.create_user())
    users_class.db.close()
