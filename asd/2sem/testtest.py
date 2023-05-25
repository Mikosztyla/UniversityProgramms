
from math import inf
from queue import PriorityQueue


def turysta(G, D, L):
    size = 0
    for v, u, w in G:
        size = max(size, u)
    N = [[]for _ in range(size + 1)]
    for v, u, w in G:
        N[v].append((u, w))
        N[u].append((v, w))
    distance = [[inf]*3 for _ in range(size + 1)]
    q = PriorityQueue()
    for i in range(3):
        distance[D][i] = 0
    q.put((0, D, 3))
    while not q.empty():
        w1, v, ilosc = q.get()
        for u, w2 in N[v]:
            if ilosc > 0 and u != L:
                if distance[u][ilosc - 1] > w1 + w2:
                    distance[u][ilosc - 1] = w1 + w2
                    q.put((distance[u][ilosc - 1], u, ilosc - 1))
            elif ilosc == 0 and u == L:
                distance[L][0] = min(distance[L][0], w1 + w2)
    return min(distance[L])


Graf=[[(1,1)],[(0,1),(2,2)],[(1,2),(3,3)],[(2,3),(4,4)],[(3,4),(5,5)],[(4,5)]]
print(turysta(Graf, 0, 5))