# Permite usar libreria coleccions, y se importa la clase counter.
from collections import Counter

# Lista de numeros
numeros = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6,
           6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 10, 10]

# Diccionario vacio donde se almacenaran como clave el numero, y como valor su frecuencia.
frecuencia = {}

# Para n en numeros, si n está en diccionario, al valor de la clave se sumará 1, si no, se iniciara el valor de la clave en 1.
for n in numeros:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

print(frecuencia)


def Mayor(diccionario):

    maximo = 0
    for i in diccionario:
        if diccionario[i] > maximo:
            maximo = diccionario[i]
            p = i

    return p, maximo

# Encontrar mayor de una lista:


"""
listofdogs = []
for dog in self.dogs:
    listofdogs.append(dog["breed"])

higher = max(listofdogs, key=listofdogs.count)
print(higher)
"""


def larga(lista):
    palabralarga = ""
    largo = 0
    for p in lista:
        if len(p) > len(palabralarga):
            palabralarga = p
            largo = len(palabralarga)

    return palabralarga, largo


print(Mayor(frecuencia))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Otra forma:

# Se crea un objeto llamando "contador" a partir de la clase Counter con parametro numeros
contador = Counter(numeros)
print(contador)
# Most common es un metodo de la clase Counter. Devuelve los valores mas comunes, en forma de tuplas dentro de una lista. Ej: Si el valor es 3, devuelve los 3 valores mas comunes.
print(contador.most_common(1))


frase = "Mi mama me mi mama y python se la come atrevesada"
print(Counter(frase).most_common(2))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quitar letras de un string.
texto = "Hola, me gusta comer pizza todos los dias. Se dice que: 1 + 1 es igual a 20. A mi mama le encanta, eso. ella tambien. si. Hola. Hola. me Me me Me me hola todos todos"

quitar = ",;:.\n!\"'"

# Para caracter en quitar, texto va a ser igual a texto.remplazar el caracter por vacio.
for caracter in quitar:
    texto = texto.replace(caracter, "")

texto = texto.lower()

# Esto, separa el texto con split y almacena cada separacion en una lista "palabra".
palabras = texto.split(" ")
print(palabras)

# Se crea diccionario vacio para almacenar frecuencia de palabras en la lista.
diccionario_frecuencia_palabras = {}
diccionario_frecuencia_letras = {}

palabras = ["mama", "perro", "mama", "mama", "perro", "perro", "mama"]

for palabra in palabras:
    if palabra in diccionario_frecuencia_palabras:
        diccionario_frecuencia_palabras[palabra] += 1
    else:
        diccionario_frecuencia_palabras[palabra] = 1

print(diccionario_frecuencia_palabras)

""" otra forma seria:
for palabra in palabras:
    diccionario_frecuencia_palabras.setdefault[palabra,0]
    diccionario_frecuencia_palabras[palabra] += 1

En este caso, setdefault lo que hace, es añadir la palabra al diccionario si es que no esta, con valor de 0. Si ya esta, no hace nada. Luego, guarda con valor de uno si es primera vez
que se almacena en diccionario, si se repeti, le vuelve a sumar +1, y asi sucesivamente    
"""

for palabra in palabras:
    for letras in palabra:
        if letras in diccionario_frecuencia_letras:
            diccionario_frecuencia_letras[letras] += 1
        else:
            diccionario_frecuencia_letras[letras] = 1

print(larga(palabras))
print(Mayor(diccionario_frecuencia_palabras))
print(Counter(palabras).most_common(3))
print(diccionario_frecuencia_palabras)
print(diccionario_frecuencia_letras)

ordenado = sorted(diccionario_frecuencia_palabras.items(),
                  key=lambda item: item[1])

print("\n")
print(ordenado)

# Imprimir segundo elemento que mas se repite
print(ordenado[-2])

# Encontrar elemento repetidos dentro de una lista.
numerosss = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 7, 8]
repetidos = []
archivo = []
repetidoss = []

for n in range(len(numerosss)):
    for r in range(len(numerosss)):
        if n != r:
            if numerosss[n] == numerosss[r] and numerosss[n] not in repetidos:
                repetidos.append(numerosss[n])

print(repetidos)

for n in numerosss:
    if n not in archivo:
        archivo.append(n)
    else:
        if n not in repetidoss:
            repetidoss.append(n)

print(repetidoss)
