k = int(input("Podaj liczbę k: "))
# y=1/x
x = 1
d = 0.0001
result = 0
while x < k:
    x += d
    temp_y = 1/x
    result += temp_y * d

print(result)