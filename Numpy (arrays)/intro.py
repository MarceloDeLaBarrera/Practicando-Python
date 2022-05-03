import numpy as np

"""Para trabajar con vectores/arreglos y matrices"""

# Array de una dimension
array_one_dimension = np.array([1, 2, 3])
print(array_one_dimension)

# Introducir una lista dentro de un array.
lista = [4, 5, 6]
array = np.array(lista)
print(array)

# Array de 2 dimensiones o  Matriz
array_2d = np.array([(2, 4, 6), (3, 5, 7), (5, 4, 2)])
print(array_2d)

array_2d_2 = np.array([(3, 5, 7), (4, 2, 1), (7, 8, 1)])


# Arreglos llenos de zero.
array_zero = np.zeros(8)
print(array_zero)

# Array con numeros random
array_random = np.random.rand(5)
print(array_random)

# Matriz llena de zeros.
matriz_zeros = np.zeros((4, 5))
print(matriz_zeros)

# Matrices de unos.
matriz_unos = np.ones((4, 5))
print(matriz_unos)

# Cambir el tipo de dato
matriz_unos = np.ones((4, 5), dtype=np.int16)
print(matriz_unos)

# Array vacio, Matriz vacia.
array_empty = np.empty(5)
print(array_empty)

matriz_empty = np.empty((2, 2))
print(matriz_empty)

# Matriz identidad y cuadrada con 0 y diagonal 1.
matriz = np.eye(3)
print(matriz)

# Matriz transpuesta
matriz.T

# Copiar un array
copy = array.copy()

# Arreglo dentro de un rango, con inicio y final, y saltos. Al igual que las listas, no considera al ultimo valor, por lo que si quiero llegar hasta 20, hay que poner 21.
array = np.arange(2, 20, 2)
array2 = np.arange(0, 11, 2.5)
array3 = np.arange(8)
print(array, array2, array3)

# Convertir array de una dimension a 2 dimensiones. La cantidad de elementos debe coincidir con la cantidad de filas y columnas dadas.
array3 = array3.reshape(4, 2)
print(array3)

# Crear matriz de uno o de ceros, ajustandose al tamaño de otra matriz.
matriz_unos = np.ones_like(array3)
matriz_zeros = np.zeros_like(array3)
matriz_empty = np.empty_like(array3)
print(matriz_unos)

# Acceder al elemento de un array
print(array[2])
print(array[-1])
print(array[2:7])

estudiantes = np.array([["Pedro", "Juan", "Diego"], [1, 2, 3], [4, 5, 6]])
print(estudiantes[0])  # Primera fila
print(estudiantes[0, 1])  # Primera fila, solo columna 1.
print(estudiantes[:, 1])  # Todas las filas, pero solo columna 1.
print(estudiantes[0:3, 1:3])  # Fila 0,1 y 2, pero columnas 1 y 2.
