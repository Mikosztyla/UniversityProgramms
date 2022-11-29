# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def fill_tab(tab, moves, start_i, start_j):
    for move in moves:
        a, b = move
        if 0 <= start_i + a < n and 0 <= start_j + b < n:
            if not tab[start_i + a][start_j + b]:
                tab[start_i + a][start_j + b] = True
                tab = fill_tab(tab, moves, start_i + a, start_j + b)
    return tab


#n = int(input("Podaj wymiary tablicy: "))
n = 2
if n > 32:
    print("klapa")
else:
    tab = [[False for _ in range(n)] for _ in range(n)]
    moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, -1))
    tab[0][0] = True
    tab = fill_tab(tab, moves, 0, 0)
    for i in range(n):
        print(tab[i])