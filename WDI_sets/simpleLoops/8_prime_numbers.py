# Zadanie 8. Prosze napisac program sprawdzajacy czy zadana liczba jest pierwsza

import math

n = 10001
d = 0
for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
        d += 1

if d > 0:
    print("Number is NOT prime")
else:
    print("Number is prime")