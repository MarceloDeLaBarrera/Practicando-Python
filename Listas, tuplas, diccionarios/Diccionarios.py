# Sintaxis diccionarios.. Sigue un esquema donde se almacena una clave:valor.... No puede haber claves duplicadas.

Diccionario = {"Prompt": "Marca punto exacto donde introducir la instrucción python.",
               "Print()": "Muestra en la pantalla/consola el resultado de la instrucción, dentro de los parentesís suele llevar una instrucción.",
               ";": "Separa instrucciones en la misma linea",
               "#": "Abre comentarios",
               "Variable": "Espacio en la memoría del ordenador donde se almacena un valor que podrá cambiar la ejecución del programa.",
               "%": "El resto de una division",
               "//": "Nos da la division entera",
               "Type()": "Útil para averiguar que tipo de variable es.",
               "Saltar lineas": "Usa triple comilla",
               "=": "Valor de asignación",
               "==": "Valor de comparación",
               "def": "Declarar una función",
               ".Append": "Agrega un nuevo elemento al final de la lista",
               ".Insert": "Permite agregar un nuevo elemento en cañquier posición de la tabla",
               ".Extend": "Permite unir listas.",
               ".Index": "Permite saber en que parte de la lista se encuestra un elemeto pero solo el primero que se encuentre no varios",
               ".Remove": "sirve para eliminar elementos de la lista y se escribe antes de print.",
               ".Keys": "Muestra los valores del diccionario",
               ".Values": "Muestra los contenidos de los valores",
               "Input()": "El programa se detendra y esperara a que introduzcamos un valor por teclado",
               "Asignar valor": "Inserta algún tipo/operador"}

print(Diccionario["Asignar valor"])  # Imprime valor de la clave especificada

# Imprime valor al pasarle la clave, y si no existe muestra mensaje indicado luego de la coma.
print(Diccionario.get("#", "No existe"))
print(Diccionario.keys())  # imprime claves
print(Diccionario.values())  # imprime valores
print("\n")
print(Diccionario.items())
del Diccionario["Asignar valor"]  # con funcion del se elimina una clave/valor
Diccionario["Chupala"] = "Accion de mamar"  # añadir al diccionacio
print(Diccionario)
del Diccionario  # eliminar diccionario.

nuevodiccionario = {"Spiderman": ("Superhero", "Marvel", "Fase 4"),
                    "Batman": ["Antihero", "DC", "DCU"]}

print(nuevodiccionario["Batman"])
print(nuevodiccionario["Spiderman"])

# Actualizar
nuevodiccionario.update(
    {"Spiderman": ("Superhero", "Marvel", "Fase3 & Fase4")})


# Eliminar o filtrar elementos de un diccionario para ponerlos en una lista segun condicion.
Peliculas = {"Batman": 9, "Inception": 8, "Gosipgirl": 2, "A comedy": 5}
listafiltrada = []

# Imprimir contenido diccionario. Recorrer diccionario
for p in Peliculas:
    print(f"{p}:{Peliculas[p]}", end=" - ")
print("\n")

for clave, valor in Peliculas.items():
    print(f"{clave}:{valor}", end=" - ")
print("\n")

# Almacenar contenido de un diccionario en una lista con cada clave:valor en forma de tuplas..Peliculas.items() en posicion p, muestra una tupla con clave,valor....
listavacia = []
for p in Peliculas.items():
    listavacia.append(p)
print(listavacia)

listavacia.clear()

# Almacenar claves en una lista. Para almacenar valores, seria Peliculas.values().
# Tambien se puede hacer como: listavacia = list(Peliculas.keys())
for p in Peliculas.keys():
    listavacia.append(p)
print(listavacia)


for p, n in Peliculas.items():
    print(f"{p}:{n}", end="-")
print("\n")

# Filtrar y almacenar en lista segun condicion.  "i"= string pelicula, la clave ; Peliculas[i] = el valor asignado a la clave.
for i in Peliculas:
    if Peliculas[i] > 5:
        listafiltrada.append(i)
    if "A comedy" == i:
        print("La nota de 'A comedy' es ", Peliculas[i])
    if "A comedy" in Peliculas:
        print("-", end=" ")

print(listafiltrada)

print("\n")

# Filtrar y almacenar en otro diccionario clave valor de un diccionario.,
dictfiltr = {}
for i in Peliculas:
    if Peliculas[i] > 5:
        dictfiltr[i] = Peliculas[i]

print(dictfiltr)


# Crear diccionario vacio:
lista = [1, 2, 3, 4]
lista2 = ["A", "B", "C", "D"]
diccvacio = dict()

# Almacenar dos listas dentro de un dicccionario como clave, valor.
for i in range(len(lista2)):
    diccvacio[lista2[i]] = lista[i]
print(diccvacio)

del diccvacio

# Funcion Zip para juntar dos listas en un diccionario
diccvacio = dict(zip(lista2, lista))
print(diccvacio)
