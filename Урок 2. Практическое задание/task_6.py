"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint


def guess_number(number, player_try=1):
    if player_try == 10:
        return f"Использованы все попытки. Вы не угадали число {number}"
    print(f"Попытка номер {player_try}")
    player_number = input("Введите число от 0 до 100: ")
    try:
        player_number = int(player_number)
    except ValueError:
        print(f"Необходимо ввести ЧИСЛО. {player_number} числом не является, попытку потеряли!")
        return guess_number(number, player_try + 1)
    else:
        if player_number == number:
            return f"Ура! Вы угадали! Загаданное число {number}"
    print(f"Упс! Не угадали!", end=" ")
    word = "попыток"
    if (10 - player_try) == 1:
        word = "попытка"
    if 1 < (10 - player_try) < 4:
        word = "попытки"
    if player_number > number:
        print(f"Загаданное число меньше чем {player_number}.")
    if player_number < number:
        print(f"Загаданное число больше чем {player_number}.")
    print(f"Осталось {10 - player_try} {word}")
    return guess_number(number, player_try + 1)


if __name__ == '__main__':
    print("Загаданно число от 0 до 100")
    random_number = randint(0, 100)
    print(guess_number(random_number))
