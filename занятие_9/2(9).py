#вариант 13
def swap(matrix):
    min_value = matrix[0][0]
    min_index = (0, 0)
    max_value = matrix[0][0]
    max_index = (0, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)
    
    
    matrix[min_index[0]][min_index[1]], matrix[max_index[0]][max_index[1]] = matrix[max_index[0]][max_index[1]], matrix[min_index[0]][min_index[1]]
    
    return matrix
