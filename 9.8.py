k = int(input())

for n in range(2, k+1):
    a = 1
    for i in range(2, n):
        if n % i == 0:
            a = False
            break
    if a == 1:
        print(n)
