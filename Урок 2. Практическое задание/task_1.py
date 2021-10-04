"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def simple_calculator():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation == "0":
        result = "Вы вышли!"
        return result
    allowed_operations = ["+", "-", "*", "/"]
    if operation not in allowed_operations:
        print('Введена не верная операция. (+, -, *, / или 0 для выхода)')
        return simple_calculator()
    first_number = input("Введите первое число: ")
    try:
        first_number = int(first_number)
    except ValueError:
        print(f"Необходимо ввести ЧИСЛО. {first_number} числом не является")
        return simple_calculator()
    second_number = input("Введите второе число: ")
    try:
        second_number = int(second_number)
    except ValueError:
        print(f"Необходимо ввести ЧИСЛО. {second_number} числом не является")
        return simple_calculator()
    if operation == "+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    elif operation == "-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operation == "*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    else:
        try:
            result_operation = first_number / second_number
        except ZeroDivisionError:
            print(f"На 0 делить нельзя!!!")
        else:
            print(f"{first_number} : {second_number} = {round(result_operation, 4)}")

    return simple_calculator()


if __name__ == '__main__':
    print(simple_calculator())
