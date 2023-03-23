# Zadanie 1. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

p, q, k, l = 1, 1, 1, 1
a, b = 1, 1
n = 440
while (a*b != n and a < n and a < b) or (a == 1 and b == 1):
    #prawą stroną przedziału idziemy do przodu
    while a*b < n and b >= a:
        p, q = q, p+q
        b = p

    #prawą stroną przedziału idziemy do tyłu
    while a*b > n and b > a:
        p, q = q-p, p
        b = p

    #lewą stroną przedziału idziemy do przodu
    while a*b < n and b > a:
        k, l = l, k+l
        a = k
if a*b == n:
    print(a, b)
else:
    print(False)