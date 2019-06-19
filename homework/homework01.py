# Задание 1. Встроенные типы данных, операторы, функции и генераторы

from timeit import timeit
from functools import reduce
from operator import mul
def fac(n):
    return functools.reduce(lambda x, y: x*y,range(1, n+1))


def fac1(n):
    for i in range(n):
        n *= i
    return n

def fac2(n):
    return reduce(mul, range(1, n+1))

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
	

def fib2():
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

def flatten(seq):
    b = []
    for i in seq:
        try:
            b.append(i)
        except:
            b += flatten(i)
    return b

def flat(seq):
    for i in seq:
    # isinstance(e, Sequence) #from collections import Sequence
    # hashstr(e, '__iter__')
        if type(e) in (list, tuple)
            yield from  flat

