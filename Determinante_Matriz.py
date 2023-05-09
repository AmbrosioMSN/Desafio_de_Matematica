def pegarMenor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinante(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)): 
            menor = pegarMenor(matrix, 0, i)
            cofactor = (-1) ** (i % 2) * determinante(menor)
            det += matrix[0][i] * cofactor
        return det

A = [[0, 0, 1, 2], [0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]   # Codigo do exemplo 2.1
B = [[1, 3, 2, 0], [3, 1, 0, 2], [2, 3, 0, 1], [0, 2, 1, 3]]   # Codigo do exemplo 2.2
detA = determinante(A)
detB = determinante(B)

print(f"Resultado da Matriz de det(A) == 0 : {detA}")
print(f"Resultado da Matriz de det(A) != 0 : {detB}")
