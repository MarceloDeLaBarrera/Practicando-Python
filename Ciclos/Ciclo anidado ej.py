# producto cartesiano entre dos listas
lista1 = [2, 3, 4]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = []

for i in lista1:
    for j in lista2:
        lista3.append(i*j)
print(lista3)

lista4 = []
for i in range(1, 6):
    for j in range(1, 6):
        lista4.append((i, j))

print(lista4)

# Lista por compresion:
lista_cartesiana = [(i, j) for i in range(1, 6) for j in range(1, 6)]
print(lista_cartesiana)
