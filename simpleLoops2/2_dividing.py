a = 12
b = 17
n = 90
if a > b:
    print(a//b, end="")
else:
    print("0", end="")
print(",", end="")
number = a%b
while n > 0:
    number *= 10
    print(number//b, end="")
    number %= b
    n -= 1
