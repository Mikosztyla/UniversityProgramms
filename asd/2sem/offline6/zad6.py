# Mikołaj Gosztyła
# Mój program tworzy graf, który składa się z 2n+2 wierzchołków, gdzie n to liczba maszyn. Pierwszy wierzchołek
# będzie połączony z każdą maszyną, każda maszyna z odpowiednim pracownikiem, a każdy pracownik z ostatnim
# wierzchołkiem. Po wykonaniu się algorytmu największego przepływu na tym grafie dostaniemy wynik, ponieważ
# każda krawędź jest wagi 1, czyli reprezentuje jednego pracownika.


from zad6testy import runtests
from collections import deque
from copy import deepcopy


def find_path(G,s,t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    result = []
    queue = [s]

    while queue:
        v = queue.pop()
        if v == t:
            break
        visited[v] = True
        for e in G[v]:
            if not visited[e]:
                parent[e] = v
                queue.append(e)

    while t != s:
        if t == -1:
            return []
        result.append(t)
        t = parent[t]

    result.append(s)
    result = result[::-1]
    return result


def max_flow(M,s,t):
    G = deepcopy(M)
    count = 0
    path = find_path(G,s,t)

    while path:
        count += 1
        for i in range(len(path)-1):
            G[path[i]].remove(path[i+1])
            G[path[i+1]].append(path[i])
        path = find_path(G,s,t)
    return count


def binworker(M):
    n = len(M)
    G = [[] for _ in range(2 * len(M) + 2)]
    len_G = len(G)
    for i in range(1, n + 1):
        G[0].append(i)
        G[i + n].append(len_G - 1)
    for i in range(n):
        for e in M[i]:
            G[i + 1].append(e + n + 1)
    return max_flow(G, 0, len_G-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
