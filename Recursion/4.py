# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def fill_tab(tab, moves, start_i, start_j, n=2):
    if n == len(tab)**2 + 1:
        for i in tab:
            print(i)
        return True
    for move in moves:
        a, b = move
        if 0 <= start_i + a < len(tab) and 0 <= start_j + b < len(tab):
            if tab[start_i + a][start_j + b] == 0:
                tab[start_i + a][start_j + b] = n
                if fill_tab(tab, moves, start_i + a, start_j + b, n+1):
                    return True
    tab[start_i][start_j] = 0
    return False


#n = int(input("Podaj wymiary tablicy: "))
n = 4
if n > 32:
    print("klapa")
else:
    tab = [[0 for _ in range(n)] for _ in range(n)]
    moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, -1))
    tab[0][0] = 1
    fill_tab(tab, moves, 0, 0)