# Задание 1. Встроенные типы данных, операторы, функции и генераторы


import functools
def fac(n):
    return functools.reduce(lambda x, y: x*y,range(1, n+1))


def gcd(a, b):
    while b != 0:
        c = a % b
        if c == 0:
            return b
        else:
            a = b
            b = c
    return a


def fib():
    a = [1, 1]
    while True:
        a.append(a[-1]+a[-2])
        if len(a) == 40:
          break
    return a
	

def flatten(seq):
    b = []
    for i in seq:
        try:
            b.append(abs(i))
        except:
            b += flatten(i)
    return b
