from egzP1btesty import runtests 
from math import inf
from queue import PriorityQueue


def min_3_points(G, s, t):

    min_result = inf

    # def dfs_visit(G, v, n, sum):
    #     if n == 3:
    #         if v == t:
    #             nonlocal min_result
    #             if sum < min_result:
    #                 min_result = sum
    #         return
    #
    #     if not visited[v]:
    #         visited[v] = True
    #         for v2, w in G[v]:
    #             dfs_visit(G, v2, n + 1, sum+w)
    #         visited[v] = False

    rem_path = []
    def dijkstra(G, s, t):
        nonlocal min_result, rem_path
        queue = PriorityQueue()
        n = len(G)
        distance = [inf for _ in range(n)]
        indexes = [5 for _ in range(n)]
        distance[s] = 0
        queue.put((0, s, 0, [0]))

        while not queue.empty():
            d, v, index, path = queue.get()
            if d < min_result:
                indexes[v] = index
                if index == 4:
                    if v == t and distance[v] < min_result:
                        min_result = distance[v]
                        rem_path = path
                elif index < 4 and v != t:
                    for curr_v, w in G[v]:
                        if curr_v not in path and (distance[curr_v] > w + distance[v] or indexes[curr_v] <= index):
                            distance[curr_v] = w + distance[v]
                            queue.put((distance[curr_v], curr_v, index + 1, path+[curr_v]))

    dijkstra(G, s, t)
    print(rem_path)
    return min_result


def turysta( G, D, L ):
    max_v = 0
    for v1, v2, value in G:
        if v2 > max_v:
            max_v = v2

    max_v += 1
    G2 = [[] for _ in range(max_v)]
    for v1, v2, value in G:
        G2[v1].append([v2, value])
        G2[v2].append([v1, value])

    return min_3_points(G2, D, L)

runtests ( turysta )