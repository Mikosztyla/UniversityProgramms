
def dfs(g):
    result = []
    visited = [False for _ in range(len(g))]

    def dfs_visit(v):
        nonlocal result
        if not visited[v]:
            visited[v] = True
            for e in g[v]:
                dfs_visit(e)
            result.append(v)

    for i in range(len(g)):
        dfs_visit(i)
    result = result[::-1]
    return result


T = [
    [0, 2, 1, 1],
    [1, 0, 1, 1],
    [2, 2, 0, 1],
    [2, 2, 2, 0]
]
g = [[] for _ in range(len(T))]
for i in range(len(T)):
    for j in range(len(T)):
        if T[i][j] == 1:
            g[i].append(j)

print(dfs(g))
