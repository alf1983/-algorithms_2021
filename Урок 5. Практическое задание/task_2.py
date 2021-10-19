"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict, deque


def dict_16_to_10():
    digits_16 = '0123456789ABCDEF'
    dict_digits = defaultdict(int)
    counter = 0
    for key in digits_16:
        dict_digits[key] += counter
        counter += 1
    return dict_digits


def convert_to_10(table, list_number=None):
    if list_number is None:
        list_number = []
    dex = 0
    list_number = deque(list_number)
    # print(type(list_number))
    i = 0
    while len(list_number) > 0:
        dex += table[list_number.pop()] * 16 ** i
        # print(f"{table[list_number[i]]} * 16 ** {i} = {table[list_number[i]] * 16 ** i}")
        i += 1
    return dex


def convert_to_16(table, number):
    result_num = deque()
    while number > 0:
        d = number % 16
        for digit in table.items():
            if digit[1] == d:
                result_num.appendleft(digit[0])
                break
        number //= 16
    return list(result_num)


class HexNumber:
    def __init__(self, number_16):
        self.number_16 = int(number_16, 16)

    def __add__(self, other):
        return hex(self.number_16 + other.number_16)

    def __mul__(self, other):
        return hex(self.number_16 * other.number_16)


first_number = input("Введите первое 16-тиричное число: ").upper()
second_number = input("Введите второе 16-тиричное число: ").upper()
table = dict_16_to_10()
print(convert_to_16(table, convert_to_10(table, first_number) + convert_to_10(table, second_number)))
print(convert_to_16(table, convert_to_10(table, first_number) * convert_to_10(table, second_number)))
print(list((HexNumber(first_number) + HexNumber(second_number)).replace("0x", "").upper()))
print(list((HexNumber(first_number) * HexNumber(second_number)).replace("0x", "").upper()))
