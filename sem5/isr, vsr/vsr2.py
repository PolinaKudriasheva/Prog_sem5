"""
    ВСР 2.1. 
    Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).
"""

import itertools


def fib(n):
    fibonacci_list = [0, 1]
    for i in itertools.count(0):
        if i > 1:
            fibonacci_list += [fibonacci_list[-2] + fibonacci_list[-1]]
        if i >= n - 1:
            break
    return fibonacci_list


num = int(input('Введите кол-во элементов ряда Фибоначчи: '))
print('Ряд Фибоначчи: ', fib(num))
