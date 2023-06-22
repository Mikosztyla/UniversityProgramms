
def numDistinct(s, t):
    n = len(s)
    m = len(t)
    last_row = [1 for _ in range(n + 1)]
    curr_row = [0 for _ in range(n + 1)]
    for j in range(m - 1, -1, -1):

        for i in range(n - 1, -1, -1):
            curr_row[i] = curr_row[i + 1]
            if t[j] == s[i]:
                curr_row[i] += last_row[i + 1]
        last_row = curr_row
        curr_row = [0 for _ in range(n + 1)]

    return last_row[0]


s = "rabbbit"
t = "rabbit"

print(numDistinct(s, t))
