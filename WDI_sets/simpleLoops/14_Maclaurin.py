# Zadanie 14. Prosze napisac program obliczajacy wartosci cos(x) z rozwiniecia w szereg Maclaurina.

import math

x = math.pi/6
divisor = 1
result = 0
for i in range(2, 11, 2):
    result += divisor
    divisor = divisor * (-1) * 1/i * 1/(i-1) * x * x
print(result)