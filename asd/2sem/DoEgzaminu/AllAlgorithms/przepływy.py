from math import inf

def dfs(tab, s, t, parent):
    n = len(tab)
    visited = [False for _ in range(n)]

    def dfs_visit(v):
        visited[v] = True
        for i in range(n):
            if tab[v][i] > 0:
                if not visited[i]:
                    parent[i] = v
                    dfs_visit(i)

    dfs_visit(s)
    return visited[t]


def przeplywy(tab, s, t):
    n = len(tab)
    max_flow = 0
    mini = 0
    while mini != -1:
        mini = -1
        parent = [-1 for _ in range(n)]
        if dfs(tab, s, t, parent):
            v = t
            mini = inf
            while parent[v] != -1:
                mini = min(mini, tab[parent[v]][v])
                v = parent[v]
            max_flow += mini
            v = t
            while parent[v] != -1:
                tab[parent[v]][v] -= mini
                tab[v][parent[v]] += mini
                v = parent[v]
    return max_flow

tab = [
    [0, 7, 9, 3, 0, 0, 0],
    [7, 0, 0, 4, 6, 0, 0],
    [9, 0, 0, 7, 0, 9, 0],
    [3, 4, 7, 0, 9, 3, 2],
    [0, 6, 0, 9, 0, 0, 8],
    [0, 0, 9, 3, 0, 0, 1],
    [0, 0, 0, 2, 8, 1, 0],
]
print(przeplywy(tab, 6, 5))