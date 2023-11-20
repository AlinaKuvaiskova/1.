def f():
    n = 0
    while n < 2:
        n = int(input('Введите N, не меньшее 2: '))
        if n >= 2:
            break
        else:
            print('Число должно быть не меньше 2')
    return n


def k():
    n = f()
    for i in range(2, n + 1):
        if n % i == 0:
            return i

print(k())
