max_element = 0
count = 0

while True:
    n = float(input())

    if n > -1:
        count += 1

        if n > max_element:
            max_element = n

    else:
        if n != -1:
            print('wrong result')
            break
        print(f'Максимальный результат: {int(max_element)}')
        print(f'Кол-во друзей: {count}')
        break
