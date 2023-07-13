# Mikołaj Gosztyła
# Mój program dodaje do tablicy E krawędzie, pomiędzy każdymi dwoma kolejnymi wierzchołkami z tablicy S
# (doda ich w sumie tyle, ile jest wierzchołków w tej tablicy), które będą miały wagę 0. Następnie wykonuje algorytm
# Dijkstry i zwraca wynik.
# Ponieważ w swoim programi przekształcam tablicę E na listę sąsiedztwa grafu G, przez co algorytm Dijkstry będzie
# miał złożoność O(E*logV), czyli cały program będzie miał złożoność O(E+V+E*logV).


from zad5testy import runtests
from queue import PriorityQueue
from math import inf


def make_list(E, n):
    G = [[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append([E[i][1], E[i][2]])
        G[E[i][1]].append([E[i][0], E[i][2]])
    return G


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


def spacetravel( n, E, S, a, b ):
    for i in range(1, len(S)):
        E.append((S[i - 1], S[i], 0))
    G = make_list(E, n)
    result = dijkstra(G, a, b)
    if result == inf:
        return None
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )