def longestIncreasingPath(matrix):
    n = len(matrix[0])
    m = len(matrix)
    dp = {}

    LIP = [[0 for _ in range(n)] for _ in range(m)]

    def dfs(r, c):
        if (r, c) in dp:
            return dp[(r, c)]

        res = 1
        if r - 1 >= 0 and matrix[r][c] < matrix[r-1][c]:
            res = max(res, dfs(r - 1, c) + 1)
        if c + 1 < n and matrix[r][c] < matrix[r][c+1]:
            res = max(res, dfs(r, c + 1) + 1)
        if r + 1 < m and matrix[r][c] < matrix[r+1][c]:
            res = max(res, dfs(r + 1, c) + 1)
        if c - 1 >= 0 and matrix[r][c] < matrix[r][c-1]:
            res = max(res, dfs(r, c - 1) + 1)
        dp[(r, c)] = res
        return res

    for i in range(m):
        for j in range(n):
            LIP[i][j] = dfs(i, j)

    result = 0
    for e in LIP:
        result = max(result, max(e))
    return result


matrix = [[1,2],[2,3]]
print(longestIncreasingPath(matrix))