n = int(input("Введите количество чисел n: "))
k = int(input("Введите порядковый номер k: "))
p = 0
c = 1
sum_fib = 0
for i in range(k):
    p, c = c, p + c

for i in range(n):
    sum_fib += c
    p, c = c, p + c

print(f"Сумма {n} чисел ряда Фибоначчи, начиная с {k}-го, равна {sum_fib}")
