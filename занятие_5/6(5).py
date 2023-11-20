def f():
    i = 1
    n = 0
    a = []
    while i != 0:
        i = int(input('Введите число последовательности: '))
        n += 1
        a.append(i)
    return (sum(a)/(n-1))
print(f())
