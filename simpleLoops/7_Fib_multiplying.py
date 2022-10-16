n = int(input())
a, b = 1, 1
while a*b < n:
    a, b = b, a+b
if a*b == n:
    print(True, a, b)
else:
    print(False)