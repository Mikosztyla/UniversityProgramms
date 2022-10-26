# 0 1 1 5
# 2 2 4 6

a1 = 0
a2 = 1
b1 = 2
b2 = 2
for i in range(0, 10):
    a_temp = a2 - b2 * a1
    b_temp = b2 + 2 * a2
    print(a_temp, b_temp)
    a1, a2 = a2, a_temp
    b1, b2 = b2, b_temp