import math
import numpy as np
import matplotlib.pyplot as plt


def func_task(x):
    return 2 * math.pow(x, 2) - math.exp(x)


''' Поиск последовательности Фибоначчи 
к примеру мы хотим сначала 10 элемент последовательности Фибоначчи, 
для этого сначала посчитаем 10 элементов, а потом обратимся к 10
это позволяет экономить время, посколько задав изначально число элементов, нам надо ихт найти всего 1 раз
'''
def fib(input_num):
    fb = {1: 1, 2: 1}
    while id < input_num:
        fb[id]


def fibonacci(a, b, eps, N=10):
    print("Поиск методом Фибоначчи")
    g = (math.sqrt(5) - 1.0) / 2
    k = 0
    a1 = a + (1 - g) * (b - a)
    b1 = a + g * (b - a)
    while abs(b - a) > eps:
        if func_task(a1) > func_task(b1):
            a = a1
            a1 = b1
            b1 = a + g * (b - a)
        else:
            b = b1
            b1 = a1
            a1 = a + (1 - g) * (b - a)
        if ++k > N:
            break
    return (a + b) / 2


if __name__ == '__main__':
    '''
    print('e = ', math.e)
    a = 0
    b = 1
    eps = 0.000001
    x = fibonacci(a, b, eps)
    fx = func_task(x)
    print('x =', x)
    print('f(x) = ', fx)
    print('округление до 6 знака')
    print('x =', round(x, 6))
    print('f(x) =', round(fx, 6))
    '''
    print(fib(200))
