n = int(input("Podaj liczbe: "))

ilosc_cyfr = 0
x = n
while x > 0:
    ilosc_cyfr += 1
    x //= 10

cyfry = [0 for i in range(0, ilosc_cyfr)]
x = n
for i in range(ilosc_cyfr-1, -1, -1):
    cyfry[i] = x % 10
    x //= 10

masks = [i for i in range(1, pow(2, ilosc_cyfr))]
for i in masks:
    liczba = 0
    iterator = 0
    for j in range(ilosc_cyfr):
        if i%2 == 1:
            liczba = liczba * 10 + cyfry[iterator]
        iterator += 1
        i = i >> 1
    if liczba % 7 == 0:
        print(liczba)