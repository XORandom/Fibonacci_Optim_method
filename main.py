import math
#import numpy as np
#import matplotlib.pyplot as plt


def func_task(x):
    return 2 * math.pow(x, 2) - math.exp(x)


# Поиск последовательности Фибоначчи
def fib(input_num, show=0):
    n = int(input_num)
    fb = [1, 1]
    for k in range(2, n):
        fb.append(fb[k - 2] + fb[k - 1])
    if show == 1:
        print('Последовательность Фибоначчи', '[', input_num, ']', ': ', fb)
    else:
        return fb[input_num-1]



def fibonacci(a, b, eps, N):
    a0 = a
    b0 = b
    k = 0
    y0 = a0+((fib(N-2)/fib(N))*(b0-a0))
    z0 = a0+((fib(N-1)/fib(N))*(b0-a0))
    while abs(b0 - a0) > eps:
        if func_task(y0) > func_task(z0):
            a0 = y0
            y0 = z0
            z0 = a0+((fib(N-k-2)/fib(N-k-1))*(b0-a0))
        else:
            b0=z0
            z0=y0
            y0=a0+((fib(N-k-3)/fib(N-k-1))*(b0-a0))
        if ++k > 10e5:
            break
    return (a0 + b0) / 2


def gold(a, b, eps):
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
        if ++k > 10e5:
            break
    return (a + b) / 2


if __name__ == '__main__':
    print('e = ', math.e)
    a = 0
    b = 1
    N = 10
    eps = 0.000001

    x = fibonacci(a, b, eps, N)
    fx = func_task(x)
    print("Поиск методом Фибоначчи")
    fib(N, 1)
    print('x =', round(x, 6))
    print('f(x) =', round(fx, 6))

    x = gold(a, b, eps)
    print("Повысим точность")
    fx = func_task(x)
    print('x =', x)
    print('f(x) = ', fx)



