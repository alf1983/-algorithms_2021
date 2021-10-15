"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = str(enter_num)
    return reversed(enter_num)


print("Функция revers_1:", end=" ")
print(
    "{:.16f}".format(timeit('revers_1(23298211)', globals=globals(), number=10000))
)
print("Функция revers_2:", end=" ")
print(
    "{:.16f}".format(timeit('revers_2(23298211)', globals=globals(), number=10000))
)
print("Функция revers_3:", end=" ")
print(
    "{:.16f}".format(timeit('revers_3(23298211)', globals=globals(), number=10000))
)
print("Функция revers_4:", end=" ")
print(
    "{:.16f}".format(timeit('revers_4(23298211)', globals=globals(), number=10000))
)

cProfile.run("revers_1(545454454)")
cProfile.run("revers_2(545454454)")
cProfile.run("revers_3(545454454)")
cProfile.run("revers_4(545454454)")

"""
Функция revers_1: 0.0203244600000000
Функция revers_2: 0.0145284830000000
Функция revers_3: 0.0040986940000000
Функция revers_4: 0.0037669060000000
Самой быстрой оказалась revers_4 с использованием встроиной функции reversed и revers_3 (чуть медленее). Хоть и
имеют сложность O(N) так же как revers_2. Думаю что это потому что встроиные функции работают быстрее
"""