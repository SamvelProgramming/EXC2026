def matrix_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        return -1
    result = []
    for i in matrix:
        total = 0
        for j in range(len(vector)):
            total += i[j] * vector[j]
        result.append(total)

    return result
matrix = [[1, 2],
          [2, 3],
          [4, 5]]
vector = [2, 4]

print(matrix_vector(matrix, vector))