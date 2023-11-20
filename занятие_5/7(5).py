def f():
    i = 1
    n = 0
    a = []
    while i != 0:
        i = int(input('Введите число последовательности: '))
        a.append(i)
    for x in range(1, len(a)):
        if a[x] > a[x -1]:
            n += 1
    return n
print(f())
