from zad8testy import runtests

def dfs(r, c, tab):
    n = len(tab[0])
    m = len(tab)
    oil_counted = [0 for _ in range(n)]
    oil_to_fill = []
    visited = [[False for _ in range(n)] for _ in range(m)]
    result = 0

    def dfs_visit(r, c):
        if not visited[r][c]:
            nonlocal oil_to_fill, result
            if r == 0:
                oil_to_fill.append(c)
            result += tab[r][c]
            visited[r][c] = True
            if r - 1 >= 0 and tab[r - 1][c] != 0:
                dfs_visit(r - 1, c)
            if c + 1 < n and tab[r][c + 1] != 0:
                dfs_visit(r, c + 1)
            if r + 1 < m and tab[r + 1][c] != 0:
                dfs_visit(r + 1, c)
            if c - 1 >= 0 and tab[r][c - 1] != 0:
                dfs_visit(r, c - 1)

    dfs_visit(r, c)
    for e in oil_to_fill:
        oil_counted[e] = result

    return oil_counted


def count_oil(tab):
    oil_visited = [False for _ in range(len(tab[0]))]
    result = [0 for _ in range(len(tab[0]))]
    for i in range(len(tab[0])):
        if tab[0][i] != 0 and not oil_visited[i]:
            oil_counted = dfs(0, i, tab)
            for i in range(len(oil_counted)):
                if oil_counted[i] != 0:
                    oil_visited[i] = True
                    result[i] = oil_counted[i]

    return result


def count_path(path):
    indexes = []
    for i in range(len(path)):
        if path[i] != 0:
            indexes.append(i)
    destination = []
    fuel_entered = [[] for _ in range(len(path))]
    fuel_entered[0].append([0, path[0]])
    for i in range(len(indexes)):
        for d, fuel in fuel_entered[indexes[i]]:
            for j in range(i + 1, len(indexes)):
                if fuel - indexes[j] + indexes[i] >= 0:
                    fuel_entered[indexes[j]].append([d+1, fuel - indexes[j] + indexes[i] + path[indexes[j]]])
            if fuel + indexes[i] >= len(path) - 1:
                destination.append(d+1)
    if len(destination) == 0:
        return None
    return min(destination)


def plan(T):
    path = count_oil(T)
    return count_path(path)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

