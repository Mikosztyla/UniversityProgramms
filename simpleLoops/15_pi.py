import math

p = 1
result = math.sqrt(0.5)
temp = result
for i in range(1, 500):
    temp *= 0.5
    temp += 0.5
    temp = math.sqrt(temp)
    result *= temp
p = 2/result
print(p)
