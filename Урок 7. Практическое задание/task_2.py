"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


def merge_sort(sort_list):
    if len(sort_list) < 2:
        return sort_list[:]
    else:
        middle = int(len(sort_list) / 2)
        left = merge_sort(sort_list[:middle])
        right = merge_sort(sort_list[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_len = int(input("Введите число элементов: "))
test_list = [random.random() for _ in range(list_len)]
print(f"Исходный - {test_list}")
print(f"Отсортированный - {merge_sort(test_list)}")
test_list = [random.randint(-100, 100) for _ in range(10)]
print("Замеры на 10", end=" - ")
print(
    timeit(
        "merge_sort(test_list[:])",
        globals=globals(),
        number=1000))
test_list = [random.randint(-100, 100) for _ in range(100)]
print("Замеры на 100", end=" - ")
print(
    timeit(
        "merge_sort(test_list[:])",
        globals=globals(),
        number=1000))
test_list = [random.randint(-100, 100) for _ in range(1000)]
print("Замеры на 1000", end=" - ")
print(
    timeit(
        "merge_sort(test_list[:])",
        globals=globals(),
        number=1000))
"""
Введите число элементов: 5
Исходный - 
[0.44831921652752404, 0.28277311891618717, 0.20917845142115787, 0.46835388177345827, 0.7837935943999725]
Отсортированный - 
[0.20917845142115787, 0.28277311891618717, 0.44831921652752404, 0.46835388177345827, 0.7837935943999725]
Замеры на 10 - 0.022262267999999974
Замеры на 100 - 0.24388582700000017
Замеры на 1000 - 3.1357581779999997
Вывод:
Хоть я и использую рекурсию результаты не плохие даже при массивах в 1000 эллементов
"""