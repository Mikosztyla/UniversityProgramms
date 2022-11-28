# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.
import random


def king(T, i, j, suma, min_sum):
    suma += T[i][j]
    if i == 7:
        if min_sum == -1:
            min_sum = suma
        else:
            if suma < min_sum:
                min_sum = suma
        return min_sum
    else:
        if j-1 >= 0:
            min_sum1 = king(T, i+1, j-1, suma, min_sum)
            if min_sum == -1:
                min_sum = min_sum1
            else:
                min_sum = min(min_sum, min_sum1)
        if j+1 <= 7:
            min_sum1 = king(T, i+1, j+1, suma, min_sum)
            if min_sum == -1:
                min_sum = min_sum1
            else:
                min_sum = min(min_sum, min_sum1)
        min_sum1 = king(T, i+1, j, suma, min_sum)
        if min_sum == -1:
            min_sum = min_sum1
        else:
            min_sum = min(min_sum, min_sum1)
    return min_sum


tab = [[random.randint(1, 10) for _ in range(8)] for _ in range(8)]
for i in range(8):
    print(tab[i])
print(king(tab, 0, 0, 0, -1))