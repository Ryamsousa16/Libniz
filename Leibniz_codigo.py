def calcular_determinante_leibniz(m):

    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det4x4 = 0
    for col in range(len(m)):
        matriz2x2 = [row[0:col] + row[col + 1:] for row in m[1:]]
        cofator = (-1) ** col * m[0][col]

        det2x2 = calcular_determinante_leibniz(matriz2x2)
        det4x4 += cofator * det2x2

    return det4x4


matriz = [[1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3],
          [4, 4, 4, 4]]

matriz1 = [[1, 0, 1, 2],
           [3, 2, 1, 1],
           [1, 2, 2, 1],
           [1, 1, 1, 3]]

d = calcular_determinante_leibniz(matriz)
d1 = calcular_determinante_leibniz(matriz1)
print("Determinante da matriz um:  ", d)
print("Determinante da matriz dois:", d1)
