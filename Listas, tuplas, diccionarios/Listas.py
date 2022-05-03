

# Las listas son el equivalente a los array de otros lenguajes, pero, pueden guardar diferentes tipos de valores.

# Sintaxis
nombres = ["Marcelo", "Juan", "Pepe"]
Apellidos = ["Ramirez", "Pereira", "Bonaparte"]

nombrelista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9]
#               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
#            -13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(f"Elemento final de {nombrelista2[8]}")

# Formas de filtrar elementos de una lista.

# Imprime toda la lista
print(f"Los nombres almacenados son: {nombres[:]}")

# imprime todos menos los 3 primeros
print(f"Elemento {nombrelista2[3:]}")

# Imprime los 3 primeros
print(f"Elemento {nombrelista2[:3]}")

# Imprime desde el elemento 3 al 5. Incluye 3, excluye 6.
print(f"Elemento  {nombrelista2[3:6]}")

# Imprime el quinto elemento contando a partir de 1 desde el final hacia el inicio.
print(f"Elemento  {nombrelista2[-5]}")

# Imprime elemento 5 desde el inicio partiendo de 0.
print(f"Elemento  {nombrelista2[5]}")

# Imprime el ultimo elemento
print(f"Elemento  {nombrelista2[-1]}")

nombrelista2.append(10)  # append agrega elemento a lista.
print(nombrelista2)

# Permite insertar elemento segun una posicion especificada. En este caso, inserta Jose en la posicion 1.
nombres.insert(1, "Jose")
print(nombres[:])

# Agregar varios elementos
nombrelista2.extend([11, 12, 13, 14, 15])
print(nombrelista2)

# Saber indice de un elemento en particular.
print(nombres.index("Pepe"))

# Funcion "in" permite ver si elemento esta en la lista, es decir, pertenece a ella... devolviendo un True o un False que lo confirme.
print("Josse" in nombres)

# Eliminar elemento con remove, indicando el valor del elemento
nombrelista2.remove(15)
print(nombrelista2)

# Con "pop" se elimina el ultimo, aunque tambien se le puede pasar el indice del elemento a eliminar.
nombrelista2.pop()
print(nombrelista2)

# Invertir orden de una lista (al reves)... Tambien funciona con strings.
nombrelista2 = nombrelista2[::-1]

# Invertir lista con reverse
nombrelista2.reverse()
print(nombrelista2)


# Suma de Listas
nombreapellido = nombres+Apellidos
print(nombreapellido)

# Almacenar dos listas dentro de 1.
a1 = [1, 2, 3, 4, 5]
a2 = [1, 3, 45, 5, 3]
a3 = [a1, a2]
print(a3)

# Sumar elementos de una lista
print(sum(nombrelista2))

# Sumar un valor a todos los elementos de una lista.
nombrelista3 = []
for i in nombrelista2:
    nombrelista3.append(i+5)
print(nombrelista3)

# Rellenar una nueva lista con los elementos de otra lista
nuevalistaparallenar = []
for i in nombrelista2:
    nuevalistaparallenar.append(i)
print(nuevalistaparallenar)

# Llenar una lista segun condicion
nombrelista4 = []
for i in nombrelista2:
    if i < 5:
        nombrelista4.append(i)
print(nombrelista4)

# Eliminar elementos de una lista... Ya que las listas son mutables, si se borra un elemento, cambia el largo de la lista, y el bucle for se salta al elemento siguiente al borrado
# Por lo cual, si 2 o mas elementos seguidos cumplen la condicion de borrado, se borrará uno si y uno no, a menos que se haga una copia de la lista, y se itere la copia ya que la copia mantiene la extension original.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 50, 32, 1, 2, 3, 4, 4, 4]
copiadenumeros = list(numeros)
for i in copiadenumeros:
    if i < 5:
        numeros.remove(i)
print(numeros)

# Eliminar elementos repetidos de una lista.
listavacia = []
for i in copiadenumeros:
    if i not in listavacia:
        listavacia.append(i)
print(listavacia)


# Multiplicar el elemento de una lista
print(nombrelista2[10]*10)

# Con "len" Muestra largo de la lista, cantidad de elementos.
print(len(nombreapellido))

# Contar cuantos elementos repetidos hay en la lista con "count"
listarepetida = [7, 7, 7, 6, 5, 4]
print(listarepetida.count(7))

# listarepetida.clear()  # Borra todos los elementos.

# Crear una lista a partir de un rango de numeros. Range incluye primer valor y excluye el ultimo. de 1 a 100 = 1,101.
# Crear una lista con metodo list.
Listarango = list((range(1, 101)))
print(Listarango)

# Ordenar los elementos de una lista de menor a mayor con "sort"
listarepetida.sort()
print(listarepetida)

for i in range(len(nombrelista2)):
    # Imprime de 1 hasta 3, de 1 hasta 2, de 1 hasta 3, etc.
    print(nombrelista2[0:i+1])

for i in range(len(nombrelista2)):
    # Imprime de a 3 valores, ejemplo primera vuelta: 1 hasta 3... Segunda vuelta: 2 hasta 4. (Recordar que el ultimo elemento se excluye al usar ej: 0:3 , 1:4, etc.)
    print(nombrelista2[i:i+3])
