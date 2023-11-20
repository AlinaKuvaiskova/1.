#вариант 8
def replace_zeros_with_average(numbers):
    average = sum(numbers) / len(numbers)
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = average
        return numbers

my_numbers = [1, 0, 5, 0, 12, 83, 0]
result = replace_zeros_with_average(my_numbers)
print(result)
