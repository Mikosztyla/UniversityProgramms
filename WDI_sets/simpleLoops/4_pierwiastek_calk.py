# Zadanie 4. Prosze napisac program obliczajacy pierwiastek całkowitoliczbowy z liczby naturalnej korzystajac
# z zaleznosci 1 + 3 + 5 + ... = n2.

n = 145
suma = 0
i = 0
while suma <= n:
    suma += 2*i + 1
    i += 1
print(i-1)