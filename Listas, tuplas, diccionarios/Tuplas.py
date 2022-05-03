# Las tuplas son como las listas pero, no se pueden añadir, remover, etc.
# Su ventaja es que son mas rapidas, y pueden utilizarse como claves en diccionario, con listas no.

# Sintaxis... (Similar a tupla pero con parentesis, tambien se puede declarar sin)
mitupla = ("Juan", 1, "Pedro", 3)
Mitupla = "JAJA", 1, 2, 3, 4, True

# Imprimir un elemento de posicion 2, imprimir toda la tupla,
print(mitupla[2])
print(mitupla)

# Convertir tupla en lista. Se confirma la conversion al fijarse en corchete/parentesis
milista = list(mitupla)
print(milista)

# Convertir lista en tupla.
mitupla2 = tuple(milista)
print(mitupla2)

# Meter dos tuplas dentro de una lista
nuevalista = [mitupla, Mitupla]
print(nuevalista)

# Metodo "in" para ver si elemento esta en tupla... Tambien se puede usar metodo count, y ver el largo con len, o index para ver si un elemento esta dentro de la tupla y en que posicion.
print("Juan" in mitupla2)
print(len(mitupla2))

# Desempaquetar tupla en variables.

Tuplaempacada = ("Marcelo", 28, "Independencia", "Chile")
nombre, edad, comuna, pais = Tuplaempacada
print(nombre, edad, comuna, pais)
