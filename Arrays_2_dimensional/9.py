# Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
# poszukuje w tablicy kwadratu o liczbie pól bedacej liczba nieparzysta wieksza od 1, którego iloczyn 4 pól
# naroznych wynosi k. Do funkcji nalezy przekazac tablice i wartosc k. Funkcja powinna zwrócic informacje
# czy udało sie znalezc kwadrat oraz współrzedne (wiersz, kolumna) srodka kwadratu.
import random


def get_squares(tab, n, k):
    for i in range(n):
        for j in range(n):
            side = 2
            while i + side < n and j + side < n:
                if tab[i][j] * tab[i][j+side] * tab[i+side][j+side] * tab[i+side][j] == k:
                    print((i+i + side)//2, (j+j + side)//2, side+1)
                    return True
                side += 2
    return False



n = int(input("Podaj zakres: "))
k = int(input("Podaj docelowy iloczyn: "))
tab = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(tab[i])

print(get_squares(tab, n, k))