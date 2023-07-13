from math import inf
from queue import PriorityQueue

tab = [
    [0, 7, 8, 3, 0, 0, 0],
    [7, 0, 0, 4, 6, 0, 0],
    [8, 0, 0, 7, 0, 9, 0],
    [3, 4, 7, 0, 9, 0, 0],
    [0, 6, 0, 9, 0, 0, 8],
    [0, 0, 9, 0, 0, 0, 1],
    [0, 0, 0, 0, 8, 1, 0],
]
s = 0
t = 5
queue = PriorityQueue()
n = len(tab)
for i in range(n):
    for j in range(i, n):
        if tab[i][j] > 0:
            queue.put((tab[i][j], i, j))

distance = [inf for _ in range(n)]
distance[s] = 0
parent = [-1 for _ in range(n)]
while not queue.empty():
    w, v1, v2 = queue.get()
    if distance[v1] != inf and distance[v2] > distance[v1] + w:
        distance[v2] = distance[v1] + w
        parent[v2] = v1
    if distance[v2] != inf and distance[v1] > distance[v2] + w:
        distance[v1] = distance[v2] + w
        parent[v1] = v2
print(distance[t])
v = t
while parent[v] != -1:
    print(v, end=" ")
    v = parent[v]
print(s)