# Zadanie 20. Dane sa ciagi: An+1 = An * Bn oraz Bn+1 = (An + Bn)/2.0. Ciagi te sa zbiezne do wspólnej
# granicy nazywanej srednia arytmetyczno-geometryczna. Prosze napisac program wyznaczajacy srednia
# arytmetyczno-geometryczna dwóch liczb.

import math

eps = 1/1000000
a, b = 3, 10
while abs(a-b) > eps:
    a_temp = math.sqrt(a*b)
    b_temp = (a+b)/2
    a = a_temp
    b = b_temp
print(a, b)