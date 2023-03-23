# Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

tab = [2, 1, 3, 5, 3, 1, 10, 8]
n = len(tab)

max_length = 0
for i in range(n):
    for j in range(i + 1, n):
        flag = True
        length = 0
        for k in range(j - i + 1):
            if tab[i + k] != tab[j - k] or tab[i+k] % 2 == 0:
                flag = False
                break
            length += 1
        if flag:
            max_length = max(max_length, length)
print(max_length)