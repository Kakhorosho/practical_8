n = int(input())

for i in range(1, n+2):
    d = 0
    k = 0
    f = i
    while i > 0 and n >= k:
        d += i * 10 ** k
        i -= 1
        k += 1
    print(f'{d} * {n} + {f} = {d * n + f}')
