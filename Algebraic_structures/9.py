# Zadanie 9. Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako
# liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować
# funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
# w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
# pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu
# cyfr.


def find_max(tab):
    pos_max = 0
    for i in range(1, len(tab)):
        iterator = 0
        while iterator < len(tab) and tab[i][iterator] == tab[pos_max][iterator]:
            iterator += 1
        if iterator < len(tab) and tab[i][iterator] == 1:
            pos_max = i
    return pos_max


def find_min(tab):
    pos_min = 0
    for i in range(1, len(tab)):
        iterator = 0
        while iterator < len(tab) and tab[i][iterator] == tab[pos_min][iterator]:
            iterator += 1
        if iterator < len(tab) and tab[i][iterator] == 0:
            pos_min = i
    return pos_min


tab = [
    [1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1]
]

print(find_max(tab), find_min(tab))