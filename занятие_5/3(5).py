n = int(input('Введите N:'))
def f(n):
    a = 2
    b = 1
    while a <= n:
        a *= 2
        b += 1
    return('Показатель: {b - 1}, Степень: {a // 2}')
print(f(n))
