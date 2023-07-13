from math import inf
from queue import PriorityQueue


def dijkstra(tab, s, t):
    n = len(tab)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    distance[s] = 0
    queue = PriorityQueue()
    queue.put((0, s))
    while not queue.empty():
        d, v = queue.get()
        for i in range(n):
            if tab[v][i] > 0:
                if d + tab[v][i] < distance[i]:
                    distance[i] = d + tab[v][i]
                    if not visited[i]:
                        queue.put((distance[i], i))

    return distance[t]


tab = [
    [0, 7, 9, 3, 0, 0, 0],
    [7, 0, 0, 4, 6, 0, 0],
    [9, 0, 0, 7, 0, 9, 0],
    [3, 4, 7, 0, 9, 3, 2],
    [0, 6, 0, 9, 0, 0, 8],
    [0, 0, 9, 3, 0, 0, 1],
    [0, 0, 0, 2, 8, 1, 0],
]
print(dijkstra(tab, 0, 5))