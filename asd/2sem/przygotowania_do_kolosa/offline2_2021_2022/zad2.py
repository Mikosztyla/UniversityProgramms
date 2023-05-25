from zad2testy import runtests


def heapify(tab, i, n):
    l = 2*i + 1
    r = 2*i + 2
    max_i = i
    if l < n and tab[l][0][0] > tab[max_i][0][0]:
        max_i = l
    if r < n and tab[r][0][0] > tab[max_i][0][0]:
        max_i = r

    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def build_heap(tab, n):
    for i in range((n-2)//2, -1, -1):
        heapify(tab, i, n)


def heap_sort(tab, n):
    build_heap(tab, n)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)
    return tab


def depth(L):
    tab = []
    for i in range(len(L)):
        tab += [[[L[i][0], L[i][1]], 0, i]]
        tab += [[[L[i][1], L[i][0]], 1, i]]
    n = len(tab)
    tab = heap_sort(tab, n)
    # print(tab)
    max_result = 0
    temp = []
    for i in range(n):
        if tab[i][1] == 0:
            temp.append([tab[i][2], 0, tab[i][0][1]])
        else:
            it = 0
            while temp[it][0] != tab[i][2]:
                temp[it][1] += 1
                it += 1
            index = it
            while index < len(temp) and temp[index][2] == tab[i][0][0]:
                if temp[index][0] != tab[i][2]:
                    temp[index][1] += 1
                index += 1
            el = temp.pop(it)
            if el[1] > max_result:
                max_result = el[1]
    while temp:
        el = temp.pop(0)
        if el[1] > max_result:
            max_result = el[1]
    return max_result


# T = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
# print(depth(T))

runtests( depth )
