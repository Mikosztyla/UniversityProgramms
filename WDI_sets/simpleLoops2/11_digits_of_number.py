# Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# jej cyfry stanowią ciąg rosnący.

n = int(input("Podaj liczbę: "))
is_seq_dec = True
last = 10
while is_seq_dec and n > 0:
    x = n % 10
    if x > last:
        is_seq_dec = False
    last = x
    n //= 10
print(is_seq_dec)