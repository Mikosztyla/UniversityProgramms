# Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem
# stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

result = int(input())
count = 1
while True:
    n = int(input())
    if n == 0:
        break

    if count >= 10:
        if n > result:
            result = n
    else:
        if n < result:
            result = n
        count += 1

print(result)

