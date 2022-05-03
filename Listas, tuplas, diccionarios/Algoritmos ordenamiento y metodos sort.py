# Ordenar diccionario

diccionario = {"pepe": 4, "Jaime": 2, "Jose": 6, "Karmen": 10, "Korrea": 15}

Ordenado = sorted(diccionario.items(), key=lambda item: item[1])
print(Ordenado)

Ordenado2 = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)
print(Ordenado2)


lista = [2, 4, 5, 3, 4, 6, 7, 8, 10, 1, 24, 100, -9, -15, -21, -2]
Ordenado3 = sorted(lista)  # para reversar= sorted(lista, reverse=True)
print(Ordenado3)
Ordenado3.reverse()
print(Ordenado3)

# Ordernar lista de tuplas
datosss = [(1, 2, 15), (5, 4, 20), (8, 4, 3)]
print(sorted(datosss, key=sum))

stringsss = ["A", "E", "o", "O", "u", "á", "ó", "ú", "U", "a", "i", "e", "I"]
print(sorted(stringsss))
print(sorted(stringsss, key=str.lower))

print(sorted(stringsss, key=lambda palabra: palabra.lower().replace(
    "á", "a").replace("ó", "o").replace("ú", "u")))

numeros = [10, 23, 20, 32, 30, 43, 40, 45, 50, 54, 60, 54, 70]
print(sorted(numeros, key=lambda n: n if n % 10 == 0 else n+101))
print(sorted(numeros, key=lambda n: n if n % 10 != 0 else n+101))

planetas = [{"Nombre": "Tierra", "Diametro": 1000}, {
    "Nombre": "Pepe", "Diametro": 3214}, {"Nombre": "dasdas", "Diametro": 501}]

print(sorted(planetas, key=lambda x: x["Diametro"]))

# Hallar el indice de la primera ocurrencia, del numero que es mayor.
masnumeros = [43, 27, 58, 12, 39, 58, 54, 32, 43, 33, 21, 58, 16, 46]
indicemayor = max(enumerate(masnumeros), key=lambda x: x[1])[0]
imayor = masnumeros.index(max(masnumeros))
print(indicemayor)
print(imayor)


# Metodo Ordenamiento por seleccion:
"""Se recorre en el primer ciclo hasta el largo menos 1, porque al comparar los valores en ambos ciclos, se compara el valor actual del primer ciclo con el valor siguiente.
Por ende, el ultimo numero del array no tiene un valor siguiente de comparación."""
array = [5, 7, 3, 4, 8, 99, 34, 56, 11, 1, 2]
aux = 0
for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[j] < array[i]:
            aux = array[j]
            array[j] = array[i]
            array[i] = aux

print(array)

# Metodo burbuja
"""Coloca el puntero sobre el primer y segundo elemento, y se van moviendo ambos punteros, comparando primer y segundo, segundo y tercero, y asi sucesivamente."""
array2 = [5, 7, 3, 4, 8, 99, 34, 56, 11, 1, 2]
aux = 0
for i in range(len(array2)-1):
    for j in range(len(array2)-1):
        if array2[j] > array2[j+1]:
            aux = array2[j]
            array2[j] = array2[j+1]
            array2[j+1] = aux

print(array2)

# Ordenamiento por Inserccion
"""
Compara al elemento con los elementos anteriores, donde con un ciclo while donde se cumpla la condicion, va remplazando valores de los elementos i-1, y disminuyendo i en 1,
para moverse hacia atras, hasta salir del while, y finalmente colocar en la posicion de i, el valor actual con el que haya iniciado la iteracion en el bucle for.
Luego pasa al siguiente elemento del bucle for, y empieza a comparar en el while, siempre y cuando se cumpla la condicion. Si no se cumple, el elemento mantiene su posicion. 
"""
lista = [5, 7, 1, 3, 8, 4, 9, 2, 6]
for i in range(1, len(lista)):
    actual = lista[i]

    while i > 0 and lista[i - 1] > actual:
        lista[i] = lista[i - 1]
        i -= 1

    lista[i] = actual

print(lista)


# Ordenamiento Quick sort

""" Se crea una funcion que particiona una lista en 3, retornando una lista con elementos menores a un pivote, el pivote, y una lista con los elementos mayores al pivote
Luego se crea la funcion para el quicksort, si la lista que se le pase como parametro tiene menos de 2 elementos, retorna la lista misma, si no, llama recursivamente a la funcion
particionado donde se almacenara en 3 variables lo que retorna particionado, y se retorna de forma recursiva para que se aplique el mismo procedimiento sobre la lista de menores y mayores sucesivamente
hasta que la lista tenga un largo menor a 2 """

lista2 = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7]


def particionado(lista):
    pivote = lista[0]
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores. append(lista[i])
    return menores, pivote, mayores


def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        menores, pivote, mayores = particionado(lista)
        return quicksort(menores) + [pivote] + quicksort(mayores)


print(quicksort(lista2))
