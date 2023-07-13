# Mikołaj Gosztyła
# Mój program na początku znajduje najkrótszą ścieżkę pomiędzy zadanymi wierzchołkami (algorytmem BFS), a następnie po
# kolei usuwa po jednej krawędzi ze znalezionej ścieżki i sprawdza, czy najmniejsza odległość pomiędzy zadanymi
# wierzchołkami się zmieniła, jeśli nie, dodaje usuniętą krawędź z powrotem i sprawdza inną krawędź, a jeśli odległość
# się zwiększyła, zwraca usuniętą krawędź.
# Zakładając, że graf G ma V wierzchołków i E krawędzi, to jego złożoność wynosi O((V + E) * E), ponieważ najkrótszą
# ścieżkę znajdujemy w O(E + V), najwięcej ma ona E krawędzi i dla każdej z nich jeszcze raz wykonujemy algorytm BFS.


from zad4testy import runtests
from collections import deque


def shortest_bfs(G, s, t):
    queue = deque()
    l = len(G)
    visited = [False for _ in range(l)]
    parent = [-1 for _ in range(l)]
    distance = [-1 for _ in range(l)]
    queue.append(s)
    visited[s] = True
    distance[s] = 0
    while len(queue) > 0:
        v = queue.popleft()
        for el in G[v]:
            if not visited[el]:
                parent[el] = v
                visited[el] = True
                distance[el] = distance[v] + 1
                if el == t:
                    return parent, distance[el]
                queue.append(el)

    return parent, -1


def longer( G, s, t ):
    parent, distance = shortest_bfs(G, s, t)
    last = t
    if distance == -1:
        return None
    for i in range(distance):
        first = parent[last]
        G[last].remove(first)
        G[first].remove(last)
        new_parent, d = shortest_bfs(G, s, t)
        if d == -1 or d > distance:
            return first, last
        G[last].append(first)
        G[first].append(last)
        last = first
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )