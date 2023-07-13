# def heapify(tab, i, n):
#     l = 2 * i + 1
#     r = 2 * i + 2
#     max_i = i
#     if l < n:
#         if len(tab[l]) > len(tab[max_i]):
#             max_i = l
#         elif len(tab[l]) == len(tab[max_i]) and tab[l] != tab[max_i]:
#             index = 0
#             while tab[l][index] == tab[max_i][index]:
#                 index += 1
#             if tab[l][index] < tab[max_i][index]:
#                 max_i = l
#     if r < n:
#         if len(tab[r]) > len(tab[max_i]):
#             max_i = r
#         elif len(tab[r]) == len(tab[max_i]) and tab[r] != tab[max_i]:
#             index = 0
#             while tab[r][index] == tab[max_i][index]:
#                 index += 1
#             if tab[r][index] < tab[max_i][index]:
#                 max_i = r
#
#     if max_i != i:
#         tab[i], tab[max_i] = tab[max_i], tab[i]
#         heapify(tab, max_i, n)
#
#
# def strong_string(T):
#     n = len(T)
#     for i in range(n):
#         if T[i][0] > T[i][-1]:
#             T[i] = T[i][::-1]
#     # tab = [0 for _ in range(n)]
#     # for i in range(n):
#     #     tab[i] = (len(T[i]), i)
#     for i in range((n - 2) // 2, -1, -1):
#         heapify(T, i, n)
#     for i in range(n-1, 0, -1):
#         T[0], T[i] = T[i], T[0]
#         heapify(T, 0, i)
#
#     max_result = 1
#     curr_result = 1
#     for i in range(1, n, 1):
#         if T[i] == T[i-1]:
#             curr_result += 1
#         else:
#             max_result = max(max_result, curr_result)
#             curr_result = 1
#     max_result = max(max_result, curr_result)
#     return max(max_result, curr_result)

def counting_sort(tab, k):
    tab2 = [0 for _ in range(len(tab))]
    values = [0 for _ in range(27)]
    for el in tab:
        if len(el) < k:
            values[0] += 1
        else:
            values[ord(el[len(el)-k]) - 96] += 1
    for i in range(1, 27):
        values[i] += values[i-1]
    for i in range(len(tab)-1, -1, -1):
        if len(tab[i]) < k:
            values[0] -= 1
            tab2[values[0]] = tab[i]
        else:
            values[ord(tab[i][len(tab[i])-k]) - 96] -= 1
            tab2[values[ord(tab[i][len(tab[i])-k]) - 96]] = tab[i]
    return tab2


def radix_sort(T):
    n = len(T)
    max_len = 0
    for el in T:
        if len(el) > max_len:
            max_len = len(el)
    lengths = [[] for _ in range(max_len)]
    for i in range(n):
        if T[i][0] > T[i][-1]:
            T[i] = T[i][::-1]
        lengths[len(T[i])-1] += [T[i]]
    T2 = []
    for i in range(max_len):
        if lengths[i]:
            for j in range(i):
                lengths[len(T[i]) - 1] = counting_sort(lengths[i], j+1)
            T2 += lengths[len(T[i]) - 1]
    T = T2
    max_result = 1
    curr_result = 1
    for i in range(1, n, 1):
        if T[i] == T[i-1]:
            curr_result += 1
        else:
            max_result = max(max_result, curr_result)
            curr_result = 1
    max_result = max(max_result, curr_result)
    return max(max_result, curr_result)


T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(strong_string(T))
print(radix_sort(T))
