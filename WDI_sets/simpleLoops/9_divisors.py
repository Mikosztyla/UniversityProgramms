# Zadanie 9. Prosze napisac program wypisujacy podzielniki liczby.

import math

n = 30
for i in range(1, int(math.sqrt(n))+1):
    if n%i == 0:
        print(i, end=" ")
        if i != n//i:
            print(n//i, end=" ")