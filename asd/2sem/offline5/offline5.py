from queue import PriorityQueue
from math import inf


def make_list(E, n):
    G = [[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append([E[i][1], E[i][2]])
        G[E[i][1]].append([E[i][0], E[i][2]])
    return G


# def optimize_vertices(G, S):
#     n = len(G)
#     v1 = S[0]
#     for i in range(1, len(S)):
#         v2 = S[i]
#         for j in range(n):
#             if (G[v1][j] == 0 and G[v2][j] != 0) or (G[v2][j] < G[v1][j] and G[v2][j] != 0):
#                 G[v1][j] = G[v2][j]
#                 G[j][v1] = G[v2][j]
#             G[v2][j] = 0
#             G[j][v2] = 0


def dijkstra(G, s, k):
    queue = PriorityQueue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[s] = 0
    queue.put((0, s))
    while not queue.empty():
        d, v = queue.get()
        if not visited[v]:
            for curr_v, w in G[v]:
                if distance[curr_v] > w + distance[v]:
                    distance[curr_v] = w + distance[v]
                    queue.put((distance[curr_v], curr_v))
                    parent[curr_v] = v
        visited[v] = True
    return distance[k]


S=[0, 2, 3]
a = 1
b = 5
n = 7
E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
for e in S:
    if a == e:
        a = S[0]
    if b == e:
        b = S[0]
result = 0
for i in range(1, len(S)):
    E.append((S[i-1], S[i], 0))
E.append((S[0], S[-1], 0))
G = make_list(E, n)
print(dijkstra(G, a, b))
