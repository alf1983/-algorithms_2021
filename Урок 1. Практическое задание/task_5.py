"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackOfPlates:
    def __init__(self, stack_max_size):
        self.plates = []
        self.stack_max_size = stack_max_size

    def is_empty(self):
        return self.plates == []

    def push_in(self, el):
        self.plates.append(el)

    def pop_out(self):
        return self.plates.pop()

    def get_plate(self):
        return self.plates[len(plates)-1]

    def stack_size(self):
        return len(self.plates)

    def is_full(self):
        return len(self.plates) >= self.stack_max_size


if __name__ == '__main__':
    plates_stack = StackOfPlates(3)
    for i in range(4):
        if plates_stack.is_full() is not False:
            plates_stack.push_in("plate" + str(i))
        else:
            plates_stack = StackOfPlates(3)
            plates_stack.push_in("plate" + str(i))

