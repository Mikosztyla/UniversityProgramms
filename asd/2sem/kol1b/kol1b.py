from kol1btesty import runtests


def sort_word(s):
    tab = [0 for _ in range(26)]
    result = ""
    for i in s:
        tab[ord(i)-97] += 1
    for i in range(26):
        if tab[i] != 0:
            result += chr(i+97)*tab[i]
    return result


def counting_sort(tab, k):
    n = len(tab)
    l = len(tab[0])
    temp = [0 for _ in range(26)]
    tab2 = [0 for _ in range(n)]
    for i in range(n):
        temp[ord(tab[i][l-k])-97] += 1
    for i in range(1, 26):
        temp[i] += temp[i-1]
    for i in range(n-1, -1, -1):
        a = ord(tab[i][l-k])-97
        temp[a] -= 1
        tab2[temp[a]] = tab[i]
    return tab2


def sort_tab(tab):
    l = len(tab[0])
    for i in range(l):
        tab = counting_sort(tab, i+1)
    return tab


def f(T):
    n = len(T)
    max_len = 0
    for i in range(n):
        T[i] = sort_word(T[i])
        l = len(T[i])
        if l > max_len:
            max_len = l
    tab = [[] for _ in range(max_len)]
    for i in range(n):
        tab[len(T[i])-1] += [T[i]]
    result_tab = []
    for i in range(max_len):
        if len(tab[i]) > 1:
            tab[i] = sort_tab(tab[i])
            result_tab += tab[i]
    max_result = 1
    curr_result = 1
    for i in range(len(result_tab)):
        if result_tab[i] == result_tab[i-1]:
            curr_result += 1
        else:
            if curr_result > max_result:
                max_result = curr_result
            curr_result = 1
    max_result = max(max_result, curr_result)
    return max_result


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
