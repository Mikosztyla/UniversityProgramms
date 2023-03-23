# Zadanie 17. Napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.

import math


def f(x):
    return x * math.log(x, 10) - math.log(2020, 10)


def df(x):
    return math.log(x, 10) + 1


x = 1
eps = 1/1000000
while abs(f(x)) > eps:
    x = x - f(x)/df(x)

print(x)