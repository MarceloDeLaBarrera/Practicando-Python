# Definir una lista con 5 float. Mostrar en pantalla solamente valores superiores a 7

Lista = [2, 3, 4, 5, 6, 7, 8, 9, 55, 6, 7, 444, 65, 7, 788]

for i in Lista:
    if i > 7:
        print(i, end=" ")

print("\n")

Lista2 = []
for i in Lista:
    if i > 7:
        Lista2.append(i)

print(Lista2)

k = 0
while k < len(Lista):
    if Lista[k] > 7:
        print(Lista[k], end=" ")
    k += 1

print("\n")

listanombres = ["mama", "papa", "perro", "gato", "chupala", "pepe", "rojo"]
count = 0

for palabra in listanombres:
    if len(palabra) == 4:
        count += 1
print(f"La cantidad de nombres que tienen 4 letras son: {count}")

i = 0
cuenta = 0
while i < len(listanombres):
    if len(listanombres[i]) == 4:
        cuenta += 1
    i += 1
print(f"La cantidad de nombres que tienen 4 letras son: {cuenta}")


# Recorrer lista por indices.
l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in range(len(l1)):
    for j in range(len(l2)):
        if i == j:
            print(l1[i]+l2[j])


# 123
# 456
# 789

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr[1][1])
