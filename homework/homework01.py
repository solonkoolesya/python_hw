# Задание 1. Встроенные типы данных, операторы, функции и генераторы


from functools import reduce

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
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

def flatten(seq):
    b = []
	
    for i in seq:
      try:
        if type(i) in (list, tuple):
          b += flatten(i)
        else:
		       b.append(i)
      except:
        pass
    
    return b
