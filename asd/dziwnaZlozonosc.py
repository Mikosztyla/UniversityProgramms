def check(B, val):
    if not B:
        return -1
    n = len(B)
    left = 0
    right = n-1
    while left <= right:
        x = (right + left)//2
        if B[x] == val:
            return x
        if B[x] < val:
            left = x + 1
        else:
            right = x - 1
    return -1


def insert(tab, x):
    tab.append()
    for i in range(len(tab)-1, 0, -1):
        tab[i] = tab[i-1]
        if tab[i-1] < x:
            tab[i] = x
    return tab


def find_values(tab):
    result = []
    for val in tab:
        idx = check(result, val)
        if idx == -1:
            tab = insert(result, val)
    return result


def counting_sort(A):
    B = find_values(A)
    C = [0 for _ in range(len(B))]
    for x in A:
        idx = check(B, x)
        C[idx] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    res = [0 for _ in range(len(A))]
    for i in range(len(A)-1, -1, -1):
        idx = check(B, A[i])
        res[C[idx] - 1] = A[i]
        C[idx] -= 1
    return res
