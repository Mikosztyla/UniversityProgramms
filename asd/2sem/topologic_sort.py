def topologic_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    def dfs_visit(G, v):
        if not visited[v]:
            for e in G[v]:
                if not visited[e]:
                    dfs_visit(G, e)
                    visited[e] = True
                    result.append(e)

    for i in range(n):
        if not visited[i]:
            dfs_visit(G, i)
    result.append(0)
    result = result[::-1]
    return result


G = [
    [1, 2, 6],
    [5],
    [1, 3],
    [4],
    [6, 7],
    [4],
    [],
    []
]
print(topologic_sort(G))