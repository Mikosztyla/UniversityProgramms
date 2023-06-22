from zad8testy import runtests
from queue import PriorityQueue


def dfs(r, c, tab):
    n = len(tab[0])
    m = len(tab)
    result = 0

    def dfs_visit(r, c):
        nonlocal result
        result += tab[r][c]
        tab[r][c] = 0
        if r - 1 >= 0 and tab[r - 1][c] != 0:
            dfs_visit(r - 1, c)
        if c + 1 < n and tab[r][c + 1] != 0:
            dfs_visit(r, c + 1)
        if r + 1 < m and tab[r + 1][c] != 0:
            dfs_visit(r + 1, c)
        if c - 1 >= 0 and tab[r][c - 1] != 0:
            dfs_visit(r, c - 1)

    dfs_visit(r, c)

    return result, tab


def count_oil(tab):
    result = [0 for _ in range(len(tab[0]))]
    for i in range(len(tab[0])):
        if tab[0][i] != 0:
            oil_counted, tab = dfs(0, i, tab)
            result[i] = oil_counted

    return result


def count_path_greedy_better(path):
    indexes = []
    for i in range(len(path)):
        if path[i] != 0:
            indexes.append(i)

    if path[0] == 0:
        return None
    queue = PriorityQueue()
    destination = len(path)
    max_range = 0
    result = 0
    for i in indexes:
        if max_range >= destination - 1:
            return result

        if max_range - i < 0:
            max_range += -queue.get()
            result += 1
        queue.put(-path[i])

    while not queue.empty():
        if max_range >= destination - 1:
            return result
        max_range += -queue.get()
        result += 1

    if max_range >= destination - 1:
        return result
    return None


def plan(T):
    path = count_oil(T)
    return count_path_greedy_better(path)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

