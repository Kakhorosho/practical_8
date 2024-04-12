count = 0
money = 0

while True:
    n = float(input())

    if n > 0:
        count += 1
        money += n

    else:
        if n != 0:
            print('wrong income')
            break
        print(f'Средний заработок: {round((money / count), 2)}')
        break
