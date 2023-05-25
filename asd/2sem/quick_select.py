import random


def one_dim_to_two_dim(i, n):
    return i//n, i%n


def partition(tab, l, p):
    px, py = one_dim_to_two_dim(p, n)
    x = tab[px][py]
    ix, iy = one_dim_to_two_dim(l, len(tab))
    i = l
    for j in range(l, p):
        jx, jy = one_dim_to_two_dim(j, n)
        if tab[jx][jy] <= x:
            ix, iy = one_dim_to_two_dim(i, n)
            tab[ix][iy], tab[jx][jy] = tab[jx][jy], tab[ix][jy]
            i += 1
    ix, iy = one_dim_to_two_dim(i, n)
    tab[ix][iy], tab[px][py] = tab[px][py], tab[ix][iy]
    return i


def quick_select(tab, l, p, k1, k2, curr_k = -1):
    if curr_k == -1:
        curr_k = k1
    if l <= p:
        q = partition(tab, l, p)
        if q == curr_k:
            if curr_k == k1:
                curr_k = k2
                return quick_select(tab, k1 + 1, len(tab)*len(tab)-1, k1, k2, curr_k)
            else:
                return tab
        elif q > curr_k:
            return quick_select(tab, l, q-1, k1, k2, curr_k)
        else:
            return quick_select(tab, q+1, p, k1, k2, curr_k)
    return -1


n = 5
tab = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
# print(tab)
# T = [0 for _ in range(n*n)]
# it = 0
# for i in range(n):
#     for j in range(n):
#         T[it] = tab[i][j]
#         it += 1

# print(T)
temp = (n*n-n)//2
tab = quick_select(tab, 0, len(tab)*len(tab)-1, temp, temp + n)
# print(T)
# it = 0
# for i in range(1, n):
#     for j in range(i):
#         tab[i][j] = T[it]
#         it += 1
#
# it = 0
# index = temp
# for i in range(n):
#     tab[i][it] = T[index]
#     index += 1
#     it += 1
#
# it = temp + n
# for i in range(2, n+1):
#     for j in range(1, i):
#         tab[n-i][n-j] = T[it]
#         it += 1

for el in tab:
    print(el)