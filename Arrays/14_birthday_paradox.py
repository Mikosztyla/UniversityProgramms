
for i in range(20, 55):
    comb = i * (i - 1) / 2
    r_prob = pow(364/365, comb)
    prob = 1 - r_prob
    print(f"Prawdopodobienstwo na to, że 2 osoby z {i} urodziły sie w tym samym dniu wynosi: {prob}%")