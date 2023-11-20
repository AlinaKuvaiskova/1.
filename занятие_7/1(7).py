#8 вариант
def calculate_operations(numbers):
    print('Числа:', numbers)
    print('Сумма всех чисел:', sum(numbers))
    
    result = 1
    for i in numbers:
        result *= i
        
    print('Произведение всех чисел:', result)

a = [1, 5, 12, 83]
calculate_operations(a)
