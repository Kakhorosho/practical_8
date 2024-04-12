k = int(input())

for n in range(2, k+1):
    d = 0
    number = n - 1

    while number > 0:
        b = n - number
        number -= 1
        if n % b == 0:
            d += b
    if d == n:
        print(d)
