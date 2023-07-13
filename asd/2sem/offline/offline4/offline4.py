from collections import deque


def shortest_dfs(G, s, t):
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


# def count_distance(parent, s, t):
#     v = parent[t]
#     distance = 1
#     while v != s:
#         if v == -1 and v != s:
#             return -1
#         distance += 1
#         v = parent[v]
#     return distance


def longer( G, s, t ):
    parent, distance = shortest_dfs(G, s, t)
    last = t
    for i in range(distance):
        first = parent[last]
        G[last].remove(first)
        G[first].remove(last)
        new_parent, d = shortest_dfs(G, s, t)
        # d = count_distance(new_parent, s, t)
        if d == -1 or d > distance:
            return first, last
        G[last].append(first)
        G[first].append(last)
        last = first
    return False


G = [
[1, 2],
[0, 3],
[0, 3],
[1, 2, 4],
[3]
]
print(longer(G, 0, 4))