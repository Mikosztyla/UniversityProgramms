# Zadanie 15. Problem 8 Hetmanów (treść oczywista)
def fill_row(i, tab):
    for k in range(8):
        tab[i][k] += 1


def fill_col(j, tab):
    for k in range(8):
        tab[k][j] += 1


def fill_diagonal(i, j, tab):
    m = 0
    i_mem = i
    j_mem = j
    while i >= 0 and j >= 0:
        tab[i][j] += 1
        i -= 1
        j -= 1
    i = i_mem
    j = j_mem
    while i >= 0 and j <= 7:
        tab[i][j] += 1
        i -= 1
        j += 1
    i = i_mem
    j = j_mem
    while i <= 7 and j >= 0:
        tab[i][j] += 1
        i += 1
        j -= 1
    i = i_mem
    j = j_mem
    while i <= 7 and j <= 7:
        tab[i][j] += 1
        i += 1
        j += 1


def check_T(tab, hetmany):
    for el in hetmany:
        x, y = el
        if tab[x][y] > 0:
            return False
    return True


def fill_tab(tab, x, y):
    fill_row(x, tab)
    fill_col(y, tab)
    fill_diagonal(x, y, tab)
    tab[x][y] -= 6


def rem_tab(tab, mem_tab):
    for m in range(8):
        for l in range(8):
            mem_tab[m][l] = tab[m][l]


def problem_hetmanow(tab, k = 0, res=[]):
    global licznik
    if k < 8:
        for i in range(8):
            if tab[i][k] ==  0:
                mem_tab = [[0 for _ in range(8)] for _ in range(8)]
                rem_tab(tab, mem_tab)
                fill_tab(tab, i, k)
                if check_T(tab, res):
                    if k == 7:
                        licznik += 1
                        for o in range(8):
                            print(tab[o])
                        print()
                        return tab
                    tab = problem_hetmanow(tab, k+1, res + [(i, k)])
                rem_tab(mem_tab, tab)
    return tab


tab = [[0 for _ in range(8)] for _ in range(8)]
licznik = 0
tab = problem_hetmanow(tab)
print(licznik)