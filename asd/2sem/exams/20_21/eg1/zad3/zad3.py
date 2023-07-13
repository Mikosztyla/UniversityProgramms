from zad3testy import runtests


def kintersect(A, k):
    max_number = 0
    for l, r in A:
        max_number = max(max_number, l, r)

    tab = [0 for _ in range(max_number + 1)]
    lists = [[] for _ in range(max_number + 1)]
    for i in range(len(A)):
        l, r = A[i]
        for j in range(l, r+1):
            tab[j] += 1
            lists[j].append(i)

    return list(range(k))


runtests(kintersect)
