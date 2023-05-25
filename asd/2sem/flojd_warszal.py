from math import inf

G = [
    [0, 5, 2, 3, 4],
    [5, 0, 6, inf, inf],
    [2, 6, 0, inf, inf],
    [3, inf, inf, 0, 1],
    [4, inf, inf, 1, 0]
]

n = len(G)
for k in range(n):
    for i in range(n):
        for j in range(n):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(n):
    print(G[i])