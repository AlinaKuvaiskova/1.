n = int(input())
par_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    part_sum += part_factorial
print(part_sum)
