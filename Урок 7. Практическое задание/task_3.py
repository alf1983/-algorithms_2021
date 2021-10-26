"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from heapq import heappop, heappush
import random


def no_sort(random_list):
    action_list = random_list[:]
    left_half = []
    right_half = []
    i = 0
    while i < len(action_list):
        for j in range(len(action_list)):
            if action_list[i] > action_list[j]:
                left_half.append(action_list[j])
            elif action_list[i] < action_list[j]:
                right_half.append(action_list[j])
            if action_list[i] == action_list[j]:
                if i > j:
                    left_half.append(action_list[j])
                if i < j:
                    right_half.append(action_list[j])
        if len(left_half) == len(right_half):
            return action_list[i]
        i += 1
        left_half = []
        right_half = []


def heap_sort(array, m):
    heap = []
    for element in array:
        heappush(heap, element)
    ordered = []
    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))
    return ordered[m]


m = int(input("Введине m: "))
print(f"Длинна массива будет 2m + 1 = {2 * m + 1}")
lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(f"Случайный список длинной {2 * m + 1}:")
print(lst)
print(f"Медиана {heap_sort(lst, m)}, найдена с помощью сортировки кучей")
print(f"Медиана {no_sort(lst)}, найдена без сортировки")
"""
Введине m: 7
Длинна массива будет 2m + 1 = 15
Случайный список длинной 15:
[68, 67, 50, -88, 5, -26, -36, -26, -51, -29, 7, -45, -67, 64, 66]
Медиана -26, найдена с помощью сортировки кучей
Медиана -26, найдена без сортировки
"""