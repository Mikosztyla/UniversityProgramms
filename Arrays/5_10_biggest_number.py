result = int(input())
count = 1
while True:
    n = int(input())
    if n == 0:
        break

    if count >= 10:
        if n > result:
            result = n
    else:
        if n < result:
            result = n
        count += 1

print(result)

