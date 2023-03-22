# Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
# wartości prawdopodobieństwa dla N z zakresu 20-40.

for i in range(20, 55):
    comb = i * (i - 1) / 2
    r_prob = pow(364/365, comb)
    prob = 1 - r_prob
    print(f"Prawdopodobienstwo na to, że 2 osoby z {i} urodziły sie w tym samym dniu wynosi: {prob}%")