
def get_reverse(n):
    x = 0
    while n > 0:
        x = x * 10 + n % 10
        n //= 10
    return x


for i in range(1, 200): # 196 nie działa!!!!
    x = i
    while x != get_reverse(x):
        x = x + get_reverse(x)
print("uff")