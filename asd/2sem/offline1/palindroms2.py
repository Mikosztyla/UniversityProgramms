def ceasar(s):
    palindroms = []
    max_result = 1
    l = len(s)
    for i in range(l):
        j = 0
        lp = len(palindroms)
        for k in range(lp):
            palindroms[j][0] += 2
            if i - palindroms[j][0] >= 0 and s[i] == s[i - palindroms[j][0]]:
                palindroms[j][1] += 2
                j += 1
            else:
                max_result = max(max_result, palindroms[j][1])
                palindroms.pop(j)

        if i - 2 >= 0 and s[i] == s[i - 2]:
            palindroms.append([2, 3])

    for i in range(len(palindroms)):
        max_result = max(max_result, palindroms[i][1])

    return max_result


print(ceasar("a"*10000))
