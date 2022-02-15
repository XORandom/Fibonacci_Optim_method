import math
import numpy as np
import matplotlib.pyplot as plt


def func_task(x):
    return 2 * math.pow(x, 2) - math.exp(x)


# Поиск последовательности Фибоначчи
def fib(input_num):
    a = int(input_num)
    fb = [1, 1]
    for x in range(2, a):
        fb.append(fb[x - 2] + fb[x - 1])
    return fb[input_num-1]


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
    print('e = ', math.e)
    a = 0
    b = 1
    print(fib(0))
    eps = 0.000001
    x = fibonacci(a, b, eps)
    fx = func_task(x)
    print('x =', x)
    print('f(x) = ', fx)
    print('округление до 6 знака')
    print('x =', round(x, 6))
    print('f(x) =', round(fx, 6))


