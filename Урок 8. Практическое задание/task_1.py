"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
import collections


class HaffMan:

    def __init__(self, string_str):
        self.string = string_str
        self.code = dict()

    def _prepare_string(self):
        digits_frequency = collections.Counter(self.string)
        sorted_elements = sorted(digits_frequency.items(), key=lambda val: val[1])
        sorted_elements = collections.deque(sorted_elements)
        return sorted_elements

    def _build_tree(self):
        cod_string = self._prepare_string()
        while len(cod_string) > 1:
            wight = cod_string[0][1] + cod_string[1][1]
            temp = {
                0: cod_string.popleft()[0],
                1: cod_string.popleft()[0]
            }
            # print(temp, end=" - ")
            # print(wight)
            for index, value in enumerate(cod_string):
                if wight <= value[1]:
                    cod_string.insert(index, (temp, wight))
                    break
            else:
                cod_string.append((temp, wight))
                # print(index, end=" - ")
                # print(value)
            # print(cod_string)
        return cod_string[0][0]

    def codding(self, path="", tree=None):
        if tree is None:
            tree = self._build_tree()
        if not isinstance(tree, dict):
            self.code[tree] = path
        else:
            self.codding(f'{path}0', tree[0])
            self.codding(f'{path}1', tree[1])
        return self.code


a = HaffMan("beep boop beer!")
print(a.codding())
