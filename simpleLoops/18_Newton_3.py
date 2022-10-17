eps = 1/1000000
n = 50
y, x = 1, 0
while abs(x-y) > eps:
    x = y
    y = (n/(x*x) + 2*x)/3
print(x)