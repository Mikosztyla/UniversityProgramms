# Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać
# funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne
# (LG) o długości większej niż 2. Funkcja powinna
# zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.


T = [1, 2, 3, 4, 8, 4, 2, 1]
r = T[1]-T[0]
q = T[1]/T[0]
la = 1
lg = 1
max_la = max_lg = 1
for i in range(1, len(T)):
    if T[i] - T[i-1] == r or T[i] / T[i-1] == q:
        if T[i] - T[i-1] == r:
            la += 1
        if T[i] / T[i-1] == q:
            lg += 1
    else:
        max_la = max(la, max_la)
        max_lg = max(lg, max_lg)
        la = lq = 1
    r = T[i] - T[i-1]
    q = T[i] / T[i-1]

max_la = max(la, max_la)
max_lg = max(lg, max_lg)

print(max_la, max_lg)
