"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""
import random


def simple_iteration(list_of_integer):
    minimum = list_of_integer[0]  # O(1)
    for i in range(1, len(list_of_integer) - 1):  # O(N)
        for j in range(2, len(list_of_integer) - 2):  # O(N)
            if i != j:  # O(1)
                if list_of_integer[j] < list_of_integer[i] <= minimum:  # O(1)
                    minimum = list_of_integer[j]  # O(1)
    return minimum  # O(1)


def min_found(list_of_integer):
    minimum = list_of_integer[0]  # O(1)
    for i in range(len(list_of_integer)):  # O(N)
        if list_of_integer[i] <= minimum:  # O(1)
            minimum = list_of_integer[i]  # O(1)
    return minimum  # O(1)


lst = [random.randint(-50, 50) for _ in range(random.randint(8, 14))]
print(lst)
print(f"{min(lst)} - минимальное число встроиной функцией")
print(f"{simple_iteration(lst)} - минимальное число - сложность O(N^2)")
print(f"{min_found(lst)} - минимальное число - сложность O(N)")
