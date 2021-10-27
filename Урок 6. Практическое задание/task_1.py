"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import memory_profiler
import timeit
from collections import deque


def prof_mem(func):
    def wrapper(*args):
        t_start = timeit.default_timer()
        m_start = memory_profiler.memory_usage()
        result = func(args[0])
        t_end = timeit.default_timer()
        m_end = memory_profiler.memory_usage()
        mem_diff = m_end[0] - m_start[0]
        time_diff = t_end - t_start
        return result, mem_diff, time_diff
    return wrapper


def odd_even_number(number, odd=0, even=0):
    if number < 0:
        number = abs(number)
    if number == 0:
        return odd, even
    if ((number % 10) % 2) == 0:
        even += 1
        return odd_even_number(number // 10, odd, even)
    else:
        odd += 1
        return odd_even_number(number // 10, odd, even)


@prof_mem
def test(number):
    return odd_even_number(number)


@prof_mem
def odd_even_number_opt(number):
    even = 0
    odd = 0
    if number < 0:
        number = abs(number)
    while number > 0:
        if ((number % 10) % 2) == 0:
            even += 1
            number //= 10
        else:
            odd += 1
            number //= 10
    return odd, even


@prof_mem
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)


@prof_mem
def func_1_opt(nums):
    gen = (nums[i] for i in range(len(nums)) if nums[i] % 2 == 0)
    return


@prof_mem
def fill_list(ellements):
    lst = []
    for i in range(ellements):
        lst.insert(0, i)


@prof_mem
def fill_deque(ellements):
    deq = deque()
    for i in range(ellements):
        deq.appendleft(i)


if __name__ == '__main__':
    res_1 = test(4546546546364378678976545)
    print(f"Количество нечетных и четных цифр в числе равно: {res_1[0]}")
    print(f"затраченая память: {res_1[1]}")
    print(f"затраченая память: {res_1[2]}")
    res_2 = odd_even_number_opt(4546546546364378678976545)
    print(f"Количество нечетных и четных цифр в числе равно: {res_2[0]}")
    print(f"затраченая память: {res_2[1]}")
    print(f"затраченая память: {res_2[2]}")

"""
Введите число: 4546546546364378678976545
Количество нечетных и четных цифр в числе равно: (11, 14)
затраченая память: 0.0078125
затраченая память: 0.10111474599999992
Количество нечетных и четных цифр в числе равно: (11, 14)
затраченая память: 0.0
затраченая память: 0.10103136499999987
ВЫВОД:
На больших числах рекурсия (odd_even_number()) "потребляет" больше памяти чем цикл (odd_even_number_opt()), но разница
во времени не значительна
"""

list_test = [i for i in range(2, 50000, 5)]
res_1 = func_1(list_test)
res_2 = func_1_opt(list_test)
print(f"затраченая func_1 память: {res_1[1]}")
print(f"затраченая время на func_1: {res_1[2]}")
print(f"затраченая func_1_opt память: {res_2[1]}")
print(f"затраченая время на func_1_opt: {res_2[2]}")

"""
затраченая func_1 память: 0.04296875
затраченая время на func_1: 0.10519190499999997
затраченая func_1_opt память: 0.0
затраченая время на func_1_opt: 0.10255671899999996
ВЫВОД:
На больших списках список (func_1()) "потребляет" больше памяти чем generator (func_1_opt()), но разница
во времени не значительна
"""

res_1 = fill_list(70000)
res_2 = fill_deque(70000)
print(f"затраченая fill_list память: {res_1[1]}")
print(f"затраченая время на fill_list: {res_1[2]}")
print(f"затраченая fill_deque память: {res_2[1]}")
print(f"затраченая время на fill_deque: {res_2[2]}")

"""
затраченая fill_list память: 0.7265625
затраченая время на fill_list: 1.328832763
затраченая fill_deque память: 0.5546875
затраченая время на fill_deque: 0.12304894200000005
ВЫВОД:
На больших числах заполнение списка с помощью insert (fill_list()) "потребляет" больше памяти чем заполнение deque
с помощью appendleft (fill_deque()), но разница во времени не значительна
"""