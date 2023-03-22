# Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje

tab = [10, 20, 1, 345, 0, 9, 6, 1, 13]
n = len(tab)

result = 0
for i in range(n):
    suma = tab[i]
    sum_iter = i
    if suma == sum_iter:
        result = max(result, 1)
    for j in range(i+1, n):
        sum_iter += j
        suma += tab[j]
        if suma == sum_iter:
            result = max(result, j-i+1)

print(result)