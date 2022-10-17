mult = 1
result = 1
for i in range(1, 12):
    mult *= i
    result += 1/mult

print(result)