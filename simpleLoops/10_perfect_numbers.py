import math

for i in range(1, 10000):
    suma = 0
    for j in range(1, int(math.sqrt(i))+1):
        if i%j == 0:
            suma += j
            if j != i//j and i != i//j:
                suma += i//j
    if suma == i:
        print(i)