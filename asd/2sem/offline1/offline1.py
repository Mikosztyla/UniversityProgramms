def ceasar(s):
    max_result = 1
    result = 1
    index = 2
    i = 0
    l = len(s)
    rem_i = -1
    while i < l:
        if i - index >= 0 and s[i] == s[i - index]:
            if rem_i == -1 and index != 2 and s[i] == s[i - 2]:
                rem_i = i
            result += 2
            index += 2
            i += 1
        else:
            if index == 2:
                i += 1
            max_result = max(result, max_result)
            # if l - max_result//2 < i:
            #     i = l
            #     rem_i = -1
            index = 2
            result = 1
            if rem_i != -1:
                i = rem_i
                rem_i = -1
    return max(result, max_result)


print(ceasar("a"*10000))