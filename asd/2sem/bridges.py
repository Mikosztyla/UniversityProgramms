from math import inf


def find_bridges(G):
    n = len(G)
    result = []
    time = 0
    times = [-1 for _ in range(n)]
    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]

    def dfs_visit(G, v, prev_v):
        nonlocal time
        if not visited[v]:
            visited[v] = True
            times[v] = time
            low[v] = time
            time += 1
            for e in G[v]:
                if not visited[e]:
                    dfs_visit(G, e, v)
                    low[v] = min(low[v], low[e])
                elif e != prev_v:
                    low[v] = min(low[v], low[e])
        if low[v] == times[v] and v != 0:
            print("bridge:", prev_v, v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(G, i, i)


G = [
    [2],
    [2],
    [0, 1, 3, 7],
    [2, 4, 5, 6, 7],
    [3, 5],
    [3, 4],
    [3],
    [2, 3]
]
find_bridges(G)