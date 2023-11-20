def f():
    i = 1
    x = 1
    y = 1
    a = []
    while i != 0:
        i = int(input('Введите число последовательности: '))
        a.append(i)
    for n in range(1, len(a)):
        if a[n] == a[n - 1]:
            x += 1
        else:
            x = 1
        if x > y:
            y = x
    return y
print(f())
