import numpy as np
# Crear funcion de numeros pares entre 2 valores.


def pares(x, y):
    if x % 2 == 0:
        array = np.arange(x, y, 2)
    else:
        array = np.arange(x+1, y, 2)
    return array


lista = list(range(10, 20))
print(lista)
