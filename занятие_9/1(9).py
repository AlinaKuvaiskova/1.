#вариант 13
def smallest(matrix):
    smallest_elements = []
    
    for i in range(len(matrix)):
        if i % 2 == 1:  
            smallest_element = min(matrix[i])  
            smallest_elements.append(smallest_element)  
            
    return smallest_elements


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

result =smallest(A)
print(result)
