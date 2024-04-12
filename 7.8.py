while True:
    n = input()

    if n.isdigit():
        print(f'Введено целое число: {n}')
        break
    else:
        print('Ошибка. Попробуйте eщё раз. Введите число:')
