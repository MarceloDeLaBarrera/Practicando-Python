"""Colecciones - Ejercicio 1: 
Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos, por último mostrar la lista."""

# Solucion, convertir a conjunto, ya que no permiten repetidos. Para tratar conjuntos se usa el metodo "SET"
Lista1 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7]
Lista2 = set(Lista1)
print(Lista2)

"""Colecciones - Ejercicio 2: 
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas."""

# Se convierte a conjuntos y se opera con union, interseccion, etc

lista3 = [1, 1, 1, 2, 3, 4, 5, 6, 6, 7]
lista4 = [1, 2, 3, 4, 55, 6, 6, 7, 8, 8888]
lista5 = set(lista3)
lista6 = set(lista4)

print(lista5 | lista6)
print(lista5.union(lista6))
print(lista5-lista6)
print(lista5.difference(lista6))
print(lista6-lista5)
print(lista6.difference(lista5))
print(lista5 & lista6)
print(lista5.intersection(lista6))

# print(lista5.union(lista6))

sett = {1, 2, 9, 1, 2, 3, 1, 4, 1, 5, 7}
lista = list(sett)

print(lista)
