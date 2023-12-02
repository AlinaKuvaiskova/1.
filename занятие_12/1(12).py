def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        reverse(n // 10)

n = 123456789
reverse(n)

