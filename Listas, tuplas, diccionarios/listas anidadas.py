
figuras = [["Cuadrado", 6, [3, 1]], ["Triangulo", 8, [2, 2]],
           ["Circulos", 5, [1, 2]], ["Rectangulo", 3, [4, 3]]]

figuras[0][1] = 5

print(figuras)

figuras[0][2] = [1, 3]

print(figuras)

figuras[0][2][1] = 9
print(figuras)

for f in figuras:
    print(f"{f[0]} - Cantidad: {f[1]} - Columna: {f[2][0]} - Fila: {f[2][1]}")


# Recorrer listas porr indices:

datos = [
    [1, 2, 3, 4],
    ["a", "b", "c", "d"],
    [5, 6, 7, 8],
    ["e", "f", "g", "h"],
    [9, 10, 11, 12],
    ["i", "j", "k", "l"]
]

for i in range(len(datos)):
    for j in range(len(datos[i])):
        print(datos[i][j], end=" ")

    print()

# Imprimir solo letras:

for i in range(len(datos)):
    if i % 2 != 0:
        for j in range(len(datos[i])):
            print(datos[i][j], end=" ")

    print()


lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = ["x", "y", "z"]

for num in lista1:
    for let in lista2:
        if lista1.index(num) == lista2.index(let):
            print(f"{num}{let}")
