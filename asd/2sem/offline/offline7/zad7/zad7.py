# Mikołaj Gosztyła
# Na początku, stworzę pomocniczą tablicę, w której dla każdego pola będę przetrzymywał 3 wartości.
# Pierwsza z nich to najdłuższa ścieżka, jaką możemy dojść do tego pola, jeśli wejdziemy na niego od góry.
# Druga z nich to najdłuższa ścieżka, jaką możemy dojść do tego pola, jeśli wejdziemy na niego od lewej strony.
# Trzecia z nich to najdłuższa ścieżka, jaką możemy dojść do tego pola, jeśli wejdziemy na niego od dołu.
# Mając te informacje, kiedy przesuniemy się na kolejne pole, możemy określić, jaka jest najdłuższa
# ścieżka dojścia do tego pola. Po polach będziemy iterować dla każdej kolumny najpierw "w dół" (od 0 do n-1),
# a później "w górę, żeby odpowiednio uzupełniać te 3 wartości dla każdego pola. Ostatecznie, wynik to maksimum
# z tych 3 wartości dla ostatniego pola (n-1, n-1).
# O(2 * n^2) = O(n^2)


from zad7testy import runtests


def maze(L):
    n = len(L)
    #   [top, left, bottom]
    tab = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                tab[i][j] = [-2, -2, -2]

    for i in range(n):
        for j in range(n):
            if L[j][i] != '#':
                if j-1 >= 0 and tab[j-1][i][0] != -2 and max(tab[j-1][i][0], tab[j-1][i][1]) != -1:
                    tab[j][i][0] = max(tab[j-1][i][0], tab[j-1][i][1]) + 1
                else:
                    if i != 0 or j != 0:
                        tab[j][i][0] = -1

                if i-1 >= 0 and tab[j][i-1][1] != -2 and max(tab[j][i-1]) != -1:
                    tab[j][i][1] = max(tab[j][i-1]) + 1
                else:
                    tab[j][i][1] = -1

        for j in range(n-1, -1, -1):
            if L[j][i] != '#':
                if j+1 < n and (tab[j+1][i][2] >= 0 or tab[j+1][i][1] >= 0) and max(tab[j+1][i][1], tab[j+1][i][2]) != -1:
                    tab[j][i][2] = max(tab[j+1][i][1], tab[j+1][i][2]) + 1
                else:
                    tab[j][i][2] = -1

    return max(tab[n-1][n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
