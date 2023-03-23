# Zadanie 19. Prosze napisac program wyznaczajacy wartosc liczby e korzystajac z zaleznosci: e = 1/0! +
# 1/1! + 1/2! + 1/3! + ...

mult = 1
result = 1
for i in range(1, 12):
    mult *= i
    result += 1/mult

print(result)