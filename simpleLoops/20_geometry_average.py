import math

eps = 1/1000000
a, b = 3, 10
while abs(a-b) > eps:
    a_temp = math.sqrt(a*b)
    b_temp = (a+b)/2
    a = a_temp
    b = b_temp
print(a, b)