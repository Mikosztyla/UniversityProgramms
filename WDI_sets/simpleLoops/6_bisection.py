# Zadanie 6. Prosze napisac program rozwiazujacy równanie xx = 2020 metoda bisekcji.

eps = 1/1000000
a = 0
b = 10
while b-a > eps:
    c = (a+b)/2
    if c**c - 2022 < 0:
        a = c
    else:
        b = c
print(a)