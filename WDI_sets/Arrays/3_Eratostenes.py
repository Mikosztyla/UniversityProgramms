# Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa

def sito(n):
    t = [True for i in range(n)]
    t[0] = t[1] = False
    for i in range(n):
        if t[i]:
            for j in range(i*i, n, i):
                t[j] = False
    for k in range(n):
        if t[k]:
            print(k)

n = int(input("Podaj liczbę:"))
sito(n)