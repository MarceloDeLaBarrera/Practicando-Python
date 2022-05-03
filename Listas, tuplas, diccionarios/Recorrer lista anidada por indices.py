import math

# Recorrer una lista anidada por sus indices.
datos = [[1, 2, 3, 4],
         ["a", "b", "c", "d"],
         [5, 6, 7, 8],
         ["e", "f", "g", "h"],
         [9, 10, 11, 12],
         ["i", "j", "k", "l"]]

for i in range(len(datos)):
    for j in range(len(datos[i])):
        print(datos[i][j], end="-")
print("\n")


# Ej: Calcular resta de la suma de diagonales. Solo funciona con igualdad de filas y columnas


def diagonalDifference(arr):
    a = 0
    b = 0
    c = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                a += arr[i][j]

            if i == len(arr)-j-1:
                b += arr[i][j]

    c = int(math.fabs(a-b))
    return c


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(diagonalDifference(arr))
