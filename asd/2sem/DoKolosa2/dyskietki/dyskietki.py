
def topologic_sort(depends):
    result = []
    visited = [False for _ in range(len(depends))]

    def dfs_visit(v):
        if not visited[v]:
            visited[v] = True
            for e in depends[v]:
                dfs_visit(e)
            result.append(v)

    for i in range(len(depends)):
        dfs_visit(i)
    print(result)


def swaps(disk, depends):
    topologic_sort(depends)


disk = ['A', 'A', 'B', 'B']
depends = [
    [2, 3],
    [],
    [1, 3],
    [1]]
swaps(disk, depends)