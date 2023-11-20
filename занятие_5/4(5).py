x = int(input('Введите X: '))
y = int(input('Введите Y: '))

def f(x):
    percent = (x / 100)*10
    x += percent
    return x

def d(x, y):
    d = 0
    while x <= y:
        x = fx(x)
        d += 1
    return d

print(d(x,y))
