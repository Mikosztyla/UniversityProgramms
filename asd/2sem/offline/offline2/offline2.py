def heapify(tab, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_i = i
    if l < n and tab[l] > tab[max_i]:
        max_i = l
    if r < n and tab[r] > tab[max_i]:
        max_i = r

    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def snow( S ):
    result = index = 0
    n = len(S)
    for i in range((n - 1) // 2, -1, -1):
        heapify(S, i, n)
    curr_i = n-1
    while S[0] - index > 0 and curr_i >= 0:
        result += S[0] - index
        index += 1
        S[0], S[curr_i] = S[curr_i], S[0]
        heapify(S, 0, curr_i)
        curr_i -= 1
    return result


print(snow([10, 10, 10]))
