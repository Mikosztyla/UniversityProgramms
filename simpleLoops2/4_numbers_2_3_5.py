n = int(input())

i = j = k = 1
s = 0
while i <= n:
    j = i
    while j <= n:
        k = j
        while k <= n:
            s += 1
            k *= 5
        j *= 3
    i *= 2
print(s)
