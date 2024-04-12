max_element = 0

while True:
    n = float(input())

    if n > -1:
        if n > max_element:
            max_element = n

    else:
        if n != -1:
            print('wrong result')
            break
        print(int(max_element))
        break
