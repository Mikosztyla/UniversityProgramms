from kolutesty import runtests


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
    return result


def dyskietki(disks, depends):
    tab_sorted = topologic_sort(depends)
    n = len(disks)
    result = [0 for _ in range(n)]
    for i in range(n):
        maxi = 0
        for e in depends[tab_sorted[i]]:
            if disks[tab_sorted[i]] == disks[e]:
                maxi = max(maxi, result[e])
            else:
                maxi = max(maxi, result[e] + 1)
        result[tab_sorted[i]] = maxi

    return max(result)


runtests( dyskietki, all_tests = True )