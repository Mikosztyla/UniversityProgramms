def ile_cyfr(x):
    s = 0
    while x > 0:
        x //= 10
        s += 1
    return s


def validate_mask(n, ile1):
    s = 0
    while n > 0:
        if n%2 == 1:
            s += 1
        n = n >> 1
    return ile1 == s

a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))

ilosc = ile_cyfr(a) + ile_cyfr(b)
masks = [i for i in range(1, pow(2, ilosc))]
cyfry1 = [0 for i in range(ile_cyfr(a))]
cyfry2 = [0 for i in range(ile_cyfr(b))]

x = a
for i in range(ile_cyfr(a)-1, -1, -1):
    cyfry1[i] = x % 10
    x //= 10

x = b
for i in range(ile_cyfr(b)-1, -1, -1):
    cyfry2[i] = x % 10
    x //= 10

for i in masks:
    if validate_mask(i, ile_cyfr(a)):
        iterator1 = 0
        iterator2 = 0
        liczba = 0
        while i > 0 or iterator1 + iterator2 < ilosc:
            if i%2 == 0:
                liczba = liczba * 10 + cyfry2[iterator2]
                iterator2 += 1
            else:
                liczba = liczba * 10 + cyfry1[iterator1]
                iterator1 += 1
            i = i >> 1
        print(liczba)