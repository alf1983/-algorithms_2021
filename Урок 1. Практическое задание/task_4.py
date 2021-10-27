"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
USERS = {
    "user":
        {
            "password": "1234",
            "is_active": True
        },
    "user1":
        {
            "password": "1234",
            "is_active": True
        },
    "user2":
        {
            "password": "1234",
            "is_active": True
        },
    "user3":
        {
            "password": "1234",
            "is_active": True
        },
    "user4":
        {
            "password": "1234",
            "is_active": False
        },
    "user5":
        {
            "password": "1234",
            "is_active": True
        },
    "user6":
        {
            "password": "1234",
            "is_active": True
        },
    "user7":
        {
            "password": "1234",
            "is_active": False
        },
    "user8":
        {
            "password": "1234",
            "is_active": True
        },
}


def user_authentication(login, password):
    if USERS.get(login) is None:  # O(1)
        print(f"Пользователя с имененем {login} нет в системе")  # O(1)
    else:
        if USERS[login]["password"] == password:  # O(1)
            if USERS[login]["is_active"]:  # O(1)
                print(f"Вы успешно вошли в систему")  # O(1)
            else:  # O(1)
                print(f"Требуется активация вашей учётной записи")  # O(1)
        else:
            print(f"Вы ввели не верный пароль")  # O(1)
    return


def user_authentication2(login, password):
    for user in USERS.keys():  # O(N)
        if login == user:  # O(1)
            if USERS[login]["password"] == password:  # O(1)
                if USERS[login]["is_active"]:  # O(1)
                    print(f"Вы успешно вошли в систему")  # O(1)
                    return  # O(1)
                else:  # O(1)
                    print(f"Требуется активация вашей учётной записи")  # O(1)
                    return  # O(1)
    print(f"Пользователя с имененем {login} нет в системе")  # O(1)
    return  # O(1)


user_authentication("user", "1234")
user_authentication("user5", "4321")
user_authentication("user7", "1234")
user_authentication("user77", "1234")
print("--------------------")
user_authentication2("user", "1234")
user_authentication2("user5", "4321")
user_authentication("user7", "1234")
user_authentication2("user77", "1234")
"""
Сложность функции user_authentication O(1)
Сложность user_authentication2 - O(N)
Первое решение лучше так как в нотации О-большое константное а во втором решении линейное что "хуже"
"""