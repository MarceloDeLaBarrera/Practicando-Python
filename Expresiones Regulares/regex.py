# Son una secuencia de caracteres que forman un patron de busqueda. Sirven para el trabajo y procesamiento de texto.

import re  # regex

cadena = "Vamos a aprender expresiones regulares"

# re.search devuelve un objeto cuando encuentra el string, pero si no, devuelve un None.
textoEncontrado = (re.search("aprender", cadena, re.IGNORECASE))

# span devuelve dentro de una tupla la posicion inicial y final del string encontrado.
print(textoEncontrado.span())

if textoEncontrado is not None:
    print("Texto encontrado")
else:
    print("Texto no encontrado")

# re.match permite buscar un string al comienzo de una cadena de texto solamente, si lo encuentra devuelve True, si no False.
# re.ignorecase permite ignorar si es minisculo o mayuscula.


if re.match("vamos", cadena, re.IGNORECASE):
    print("Vamos ha sido encontrado")
else:
    print("No ha sido encontrado")


cadena2 = "Hola, mama mama , mama"
buscar = "mama"

# re.findall devuelve una lista que contiene reiteradamente el string buscado.
print(re.findall(buscar, cadena2))
print(len(re.findall(buscar, cadena2)))

# Metacaracteres

lista = ["Juan Poblete", "Juan Rebolledo", "Jorge Andrade",
         "Alonso Rebolledo", "Pedro Romane", "Pedro Andrade", "Ramon Folledo"]

# ^ ... Para buscar los que empiezan por ^..
for nombre in lista:
    if re.findall("^Juan", nombre):
        print(nombre)

print("\n")

# $ ... Para buscar los que terminen por...
for nombre in lista:
    if re.findall("edo$", nombre):
        print(nombre)

# Buscar entre un rango de caracteres. Si se antepone ^, busca los que empiecen por, si no se incluye busca las letras dentro del rango en todos los elementos de la lista, y si se pone $ al final, busca los que terminan por.
for nombre in lista:
    if re.findall("^[a-pA-P]", nombre):
        print(nombre)

lista2 = ["Ma1", "Ma2", "Ma3", "Ma4", "MaA",
          "MaB", "MaC", "MaD", "FE01", "FE02", "FE03"]
for nombre in lista2:
    if re.findall("Ma[1-3B-D]", nombre):
        print(nombre)


# Todos los caracteres colocados entre "[]", seran patrones de busqueda, tambien se puede usar entre medio de palabras.
listaprueba = ["camion", "camión"]
for e in listaprueba:
    if re.findall("cami[oó]n", e):
        print(e)


# Utilidad para validar emails
email = ["Marcelo@hotmail.com", "mamama@kakapeo.com",
         "perro", "chupala@gmail.com", "mimama@m@imama"]

for e in email:
    if len(re.findall("@", e)) == 1:
        print("Email Valido")
    else:

        print("Email Invalido")


def compruebaMail(mail):

    arroba = mail.count("@")

    if arroba != 1 or mail.rfind("@") == len(mail)-1:
        print("Email invalido")
    else:
        print("Email correcto")


compruebaMail("mariochupatula@hotmail.com")


def compruebaMail2(mail):
    comprueba = False

    if mail[-1] == "@":
        comprueba = True
    else:
        comprueba = False

    if len(re.findall("@", mail)) != 1 or comprueba:
        print("Email invalido")
    else:
        print("Email correcto")


compruebaMail2("mamamabuenapara@hotmail.com")

# Evalua si elemento de lista tiene un arroba en medio de texto. Si fuera una cadena, evaluaria si una palabra cumple con dicha condicion.
listaemail = (re.findall(r'[\w\.-]+@[\w\.-]+\.[\w-]', str(email)))
for e in listaemail:
    print(e)

listaemail = (re.findall(
    r'(?:\.?)([\w\-_+#~!$&\'\.]+(?<!\.)(@|[ ]?\(?[ ]?(at|AT)[ ]?\)?[ ]?)(?<!\.)[\w]+[\w\-\.]*\.[a-zA-Z-]{2,3})(?:[^\w])', str(email)))
for e in listaemail:
    print(e)
