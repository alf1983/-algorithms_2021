"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def fill_dict(dct, ellements):
    for i in range(ellements):
        dct[str(i)] = i


def fill_dict_od(ellements):
    OrderedDict([(str(i), i) for i in range(ellements)])


dct = {}
for i in range(50):
    dct[str(i)] = i
dict_od = OrderedDict([(str(i), i) for i in range(50)])
test1 = """dct.get("99")"""
test2 = """dict_od.get("99")"""
print(f"время затраченное на заполнение словоря c помощью", end=" ")
print(timeit(f"{fill_dict({}, 100)}", globals=globals()))
print(f"время затраченное на заполнение словоря", end=" ")
print(timeit(f"{fill_dict_od(100)}", globals=globals()))
print("{:.16f}".format(timeit(test1,
                              setup='from __main__ import test1, dct',
                              number=100)))
print("{:.16f}".format(timeit(test2,
                              setup='from __main__ import test2, dict_od',
                              number=100)))
"""
время затраченное на заполнение словоря c помощью 0.006992552999999997
время затраченное на заполнение словоря 0.006994383999999999
0.0000062410000000
0.0000069210000000
Согласно замерам не имеет смысла исп-ть OrderedDict в Python 3.6 и более поздних версиях, так как 
время ыполния операций (заполнение, получение элемента) примерно одинаковое (разница не существенна)"""
