"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

@profile
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


@profile
def my_way():
    return odd_even_number(2342)


my_way()

"""
Если сделать профилировку рекурсии то декоратор будет сробатывать каждый раз при вызове функции
моё решение сделать профилактику функции которая возвращает результат рекурсии
"""