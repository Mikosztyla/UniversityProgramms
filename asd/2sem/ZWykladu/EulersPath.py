def set_next_to_visit(G, v, v_it):
    it = v_it
    while it < len(G) and G[v][it] == 0:
        it += 1
    if it < n:
        return it
    return n


def dfs(G, s, next_to_visit, n):
    for i in range(n):
        if next_to_visit[i] < n:
            dfs_visit(G, next_to_visit, i)


def dfs_visit(G, next_to_visit, v):
    if next_to_visit[v] == n:
        print(v)
        return
    G[v][next_to_visit[v]] = 0
    G[next_to_visit[v]][v] = 0
    rem_next_visit = next_to_visit[v]
    next_to_visit[next_to_visit[v]] = set_next_to_visit(G, next_to_visit[v], next_to_visit[next_to_visit[v]])
    next_to_visit[v] = set_next_to_visit(G, v, next_to_visit[v])
    while rem_next_visit < n:
        dfs_visit(G, next_to_visit, rem_next_visit)
        rem_next_visit = next_to_visit[v]
        if rem_next_visit < n:
            G[v][next_to_visit[v]] = 0
            G[next_to_visit[v]][v] = 0
            next_to_visit[next_to_visit[v]] = set_next_to_visit(G, next_to_visit[v], next_to_visit[next_to_visit[v]])
            next_to_visit[v] = set_next_to_visit(G, v, next_to_visit[v])
    print(v)


G = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0]
]
n = len(G)
next_to_visit = [0 for _ in range(n)]
for i in range(n):
    next_to_visit[i] = set_next_to_visit(G, i, next_to_visit[i])

dfs(G, 0, next_to_visit, n)
