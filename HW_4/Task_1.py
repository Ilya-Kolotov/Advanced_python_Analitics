"""
Напишите функцию для транспонирования матрицы
"""

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    return new_matrix


def trans_matrix_zip(matrix: list):
    return list(zip(*matrix))

matrix = [[99, 72, 11, 93], [24, 36, 33, 60], [97, 81, 91, 39], [97, 43, 75, 85], [29, 56, 33, 68]]
for i in matrix:
    print(i)
transposed_matrix = transpose_matrix(matrix)
print('===========')
for i in transposed_matrix:
    print(i)
transposed_matrix = trans_matrix_zip(matrix)
print('===========')
for i in transposed_matrix:
    print(i)