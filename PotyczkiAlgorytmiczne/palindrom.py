# aaaababaabb 9
# aaaab
#      a
# bbaab
# 0 1 2 3 4 5 6 7 8 9 10
# b b b a b a b a b b a
# a b b a b b b a b b a
# b b b a a b a a b b b

#slowo = input()


def palindrom(slowo, n, letter, take_additional):
    counter = 0
    temp = []
    result = 0
    for i in range(len(slowo)):
        if slowo[i] == letter:
            if counter < n:
                temp.append(i)
                counter += 1
            else:
                if counter == n and take_additional:
                    temp.append(len(slowo)//2)
                    counter += 1
                result += abs(len(slowo) - 1 - i - temp[-1])
                temp = temp[:-1]
    print(result)


slowo = "bbbabababba"
ilosc_a = 0
for s in slowo:
    if s == 'a':
        ilosc_a += 1
ilosc_b = len(slowo)-ilosc_a
l = len(slowo)-1
take_a = True
how_many_to_take = 0
if ilosc_a % 2 == 1 and ilosc_b % 2 == 1:
    if ilosc_a == 1 or ilosc_b == 1 or ilosc_a == ilosc_b:
        print(-1)
    else:
        palindrom(slowo, ilosc_a // 2, 'a', False)
else:
    if ilosc_a % 2 == 0 and ilosc_b % 2 == 1:
        palindrom(slowo, ilosc_b // 2, 'b', True)
    elif ilosc_a % 2 == 1 and ilosc_b % 2 == 0:
        palindrom(slowo, ilosc_a // 2, 'a', True)
    else:
        palindrom(slowo, ilosc_a // 2, 'a', False)

