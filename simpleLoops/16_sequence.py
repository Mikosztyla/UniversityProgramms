max_steps = 0
max_a = 0
for i in range(2, 10000):
    a = i
    steps = 0
    while a != 1:
        if a % 2 == 0:
            a = a//2
        else:
            a = 3*a + 1
        steps += 1
    if steps > max_steps:
        max_a = i
        max_steps = steps

print(max_a, max_steps)