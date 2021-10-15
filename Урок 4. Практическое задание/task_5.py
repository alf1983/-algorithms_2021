"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosfen(i):
    if i == 1:
        return 2
    if i == 2:
        return 3
    n = 4
    simple_numbers = set()
    while len(simple_numbers) - 1 != i:
        sieve = list(range(n + 1))
        sieve[1] = 0
        for x in sieve:
            if x > 1:
                for j in range(x + x, len(sieve), x):
                    sieve[j] = 0
        simple_numbers = set(sieve)
        n += 1

    return max(simple_numbers)


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(eratosfen(i))

print("Функция simple:", end=" ")
print(
    "{:.16f}".format(timeit('simple(1000)', globals=globals(), number=1))
)
print("Функция eratosfen:", end=" ")
print(
    "{:.16f}".format(timeit('eratosfen(1000)', globals=globals(), number=1))
)

"""
Результаты замеров для 10 простого числа (10 запусков)
Функция simple: 0.0002803240000000
Функция eratosfen: 0.0011067690000000

Результаты замеров для 100 простого числа (10 запусков)
Функция simple: 0.0251234770000002
Функция eratosfen: 0.2381148589999995

Результаты замеров для 1000 простого числа (10 запусков)
Функция simple: 3.3044807910000000
Функция eratosfen: 56.8694906079999996

сложность simple O(N^2)
сложность eratosfen O(N^n)
"""