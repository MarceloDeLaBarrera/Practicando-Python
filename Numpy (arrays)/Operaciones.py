import numpy as np


array_one_dimension = np.array([1, 2, 3])
array = np.array([3, 4, 5])
array_2d = np.array([(2, 4, 6), (3, 5, 7), (5, 4, 2)])
array_2d_2 = np.array([(3, 5, 7), (4, 2, 1), (7, 8, 1)])

# Suma/multiplicacion/division/resta de arrays, deben tener la misma cantidad de valores,es decir, ser del mismo tamaño.
print(array_one_dimension / array)
array *= 3
print(array)
print(array_2d+array_2d_2)

# Producto punto
print(array_2d.dot(array_2d_2))
#print(np.dot(array_2d, array_2d_2))

# Suma por columnas de una matriz
print(array_2d)
print(array_2d.sum(axis=0))

# Suma por filas
print(array_2d.sum(axis=1))

# Maximo, minimo, suma de un array.
print(array.max())
print(array.min())
print(array.sum())

# Maximo, minimo de una fila o columna
array_2d.min(axis=1)
array_2d.max(axis=0)

# Raiz cuadrada
cuadrada = np.sqrt(array_one_dimension)
print(cuadrada)
