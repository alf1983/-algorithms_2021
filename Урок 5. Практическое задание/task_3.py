"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""


from collections import deque
from timeit import timeit


def fill_list(ellements):
    lst = []
    for i in range(ellements):
        lst.insert(0, i)


def fill_deque(ellements):
    deq = deque()
    for i in range(ellements):
        deq.appendleft(i)
    return deq.popleft()


test_list = [i for i in range(10000)]
test_deque = deque(test_list)
list_to_add = [i for i in range(10000, 20000)]


def pop_0_test(t):
    t.pop(0)


def popleft_test(d):
    d.popleft()


def extend_list(lst, lst_to_add):
    lst.extend(lst_to_add)


def extend_deque(deq, lst_to_add):
    deq.extendleft(lst_to_add)


print(f"время затраченное на заполнение списка с помощью insert:", end=" ")
print(timeit(f"{fill_list(100)}", globals=globals()))
print(f"время затраченное на заполнение deque с помощью popleft:", end=" ")
print(timeit(f"{fill_deque(100)}", globals=globals()))
print(f"время затраченное на вырезание первого элемента списка:", end=" ")
print("{:.16f}".format(timeit('pop_0_test(test_list)',
                              setup='from __main__ import pop_0_test, test_list',
                              number=10000)))
print(f"время затраченное на вырезание первого элемента deque:", end=" ")
print("{:.16f}".format(timeit('popleft_test(test_deque)',
                              setup='from __main__ import popleft_test, test_deque',
                              number=10000)))
print(f"время затраченное на расширение списка:", end=" ")
print("{:.16f}".format(timeit(
    'extend_list(test_list, list_to_add)',
    setup='from __main__ import extend_list, test_list, list_to_add', number=10000)))
print(f"время затраченное на расширение deque:", end=" ")
print("{:.16f}".format(timeit(
    'extend_deque(test_deque, list_to_add)',
    setup='from __main__ import extend_deque, test_deque, list_to_add', number=10000)))
# print(timeit(test_1, globals=globals(), number=100))
