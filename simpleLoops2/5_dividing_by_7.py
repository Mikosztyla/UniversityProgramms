def get_masks(n):
    for i in range(0, n):
        bitMasks[i] = convert_int(i)


def convert_int(x):
    mask = ''
    while x > 0:
        if x % 2 == 0:
            x //= 2
            mask += '0'
        else:
            x = (x-1)//2
            mask += '1'
    while len(mask) < numberOfDigits:
        mask += '0'
    return mask


def get_numbers():
    iterator = numberOfDigits-1
    digits = [0 for i in range(0, numberOfDigits)]
    x = n
    while x > 0:
        digits[iterator] = x % 10
        x //= 10
        iterator -= 1
    iterator = 0
    for i in bitMasks:
        x = n
        number = 0
        d_iterator = 0

        for j in i:
            if j == '1':
                number = number * 10 + digits[d_iterator]
            d_iterator += 1
        numbers[iterator] = number
        iterator += 1


n = int(input("Podaj liczbę: "))

numberOfDigits = 0
x = n

while x > 0:
    x //= 10
    numberOfDigits += 1

cases = pow(2, numberOfDigits)
bitMasks = ['' for i in range(0, cases)]
numbers = pow(2, numberOfDigits)
numbers = [0 for i in range(0, cases)]

get_masks(cases)
get_numbers()
for i in numbers:
    if i % 7 == 0 and i != 0:
        print(i)