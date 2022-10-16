import math

for i in range(1, 1000000):
    suma = 0
    suma2 = 0
    for j in range(1, int(math.sqrt(i))+1):
        if i%j == 0:
            suma += j
            if j != i//j and i != i//j:
                suma += i//j
    for j in range(1, int(math.sqrt(suma))+1):
        if suma%j == 0:
            suma2 += j
            if j != suma//j and suma != suma//j:
                suma2 += suma//j
    if suma2 == i  and suma > i:
        print(i, suma)

# def czy_pierwsza(number):
#     d = 0
#     for i in range(2, int(math.sqrt(number))+1):
#         if number%i == 0:
#             d += 1
#     if d == 0:
#         return True
#     else:
#         return False
#
# n = 4
# a = pow(2, n)
# b = 2
# for i in range(1, n+1):
#     # p = ((b + 1) * a * 2 / b) - 1
#     # q = ((b + 1) * a * 2) - 1
#     # r = ((b + 1) * (b + 1) * a * a * 4 / b) - 1
#     p = (pow(2, i) + 1) * pow(2, n+1-i) - 1
#     q = (pow(2, i) + 1) * pow(2, n+1) - 1
#     r = (pow(2, i) + 1) * (pow(2, i) + 1) * pow(2, 2*n+2-i) - 1
#     #print(b)
#     #print(p, q, r, end="\n")
#     if czy_pierwsza(p) and czy_pierwsza(q) and czy_pierwsza(r):
#         print(a*2*p*q, a*2*r)
#     b *= 2