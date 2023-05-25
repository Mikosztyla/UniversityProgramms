from egzP3btesty import runtests 
from queue import PriorityQueue
from math import inf


def prim(G):
    n = len(G)
    queue = PriorityQueue()
    edges_sum = 0
    for i in G:
        for e in i:
            edges_sum += e[1]
    edges_sum //= 2
    visited = [False for _ in range(n)]
    queue.put([0, 0])
    mst = 0
    best_edge = 0
    while not queue.empty():
        w1, v = queue.get()
        w1 = -w1
        if not visited[v]:
            mst += w1
        else:
            if w1 > best_edge:
                best_edge = w1
        visited[v] = True
        for u, w2 in G[v]:
            if not visited[u]:
                queue.put([-w2, u])

    return edges_sum - mst - best_edge


def lufthansa ( G ):

    return prim(G)


runtests ( lufthansa, all_tests=True )