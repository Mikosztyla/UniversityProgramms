import random


def print_sudoku(tab):
    for i in range(9):
        if i % 3 == 0:
            if i == 0:
                print(" ", end="")
                print("-"*23)
            else:
                print("|", end="")
                print("-"*23, end="")
                print("|")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            print(tab[i][j], end=" ")
        print("|")
    print(" ", end="")
    print("-"*23)


def check_row(tab, w):
    temp = [0 for _ in range(10)]
    for j in range(9):
        temp[tab[w][j]] += 1
    for i in range(1, 10):
        if temp[i] > 1:
            return False
    return True


def check_column(tab, k):
    temp = [0 for _ in range(10)]
    for i in range(9):
        temp[tab[i][k]] += 1
    for i in range(1, 10):
        if temp[i] > 1:
            return False
    return True


def check_square(tab, w, k):
    x = w//3
    y = k//3
    x *= 3
    y *= 3
    temp = [0 for _ in range(10)]
    for i in range(x, x+3):
        for j in range(y, y+3):
            temp[tab[i][j]] += 1
    for i in range(1, 10):
        if temp[i] > 1:
            return False
    return True


def solve_sudoku(tab):
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                number_added = False
                for n in range(1, 10):
                    tab[i][j] = n
                    if check_row(tab, i) and check_column(tab, j) and check_square(tab, i, j):
                        if solve_sudoku(tab):
                            return True
                    tab[i][j] = 0
                if not number_added:
                    return False
    return True


sudoku = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
tab2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 5, 4, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 4, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
]
print_sudoku(tab2)
# print(check_square(tab2, 2, 7))
# print(check_row(tab2, 1))
# print(check_column(tab2, 2))
solve_sudoku(tab2)
print_sudoku(tab2)