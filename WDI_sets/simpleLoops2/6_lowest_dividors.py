# Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.

import math

n = int(input("Podaj liczbę: "))
x = int(math.sqrt(n)) + 1
d = 0
sub_min = n
iterator = 0
while iterator < x-1:
    number1, number2 = 1, 1
    if n % (x+iterator) == 0:
        number1 = x + iterator
    if n % (x-iterator) == 0:
        number2 = x - iterator
    a1 = abs(n//number1 - number1)
    a2 = abs(n//number2 - number2)
    if a1 < sub_min:
        sub_min = a1
        d = number1
    if a2 < sub_min:
        sub_min = a2
        d = number2
    iterator += 1

print(d, n//d)

